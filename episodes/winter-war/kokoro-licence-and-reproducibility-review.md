# Kokoro narration stack — licence and reproducibility review

Review date: 31 October 2026
Episode: Winter War
Generated artifact: `winter-war-narration.wav`
Voice preset: `am_michael`
Workflow run: 41153809016

## What the completed run actually used

The GitHub Actions log records:
- Python 3.11.17
- `kokoro==0.9.4`
- `torch==2.15.0`
- `numpy==2.4.6`
- `soundfile==0.14.0`
- `phonemizer-fork==3.3.2`
- `espeakng-loader==0.2.4`
- `en-core-web-sm==3.8.0` (downloaded by the runtime during initialization)
- System `espeak-ng` installed through Ubuntu packages.
- Model repository selected by the package: `hexgrad/Kokoro-82M`.
- The exact model repository commit/revision used by that run was not captured in the workflow log.

The install was not a minimal CPU-only dependency set: pip also downloaded CUDA 13 libraries and related packages even though this GitHub job used a standard hosted CPU runner. This increased download size and install time. No separate paid inference API was used, but GitHub-hosted runner usage is still subject to GitHub plan limits and terms.

## Licence evidence located

1. The official Hugging Face model card identifies `hexgrad/Kokoro-82M` as Apache-2.0 and describes the weights as Apache-licensed:
   https://huggingface.co/hexgrad/Kokoro-82M
2. The `am_michael` voice file is present in that model repository:
   https://huggingface.co/hexgrad/Kokoro-82M/blob/30618d04b530efb8e3ac3bace784f9d4a8dcaa01/voices/am_michael.pt
   The file is within the Apache-labelled repository. Save the repository licence and applicable model/voice file provenance with the production records.
3. The upstream project identifies its model weights as Apache-2.0:
   https://github.com/hexgrad/kokoro
4. The upstream model card notes a GPLv3 eSpeak NG dependency. The generated audio is not itself a redistribution of eSpeak source, but the runtime and any redistributed software bundle must comply with the applicable component licences.

## Current decision

The upstream model and repository metadata provide positive evidence that the core model weights and included voice files are Apache-2.0. This is not a complete legal clearance of the actual runtime stack. The exact package dependency tree, model revision and every third-party component still need to be pinned and archived before declaring the pipeline reproducible and fully cleared.

Do not describe the entire stack as a single Apache-licensed package. Do not redistribute the runtime bundle without reviewing all dependency notices and obligations.

## Required fixes before the next production generation

- Pin `kokoro==0.9.4` and every direct dependency used by the workflow.
- Capture `pip freeze` and the package licence metadata as a workflow artifact.
- Pin the Hugging Face model repository to a verified immutable commit and record the downloaded model/voice hashes.
- Review the licences of `phonemizer-fork`, `espeakng-loader`, `eSpeak NG`, PyTorch and any other transitive packages used in the generated distribution.
- Remove unnecessary CUDA dependency downloads from future CPU jobs if a tested CPU-only dependency route exists.
- Archive the Apache-2.0 licence text and attribution notices alongside the project.
- Keep the generated voiceover on HOLD for publication until a human listening review and all rights checks are complete.

## Sources
- Official Kokoro model card: https://huggingface.co/hexgrad/Kokoro-82M
- Official Kokoro repository: https://github.com/hexgrad/kokoro
- Exact `am_michael` voice file at a fixed repository revision: https://huggingface.co/hexgrad/Kokoro-82M/blob/30618d04b530efb8e3ac3bace784f9d4a8dcaa01/voices/am_michael.pt
- eSpeak NG project and licence: https://github.com/espeak-ng/espeak-ng

Decision: PARTIAL EVIDENCE — NOT FULL STACK CLEARANCE.
