# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Key workflow rule

**Never edit `README.md` directly.** It is auto-generated from `resources.json`. After editing `resources.json`, regenerate it:

```bash
python3 scripts/generate_readme.py
```

The pre-commit hook does this automatically when `resources.json` is staged. Install it once per clone:

```bash
git config core.hooksPath .githooks
```

## Architecture

The repo has two artifacts:

- **`resources.json`** — the source of truth. A flat JSON array of resource objects.
- **`README.md`** — generated from `resources.json` by `scripts/generate_readme.py`.

`generate_readme.py` reads `resources.json`, derives section order from first-appearance of each `category` value, builds a TOC and Markdown tables, and writes `README.md`.

## `resources.json` schema

Each entry:

| Field | Type | Notes |
|---|---|---|
| `id` | string | Unique slug |
| `name` | string | Display name |
| `category` | string | Section heading; order of first appearance determines section order in README |
| `description` | string | |
| `formats` | string[] | e.g. `["XML", "TSV"]` |
| `license` | string | |
| `github` | string \| null | Full GitHub URL |
| `url` | string \| null | Non-GitHub URL |
| `acquire` | string[] | CLI commands shown as inline code in Get It column |
| `notes` | string | Internal notes, not rendered |
| `get_it` | string | Optional — overrides the auto-rendered Get It cell with hand-crafted Markdown |

The **Get It** column is auto-rendered: GitHub link (or `url` link if no `github`), then each `acquire` command as inline code, joined by ` · `. Set `get_it` to override entirely (e.g. for multi-link or complex acquisition instructions).
