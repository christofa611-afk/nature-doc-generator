# Zero-budget moving-footage provider assessment — 31 October 2026

**Purpose:** identify browser-based sources of genuine moving video for the Winter War documentary while preserving the user's zero-budget, no-install, commercial-use and no-watermark requirements.

**Decision:** LoreMotion is the strongest current candidate for a controlled pilot, not an automatically approved production supplier. Generate a single test clip first, download it immediately, inspect it frame-by-frame, and preserve the exact terms and model information before scaling. No footage has been generated or approved by this assessment.

## Candidate assessment

| Provider | Free allowance evidenced on official page | Output / watermark | Commercial-use statement | Fit for this project | Decision |
|---|---|---|---|---|---|
| LoreMotion | LTX-Video 2.5 and MiniMax H3 advertised as free and unlimited, supported by an ad per render. | LTX up to 720p; MiniMax H3 free tier varies with queue, generally 480p up to 5–10s or 720p up to 5s. Unwatermarked MP4. | Site says creator retains full rights, subject to model provider terms. | Best apparent throughput for testing 17 different moving shots; queue pressure and model licence conditions matter. | **PILOT FIRST; rights hold until exact model terms and output use are confirmed.** |
| Free.ai image-to-video | Signed-in free account gets 30,000 tokens/day; default self-hosted image-to-video costs 30,000 tokens per 2–6s clip, effectively one clip every two days. | Wan 2.2 TI2V-5B, 720p/24fps, no watermark. | Page states personal and commercial use. | Stronger as a fallback for carefully prepared first frames; very slow throughput for 17 scenes. | **FALLBACK; test image quality and retain rights evidence.** |
| Rendastic | One free creation per UTC day. | 3 or 5 seconds, 480p, no watermark. | Site says commercial use is allowed subject to input rights, law and selected model provider terms. | Too short/low-resolution for primary documentary coverage; can be a test or insert only if visually acceptable. | **NOT PRIMARY.** |
| HelloGen | Unlimited free image generation; AI video is credit-based. Unlimited video is Pro/Max, paid. | No-watermark commercial images; video credits/paid plan. | Commercial use statement for images; paid video terms. | Does not meet zero-cost video requirement. | **EXCLUDE FOR VIDEO.** |
| MakeFun AI | Signup bonus credits and daily check-in credits advertised. | 5–15s, 720p/1080p depending on credits. | Commercial use applies to paid plans only. | Free signup credits are not a sustainable free production route. | **EXCLUDE FOR MONETIZED OUTPUT ON FREE PLAN.** |
| Ikat | 10 signup credits; enough for one 5-second 720p clip. | No watermark. | Site claims commercial use, but free allowance is a one-off signup grant. | Useful for one-off test only, not repeatable production. | **NOT PRIMARY.** |
| WanGP third-party hosted page | Advertises unlimited free/no-signup image-to-video. | Claims no watermark; details and queue limits unclear. | No sufficiently clear commercial-use grant found in surfaced page. | Insufficient rights transparency for a monetized channel. | **REJECT UNTIL RIGHTS TERMS ARE VERIFIED.** |

## Primary pilot: LoreMotion

Official pages:
- About / free model claim: https://loremotion.com/about/
- Generator and current free limits: https://loremotion.com/generate/
- Acceptable Use Policy: https://loremotion.com/acceptable-use/
- Changelog: https://loremotion.com/changelog/
- V2 policy summary: https://loremotion.com/blog/loremotion-v2/

### Important qualifications

1. LoreMotion's current page advertises LTX-Video 2.5 and MiniMax H3 as free, unlimited and unwatermarked, with one short ad per render. The exact H3 resolution/duration can be reduced during high queue load.
2. LoreMotion says generated output is commercially usable, but also says rights are subject to the model provider's terms. Do not interpret the site statement as overriding the underlying model licence.
3. The model versions can change. Save the selected model name, model/version displayed at generation time, generation date, and a PDF/screenshot of the applicable terms for every production batch.
4. LoreMotion's Acceptable Use Policy blocks weapon synthesis instructions and certain harmful content. Historical documentary prompts must describe non-instructional historical scenes, not provide weapon-building instructions.
5. Generated video clips are reported to expire after 48 hours on the free tier. Download every accepted clip immediately; never rely on a dashboard as the archive.
6. The user must generate and download clips in their own browser session. This chat cannot access the user's logged-in session or operate the generator UI.

### First pilot shot

Use scene S05 (winter landscape) as the first low-risk quality test. It avoids human anatomy, insignia and weapon accuracy issues while testing whether the model produces real continuous movement rather than a zoomed still.

**Prompt:**
A continuous photorealistic live-action documentary aerial glide above a remote Finnish winter forest in December 1939: dense snow-covered conifers, a frozen lake and a narrow road visible far below. The camera advances steadily at a plausible low aircraft speed. Wind visibly moves the treetops; fine loose snow drifts across the frozen lake; distant cloud shadows travel slowly over the forest. Natural overcast Nordic winter light, restrained archival-documentary realism, physically plausible landscape and motion. One continuous shot, stable geography, no cuts, no titles, no text, no logos, no people, no military equipment, no artificial zoom across a still image.

**Acceptance checks:** continuous movement in the trees, drifting snow and camera; no morphing or flicker; plausible Finnish winter landscape; no repeated frames masquerading as motion; no watermarks; clean 16:9 export if available; retain original MP4 and metadata.

## Production arithmetic

The 17-scene plan includes three original editorial graphics and 14 footage scenes. The user requires actual moving footage, not static-image pans. A 5-second generation is only a source shot; final edit needs multiple distinct clips and coverage, not one clip per entire scene. LoreMotion's free lane is the only candidate in this shortlist that currently advertises unlimited hosted video, but that claim is provider-controlled and can change. No fixed output volume or uptime is guaranteed.

## Go / no-go gate

Do not use a provider for a monetized upload unless:
- the current free-tier commercial-use grant is explicit;
- the underlying model licence permits the intended use and historical subject;
- input image/reference rights are cleared;
- downloaded output is unwatermarked and visually acceptable;
- all AI-realistic-content disclosure obligations are met;
- evidence of terms and generation settings is archived.

**Current decision: LoreMotion pilot candidate only. All production scene assets remain HOLD.**
