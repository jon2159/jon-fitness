#!/usr/bin/env python3
"""Build REVL-style human-readable output from the Daily Pump index: one INDEX.md (catalog) and one
raw_data.md (deduplicated OCR transcript) per ISO week, under $DP_DATA_ROOT/weeks/.

Mirrors source/extract_revl.py's output shape (source/revl_raw_data.md + a block INDEX.md): this is
build output, safe to delete and regenerate any time from index.jsonl + ocr/*.txt. It never touches
raw/ (the source screenshots) or the scheduler's own path scheme.

Each captured page (a day's Daily Pump workout, a 4-Day split day, or the week's notes) is an
overlapping series of scrolled screenshots. Frame texts are deduplicated (exact-line, order-preserving)
into ONE continuous transcript per page, the way a REVL session is one reading of one poster.

Usage:
    python source/dailypump/dp_report.py            # rebuild every week found in the index
    python source/dailypump/dp_report.py --week 2026-W39
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import dp_common as C  # noqa: E402

CHROME = re.compile(
    r"^(dailypump|september|home|resources|journal|settings|start workout|read more|"
    r"daily pump$|quick pump$|4-day$|julian|the pump archive|revisit past|"
    r"warm up|add to workout|notes for the week)", re.I)
# Real page titles (body part, or the split's own day-name). Deliberately excludes the bare chip
# labels ("Day 1".."Day 4") that are always visible on every 4-Day Pump page regardless of which one
# is open - matching those would make every split day report as "Day 1" (the first, always-present chip).
TITLE_WORDS = re.compile(
    r"^(Chest|Back|Shoulders|Biceps.?Triceps|Quads.?Adductors|Hamstrings.?Glutes|Calves.?Abs.?Neck|"
    r"Upper body \d|Lower body \d|Active Rest|Push$|Pull$|Legs$)\b", re.I)
CHIP_LABEL = re.compile(r"^Day \d+$", re.I)


def norm(line: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"\s*\[\?[^\]]*\]", "", line)).strip()


def clean_lines(raw: str) -> list[str]:
    return [ln for ln in (norm(l) for l in raw.splitlines()) if ln and not CHROME.match(ln)]


def load_index() -> list[dict]:
    if not C.INDEX.exists():
        return []
    return [json.loads(l) for l in C.INDEX.read_text().splitlines() if l.strip()]


def week_range(iso_year: int, iso_week: int) -> tuple[dt.date, dt.date]:
    mon = dt.date.fromisocalendar(iso_year, iso_week, 1)
    return mon, mon + dt.timedelta(days=6)


def group_key(r: dict) -> tuple[str, str, int | None]:
    return (r["date"], r["kind"], r.get("split_day"))


def page_title(kind: str, split_day: int | None, lines: list[str]) -> str:
    for ln in lines:
        if CHIP_LABEL.match(ln):
            continue  # one of the always-visible "Day N" chip labels, not this page's actual title
        m = TITLE_WORDS.match(ln)
        if m:
            return m.group(0)
    if kind == "split" and split_day:
        return f"(title not read — Day {split_day})"
    if kind == "notes":
        return "Julian's Notes"
    return "(title not read)"


def dedupe_across_frames(frame_lines_list: list[list[str]]) -> tuple[list[str], int]:
    """Overlapping scroll captures repeat most lines frame-to-frame; keep first occurrence, preserve
    order. Returns (transcript_lines, count_of_disagreement_markers_seen_upstream)."""
    seen: set[str] = set()
    out: list[str] = []
    for lines in frame_lines_list:
        for ln in lines:
            key = ln.lower()
            if key not in seen:
                seen.add(key)
                out.append(ln)
    return out, 0


def build_week(iso_year: int, iso_week: int, rows: list[dict]) -> None:
    start, end = week_range(iso_year, iso_week)
    wk_dir = C.WEEKS / f"{iso_year}-W{iso_week:02d}"
    wk_dir.mkdir(parents=True, exist_ok=True)

    groups: dict[tuple, list[dict]] = defaultdict(list)
    for r in rows:
        groups[group_key(r)].append(r)

    index_rows = []
    raw_sections = []
    split_labels: dict[str, str] = {}

    order = sorted(groups, key=lambda k: (k[0], {"daily": 0, "split": 1, "notes": 2}[k[1]], k[2] or 0))
    for date_s, kind, split_day in order:
        recs = sorted(groups[(date_s, kind, split_day)], key=lambda r: r["n"])
        frame_texts = []
        for r in recs:
            ocr_path = C.OCR / (Path(r["file"]).stem + ".txt")
            frame_texts.append(clean_lines(ocr_path.read_text()) if ocr_path.exists() else [])
        transcript, _ = dedupe_across_frames(frame_texts)
        title = page_title(kind, split_day, transcript)
        d = dt.date.fromisoformat(date_s)
        weekday = d.strftime("%A")
        split_label = recs[0].get("split_label") or "(unknown — no split_log.csv row for this date)"
        track = "4day" if kind == "split" else "daily"
        split_labels[track] = split_label
        flag_total = sum(len(r.get("ocr_flags", [])) for r in recs)

        index_rows.append({
            "date": date_s, "weekday": weekday, "kind": kind, "split_day": split_day,
            "title": title, "frames": len(recs), "flags": flag_total,
        })

        heading = f"{weekday} {date_s} — " + (
            f"4-Day Pump Day {split_day}" if kind == "split" else
            "Julian's Notes" if kind == "notes" else "Daily Pump")
        raw_sections.append(
            f"## {heading} — {title}\n\n"
            f"_Split: {split_label}_  ·  _{len(recs)} overlapping capture frame(s), deduplicated_"
            + (f"  ·  _{flag_total} OCR disagreement flag(s) in the source frames_" if flag_total else "")
            + "\n\n```\n" + "\n".join(transcript) + "\n```\n"
        )

    n_daily = sum(1 for r in index_rows if r["kind"] == "daily")
    n_split_days = sum(1 for r in index_rows if r["kind"] == "split")
    index_md = [
        f"# Daily Pump — {iso_year} W{iso_week:02d} ({start:%B %d} – {end:%B %d})\n",
        "Auto-generated by `source/dailypump/dp_report.py` from the local capture index. "
        "Regenerate any time; never hand-edit.\n",
        "Julian Smith's paid programming, captured locally for personal reference only — "
        "never published or committed. See `../README.md`.\n",
        f"**{n_daily} Daily Pump day(s)** captured this week"
        + (f", **{n_split_days}/4** 4-Day Pump days" if n_split_days else "")
        + (", notes captured" if any(r["kind"] == "notes" for r in index_rows) else ", notes not captured")
        + ".\n",
    ]
    if "daily" in split_labels:
        index_md.append(f"**Daily-split label:** {split_labels['daily']}\n")
    if "4day" in split_labels:
        index_md.append(f"**4-Day-split label:** {split_labels['4day']}\n")
    index_md.append("| Date | Day | Page | Title | Frames | OCR flags |")
    index_md.append("|---|---|---|---|--:|--:|")
    for r in index_rows:
        page = f"4-Day #{r['split_day']}" if r["kind"] == "split" else r["kind"].capitalize()
        index_md.append(f"| {r['date']} | {r['weekday']} | {page} | {r['title']} | {r['frames']} | {r['flags']} |")
    missing = [(start + dt.timedelta(days=i)) for i in range(7)
               if (start + dt.timedelta(days=i)) <= dt.date.today()
               and (start + dt.timedelta(days=i)).isoformat() not in {r["date"] for r in index_rows if r["kind"] == "daily"}]
    if missing:
        index_md.append("\n**Not captured (yet):** " + ", ".join(d.isoformat() for d in missing))
    (wk_dir / "INDEX.md").write_text("\n".join(index_md) + "\n", encoding="utf-8")

    raw_md = [
        f"# Daily Pump — {iso_year} W{iso_week:02d} — raw extracted text\n",
        "Auto-generated by `source/dailypump/dp_report.py`. Two independent OCR readers per screenshot "
        "(rapidocr-onnxruntime + Apple Vision, see `../../extract_revl.py`); `[?]` in the source frames "
        "marks lines the two engines disagreed on (stripped here for readability — see `../ocr/*.txt` "
        "for the flagged per-frame originals). Each page below is several overlapping scroll captures "
        "merged into one deduplicated transcript, in the order the app showed them: never re-order or "
        "hand-edit — treat any specific load/rep/tempo here as *approximate*, cross-check the source "
        f"frames in `../raw/{iso_year}/W{iso_week:02d}/` before treating a number as fact.\n",
        "---\n",
    ]
    raw_md.extend(raw_sections)
    (wk_dir / "raw_data.md").write_text("\n".join(raw_md), encoding="utf-8")
    print(f"W{iso_week:02d} {iso_year}: {len(index_rows)} pages -> {wk_dir}", file=sys.stderr)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--week", help="only rebuild one week, e.g. 2026-W39")
    a = ap.parse_args(argv)
    rows = load_index()
    if not rows:
        print("index is empty; nothing to report", file=sys.stderr)
        return 0
    by_week: dict[tuple, list] = defaultdict(list)
    for r in rows:
        by_week[(r["iso_year"], r["iso_week"])].append(r)
    C.WEEKS.mkdir(parents=True, exist_ok=True)
    for (y, w), wk_rows in sorted(by_week.items()):
        if a.week and a.week != f"{y}-W{w:02d}":
            continue
        build_week(y, w, wk_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
