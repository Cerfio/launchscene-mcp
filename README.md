# Launchscene MCP server and agent skills

[Launchscene](https://launchscene.app) is a library of real tech launch videos, broken down scene by scene: the role of each scene in the story, its motion techniques, on-screen text, camera moves, sound and timing. This repository is the public home of the hosted Launchscene MCP server: documentation, the registry `server.json` and the agent skills. The server code is not here; the server runs at:

```
https://launchscene.app/api/mcp
```

Streamable HTTP, OAuth 2.0 with dynamic client registration and PKCE. You sign in with your Launchscene account the first time your client connects. The MCP is free with any account during the beta.

Your agent searches launch scenes, reads their measured timing, text, camera and sound, then builds something that belongs to your product. Every value says how it was measured and what is unknown. Source videos, music, fonts and brand assets are never distributed.

## Connect

**Claude** (web, desktop, mobile): Settings, Connectors, Add custom connector, paste the URL above.

**Claude Code**

```sh
claude mcp add --transport http launchscene https://launchscene.app/api/mcp
```

**Cursor** (`~/.cursor/mcp.json`) **and other clients**

```json
{
  "mcpServers": {
    "launchscene": { "url": "https://launchscene.app/api/mcp" }
  }
}
```

**VS Code** (`.vscode/mcp.json`)

```json
{
  "servers": {
    "launchscene": { "type": "http", "url": "https://launchscene.app/api/mcp" }
  }
}
```

**ChatGPT**: Plugins, Add, Add custom MCP server, paste the URL above with OAuth.

One-click install buttons and the full guide: https://launchscene.app/mcp

## Start with three tools

| Tool | What it does |
| --- | --- |
| `search_scenes` | Describe a scene in plain words ("a cursor clicks Export and the file appears"). Each result comes back as an image your agent can see, signed with the brand, the narrative role and the time. |
| `search_videos` | Whole launch films by description, brand, industry, timing, sound and style, each as an image of its scenes colored by role. |
| `reference_brief` | One scene or a window as frame numbers for your motion build: text entrances, landings, readable holds, camera and audio cues, plus a REFERENCE.md to save. |

The other tools go deeper:

- **Inspect**: `get_scene`, `get_scenes`, `get_video`, `get_video_structure`, `get_frames`
- **Measure**: `get_text_track`, `get_camera_track`, `get_transcript`, `get_audio_map`
- **Explore the corpus**: `find_similar`, `corpus_stats`, `typical_structure`, `compare_groups`, `transitions_after`, `pattern_search`, `trends`, `search_by_moment`, `list_formulas`, `get_formula`
- **Work in a brand's style**: `list_brands`, `get_brand`, `get_brand_kit` (a brand's house style as rules measured on its own launches: palette, type, format, techniques, transitions, opening, call to action, voice, pacing, each with examples)
- **Plan your own film**: `plan_from_references` (your brief plus references becomes a beat sheet and shot list), `storyboard`, `plan_structure`, `adapt_scene`, `beat_grid`, `generation_prompts`, `music_brief`
- **Build and check it**: `export_recipe` (Remotion or HyperFrames starter code), `critique_plan`, `compare_to_reference`, `readability_check`
- **Keep**, with a linked account: `save_to_board`, `list_boards`, `get_history`, `suggest_correction`

Optional tools appear only when their service is configured. Use `tools/list` to see what your credentials can call.

## Try these prompts

- *Find three launch-video scenes where a cursor clicks Export and the file appears, and show them side by side.*
- *Plan a 30-second launch film for my CLI tool from two contrasting references, then storyboard it.*
- *Turn the first scene into a frame-numbered reference brief for a 30 fps Remotion build.*
- *What does Linear's house style look like in its launch videos? Plan my film in a similar style without reusing its assets.*
- *Is the headline "Ship your docs in minutes" readable if it stays on screen for 1.2 seconds?*

## Skills

| Skill | What it does |
| --- | --- |
| [`launchscene`](skills/launchscene/SKILL.md) | Research, plan, adapt or review a launch film from measured references, with Remotion and HyperFrames exports. |
| [`launchscene-reference`](skills/launchscene-reference/SKILL.md) | Turn one launch scene into a frame-numbered REFERENCE.md and BRIEF.md before you build the shot. |
| [`launchscene-timing-check`](skills/launchscene-timing-check/SKILL.md) | Check every text in your composition against real launches, render the frames that matter, propose scoped fixes. |
| [`launchscene-reconstruct`](skills/launchscene-reconstruct/SKILL.md) | Build an editable scene or launch-film MP4 from a reference brief, with your own words, identity and media. |
| [`launchscene-check-render`](skills/launchscene-check-render/SKILL.md) | Inspect a rendered video against its brief and report measured properties, visible defects and what was not verified. |

Copy a skill folder into your agent's skills directory (for example `~/.claude/skills/` or `.cursor/skills/`).

## What the measurements are, and are not

- A text box is the position of the text at one recorded OCR frame, not its whole trajectory.
- Camera moves are measured; the easing class is an estimate of their shape, never the original keyframes.
- Every result says how far it was checked: reviewed by a person, reviewed by AI, or only annotated by AI. Annotations can be wrong.
- Corpus statistics come with their sample size. They describe a curated library of tech launches, not what works.

## Links

- Library: https://launchscene.app
- MCP guide: https://launchscene.app/mcp
- Benchmarks: https://launchscene.app/benchmarks
- Browse by topic: [YC launch videos](https://launchscene.app/yc-launch-videos), [SaaS launch video examples](https://launchscene.app/saas-launch-video-examples), [startup launch videos](https://launchscene.app/startup-launch-video-examples), [motion design launch videos](https://launchscene.app/motion-design-launch-video-examples), [product demo videos](https://launchscene.app/product-demo-video-examples), [best launch videos of 2026](https://launchscene.app/best-product-launch-videos-2026)
- Official MCP Registry: `app.launchscene/launchscene`
- Contact: hello@launchscene.app

## License

The documentation and skills in this repository are MIT licensed. Launch videos belong to their brands and studios; Launchscene shows short excerpts for study and reference, and credits the source.
