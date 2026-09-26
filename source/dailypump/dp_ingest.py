#!/usr/bin/env python3
"""Ingest Daily Pump screenshots: OCR (two engines), attach date / ISO week / split, index them.

Reuses the REVL OCR engines (rapidocr + Apple Vision) from source/extract_revl.py so both datasets
are read the same way and engine disagreements stay visible ([?] flags), never silently guessed.

Input : $DP_DATA_ROOT/raw/<iso_year>/W<ww>/<YYYY-MM-DD>_<daily|split|notes>[_n].png
Output: $DP_DATA_ROOT/ocr/<stem>.txt and one line per capture in $DP_DATA_ROOT/index.jsonl
        (idempotent: files already indexed by sha256 are skipped).

Fields are provenance-tagged: the date and kind come from the FILENAME (set by the capture step);
the split label comes from split_log.csv (a dated log) - if there is none, it is recorded as unknown,
never guessed.

Usage:
    python source/dailypump/dp_ingest.py            # ingest everything new
    python source/dailypump/dp_ingest.py --no-vision --limit 3 --dry-run
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import dp_common as C  # noqa: E402


def load_revl_engines():
    spec = importlib.util.spec_from_file_location("extract_revl", HERE.parent / "extract_revl.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def vision_text(er, path: Path) -> str:
    """Run the Vision helper on a COPY inside DATA_ROOT/.tmp so paid content is never written
    into the (iCloud-synced) repo folder, even temporarily."""
    C.TMP.mkdir(parents=True, exist_ok=True)
    tmp = C.TMP / (hashlib.md5(str(path).encode()).hexdigest()[:16] + ".png")
    side = Path(str(tmp) + ".visiontxt")
    try:
        shutil.copyfile(path, tmp)
        subprocess.run([str(er.VISION_BIN), str(tmp)], capture_output=True, timeout=90)
        return side.read_text(encoding="utf-8") if side.exists() else "__VISION_NO_OUTPUT__"
    except Exception as exc:  # noqa: BLE001
        return f"__VISION_ERROR__ {exc}"
    finally:
        for p in (tmp, side):
            try:
                p.unlink()
            except OSError:
                pass


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_index() -> dict[str, dict]:
    out: dict[str, dict] = {}
    if C.INDEX.exists():
        for line in C.INDEX.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                out[r["sha256"]] = r
    return out


def split_for(date: dt.date, track: str = "daily") -> tuple[str | None, str]:
    """Most recent split_log.csv row for `track` (daily | 4day) on or before `date`. Unknown stays unknown."""
    if not C.SPLITS.exists():
        return None, "unknown (no split_log.csv)"
    best = None
    with open(C.SPLITS, newline="") as f:
        for row in csv.DictReader(f):
            if row.get("track", "daily") != track:
                continue
            d = dt.date.fromisoformat(row["date"])
            if d <= date and (best is None or d > best[0]):
                best = (d, row["split"], row.get("provenance", "split_log"))
    return (best[1], f"split_log {best[0].isoformat()} ({best[2]})") if best else (None, "unknown (before first split_log row)")


PROGRAM_TOKENS = re.compile(r"QUICK PUMP|4[- ]?DAY PUMP|PUSH|PULL|LEGS?|ACTIVE REST|ARMS|CHEST|BACK|SHOULDERS?|ABS", re.I)


def ingest(no_vision: bool, limit: int | None, dry: bool) -> int:
    C.ensure_dirs()
    er = load_revl_engines()
    use_vision = er.vision_available(no_vision)
    seen = load_index()
    files = sorted(C.RAW.rglob("*.png"))
    todo = []
    for p in files:
        m = C.FNAME.match(p.name)
        if not m:
            print(f"skip (name does not match <date>_<daily|split|notes>[_n].png): {p}", file=sys.stderr)
            continue
        h = sha256(p)
        if h in seen:
            continue
        todo.append((p, m, h))
    if limit:
        todo = todo[:limit]
    print(f"{len(files)} images, {len(todo)} to ingest (vision={'on' if use_vision else 'off'})", file=sys.stderr)
    n = 0
    for p, m, h in todo:
        d = dt.date.fromisoformat(m.group(1))
        kind, split_day, num = m.group(2), m.group(3), int(m.group(4) or 1)
        y, w, wd = C.iso_parts(d)
        a = er.ocr_rapid(p)
        if a.startswith("__RAPID_ERROR__"):
            a = ""   # rapidocr unavailable: treat as no reading, record single-engine below
        b = vision_text(er, p) if use_vision else "__ENGINE_UNAVAILABLE__"
        merged, flags = er.merge_readings(a, b)
        text = "\n".join(merged)
        split, split_prov = split_for(d, "4day" if kind == "split" else "daily")
        rec = {
            "file": str(p.relative_to(C.DATA_ROOT)), "sha256": h,
            "date": d.isoformat(), "iso_year": y, "iso_week": w, "weekday": wd,
            "kind": kind, "split_day": int(split_day) if split_day else None, "n": num,
            "provenance": {"date_kind": "filename (set by capture step)", "split": split_prov},
            "split_label": split,
            "program_tokens": sorted({t.upper() for t in PROGRAM_TOKENS.findall(text)}),
            "engines": (["rapidocr"] if a else []) + (["vision"] if use_vision else []),
            "ocr_flags": flags[:10], "ocr_line_count": len(merged),
            "captured_at": dt.datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="seconds"),
            "ingested_at": dt.datetime.now().isoformat(timespec="seconds"),
        }
        if not dry:
            (C.OCR / f"{p.stem}.txt").write_text(text, encoding="utf-8")
            # upsert by file path: a re-captured frame replaces its old row (no duplicates in the index)
            keep = [ln for ln in (C.INDEX.read_text().splitlines() if C.INDEX.exists() else [])
                    if ln.strip() and json.loads(ln).get("file") != rec["file"]]
            C.INDEX.write_text("\n".join(keep + [json.dumps(rec)]) + "\n", encoding="utf-8")
        n += 1
        print(f"  {d} {kind}#{num} W{w:02d} split={split!r} lines={len(merged)} flags={len(flags)}", file=sys.stderr)
    return n


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-vision", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    ingest(a.no_vision, a.limit, a.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
