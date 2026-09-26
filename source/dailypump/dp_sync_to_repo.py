#!/usr/bin/env python3
"""Copy the Daily Pump OCR/text layer into the jon-fitness repo as a REVL-style reference folder.

Two-job workflow (agreed 2026-09-27):
  Job 1 (dp_capture.py + dp_ingest.py + dp_report.py) - screenshots, OCR and the readable weeks/
         report all stay in $DP_DATA_ROOT (default ~/DailyPumpData), OUTSIDE the repo.
  Job 2 (this script)                                 - copies only the TEXT/metadata layer -
         weeks/ (INDEX.md + raw_data.md), ocr/*.txt, index.jsonl, split_log.csv - into
         "<repo>/Daily Pump 2026/", mirroring how a REVL block folder sits in the repo.

Deliberately NEVER copies raw/ (the screenshot PNGs) into the repo - those are the one thing that
must stay outside it; see REPO/.gitignore ("Daily Pump*/", matching "REVL Block*/"). Both the source
(~/DailyPumpData) and repo copies are local-only and are never committed or pushed.

Usage:
    python source/dailypump/dp_sync_to_repo.py
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import dp_common as C  # noqa: E402

DEST = REPO / "Daily Pump 2026"
TEXT_ITEMS = ["weeks", "ocr", "index.jsonl", "split_log.csv"]


def sync_item(name: str) -> None:
    src = C.DATA_ROOT / name
    dst = DEST / name
    if not src.exists():
        return
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def main() -> int:
    if not C.DATA_ROOT.exists():
        print(f"error: {C.DATA_ROOT} does not exist", file=sys.stderr)
        return 1
    DEST.mkdir(parents=True, exist_ok=True)
    for item in TEXT_ITEMS:
        sync_item(item)
    print(f"synced text layer ({', '.join(TEXT_ITEMS)}) -> {DEST}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
