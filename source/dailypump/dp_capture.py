#!/usr/bin/env python3
"""Capture the current week of the Daily Pump app (macOS, iOS app on Apple Silicon) into the local dataset.

What it captures (CURRENT WEEK ONWARD ONLY - the Pump Archive is deliberately NOT touched):
  * daily  : the Daily Pump tab for every date chip in the current week that is <= today
  * split  : the 4-Day tab, Day 1..4 (once per ISO week)
  * notes  : "Julian's Notes" (once per ISO week) - carries the split name / week counter / changes

Only the app's own window is captured (screencapture -l <window id>), never the whole screen.
Frames are overlapping scroll captures: <date>_<kind>[_d<k>]_<frame>.png under
$DP_DATA_ROOT/raw/<iso_year>/W<ww>/  (default ~/DailyPumpData - local only, never committed).

Idempotent: days already captured are skipped, so a catch-up run only fills gaps.
Needs: Accessibility + Screen Recording permission for the process that runs it, the Mac awake and
logged in, and the app signed in. Run `python source/dailypump/dp_capture.py --dry-run` to see the plan.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import dp_common as C  # noqa: E402
import dp_ingest as I  # noqa: E402

DPUI = HERE / "dpui"
APP = "/Applications/DailyPump.app"

# Window-relative coordinates in points (the window is 375 x 699), read off a 2x screenshot.
SCROLL_AT = (187, 450)
TAB = {"daily": (80, 394.5), "quick": (188, 394.5), "split": (295.5, 394.5)}
DAILY_CHIPS_X = [33, 84.5, 136, 187.5, 238.5, 290, 341]   # left -> right = newest -> oldest
DAILY_CHIP_Y = 292.5
SPLIT_CHIPS_X = [53, 142.5, 232, 322]                     # Day 1..4
SPLIT_CHIP_Y = 290
NOTES_READ_MORE = (312.5, 151)
NOTES_CLOSE = (349, 157.5)
SCROLL_STEP = -260
MAX_FRAMES = 30

_win = None
_er = None
BACK_ARROW = (14, 73.5)


def log(msg: str) -> None:
    print(f"[dp_capture {dt.datetime.now():%H:%M:%S}] {msg}", file=sys.stderr, flush=True)


def window():
    r = subprocess.run([str(DPUI), "window"], capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    i, x, y, w, h = (int(v) for v in r.stdout.split())
    return {"id": i, "x": x, "y": y, "w": w, "h": h}


def activate() -> dict:
    global _win
    subprocess.run(["open", "-a", APP], capture_output=True)
    for _ in range(15):
        subprocess.run(["osascript", "-e", 'tell application "DailyPump" to activate'], capture_output=True)
        time.sleep(1)
        _win = window()
        if _win:
            return _win
    sys.exit("error: DailyPump window not found on screen (is the Mac awake, logged in and the app signed in?)")


def click(rel) -> None:
    w = window() or _win
    subprocess.run([str(DPUI), "click", str(w["x"] + rel[0]), str(w["y"] + rel[1])])
    time.sleep(1.6)


def scroll(dy: int) -> None:
    w = window() or _win
    subprocess.run([str(DPUI), "scroll", str(w["x"] + SCROLL_AT[0]), str(w["y"] + SCROLL_AT[1]), str(dy)])


def snap(dest: Path) -> None:
    """Capture only the app window. If the window vanished (closed/minimised) or the capture fails, reopen the
    app and retry a few times before giving up."""
    global _win
    dest.parent.mkdir(parents=True, exist_ok=True)
    err = ""
    for attempt in range(4):
        w = window()
        if not w:
            subprocess.run(["open", "-a", APP], capture_output=True)
            subprocess.run(["osascript", "-e", 'tell application "DailyPump" to activate'], capture_output=True)
            time.sleep(2.5)
            w = window()
        if w:
            _win = w
            r = subprocess.run(["screencapture", "-x", "-o", "-l", str(w["id"]), str(dest)], capture_output=True, text=True)
            if r.returncode == 0 and dest.exists():
                return
            err = r.stderr.strip()
        time.sleep(1.5)
    sys.exit(f"error: window capture failed ({err or 'no DailyPump window'}). Usual causes: the screen is locked or asleep, "
             "or Screen Recording is not granted to DailyPumpCapture.app.")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def to_top() -> None:
    for _ in range(9):
        scroll(400)
        time.sleep(0.25)
    time.sleep(0.6)


def screen_text() -> str:
    tmp = C.TMP / "check.png"
    snap(tmp)
    text = I.vision_text(_er, tmp)
    tmp.unlink(missing_ok=True)
    return text


def home_ok() -> bool:
    """True when the Home screen top is showing (Julian's Notes / week header present)."""
    text = screen_text()
    return "Julian" in text and "Notes" in text


def wait_out_splash(max_seconds: int = 25) -> None:
    """The launch splash ('THE DAILY PUMP' over a photo) has no Home content and no back arrow - clicking
    through it wastes attempts. Just wait for it to clear on its own before the normal retry logic runs."""
    waited = 0.0
    while waited < max_seconds:
        text = screen_text()
        if "Julian" in text or "Home" in text or "Resources" in text:
            return  # past the splash (Home, or at least the app chrome, is up)
        if text.strip():
            return  # some other real screen; let ensure_home's normal retry handle it
        log(f"splash screen up, waiting ({waited:.0f}s/{max_seconds}s)")
        time.sleep(3)
        waited += 3


def relaunch() -> None:
    """Force-quit and reopen the app. Used when Home is showing but its data (e.g. the date strip) looks
    stale, since a normal 'activate' does not make the app refresh its idea of 'today'."""
    log("relaunching the app to clear stale state")
    r = subprocess.run(["pgrep", "-f", "DailyPump.app/DailyPump"], capture_output=True, text=True)
    for pid in r.stdout.split():
        subprocess.run(["kill", "-9", pid], capture_output=True)
    time.sleep(2)
    activate()
    wait_out_splash()


def ensure_home() -> None:
    """Scroll to the top and make sure we are on Home; use the back arrow if we wandered into a detail page.
    Aborts rather than capturing junk."""
    wait_out_splash()
    for attempt in range(4):
        to_top()
        if home_ok():
            return
        log(f"not on Home (attempt {attempt + 1}); pressing back")
        click(BACK_ARROW)
    sys.exit("error: could not get back to the Home screen; stopping to avoid capturing the wrong pages.")


STALL_RETRIES = 3  # a scroll that doesn't register (page still settling from a click, etc.) is common;
                   # don't mistake it for "reached the end of the page" without retrying first.


def capture_frames(stem_fn) -> int:
    """Scroll from the top, saving frames until the view genuinely stops changing. stem_fn(n) -> Path.
    A no-change reading is retried (re-scroll + re-snap) before being accepted as the real end, so a
    single missed scroll early on cannot truncate the capture (seen 2026-09-24: 1 frame, header only,
    zero exercises - the first scroll after the chip click silently failed to register)."""
    prev, n = None, 0
    for _ in range(MAX_FRAMES):
        tmp = C.TMP / "frame.png"
        C.TMP.mkdir(parents=True, exist_ok=True)
        snap(tmp)
        h = sha(tmp)
        if h == prev:
            for retry in range(STALL_RETRIES):
                scroll(SCROLL_STEP)
                time.sleep(1.0)
                snap(tmp)
                h = sha(tmp)
                if h != prev:
                    break
            if h == prev:
                break  # genuinely no more content after retries
        n += 1
        dest = stem_fn(n)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(tmp), dest)
        prev = h
        scroll(SCROLL_STEP)
        time.sleep(0.9)
    return n


