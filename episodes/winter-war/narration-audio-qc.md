# Winter War narration — generation record and audio QC

Status: WAV generated successfully; human listening review still required.

## Generation record
- Workflow: GitHub Actions run 41153809016
- Result: success
- Voice: Kokoro preset `am_michael` (synthetic voice; not a clone)
- Source script: `episodes/winter-war/narration.md`
- Output: `winter-war-narration.wav`
- Artifact: `winter-war-narration-wav` (artifact ID 13025015555)

## Technical inspection
- Duration: 535.025 seconds (8:55.025)
- Encoding: PCM signed 16-bit little-endian
- Sample rate: 24,000 Hz
- Channels: mono
- Peak sample: approximately -2.9 dBFS
- RMS level: approximately -27.7 dBFS
- Clipped samples: 0

## Quality status
- File exists and is readable: PASS
- Technical format: PASS for a source voice track; convert to the editor's 48 kHz project rate during mastering.
- Clipping: no clipped samples detected.
- Loudness: not yet measured to an integrated LUFS target.
- Pronunciation, pacing, pauses, emphasis, names and audible artefacts: NOT LISTENING-REVIEWED.
- Script fact-check: NOT APPROVED.
- Commercial rights: verify the exact Kokoro package, model weights, voice assets and dependency licences before monetized publication.

## Release restriction
This is a generated draft voice track, not a final approved narration. Do not publish until a human listens to the entire file, checks pronunciation against the script, corrects any errors, and verifies applicable licences.
