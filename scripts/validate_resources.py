#!/usr/bin/env python3
"""Check resources.json before it is committed.

The catalog had two entries with the id `scripture-burrito` and, briefly, two with
`cntr-transcriptions` — the second added by someone who did not think to look first. Nothing
noticed either, because nothing checked. A duplicate id is the worst of the failures this
catches: consumers key on the id, so one entry silently shadows the other and which one wins
depends on how the file happens to be read.

Run it directly, or let the pre-commit hook run it:

    python3 scripts/validate_resources.py
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

#: Every field the README generator or a consumer reads. A key outside this set is a typo
#: until someone adds it here deliberately.
KNOWN_FIELDS = {
    "id", "name", "category", "description", "formats", "license",
    "github", "url", "acquire", "notes", "get_it", "download", "provides",
}

REQUIRED_FIELDS = ("id", "name", "category", "description", "license")

#: Fields every entry in a `provides` block needs. They are what lets a tool open the resource
#: without a human reading its README: which file, what shape, and how it is numbered.
PROVIDES_REQUIRED = ("id", "name", "kind", "path", "versification", "canon", "language")

ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def check(resources: list) -> list:
    problems: list = []

    counts = Counter(r.get("id") for r in resources)
    for identifier, count in sorted(counts.items()):
        if count > 1:
            problems.append(f"id {identifier!r} appears {count} times; ids must be unique")

    provided = Counter()

    for index, entry in enumerate(resources):
        where = f"entry {index} ({entry.get('id') or 'no id'})"

        for field in REQUIRED_FIELDS:
            if not entry.get(field):
                problems.append(f"{where}: missing required field {field!r}")

        identifier = str(entry.get("id") or "")
        if identifier and not ID_PATTERN.match(identifier):
            problems.append(f"{where}: id must be a lower-case slug")

        for field in sorted(set(entry) - KNOWN_FIELDS):
            problems.append(f"{where}: unknown field {field!r} — a typo, or add it to KNOWN_FIELDS")

        if not isinstance(entry.get("formats", []), list):
            problems.append(f"{where}: `formats` must be a list")
        if not isinstance(entry.get("acquire", []), list):
            problems.append(f"{where}: `acquire` must be a list")

        for field in ("github", "url", "download"):
            value = entry.get(field)
            if value is not None and not str(value).startswith(("http://", "https://")):
                problems.append(f"{where}: `{field}` should be a URL or null")

        for item in entry.get("provides") or []:
            label = f"{where}: provides[{item.get('id') or '?'}]"
            for field in PROVIDES_REQUIRED:
                if not item.get(field):
                    problems.append(f"{label}: missing {field!r}")
            path = str(item.get("path") or "")
            if path.startswith("/") or ".." in path:
                problems.append(f"{label}: `path` must be relative and stay inside the download")
            provided[item.get("id")] += 1

    for identifier, count in sorted(provided.items()):
        if count > 1:
            problems.append(f"provides id {identifier!r} appears {count} times; it must be unique")

    return problems


def main() -> int:
    path = ROOT / "resources.json"
    try:
        resources = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(f"resources.json is not valid JSON: {error}", file=sys.stderr)
        return 1

    if not isinstance(resources, list):
        print("resources.json must be a JSON array of entries", file=sys.stderr)
        return 1

    problems = check(resources)
    if problems:
        print(f"resources.json: {len(problems)} problem(s)", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1

    categories = sorted({r["category"] for r in resources})
    print(f"resources.json OK — {len(resources)} entries, {len(categories)} categories.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
