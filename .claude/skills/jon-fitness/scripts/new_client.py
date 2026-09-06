#!/usr/bin/env python3
"""Scaffold a <client_slug>_fitness_plan.{md,csv} pair from templates/.

Usage:
    python scripts/new_client.py "John Tan"
    python scripts/new_client.py "Sarah Lim" --dir /path/to/clients

Name normalization (matches SKILL.md): lowercase -> strip -> spaces to
underscores -> keep only [a-z0-9_] -> collapse repeats. The same slug must be
reused for every future update of that client.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent


def slugify(name: str) -> str:
    s = name.strip().lower()
    s = s.replace(" ", "_")
    s = re.sub(r"[^a-z0-9_]", "", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("name", help="Client's name, e.g. \"John Tan\"")
    ap.add_argument(
        "--dir",
        default=str(SKILL_ROOT / "clients"),
        help="Directory to write the plan pair into (default: <skill>/clients)",
    )
    ap.add_argument(
        "--force", action="store_true", help="Overwrite existing files"
    )
    args = ap.parse_args(argv)

    slug = slugify(args.name)
    if not slug:
        print(f"error: {args.name!r} normalizes to an empty slug", file=sys.stderr)
        return 2

    out_dir = Path(args.dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    md_path = out_dir / f"{slug}_fitness_plan.md"
    csv_path = out_dir / f"{slug}_fitness_plan.csv"

    for p in (md_path, csv_path):
        if p.exists() and not args.force:
            print(
                f"error: {p} already exists (use --force to overwrite, "
                f"or this client already has a plan — update it instead)",
                file=sys.stderr,
            )
            return 1

    today = _dt.date.today().isoformat()
    md_tmpl = (SKILL_ROOT / "templates" / "client_fitness_plan.md").read_text()
    md = (
        md_tmpl.replace("{{CLIENT_NAME}}", args.name.strip())
        .replace("{{client_slug}}", slug)
        .replace("{{DATE}}", today)
    )
    md_path.write_text(md)
    csv_path.write_text(
        (SKILL_ROOT / "templates" / "client_fitness_plan.csv").read_text()
    )

    print(f"created {md_path}")
    print(f"created {csv_path}")
    print(f"\nclient slug: {slug}  (reuse this exact slug for all future updates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
