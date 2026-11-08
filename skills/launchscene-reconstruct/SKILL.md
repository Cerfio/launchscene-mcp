---
name: launchscene-reconstruct
description: Build an editable scene or launch-film MP4 from a Launchscene reference brief, using the user's own words, identity and media. Use when the user wants to make a video, not only find references.
---

# Reconstruct with your own material

Deliver an editable project, a rendered MP4 and a short evidence report. Start from the user's pasted Launchscene prompt or reference brief; no account or connector is required for that path.

## Make the brief executable

- Establish the requested scope: one scene or a whole film, product action, audience, copy, duration, canvas and frame rate. Reuse information already supplied. Preserve the user's engine and format choices. If none is specified, use Remotion for the first pilot when available; use one engine rather than comparing several.
- Inspect the supplied assets. Map every reference element to the user's logo, screens, footage, type or new illustration. Never extract the reference brand's logo, video, music or imagery as production assets. Reference images remain evidence, not layers in the new film.
- A shot of a person, place or physical action needs the user's footage, a concrete shot to film, or a visibly different illustrated treatment. Do not substitute an avatar service, face recreation or a pretend screenshot. Clearly label a proposed illustration or UI mockup. If an essential asset is absent, progress on the independent parts and identify the specific missing input.
- Save a compact brief with an asset map and a timeline in the target frame rate. Describe visible events: entrance, landing, click, state change, reading hold, exit. Keep **measured**, **annotated**, **derived**, **proposed** and **unknown** distinct. A midpoint text box is not a motion path; a guessed font or easing curve is not a measurement.

## Build and inspect

Implement the requested scope with the available project and its documented render command. A reference brief is input to a composition, not evidence that a playable composition already exists. For a whole film, connect all requested scenes and produce one complete export.

Render early enough to catch timing and asset failures. Inspect actual output frames at text holds, state changes, transition boundaries and the final frame. Check readable copy, visible product action, cropping, missing media and accidental blank frames. A demonstration should show the action and its result. Inspect the audio when present; distinguish a complete listening pass from sampled checks or measurements alone.

Use FFprobe or the renderer's output metadata to record dimensions, duration, frame rate, frame count and audio streams. Decode the complete MP4 with FFmpeg or an equivalent checker. Repair observed defects and rerender affected output. If rendering cannot run, report the concrete missing prerequisite and provide the editable work; do not call an unrendered project a completed film.

Return the MP4 and project paths, exact render command, asset provenance, checks performed and remaining limitations. State reference resemblance as an observation, never an invented pixel-fidelity score. Do not publish or upload as an implicit part of rendering.

## Optional Launchscene context

If a connector is available, discover its current `tools/list` before choosing tools. The connector inventory observed on 6 November 2026 contains 33 tools, with no render-upload tool; runtime discovery takes precedence. `get_video`, `get_scene`, `reference_brief` and `get_frames` can supply reference context when offered. Read actual frame times and measurement provenance. A copied standalone prompt remains usable when the connector is absent.

Examples: https://launchscene.app/examples . Starting points: https://launchscene.app/make/interface-demo and https://launchscene.app/make/launch-film . These links are optional context, not required dependencies.
