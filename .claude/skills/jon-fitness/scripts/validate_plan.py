#!/usr/bin/env python3
"""Consistency checks for a jon-fitness client plan pair.

Usage:
    python scripts/validate_plan.py clients/john_tan_fitness_plan.md
    python scripts/validate_plan.py clients/john_tan_fitness_plan.csv
    python scripts/validate_plan.py clients/            # check every pair

Checks (heuristic — this backs up human review, it does not replace it):

  1. Filename convention: <slug>_fitness_plan.md and .csv, slug is [a-z0-9_],
     and the .md and .csv share the same slug.
  2. Both members of the pair exist.
  3. CSV parses, has the expected leading columns, no empty exercise rows, and
     every data row has the same field count as the header.
  4. CSV "week"/"day" values look consistent (weeks are positive ints).
  5. The .md still contains its required section headings.
  6. Evidence present: the .md cites the course somewhere (a "Wk"/"Ch"/"Table"
     / "p<NN>" reference) and the "ISA CPT Evidence" section is not empty.
  7. Placeholder leakage: no unfilled "{{...}}" tokens remain in the .md.
  8. Cross-check: exercises named in the CSV appear somewhere in the .md
     (warn only — the .md may summarise rather than list every accessory).

Exit code 0 = no errors (warnings allowed), 1 = errors found, 2 = bad usage.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REQUIRED_MD_HEADINGS = [
    "Client Profile",
    "Goals",
    "Screening",
    "Program Strategy",
    "Training Variable Reasoning",
    "Exercise Selection Reasoning",
    "Progression Strategy",
    "Monitoring & Reassessment",
    "ISA CPT Evidence",
    "Decision Log",
    "Revision History",
]
EXPECTED_CSV_LEAD = ["week", "day"]
SLUG_RE = re.compile(r"^([a-z0-9_]+)_fitness_plan\.(md|csv)$")
CITE_RE = re.compile(r"(Wk\s?\d|Ch\s?\d|Table\s|p\d{1,3}\b|Page\s\d)", re.I)

errors: list[str] = []
warnings: list[str] = []


def err(m: str) -> None:
    errors.append(m)


def warn(m: str) -> None:
    warnings.append(m)


def check_pair(slug: str, directory: Path) -> None:
    md = directory / f"{slug}_fitness_plan.md"
    csv_path = directory / f"{slug}_fitness_plan.csv"

    if not md.exists():
        err(f"[{slug}] missing {md.name}")
    if not csv_path.exists():
        err(f"[{slug}] missing {csv_path.name}")
    if md.exists():
        _check_md(slug, md)
    csv_rows = _check_csv(slug, csv_path) if csv_path.exists() else []
    if md.exists() and csv_rows:
        _cross_check(slug, md.read_text(), csv_rows)


def _check_md(slug: str, path: Path) -> None:
    text = path.read_text()

    for token in set(re.findall(r"\{\{[^}]+\}\}", text)):
        err(f"[{slug}] unfilled placeholder in .md: {token}")

    for h in REQUIRED_MD_HEADINGS:
        if h not in text:
            err(f"[{slug}] .md missing required section: '{h}'")

    if not CITE_RE.search(text):
        err(f"[{slug}] .md contains no course citation (expected e.g. 'Wk07 Ch11 p29')")

    # ISA CPT Evidence section should have content beyond the template scaffold.
    m = re.search(r"##\s*ISA CPT Evidence\s*(.*?)(?:\n##\s|\Z)", text, re.S)
    if m:
        body = m.group(1)
        # strip table header / separator / template prompt lines
        meaningful = [
            ln for ln in body.splitlines()
            if ln.strip()
            and not ln.strip().startswith("|---")
            and "Client fact | ISA CPT" not in ln
            and not ln.strip().startswith("_")
        ]
        if len(meaningful) <= 1:
            warn(f"[{slug}] 'ISA CPT Evidence' section looks empty — fill the traceability chain")

    if "Last updated:" not in text:
        warn(f"[{slug}] .md has no 'Last updated:' line")


def _check_csv(slug: str, path: Path) -> list[dict]:
    try:
        raw = path.read_text().splitlines()
        reader = csv.reader(raw)
        rows = [r for r in reader if r and any(c.strip() for c in r)]
    except Exception as e:  # noqa: BLE001
        err(f"[{slug}] cannot parse .csv: {e}")
        return []

    if not rows:
        err(f"[{slug}] .csv is empty")
        return []

    header = [c.strip().lower() for c in rows[0]]
    if header[: len(EXPECTED_CSV_LEAD)] != EXPECTED_CSV_LEAD:
        warn(
            f"[{slug}] .csv header starts with {header[:2]}, expected "
            f"{EXPECTED_CSV_LEAD} — adjust columns to the program's needs but keep week/day"
        )
    if "exercise" not in header:
        err(f"[{slug}] .csv has no 'exercise' column")

    ncols = len(header)
    ex_idx = header.index("exercise") if "exercise" in header else None
    wk_idx = header.index("week") if "week" in header else None

    dict_rows: list[dict] = []
    for i, r in enumerate(rows[1:], start=2):
        if len(r) != ncols:
            err(f"[{slug}] .csv line {i}: {len(r)} fields, header has {ncols}")
            continue
        rec = dict(zip(header, [c.strip() for c in r]))
        dict_rows.append(rec)
        if ex_idx is not None and not r[ex_idx].strip():
            err(f"[{slug}] .csv line {i}: empty 'exercise'")
        if wk_idx is not None:
            wv = r[wk_idx].strip()
            if wv and not re.fullmatch(r"\d+(-\d+)?", wv):
                warn(f"[{slug}] .csv line {i}: 'week' = {wv!r} is not an int or range")

    return dict_rows


def _cross_check(slug: str, md_text: str, csv_rows: list[dict]) -> None:
    md_low = md_text.lower()
    seen = set()
    for rec in csv_rows:
        ex = (rec.get("exercise") or "").strip()
        if not ex or ex.lower() in seen:
            continue
        seen.add(ex.lower())
        # match on the first two words to tolerate variation wording
        key = " ".join(re.findall(r"[a-z]+", ex.lower())[:2])
        if key and key not in md_low:
            warn(f"[{slug}] CSV exercise '{ex}' not mentioned in the .md reasoning")


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2

    target = Path(argv[0])
    pairs: dict[Path, set[str]] = {}

    if target.is_dir():
        candidates = sorted(target.glob("*_fitness_plan.*"))
        if not candidates:
            print(f"no *_fitness_plan.* files in {target}")
            return 0
        for p in candidates:
            m = SLUG_RE.match(p.name)
            if m:
                pairs.setdefault(p.parent, set()).add(m.group(1))
            else:
                warn(f"{p.name}: does not match <slug>_fitness_plan.(md|csv)")
    else:
        m = SLUG_RE.match(target.name)
        if not m:
            err(
                f"{target.name}: filename must be <slug>_fitness_plan.md or .csv "
                f"with slug in [a-z0-9_]"
            )
        else:
            pairs.setdefault(target.parent, set()).add(m.group(1))

    for directory, slugs in pairs.items():
        for slug in sorted(slugs):
            check_pair(slug, directory)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")

    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"\nOK — 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