def week_range(vision_er) -> tuple[dt.date, dt.date]:
    """Read 'September 14 - September 20' off the top of the Home screen."""
    tmp = C.TMP / "header.png"
    snap(tmp)
    text = I.vision_text(vision_er, tmp)
    tmp.unlink(missing_ok=True)
    m = re.search(r"([A-Z][a-z]+)\s+(\d{1,2})\s*[-–]\s*([A-Z][a-z]+)\s+(\d{1,2})", text)
    if not m:
        sys.exit("error: could not read the week range from the Home screen (OCR).")
    today = dt.date.today()

    def mk(mon: str, day: str) -> dt.date:
        d = dt.datetime.strptime(f"{mon[:3]} {day} {today.year}", "%b %d %Y").date()
        if d > today + dt.timedelta(days=200):
            d = d.replace(year=today.year - 1)
        return d

    return mk(m.group(1), m.group(2)), mk(m.group(3), m.group(4))


MON = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def chip_dates(vision_er) -> list[dt.date]:
    """Read the 7 date chips (left -> right) off the Home screen. The strip is a ROLLING 7 days ending today,
    NOT the header's week range. Never guess: abort unless exactly 7 labels are read and they descend by one day."""
    tmp = C.TMP / "chips.png"
    snap(tmp)
    text = " ".join(I.vision_text(vision_er, tmp).split())
    tmp.unlink(missing_ok=True)
    today = dt.date.today()
    found = re.findall(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s*(\d{1,2})\b", text)
    out = []
    for mon, day in found:
        d = dt.date(today.year, MON[mon], int(day))
        if d > today + dt.timedelta(days=31):
            d = d.replace(year=today.year - 1)
        out.append(d)
    out = out[:7]
    ok = len(out) == 7 and all((out[i] - out[i + 1]).days == 1 for i in range(6))
    if not ok:
        sys.exit(f"error: could not read the 7 date chips reliably (got {[d.isoformat() for d in out]}); stopping.")
    return out


def chip_dates_fresh(vision_er) -> list[dt.date]:
    """chip_dates(), but guards against the app's Home screen showing a STALE 'today' (its newest chip still
    one or more days behind the system clock - seen 2026-09-22: chips read as ending 09-21 at 13:09, only
    fixed by relaunching). Never trust a stale reading silently: relaunch and retry once, then abort loudly
    rather than reporting a day as already-captured when it was never actually looked at."""
    today = dt.date.today()
    chips = chip_dates(vision_er)
    if chips[0] == today:
        return chips
    log(f"chip strip looks stale (newest chip {chips[0]}, system today {today})")
    relaunch()
    click(TAB["daily"])
    ensure_home()
    chips = chip_dates(vision_er)
    if chips[0] == today:
        log("stale strip cleared after relaunch")
        return chips
    sys.exit(f"error: date strip still stale after relaunch (newest chip {chips[0]}, today {today}); "
             "stopping rather than risk silently skipping today or mislabelling a capture.")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="print the plan; capture nothing")
    ap.add_argument("--check", action="store_true",
                    help="filesystem-only check (never touches the app): exit 0 if nothing is missing, 10 if a capture is needed")
    ap.add_argument("--force", action="store_true", help="recapture days/pages that already exist")
    ap.add_argument("--only", choices=["daily", "split", "notes"], nargs="+", help="limit what is captured")
    a = ap.parse_args(argv)
    want = set(a.only or ["daily", "split", "notes"])
    C.ensure_dirs()
    if a.check:
        today = dt.date.today()
        window7 = [today - dt.timedelta(days=i) for i in range(7)]      # the app's strip is a rolling 7 days
        missing = [d for d in window7 if d >= C.FLOOR and not C.raw_path(d, "daily", 1).exists()]
        iso = today.isocalendar()
        wk = C.RAW / str(iso.year) / f"W{iso.week:02d}"
        need_split = not (wk.exists() and list(wk.glob("*_split_d1_1.png")))
        need_notes = not (wk.exists() and list(wk.glob("*_notes_1.png")))
        log(f"check: missing daily {[d.isoformat() for d in missing]}, split {'needed' if need_split else 'ok'}, notes {'needed' if need_notes else 'ok'}")
        return 10 if (missing or need_split or need_notes) else 0
    global _er
    er = _er = I.load_revl_engines()
    if not er.vision_available(False):
        sys.exit("error: Apple Vision helper unavailable (needs swiftc) - cannot read the week header.")
    win = activate()
    log(f"window id={win['id']} {win['w']}x{win['h']}")
    ensure_home()
    click(TAB["daily"])
    to_top()
    today = dt.date.today()
    chips = chip_dates_fresh(er)
    log(f"date chips (left->right): {chips[0]} .. {chips[-1]}; today {today}")
    iso = today.isocalendar()
    done_split = list((C.RAW / str(iso.year) / f"W{iso.week:02d}").glob("*_split_d1_1.png")) if (C.RAW / str(iso.year)).exists() else []
    done_notes = list((C.RAW / str(iso.year) / f"W{iso.week:02d}").glob("*_notes_1.png")) if (C.RAW / str(iso.year)).exists() else []

    plan = []
    if "daily" in want:
        for i, x in enumerate(DAILY_CHIPS_X):
            d = chips[i]
            if d < C.FLOOR or d > today:
                continue
            if C.raw_path(d, "daily", 1).exists() and not a.force:
                continue
            plan.append(("daily", d, x))
    if "split" in want and (a.force or not done_split):
        plan.append(("split", today, None))
    if "notes" in want and (a.force or not done_notes):
        plan.append(("notes", today, None))
    log("plan: " + (", ".join(f"{k}:{d}" for k, d, _ in plan) or "nothing to do (all captured)"))
    if a.dry_run:
        return 0

    new = 0
    prev_daily_hash = None
    for kind, d, x in plan:
        if kind == "daily":
            captured = False
            for attempt in range(3):
                ensure_home(); click(TAB["daily"]); ensure_home()
                click((x, DAILY_CHIP_Y)); ensure_home()
                tmp = C.TMP / "verify.png"
                snap(tmp)
                h = sha(tmp)
                if prev_daily_hash is not None and h == prev_daily_hash:
                    log(f"daily {d}: chip click did not register (attempt {attempt + 1}); retrying")
                    continue
                n = capture_frames(lambda k, d=d: C.raw_path(d, "daily", k))
                if n == 0:
                    log(f"daily {d}: capture produced nothing (attempt {attempt + 1}); retrying")
                    continue
                log(f"daily {d}: {n} frames"); new += n
                prev_daily_hash = h
                captured = True
                break
            if not captured:
                log(f"daily {d}: could not capture after retries; leaving as missing for the next run")
        elif kind == "split":
            ensure_home(); click(TAB["split"]); ensure_home()
            for day, sx in enumerate(SPLIT_CHIPS_X, start=1):
                ensure_home(); click((sx, SPLIT_CHIP_Y)); ensure_home()
                n = capture_frames(lambda k, d=d, day=day: C.raw_path(d, "split", k, day))
                log(f"split {d} day {day}: {n} frames"); new += n
            ensure_home(); click(TAB["daily"]); ensure_home()
        elif kind == "notes":
            ensure_home()
            click(NOTES_READ_MORE); time.sleep(1.5)
            n = capture_frames(lambda k, d=d: C.raw_path(d, "notes", k))
            log(f"notes {d}: {n} frames"); new += n
            click(NOTES_CLOSE); ensure_home()
    log(f"done: {new} new frames")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
