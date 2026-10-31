#!/usr/bin/env python3
"""Generate original synthetic narration with the open-weight Kokoro TTS model.
No paid API is used. Model and inference package are downloaded at run time.
Voice: am_michael (preset synthetic voice; not a clone of a real person).
"""
from pathlib import Path
import re, sys
import numpy as np
import soundfile as sf
from kokoro import KPipeline

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/"episodes/winter-war/narration.md"
OUT=ROOT/"episodes/winter-war/generated/winter-war-narration.wav"
VOICE="am_michael"
LANG="a"
SAMPLE_RATE=24000

def clean_markdown(text):
    text=re.sub(r"^#.*$","",text,flags=re.M)
    text=re.sub(r"^\*\*.*$","",text,flags=re.M)
    text=re.sub(r"^\*\*End\.\*\*\s*$","",text,flags=re.M)
    text=re.sub(r"\*([^*]+)\*","\\1",text)
    text=re.sub(r"\([^)]*\)","",text)
    text=re.sub(r"\s+"," ",text)
    return text.strip()

def main():
    if not SCRIPT.exists():
        raise SystemExit(f"Missing narration script: {SCRIPT}")
    text=clean_markdown(SCRIPT.read_text(encoding="utf-8"))
    if len(text)<500:
        raise SystemExit("Narration is too short; refusing to generate.")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    print(f"Loading Kokoro TTS; {len(text)} characters; voice={VOICE}")
    pipe=KPipeline(lang_code=LANG)
    chunks=[]
    # Split on sentence boundaries to preserve prosody and keep memory stable.
    sentences=re.split(r"(?<=[.!?])\s+",text)
    batch=""
    batches=[]
    for sentence in sentences:
        if len(batch)+len(sentence)>420 and batch:
            batches.append(batch.strip()); batch=sentence
        else:
            batch=(batch+" "+sentence).strip()
    if batch: batches.append(batch)
    for idx,part in enumerate(batches,1):
        print(f"Synthesizing section {idx}/{len(batches)}")
        for _,_,audio in pipe(part, voice=VOICE, speed=0.96):
            if audio is not None and len(audio):
                chunks.append(np.asarray(audio,dtype=np.float32))
    if not chunks:
        raise SystemExit("TTS returned no audio.")
    audio=np.concatenate(chunks)
    # Brief, clean pauses between paragraph-like chunks are naturally retained by the model.
    sf.write(OUT,audio,SAMPLE_RATE,subtype="PCM_16")
    duration=len(audio)/SAMPLE_RATE
    print(f"Saved {OUT}; duration={duration:.1f}s; samples={len(audio)}")
    if duration<300 or duration>1200:
        print("WARNING: generated runtime is outside the expected 5–20 minute range; review pacing.")
if __name__=="__main__":
    main()
