#!/usr/bin/env python3
"""Generate synthetic narration plus segment-aligned caption drafts.

The SRT timestamps are derived from the exact audio chunk boundaries returned
by Kokoro. They still require human correction against the final mastered track.
"""
from pathlib import Path
import json
import re
import numpy as np
import soundfile as sf
from kokoro import KPipeline

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "episodes/winter-war/narration.md"
OUT_DIR = ROOT / "episodes/winter-war/generated"
OUT = OUT_DIR / "winter-war-narration.wav"
TIMING_JSON = OUT_DIR / "winter-war-narration-segments.json"
SRT = OUT_DIR / "winter-war-narration-draft.srt"
VOICE = "am_michael"
LANG = "a"
SAMPLE_RATE = 24000

def clean_markdown(text):
    # Strip headings and editorial metadata; retain only narration paragraphs.
    kept = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if re.match(r"^\*\*(?:Narration draft|Target|Editorial position)\b", stripped, re.I):
            continue
        if re.match(r"^\*\*End\.\*\*$", stripped, re.I):
            continue
        if re.match(r"^[-*_]{3,}$", stripped):
            continue
        kept.append(stripped)
    text = "\n".join(kept)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def srt_time(seconds):
    ms = round(seconds * 1000)
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def main():
    if not SCRIPT.exists():
        raise SystemExit(f"Missing narration script: {SCRIPT}")
    text = clean_markdown(SCRIPT.read_text(encoding="utf-8"))
    if len(text) < 500:
        raise SystemExit("Narration is too short; refusing to generate.")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Loading Kokoro TTS; {len(text)} characters; voice={VOICE}")
    pipe = KPipeline(lang_code=LANG)
    # One narration sentence per synthesis batch gives useful sentence-level
    # cue boundaries. Never invent sub-sentence timestamps.
    batches = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]

    chunks, segments = [], []
    cursor = 0.0
    for idx, part in enumerate(batches, 1):
        print(f"Synthesizing section {idx}/{len(batches)}")
        yielded = False
        for gs, ps, audio in pipe(part, voice=VOICE, speed=0.96):
            if audio is None or not len(audio):
                continue
            yielded = True
            audio = np.asarray(audio, dtype=np.float32)
            duration = len(audio) / SAMPLE_RATE
            segment_text = str(gs).strip() if gs is not None else ""
            if not segment_text:
                segment_text = part
            chunks.append(audio)
            segments.append({
                "index": len(segments) + 1,
                "start": round(cursor, 3),
                "end": round(cursor + duration, 3),
                "text": segment_text,
                "phonemes": str(ps) if ps is not None else ""
            })
            cursor += duration
        if not yielded:
            print(f"WARNING: no audio returned for section {idx}")

    if not chunks:
        raise SystemExit("TTS returned no audio.")
    audio = np.concatenate(chunks)
    sf.write(OUT, audio, SAMPLE_RATE, subtype="PCM_16")
    duration = len(audio) / SAMPLE_RATE
    TIMING_JSON.write_text(json.dumps({
        "source_script": "episodes/winter-war/narration.md",
        "voice": VOICE,
        "sample_rate": SAMPLE_RATE,
        "duration_seconds": round(duration, 3),
        "timing_basis": "Kokoro yielded audio chunk boundaries; human caption review required",
        "segments": segments
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = []
    for seg in segments:
        lines.extend([
            str(seg["index"]),
            f'{srt_time(seg["start"])} --> {srt_time(seg["end"])}',
            seg["text"],
            ""
        ])
    SRT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved {OUT}; duration={duration:.1f}s; samples={len(audio)}")
    print(f"Saved {TIMING_JSON}; segments={len(segments)}")
    print(f"Saved {SRT}; review required")
    if duration < 300 or duration > 1200:
        print("WARNING: generated runtime is outside the expected 5–20 minute range; review pacing.")

if __name__ == "__main__":
    main()
