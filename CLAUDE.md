# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Key workflow rule

**`resources.json` is the only file a human edits. Never edit `README.md` directly** — it is generated from `resources.json`. After editing `resources.json`, validate it and regenerate:

```bash
python3 scripts/validate_resources.py
python3 scripts/generate_readme.py
```

**Validation runs first and blocks.** `validate_resources.py` refuses a duplicate `id`, a missing required field (`id`, `name`, `category`, `description`, `license`), an `id` that is not a lower-case slug, an unknown field, a `formats`/`acquire` that is not a list, and a `github`/`url`/`download` that is not a URL or `null`. Generating a README from a broken catalog would either fail confusingly or quietly publish the defect.

The pre-commit hook runs both — validating, then regenerating `README.md` and staging it — when `resources.json` is staged. Install it once per clone:

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
| `download` | string \| null | Optional — direct download URL for the resource itself |
| `provides` | object[] | Optional — what a tool can open without a human reading the resource's README. Each entry needs `id`, `name`, `kind`, `path`, `versification`, `canon`, `language`; `path` is relative and must stay inside the download, and `provides` ids are unique across the whole catalog |

`validate_resources.py` holds the authoritative field list in `KNOWN_FIELDS`; a key outside it is rejected as a typo.

The **Get It** column is auto-rendered: GitHub link (or `url` link if no `github`), then each `acquire` command as inline code, joined by ` · `. Set `get_it` to override entirely (e.g. for multi-link or complex acquisition instructions).
