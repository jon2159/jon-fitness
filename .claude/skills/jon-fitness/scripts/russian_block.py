#!/usr/bin/env python3
"""Generate the CSV for a Russian Strength Program block (the strength-block archetype).

See `references/russian-strength-program.md` for the framework, the eligibility gate,
and the CPT mapping. This script only does the arithmetic the source spreadsheet does:
target load = round(pct * 1RM) to the nearest plate step, laid out week by week, plus
warm-up / accessory / cool-down / (optional) conditioning rows in the skill's CSV schema.

Usage
-----
    python scripts/russian_block.py --variant v5 \
        --oneRM "squat=140,bench=100,deadlift=180,press=70,pullup=25" \
        --out clients/john_tan_fitness_plan.csv

    python scripts/russian_block.py --variant classic --focus squat \
        --oneRM "squat=180,bench=120,deadlift=220" --units kg

    python scripts/russian_block.py --variant masters --fat-loss \
        --oneRM "squat=110,bench=80,deadlift=140,press=55" \
        --wave-lifts "squat,deadlift"

Notes
-----
* `--oneRM` values are true or estimated 1-RMs. For a general-population client these
  should be ESTIMATED from a sub-maximal rep test (Table 10-25), not a true single.
* `--wave-lifts` restricts the linear wave to a subset; the other main lifts are
  written as fixed maintenance work (3 x 6-8 @ ~70%).
* The CSV is a starting point. The trainer still edits it against the .md reasoning
  and runs `validate_plan.py`.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

CSV_HEADER = [
    "week", "day", "session", "block", "exercise", "sets", "reps",
    "intensity", "rest", "tempo", "duration", "progression", "notes",
]

# Canonical lift names + their default accessories and workout grouping.
LIFTS = {
    "squat": {"name": "Back Squat", "group": "A"},
    "bench": {"name": "Bench Press", "group": "A"},
    "deadlift": {"name": "Deadlift", "group": "B"},
    "press": {"name": "Military Press", "group": "B"},
    "pullup": {"name": "Weighted Pull-up", "group": "B"},
}
ACCESSORIES = {
    "A": [("Bulgarian Split Squat", "3", "10/side"), ("Dips", "3", "8-12")],
    "B": [("Romanian Deadlift", "3", "10"), ("Face Pull", "3", "15")],
}

WAVE_PROG = "linear wave (plan: Strength Block); autoregulate per RPE (plan: Autoregulation)"
ACC_PROG = "double progression 8-12; 2-for-2 then +5% (Wk07 Ch11 p7, p20)"

# Progression-day scheme per week: (sets, reps, pct). Anchor days are always 6x2 @ anchor_pct.
V5_WAVE = [
    (6, 2, 0.80), (6, 4, 0.80), (6, 5, 0.80), (6, 6, 0.80),
    (5, 5, 0.85), (4, 4, 0.90), (3, 3, 0.95), (2, 2, 1.00), (1, 1, 1.05),
]
# Classic Russian Squat Routine, 3 days/wk. Per week: (Mon, Wed, Fri) each (sets, reps, pct).
CLASSIC_WAVE = [
    [(6, 2, 0.80), (6, 3, 0.80), (6, 2, 0.80)],
    [(6, 4, 0.80), (6, 2, 0.80), (6, 5, 0.80)],
    [(6, 2, 0.80), (6, 6, 0.80), (6, 2, 0.80)],
    [(5, 5, 0.85), (6, 2, 0.80), (4, 4, 0.90)],
    [(6, 2, 0.80), (3, 3, 0.95), (6, 2, 0.80)],
    [(2, 2, 1.00), (6, 2, 0.80), (1, 1, 1.05)],
]
# Masters variant, 2 days/wk, 8 weeks. Anchor day @ 0.65. General-knowledge adaptation.
MASTERS_WAVE = [
    (6, 3, 0.75), (6, 4, 0.75), (6, 5, 0.775), (5, 5, 0.80),
    (5, 4, 0.85), (4, 3, 0.875), (3, 2, 0.925), (2, 2, 0.975),
]
MASTERS_ANCHOR_PCT = 0.65


def parse_one_rm(spec: str) -> dict[str, float]:
    out: dict[str, float] = {}
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            sys.exit(f"error: --oneRM entry {part!r} is not name=value")
        k, v = part.split("=", 1)
        k = k.strip().lower()
        if k not in LIFTS:
            sys.exit(f"error: unknown lift {k!r} (known: {', '.join(LIFTS)})")
        try:
            out[k] = float(v)
        except ValueError:
            sys.exit(f"error: --oneRM value for {k!r} is not a number: {v!r}")
    if not out:
        sys.exit("error: --oneRM is empty")
    return out


def round_load(value: float, step: float) -> float:
    return round(value / step) * step


def fmt(value: float) -> str:
    return f"{value:g}"


def intensity_cell(pct: float, one_rm: float, step: float, unit: str, anchor: bool) -> str:
    load = round_load(pct * one_rm, step)
    tag = " - anchor/speed" if anchor else ""
    if load <= 0:
        return f"{round(pct * 100)}% 1RM - bodyweight{tag}"
    return f"{round(pct * 100)}% 1RM ({fmt(load)} {unit}){tag}"


def rest_for(pct: float) -> str:
    return "3-5 min" if pct >= 0.85 else "2-3 min"


def row(week, day, session, block, exercise, sets, reps, intensity, rest,
        tempo="2-0-1", duration="", progression="", notes="") -> list[str]:
    return [str(week), day, session, block, exercise, str(sets), str(reps),
            intensity, rest, tempo, duration, progression, notes]


def warmup_row(week, day, session) -> list[str]:
    return row(week, day, session, "warm-up",
              "Movement-phase warm-up: 5 patterns + ramp sets to first work load",
              1, "-", "bodyweight -> light", "-", "controlled",
              "8-10 min", "-", "Session components Wk07 Ch11 p18")


def cooldown_row(week, day, session) -> list[str]:
    return row(week, day, session, "cool-down",
              "Static stretch: hip flexors, hamstrings, pecs, lats",
              1, "2/side", "to slight discomfort", "-", "hold 20-30s",
              "5 min", "-", "Flexibility FITT-VP Table 11-7 (Wk07 Ch11 p25)")


def conditioning_rows(week, unit) -> list[list[str]]:
    return [
        row(week, "Wed", "cond", "conditioning",
            "Zone 1-2 low-impact cardio (bike / brisk walk / row)",
            1, "-", "< VT1 / RPE 3-4", "-", "-", "30-40 min", "+<=10%/wk",
            "Fat-loss: Wk09 Ch12 p32 (150-250 min/wk). Kept off heavy lower-body days."),
        row(week, "Sat", "cond", "conditioning",
            "Zone 1-2 low-impact cardio + easy accessory circuit",
            1, "-", "< VT1 / RPE 3-4", "-", "-", "30-45 min", "+<=10%/wk",
            "Fat-loss: energy expenditure toward the weekly target."),
    ]


def emit_v5(one_rm, wave_lifts, step, unit, fat_loss) -> list[list[str]]:
    rows: list[list[str]] = []
    day_map = [("Mon", "A", True), ("Tue", "B", True),
               ("Thu", "A", False), ("Fri", "B", False)]
    for wk in range(1, 10):
        p_sets, p_reps, p_pct = V5_WAVE[wk - 1]
        for day, grp, is_anchor in day_map:
            rows.append(warmup_row(wk, day, grp))
            grp_lifts = [k for k, v in LIFTS.items() if v["group"] == grp]
            for k in grp_lifts:
                if k not in one_rm:
                    continue
                nm = LIFTS[k]["name"]
                if k in wave_lifts:
                    if is_anchor:
                        sets, reps, pct = 6, 2, 0.80
                    else:
                        sets, reps, pct = p_sets, p_reps, p_pct
                    note = "wave lift"
                    if not is_anchor and wk == 9:
                        note = "RETEST week - see Retest Plan (Wk06 Ch10 p69-74)"
                    rows.append(row(
                        wk, day, grp, "strength", nm, sets, reps,
                        intensity_cell(pct, one_rm[k], step, unit, is_anchor),
                        rest_for(pct), "2-0-1", "", WAVE_PROG, note))
                else:
                    rows.append(row(
                        wk, day, grp, "strength", nm, 3, "6-8",
                        f"~70% 1RM ({fmt(round_load(0.70 * one_rm[k], step))} {unit})",
                        "2-3 min", "2-0-1", "", ACC_PROG,
                        "maintenance lift (not on the wave)"))
            for nm, sets, reps in ACCESSORIES[grp]:
                rows.append(row(wk, day, grp, "accessory", nm, sets, reps,
                                "RPE 7-8", "60-90s", "2-0-1", "", ACC_PROG, ""))
            rows.append(cooldown_row(wk, day, grp))
        if fat_loss:
            rows.extend(conditioning_rows(wk, unit))
    return rows


def emit_classic(one_rm, focus, step, unit, fat_loss) -> list[list[str]]:
    rows: list[list[str]] = []
    if focus not in one_rm:
        sys.exit(f"error: --focus {focus!r} has no --oneRM value")
    days = ["Mon", "Wed", "Fri"]
    others = [k for k in one_rm if k != focus]
    for wk in range(1, 7):
        for di, day in enumerate(days):
            sets, reps, pct = CLASSIC_WAVE[wk - 1][di]
            is_anchor = (sets, reps) == (6, 2)
            rows.append(warmup_row(wk, day, "full"))
            note = "focus / wave lift"
            if wk == 6 and day == "Fri":
                note = "RETEST week - see Retest Plan (Wk06 Ch10 p69-74)"
            rows.append(row(
                wk, day, "full", "strength", LIFTS[focus]["name"], sets, reps,
                intensity_cell(pct, one_rm[focus], step, unit, is_anchor),
                rest_for(pct), "2-0-1", "", WAVE_PROG, note))
            # maintain one other main lift per day, rotating
            if others:
                k = others[di % len(others)]
                rows.append(row(
                    wk, day, "full", "strength", LIFTS[k]["name"], 3, "6-8",
                    f"~70% 1RM ({fmt(round_load(0.70 * one_rm[k], step))} {unit})",
                    "2-3 min", "2-0-1", "", ACC_PROG, "maintenance lift"))
            for nm, s, r in ACCESSORIES["A" if di == 0 else "B"]:
                rows.append(row(wk, day, "full", "accessory", nm, s, r,
                                "RPE 7-8", "60-90s", "2-0-1", "", ACC_PROG, ""))
            rows.append(cooldown_row(wk, day, "full"))
        if fat_loss:
            rows.extend(conditioning_rows(wk, unit))
    return rows


def emit_masters(one_rm, wave_lifts, step, unit, fat_loss) -> list[list[str]]:
    rows: list[list[str]] = []
    day_map = [("Mon", "A", True), ("Thu", "B", False)]
    for wk in range(1, 9):
        p_sets, p_reps, p_pct = MASTERS_WAVE[wk - 1]
        for day, grp, is_anchor in day_map:
            rows.append(warmup_row(wk, day, grp))
            for k in one_rm:
                nm = LIFTS[k]["name"]
                if k in wave_lifts:
                    if is_anchor:
                        sets, reps, pct = 5, 5, MASTERS_ANCHOR_PCT
                    else:
                        sets, reps, pct = p_sets, p_reps, p_pct
                    note = "wave lift (Masters variant - reduced load, General knowledge adaptation)"
                    if not is_anchor and wk == 8:
                        note = "final week - retest via rep-max -> estimated 1RM (Wk06 Ch10 p75)"
                    rows.append(row(
                        wk, day, grp, "strength", nm, sets, reps,
                        intensity_cell(pct, one_rm[k], step, unit, is_anchor),
                        rest_for(pct), "2-0-1", "", WAVE_PROG, note))
                else:
                    rows.append(row(
                        wk, day, grp, "strength", nm, 3, "6-8",
                        f"~65% 1RM ({fmt(round_load(0.65 * one_rm[k], step))} {unit})",
                        "2-3 min", "2-0-1", "", ACC_PROG, "maintenance lift"))
            for nm, s, r in ACCESSORIES[grp]:
                rows.append(row(wk, day, grp, "accessory", nm, s, r,
                                "RPE 7", "60-90s", "2-0-1", "", ACC_PROG, ""))
            rows.append(cooldown_row(wk, day, grp))
        if fat_loss:
            rows.extend(conditioning_rows(wk, unit))
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--variant", choices=["v5", "classic", "masters"], default="v5")
    ap.add_argument("--oneRM", required=True,
                    help='e.g. "squat=140,bench=100,deadlift=180,press=70,pullup=25"')
    ap.add_argument("--wave-lifts", default="",
                    help="subset to put on the wave (default: all provided lifts)")
    ap.add_argument("--focus", default="squat",
                    help="classic variant only: the single lift on the wave")
    ap.add_argument("--units", choices=["kg", "lb"], default="kg")
    ap.add_argument("--fat-loss", action="store_true",
                    help="add Zone 1-2 conditioning rows on non-lower-body days")
    ap.add_argument("--out", default="-",
                    help="output CSV path (default: stdout)")
    args = ap.parse_args(argv)

    one_rm = parse_one_rm(args.oneRM)
    step = 2.5 if args.units == "kg" else 5.0
    wave_lifts = ([w.strip().lower() for w in args.wave_lifts.split(",") if w.strip()]
                  or list(one_rm))
    for w in wave_lifts:
        if w not in LIFTS:
            sys.exit(f"error: unknown wave lift {w!r}")

    if args.variant == "v5":
        rows = emit_v5(one_rm, wave_lifts, step, args.units, args.fat_loss)
    elif args.variant == "classic":
        rows = emit_classic(one_rm, args.focus.lower(), step, args.units, args.fat_loss)
    else:
        rows = emit_masters(one_rm, wave_lifts, step, args.units, args.fat_loss)

    out = sys.stdout if args.out == "-" else open(args.out, "w", newline="")
    try:
        w = csv.writer(out)
        w.writerow(CSV_HEADER)
        w.writerows(rows)
    finally:
        if out is not sys.stdout:
            out.close()
            print(f"wrote {len(rows)} rows to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
