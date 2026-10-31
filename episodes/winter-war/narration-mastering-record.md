# Winter War narration — editor-ready audio derivative

Generated from the successful Kokoro draft WAV using FFmpeg loudness normalization.

## Output
- File: `winter-war-narration-mastered-48k.wav`
- Duration: 535.025 seconds (8:55.025)
- Format: PCM 24-bit, 48,000 Hz, mono
- Integrated loudness measured on output: approximately -16.29 LUFS
- True peak measured on output: approximately -1.50 dBTP
- No timing change; duration matches the source.

## Processing
- Input: `winter-war-narration.wav` (24 kHz mono PCM 16-bit)
- Filter: FFmpeg loudnorm, target -16 LUFS, -1.5 dBTP, LRA target 11
- Output re-sampled to 48 kHz and encoded as PCM 24-bit.

## Important
This is a technical audio derivative only. Loudness normalization does not verify pronunciation, factual accuracy, voice quality, commercial licensing, or YouTube policy compliance. Human full-length listening review remains mandatory before publication.
