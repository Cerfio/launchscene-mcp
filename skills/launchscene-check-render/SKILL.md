---
name: launchscene-check-render
description: Inspect a rendered video against its brief and report measured technical properties, visible defects and unverified areas. Use for an existing MP4 or video export, not for scoring an unrendered plan.
---

# Check the actual render

Work from the rendered file and the user's brief. Prefer local inspection. A storyboard, composition source or preview screenshot cannot establish that the exported film decodes correctly.

## Measure, then look

1. Identify the intended duration, dimensions, frame rate, scenes and audio. Compare only against requirements actually supplied; an unstated target stays unknown. Keep the reference's properties separate from the chosen output specification.
2. Run the bundled local checker with Python 3, FFprobe and FFmpeg:

   ```sh
   python3 scripts/inspect_render.py /absolute/path/film.mp4 --output /absolute/path/check
   ```

   Resolve `scripts/inspect_render.py` relative to this skill directory. If only SKILL.md was supplied, perform the same metadata and complete-decoding checks directly with installed FFprobe and FFmpeg; the helper is optional. Optional `--expect-width`, `--expect-height`, `--expect-duration`, `--expect-fps` and `--expect-audio` flags check explicit delivery requirements. The helper writes `render-check.json`, probes the actual streams and decodes the complete file. It does not upload anything, score visual quality or prove constant frame rate. Missing tools or timeouts are reported as unverified, not passed.
3. Open output images around text holds, clicks, state changes, transitions and the ending. Record which times were inspected. Check cropping, overlap, readable copy, visible action/result, blank frames and missing assets. Inspect playback where still frames cannot settle motion. Listen when possible; state the sampled or complete coverage. An audio stream's presence does not prove good sound or absence of clipping.
4. Compare structure only when a timed structure was actually annotated or measured. Keep hard cuts, narrative scene boundaries and progressive transitions separate. Automated cut counts are provisional. OCR boxes are observations at particular times; missing OCR does not prove missing text. If a track is absent, say **not measured**. Preserve uncertainty instead of inventing scene durations, easing, camera paths or synchronization.

## Return an actionable report

Separate **measured result**, **visual/audio observation**, **interpretation** and **not checked**. For each defect, include an output time or frame, evidence, impact and a scoped correction. Distinguish delivery failures from editorial choices. Never manufacture a global quality score, pixel similarity percentage or claim that every frame was reviewed from a few samples.

If fixing is within the user's request, repair the supported issue, rerender and repeat the relevant check. Stop when the requested deliverable passes the specified checks, or report the unresolved prerequisite. Return the MP4, report and any inspected-frame paths, plus remaining limits.

## Optional private online verification

The local workflow works without a Launchscene account. If the user explicitly requests private upload and analysis, check the current https://launchscene.app/verify page and documented authenticated API before using them. The browser verification flow is being prepared; do not claim it is deployed merely because this skill mentions it. Account-private upload requires the user's account and an actually available service. Keep the upload private and do not publish it to the catalogue.

For MCP, discover current `tools/list`. The connector observed on 6 November 2026 exposes 33 tools and no upload/critique-render tool. Do not invent an upload through that connector or pass a local file path as uploaded bytes. `critique_plan` reviews a plan, not the rendered pixels. If a private web/API task is genuinely available and authorized, follow its returned upload instructions, limits and task status; report only finished measurements. Otherwise complete the local check and state that remote analysis was unavailable.
