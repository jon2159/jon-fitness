#!/usr/bin/env python3
"""Generate the 12-week, 4-day hybrid strength + conditioning block as skill-schema CSV.

Spec: `docs/twelve-week-four-day-program.md` (decisions, evidence grades, limits).
Builds on `russian_block.py` (V5 wave, source: the V5 workbook) and adds the conditioning,
primer, carry, test and rebuild layers. Only the V5 wave numbers are source; everything
else is coach judgement, labelled in the `notes` column.

Weeks 1-9  : V5 wave on the wave lifts (default squat, bench, deadlift); press and pull-up at
             maintenance; low-dose box-jump primer; Friday PM sprint session, separate from lifting.
Week 10    : test / reassess (light technique lifting, conditioning re-test, gate re-check).
Weeks 11-12: RPE-based rebuild on two lifts, hypertrophy accessories near failure, rotated variations.

Usage
-----
    python scripts/hybrid_block.py \
        --oneRM "squat=140,bench=100,deadlift=180,press=70,pullup=25" \
        --out clients/john_tan_fitness_plan.csv

Requires the eligibility gate (G1-G7) and intake P19 to be complete first. If G4 fails
(no true 1RM), pass estimated 1RMs and use `--cap-100` so no 105% single is prescribed.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import russian_block as rb  # noqa: E402

DAY_ORDER = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
JUDGE = "coach judgement (docs/twelve-week-four-day-program.md)"

# Friday-PM sprint session by week: (sets-text, reps-text, note). None = no session.
SPRINT = {
    1: ("test", "12-min", "BASELINE: repeatable 12-min bike or row distance test - record it"),
    2: (6, "8-10 s all-out", ""), 3: (7, "8-10 s all-out", ""), 4: (8, "8-10 s all-out", ""),
    5: (5, "8 s all-out", ""), 6: (4, "8 s all-out", ""), 7: (5, "8 s all-out", ""), 8: (4, "8 s all-out", ""),
    9: None,
    10: ("test", "12-min", "RE-TEST: same 12-min distance test as week 1"),
    11: (6, "8-10 s all-out", ""), 12: (8, "8-10 s all-out", ""),
}
EASY_WED = set(range(1, 13))
EASY_WEEKEND = {1, 2, 3, 4, 5, 6, 7, 8, 11, 12}  # weeks 9-10: recovery/test, Wed only


def choose_placement(primary_goal, conditioning, trained, can_split, fifth_day_ok, recovery_ok, fat_loss=False):
    """Pick where the sprint/conditioning session goes. Returns (option, [reasons]).

    A = separate session on Friday (>= 3 h after lifting), B = right after Friday lifting,
    C = separate non-lifting day (a fifth training day), D = no sprint block (easy aerobic only).
    Rules run in order; the first that fires decides. Inputs come from intake P19/P20.
    """
    why = []
    if conditioning == "none":
        return "D", ["client wants no conditioning beyond easy aerobic work"]
    if not recovery_ok:
        return "D", ["recovery context does not support added intensity (gate G6 / sleep / stress) - "
                     "remove the sprint block first (russian-strength-program.md sec 2, G6)"]
    if fat_loss:
        why.append("fat loss / 'shredded' is a goal, so conditioning matters as much as strength; the deficit also "
                   "lowers recovery, so protect lifting by separating the modes where possible")
        if fifth_day_ok:
            return "C", why + ["a separate fifth day adds expenditure without touching the lifting sessions"]
        if can_split:
            return "A", why + ["no fifth day, but a split Friday keeps the >= 3 h separation"]
        return "B", why + ["only a single Friday visit is possible: keep the block short after lifting, and "
                            "lean on steps and easy aerobic work for expenditure"]
    if primary_goal == "max_strength" and trained:
        why.append("maximal strength is the priority and the client is a trained lifter, so separate the "
                   "modes (Petre 2021: lower-body 1RM fell in trained lifters, more so same-session)")
        if can_split:
            return "A", why + ["client can train twice on Friday, so use a >= 3 h gap"]
        if fifth_day_ok:
            return "C", why + ["no split Friday, but a fifth day is acceptable"]
        return "B", why + ["neither a split day nor a fifth day is possible, so keep the block short after "
                            "lifting and drop it first if freshness slips (accepts the same-session cost)"]
    if conditioning == "equal":
        why.append("conditioning is as important as strength, so full separation is worth a fifth day")
        if fifth_day_ok:
            return "C", why
        if can_split:
            return "A", why + ["no fifth day, but a split Friday works"]
        return "B", why + ["only a single Friday visit is possible"]
    if not trained:
        return "B", ["client is not a trained lifter: Petre 2021 found no lower-body strength penalty in "
                     "untrained or moderately trained people, so one visit is acceptable"] + \
                    (["a split Friday is optional if they prefer it"] if can_split else [])
    if can_split:
        return "A", ["default for a trained lifter with a split-day option"]
    return "B", ["default when no separation is possible"]


def easy_row(week, day):
    return rb.row(week, day, "aerobic", "conditioning", "Easy aerobic (bike / brisk walk / row)",
                  1, "-", "below VT1 - talk test / RPE 3-4", "-", "-",
                  "30-40 min" if day == "Wed" else "30-45 min", "-",
                  "Zone 1 = below VT1 (ISA three-zone model, Table 8-11); dose is " + JUDGE)


PLACEMENT = {  # option -> (day, session tag, placement note)
    "A": ("Fri", "cond-PM", "PM session, >= 3 h after lifting"),
    "B": ("Fri", "cond-post", "straight after lifting (same-session cost accepted - keep it short)"),
    "C": ("Sat", "cond-day5", "separate non-lifting day = a FIFTH planned training day"),
}


def sprint_rows(week, option):
    spec = SPRINT[week]
    if spec is None or option == "D":
        return []
    day, tag, where = PLACEMENT[option]
    sets, reps, note = spec
    if sets == "test":
        return [rb.row(week, day, tag, "test", "Conditioning test - 12-min maximal distance",
                       1, reps, "max sustainable", "-", "-", "12 min", "record distance",
                       where + ". " + note + ". " + JUDGE)]
    return [
        rb.row(week, day, tag, "conditioning", "Bike sprint intervals (5-min easy warm-up first)",
               sets, reps, "all-out, 90 s easy between", "90 s", "-", "~12 min",
               "keep sprints <= 10 s; drop the session first if freshness slips",
               where + "; never before lifting (Petre 2021; Vechin 2021; "
               "Ferraro-Farro 2026). Dose is " + JUDGE),
    ]


def primer_row(week, day):
    if week <= 6:
        s, r = 4, 5
    else:
        s, r = 3, 3
    return rb.row(week, day, "primer", "power", "Box jump (low dose, full recovery)", s, r,
                  "max intent, submax height", "60-90 s between sets", "-", "",
                  "-", "20 contacts is a technique/maintenance dose, not a power block "
                  "(de Villarreal 2009). " + JUDGE)


def carry_row(week):
    return rb.row(week, "Tue", "B", "accessory", "Farmer carry", 4, "30 m", "heavy but tall posture",
                  "60-90 s", "-", "", "add load when all 4 are clean", JUDGE)


def is_lower_boundary(exercise):
    return exercise == "Romanian Deadlift"


def week_1_to_9(one_rm, wave_lifts, step, unit, cap100):
    base = rb.emit_v5(one_rm, wave_lifts, step, unit, fat_loss=False)
    out = []
    for r in base:
        week, day, exercise = int(r[0]), r[1], r[4]
        if is_lower_boundary(exercise):
            continue  # RDL omitted: deadlift already loaded 2x/wk (documented deviation, judgement)
        if cap100 and week == 9 and r[3] == "strength" and "105%" in r[7]:
            # no 105% single without a valid 1RM test (G4): repeat the week-8 double instead
            r = list(r)
            r[5], r[6] = "2", "2"
            r[7] = r[7].replace("105%", "100%")
            r[12] = "capped at 100% (G4 not passed) - test via rep-max -> estimated 1RM"
        out.append(r)
        if r[3] == "warm-up" and day in ("Mon", "Thu") and not (day == "Thu" and week > 6):
            out.append(primer_row(week, day))
        if r[3] == "warm-up" and day == "Tue":
            pass
    # carry on Tuesday after the strength rows: insert before the Tue cool-down
    final = []
    for r in out:
        if r[1] == "Tue" and r[3] == "cool-down":
            final.append(carry_row(int(r[0])))
        final.append(r)
    return final


def week_10(one_rm, wave_lifts, step, unit):
    rows = []
    for day, grp in (("Mon", "A"), ("Thu", "B")):
        rows.append(rb.warmup_row(10, day, grp))
        for k, meta in rb.LIFTS.items():
            if meta["group"] == grp and k in one_rm and k in wave_lifts:
                rows.append(rb.row(10, day, grp, "strength", meta["name"], 3, "3-5",
                                   f"~65% 1RM ({rb.fmt(rb.round_load(0.65 * one_rm[k], step))} {unit})",
                                   "2-3 min", "2-0-1", "", "technique focus - stop with reps in reserve",
                                   "test / reassess week: reduced load, no maximal work. " + JUDGE))
        if day == "Mon":
            rows.append(rb.row(10, day, grp, "assessment", "Re-run the eligibility gate (G1-G7); review the training log; "
                               "record 1RMs (or estimated); choose next cycle's lifts", 1, "-", "-", "-", "-", "10 min", "-",
                               "Reassess before the next block (SKILL.md B4; russian-strength-program.md sec 2)"))
        rows.append(rb.cooldown_row(10, day, grp))
    return rows


REBUILD_ACC = {
    "A": [("Walking Lunge", "2-3", "8-12/side"), ("Dips", "2-3", "8-12")],
    "B": [("Back Extension", "2-3", "8-12"), ("Face Pull", "2-3", "8-12"),
          ("Rear Delt Fly", "2-3", "15-20")],
}


def weeks_11_12(one_rm, wave_lifts, step, unit):
    rebuild = [k for k in wave_lifts if k in one_rm][:2]
    rows = []
    for wk in (11, 12):
        for day, grp, heavy in (("Mon", "A", True), ("Tue", "B", True), ("Thu", "A", False), ("Fri", "B", False)):
            rows.append(rb.warmup_row(wk, day, grp))
            for k, meta in rb.LIFTS.items():
                if meta["group"] != grp or k not in one_rm:
                    continue
                if k in rebuild:
                    sets = 4 if heavy else 3
                    rows.append(rb.row(wk, day, grp, "strength", meta["name"], sets, "5-8",
                                       f"RPE 7-8 (~70-75% 1RM = {rb.fmt(rb.round_load(0.725 * one_rm[k], step))} {unit})",
                                       "2-3 min", "2-0-1", "", "add load when all sets hit the top of the range at RPE <= 8",
                                       "rebuild: effort governs, not %1RM. " + JUDGE))
                else:
                    rows.append(rb.row(wk, day, grp, "strength", meta["name"], 3, "6-8",
                                       f"~65% 1RM ({rb.fmt(rb.round_load(0.65 * one_rm[k], step))} {unit})",
                                       "2-3 min", "2-0-1", "", rb.ACC_PROG, "maintenance lift"))
            for nm, s, r in REBUILD_ACC[grp]:
                rows.append(rb.row(wk, day, grp, "accessory", nm, s, r, "RIR 1-3 (near failure)", "60-90 s",
                                   "2-0-1", "", rb.ACC_PROG,
                                   "variation rotated from weeks 1-9; effort near failure only on accessories. " + JUDGE))
            rows.append(rb.cooldown_row(wk, day, grp))
    return rows


def build(one_rm, wave_lifts, step, unit, cap100, option="A", fat_loss=False):
    rows = week_1_to_9(one_rm, wave_lifts, step, unit, cap100)
    rows += week_10(one_rm, wave_lifts, step, unit)
    rows += weeks_11_12(one_rm, wave_lifts, step, unit)
    for wk in range(1, 13):
        if wk in EASY_WED:
            rows.append(easy_row(wk, "Wed"))
        if wk in EASY_WEEKEND and not (option == "C" and SPRINT.get(wk)):
            rows.append(easy_row(wk, "Sat"))
        elif wk in EASY_WEEKEND:
            rows.append(easy_row(wk, "Sun"))
        rows += sprint_rows(wk, option)
    if fat_loss:
        for wk in range(1, 13):
            phase = ("maintenance calories (protect the wave and the retest)" if 6 <= wk <= 10
                     else "moderate deficit if the client/RD chooses one")
            rows.append(rb.row(wk, "Sun", "fat-loss", "conditioning", "Daily steps target",
                               1, "-", ">= 7000 steps/day; add ~2000 toward the target", "-", "-", "-",
                               "raise steps before adding structured cardio",
                               "NEAT lever (Wk05 Ch8 p10, p26). Energy intake this week: " + phase +
                               ". Calories and diet detail are the client's / a registered dietitian's call "
                               "(russian-strength-program.md sec 5; trained-population-evidence.md: slower loss and "
                               "deficits <= ~500 kcal/day protect lean mass)."))
    rows.sort(key=lambda r: (int(r[0]), DAY_ORDER[r[1]]))  # stable: keeps within-day order
    return rows


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--oneRM", required=True, help='e.g. "squat=140,bench=100,deadlift=180,press=70,pullup=25"')
    ap.add_argument("--wave-lifts", default="squat,bench,deadlift", help="lifts on the V5 wave")
    ap.add_argument("--units", choices=["kg", "lb"], default="kg")
    ap.add_argument("--cap-100", action="store_true", help="G4 not passed: no 105% single in week 9")
    ap.add_argument("--placement", choices=["auto", "A", "B", "C", "D"], default="auto",
                    help="where the sprint session goes; auto uses the intake answers below")
    yn = ["yes", "no"]
    ap.add_argument("--primary-goal", choices=["max_strength", "hybrid", "general"])
    ap.add_argument("--conditioning", choices=["none", "minimum", "equal"],
                    help="how much conditioning the client wants alongside strength")
    ap.add_argument("--trained-lifter", choices=yn, help="experienced strength trainee?")
    ap.add_argument("--can-split-friday", choices=yn, help="can train twice on Friday with a >= 3 h gap?")
    ap.add_argument("--fifth-day-ok", choices=yn, help="is a fifth planned training day acceptable?")
    ap.add_argument("--recovery-ok", choices=yn, help="sleep/stress/G6 support added intensity?")
    ap.add_argument("--fat-loss", choices=yn, help="does the client want to get lean / 'shredded' (a deficit)?")
    ap.add_argument("--out", default="-")
    a = ap.parse_args(argv)
    one_rm = rb.parse_one_rm(a.oneRM)
    wave = [w.strip().lower() for w in a.wave_lifts.split(",") if w.strip()]
    for w in wave:
        if w not in rb.LIFTS:
            sys.exit(f"error: unknown wave lift {w!r}")
    step = 2.5 if a.units == "kg" else 5.0
    if a.placement == "auto":
        need = {"--primary-goal": a.primary_goal, "--conditioning": a.conditioning,
                "--trained-lifter": a.trained_lifter, "--can-split-friday": a.can_split_friday,
                "--fifth-day-ok": a.fifth_day_ok, "--recovery-ok": a.recovery_ok,
                "--fat-loss": a.fat_loss}
        missing = [k for k, v in need.items() if v is None]
        if missing:
            sys.exit("error: --placement auto needs intake answers (ask them; Unknown is not Yes): "
                     + ", ".join(missing) + ". Or pass --placement A|B|C|D explicitly.")
        option, why = choose_placement(a.primary_goal, a.conditioning, a.trained_lifter == "yes",
                                       a.can_split_friday == "yes", a.fifth_day_ok == "yes",
                                       a.recovery_ok == "yes", a.fat_loss == "yes")
    else:
        option, why = a.placement, ["set explicitly by the coach"]
    print(f"conditioning placement: option {option} - " + "; ".join(why), file=sys.stderr)
    rows = build(one_rm, wave, step, a.units, a.cap_100, option, a.fat_loss == "yes")
    out = sys.stdout if a.out == "-" else open(a.out, "w", newline="")
    try:
        w = csv.writer(out)
        w.writerow(rb.CSV_HEADER)
        w.writerows(rows)
    finally:
        if out is not sys.stdout:
            out.close()
            print(f"wrote {len(rows)} rows to {a.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
