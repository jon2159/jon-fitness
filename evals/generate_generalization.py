#!/usr/bin/env python3
"""Build the jon-fitness *generalization* set — the held-out benchmark.

This set answers a different question from `scenarios.json`:

    scenarios.json   "does the skill handle the situations we trained it on?"
    generalization    "did we make the skill better, or teach it our test?"

It is deterministic and STABLE. It reuses the *structural* axes from
`generate_scenarios.py` (environment, REVL phase, training age, PT frequency —
the things that change what a good coach does) but pairs them with **held-out
goal / recovery / constraint vocabulary that the training generator never
emits**. So every item is a novel decision problem built from familiar parts:
disjoint from the training library by construction, no overlap to police.

Rules of use (see evals/README.md):
  - The optimizer never trains on this set. It is scored, tracked, and compared
    against baseline — nothing more.
  - Regenerate freely: the output is a pure function of the axes below + the
    seed, so the same item keeps the same id across runs and stays comparable
    over time.
  - Keep it separate from the Claude-authored wildcard set (`wildcards.py`),
    which is exploratory and non-deterministic.

Usage:
    python evals/generate_generalization.py           # write scenarios/generalization.json
    python evals/generate_generalization.py --stats
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from generate_scenarios import ENVIRONMENTS, REVL_PHASES, TRAINING_AGE, PT_FREQ, NAMES

HERE = Path(__file__).resolve().parent
OUT = HERE / "scenarios" / "generalization.json"

random.seed(20260910)  # deterministic, and distinct from the training seed

# --------------------------------------------------------------------- held-out axes
# None of these keys or phrasings appear in generate_scenarios.py. They are
# realistic PT situations the skill was NOT tuned against.

HELD_OUT_GOALS = {
    "return_to_sport": dict(
        text="get back to playing competitive netball after an ACL reconstruction 9 months ago (surgeon has cleared return to sport)",
        priorities=["Confirm surgical clearance and any outstanding rehab criteria before loading",
                    "Progress from strength/control to power to change-of-direction, in that order",
                    "Build a return-to-play timeline, not just a single session"],
        traps=["Jumping straight to plyometrics / agility without a strength and control base",
               "Treating this as a normal hypertrophy client because they were 'cleared'"],
        must_not=["Give rehab exercise prescription that belongs to the treating physio",
                  "Ignore the injury history"]),
    "hyrox_prep": dict(
        text="finish a Hyrox race in under 90 minutes in 14 weeks (first one)",
        priorities=["Identify the limiter — running economy, compromised running, or the strength stations",
                    "Concurrent training: protect the running with session order and hard-day spacing",
                    "Rehearse the specific station movements under fatigue"],
        traps=["Writing a generic strength block with no running integration",
               "Adding conditioning volume to someone already running several times a week"]),
    "first_meet": dict(
        text="compete in their first powerlifting meet in 12 weeks and not bomb out",
        priorities=["Peak the competition lifts specifically; taper into meet week",
                    "Rehearse commands, openers, and attempt selection",
                    "Openers at a load they could hit on their worst day"],
        traps=["Still adding hypertrophy volume in the last three weeks",
               "Chasing a gym PR in training instead of a meet total"]),
    "menopause_strength": dict(
        text="maintain strength and bone density through menopause — symptoms include hot flushes and disturbed sleep",
        priorities=["Prioritise progressive heavy resistance training for bone and muscle",
                    "Work with the disturbed sleep — autoregulate rather than force fixed loads",
                    "Impact / loading variety within tolerance"],
        traps=["Defaulting to light 'toning' work because of age or symptoms",
               "Ignoring the sleep disruption when setting intensity"],
        must_not=["Give HRT or medical management advice"]),
    "desk_tension": dict(
        text="reduce the neck and upper-back tension and tension headaches they get from long days at a desk",
        priorities=["Screen for red-flag headache features and refer if present",
                    "Position this as load tolerance + movement variety, not 'fixing posture'",
                    "Realistic in-day habits alongside the training"],
        traps=["Promising posture correction will cure the headaches",
               "Prescribing endless stretching with no strengthening"],
        must_not=["Diagnose the cause of the headaches"]),
    "pregnancy_second_tri": dict(
        text="keep training safely through pregnancy — currently 18 weeks, was training 4x/week before, no complications and OB is supportive",
        priorities=["Confirm no contraindications and ongoing OB clearance",
                    "Adjust: reduce supine work over time, manage intra-abdominal pressure, RPE cap",
                    "Expect to regress load through the pregnancy and that is fine"],
        traps=["Applying general-population intensity progression",
               "Stopping resistance training entirely 'to be safe'"],
        must_not=["Override the client's OB guidance", "Give obstetric advice"]),
    "grip_and_carry": dict(
        text="be able to carry both kids and the shopping up three flights without stopping — they find stairs and carrying genuinely hard",
        priorities=["Train the actual task: loaded carries, stairs, unilateral strength",
                    "Build work capacity for the repeated-effort demand",
                    "Anchor progress to the real-world task, not gym numbers"],
        traps=["Writing an aesthetic split that never addresses carrying or stairs"]),
    "post_covid_return": dict(
        text="rebuild after a chest infection knocked them out for three weeks — cleared by their GP, still notice they get breathless quickly",
        priorities=["Re-ramp gradually; use symptoms (breathlessness, fatigue next day) as the guide",
                    "Start well below pre-illness loads and rebuild",
                    "Watch for post-exertional malaise and refer back if it appears"],
        traps=["Resuming at pre-illness loads because the client 'feels ready'",
               "Pushing through breathlessness as if it were normal deconditioning"],
        must_not=["Give medical clearance or manage the recovery clinically"]),
}

HELD_OUT_RECOVERY = {
    "newborn": "has a 10-week-old baby and is getting broken sleep in 2-3 hour blocks",
    "shift_rotating": "works rotating shifts — days one week, nights the next — so their sleep window keeps moving",
    "bereavement": "recently lost a parent and says training is one of the few things keeping them going, but energy is low",
    "exam_season": "is a student in exam season, sitting for long hours and sleeping poorly for the next month",
    "long_haul_return": "just flew back from a 12-hour time-zone shift two days ago",
    "ramp_after_illness": "had a bad flu last week, first week back, still at maybe 80%",
}

HELD_OUT_CONSTRAINTS = {
    "custody_schedule": "has the kids half the week on a schedule that changes, so which days they can train is unpredictable",
    "fasting_month": "is fasting sunrise to sunset for the next month and can only train fasted in the late afternoon or well after dark",
    "hotel_gyms": "is on the road for six weeks and will only have hotel gyms — a few dumbbells up to 20 kg, a treadmill, a cable machine",
    "no_impact": "has been told by their physio to avoid running and jumping for now but everything else is fine",
    "wrist_cast": "is in a wrist cast for four more weeks and can't load the right hand",
    "shared_rack": "trains at peak hours and can rarely get a squat rack or barbell — everything else is usually free",
    "early_only": "can only train at 5:30am before work and says they feel stiff and half-asleep at that hour",
}


def priorities(env_key, phase, goal_key, rec_key, con_key):
    env = ENVIRONMENTS[env_key]
    g = HELD_OUT_GOALS[goal_key]
    pri = list(g["priorities"])
    traps = list(g.get("traps", []))
    must_not = list(g.get("must_not", []))

    if "revl" in env_key:
        pri.append("Count the REVL stimulus already in the week before adding anything")
        traps.append("Programming the PT session as if REVL were not happening")
        must_not.append("Assert a specific REVL load/%/rep count as fact")
        if phase and REVL_PHASES[phase]["headroom"] in ("none", "minimal"):
            pri.append(f"Recognise {phase} leaves little/no headroom — support, don't add load")
    if env["family"] == "mixed":
        pri.append("Account for total weekly stress across both activities, not each alone")
    if env["family"] == "commercial":
        pri.append("Impose a progression model, don't just add exercises")

    if rec_key:
        pri.append("Autoregulate to the stated recovery context rather than forcing fixed loads")
        traps.append("Ignoring the recovery context, or defaulting straight to 'take time off'")
    if con_key:
        pri.append("Build the plan around the stated constraint, not despite it")
        traps.append("Prescribing something the constraint rules out")

    # de-dup, keep order
    def uniq(xs):
        seen, out = set(), []
        for x in xs:
            if x not in seen:
                seen.add(x); out.append(x)
        return out
    return uniq(pri), uniq(traps), uniq(must_not)


def make_prompt(env_key, freq, phase, goal_key, age_key, age_band, rec_key, con_key, pt, name):
    env = ENVIRONMENTS[env_key]
    g = HELD_OUT_GOALS[goal_key]
    bits = [f"{name}, {age_band}, {TRAINING_AGE[age_key]}."]
    if env_key.startswith("revl"):
        p = f" They're in the **{phase}** phase (week {REVL_PHASES[phase]['wk']})." if phase else ""
        bits.append(f"They do REVL {freq}.{p}")
        if env_key == "revl_plus_running":
            bits.append("They also run about 25 km a week.")
        if env_key == "revl_plus_commercial":
            bits.append("They also do a couple of their own gym sessions.")
    elif env_key == "commercial_plus_running":
        bits.append(f"They lift {freq} and run about 25 km a week.")
    elif env_key in ("group_plus_bodybuilding", "group_plus_powerlifting"):
        bits.append(f"They do group classes {freq} plus {env['already']}.")
    else:
        bits.append(f"They train {freq} at a commercial gym — {env['already']}.")
    bits.append(f"They want to {g['text']}.")
    if rec_key:
        bits.append(f"Right now they {HELD_OUT_RECOVERY[rec_key]}.")
    if con_key:
        bits.append(f"Also, they {HELD_OUT_CONSTRAINTS[con_key]}.")
    bits.append(f"I've got them for PT {pt}. What should I do with them?")
    return " ".join(bits)


def build():
    rec_keys = list(HELD_OUT_RECOVERY)
    con_keys = list(HELD_OUT_CONSTRAINTS)
    age_bands = ["late 20s", "30s", "40s", "50s"]
    out = []
    gid = 0
    for goal_key in HELD_OUT_GOALS:
        # each held-out goal gets a small spread of structural contexts
        combos = [
            ("commercial_structured", "3x/week", None),
            ("revl", "4x/week", random.choice(list(REVL_PHASES))),
            ("revl_plus_running", "3x/week", random.choice(list(REVL_PHASES))),
            ("commercial_unstructured", "4x/week", None),
            ("group_plus_powerlifting", "3x/week", None),
        ]
        goal_age_bands = {"menopause_strength": ["40s", "50s"],
                          "pregnancy_second_tri": ["late 20s", "30s", "40s"]}.get(goal_key, age_bands)
        for env_key, freq, phase in combos:
            gid += 1
            age_key = random.choice(list(TRAINING_AGE))
            age_band = random.choice(goal_age_bands)
            rec_key = rec_keys[gid % len(rec_keys)] if gid % 2 == 0 else None
            con_key = con_keys[gid % len(con_keys)] if gid % 3 != 0 else None
            pt = random.choice(PT_FREQ)
            name = NAMES[(gid * 7) % len(NAMES)]
            pri, traps, must_not = priorities(env_key, phase, goal_key, rec_key, con_key)
            out.append(dict(
                id=f"GEN-{gid:03d}",
                family="generalization",
                set="generalization",
                environment=env_key,
                environment_label=ENVIRONMENTS[env_key]["label"],
                weekly_frequency=freq,
                revl_phase=phase,
                goal=goal_key,
                goal_label=HELD_OUT_GOALS[goal_key]["text"][:60],
                training_age=age_key,
                age_band=age_band,
                recovery=rec_key or "good",
                constraint=con_key or "none",
                pt_frequency=pt,
                prompt=make_prompt(env_key, freq, phase, goal_key, age_key, age_band,
                                   rec_key, con_key, pt, name),
                expected_priorities=pri,
                traps=traps,
                must_not=must_not,
                source="held-out",
            ))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()
    s = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(dict(
        version=1, generated_by="evals/generate_generalization.py",
        note="HELD-OUT. Never used for optimization. Scored and tracked only.",
        count=len(s), scenarios=s), indent=1))
    print(f"wrote {OUT.relative_to(HERE.parent)}  —  {len(s)} held-out scenarios")
    if args.stats:
        from collections import Counter
        for f in ("goal", "environment", "revl_phase", "recovery", "constraint"):
            print(f"\n{f}:")
            for k, v in Counter(x.get(f) for x in s).most_common():
                print(f"   {str(k):24s} {v}")


if __name__ == "__main__":
    main()
