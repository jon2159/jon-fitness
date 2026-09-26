"""Shared paths and helpers for the Daily Pump local dataset.

PRIVACY: the raw captures, OCR text and index are a paid creator's content. They live OUTSIDE the
repo (default ~/DailyPumpData, which is not iCloud-synced like ~/Desktop) and are never committed.
Only code and aggregate analysis output belong in the repo.
"""
from __future__ import annotations

import datetime as dt
import os
import re
from pathlib import Path

DATA_ROOT = Path(os.environ.get("DP_DATA_ROOT", str(Path.home() / "DailyPumpData"))).expanduser()
RAW = DATA_ROOT / "raw"            # raw/<iso_year>/W<ww>/<date>_<kind>[_n].png
OCR = DATA_ROOT / "ocr"            # ocr/<stem>.txt  (merged reading, engine flags)
TMP = DATA_ROOT / ".tmp"
INDEX = DATA_ROOT / "index.jsonl"  # one JSON record per capture, keyed by sha256
SPLITS = DATA_ROOT / "split_log.csv"  # date,split,provenance  (which program/split is active from that date)
WEEKS = DATA_ROOT / "weeks"       # human-readable output: weeks/<iso_year>-W<ww>/{INDEX,raw_data}.md

FLOOR = dt.date(2026, 9, 14)   # scope agreed 2026-09-20: current week onward only; never capture earlier days
KINDS = ("daily", "split", "notes")   # daily workout | the 4-day split page | Julian's "read more" notes
# <date>_<kind>[_d<k>][_<frame>].png  e.g. 2026-09-20_daily_3.png, 2026-09-20_split_d2_4.png (4-Day track, Day 2, frame 4)
FNAME = re.compile(r"^(\d{4}-\d{2}-\d{2})_(daily|split|notes)(?:_d(\d))?(?:_(\d+))?\.png$")


def iso_parts(d: dt.date) -> tuple[int, int, str]:
    y, w, wd = d.isocalendar()
    return y, w, d.strftime("%A")


def raw_path(d: dt.date, kind: str, n: int = 1, day: int | None = None) -> Path:
    if kind not in KINDS:
        raise ValueError(f"kind must be one of {KINDS}")
    y, w, _ = iso_parts(d)
    dpart = f"_d{day}" if day else ""
    return RAW / str(y) / f"W{w:02d}" / f"{d.isoformat()}_{kind}{dpart}_{n}.png"


def ensure_dirs() -> None:
    for p in (RAW, OCR, TMP):
        p.mkdir(parents=True, exist_ok=True)
