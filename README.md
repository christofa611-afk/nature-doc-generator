# Untapped History & Storytelling — Documentary Production System

A zero-budget, browser-first production-control repository for original, faceless historical documentaries.

## Operating principles
- Research every material claim; retain a source register and distinguish fact, interpretation, and uncertainty.
- Use original narration and a distinct moving-footage plan. A still image with a pan/zoom effect is not moving footage.
- Verify item-level commercial reuse rights for every archival asset. Historical age does not automatically mean public domain.
- Photorealistic AI reconstructions must be historically plausible, disclosed where required, and never presented as authentic archival footage.
- Never fabricate quotations, dialogue, statistics, sources, or visual evidence.
- Do not publish until all rights, accuracy, originality, audience-safety, monetization, and synthetic-content checks pass.
- This repository manages production records and validates completeness. It does not generate AI video, provide GPU compute, or upload to YouTube.

## Current episode
**The Winter War: How Finland Survived Stalin's Invasion (1939–1940)**

Status: development. Narration draft, 17-scene moving-footage plan, source register, episode metadata, policy checklist and automated structural validator are committed. Video assets, voiceover, final edit and publication are not complete.

## Workflow
1. Review `episodes/winter-war/episode.json`, `narration.md`, `scenes.json`, and `sources.json`.
2. Verify each factual claim against primary or high-quality scholarly sources.
3. Obtain/produce genuinely moving footage and record item-level commercial rights in each scene record.
4. Run `python tools/validate_episode.py episodes/winter-war`.
5. Resolve all errors. Manually complete `episodes/winter-war/POLICY_REVIEW.md` and `POLICY_AND_RIGHTS_GATE.md`.
6. Only after all checks pass, render, review and prepare upload.

A passing automated check is not proof of historical accuracy, licence validity, video quality or policy compliance.
