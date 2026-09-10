#!/usr/bin/env python3
"""Build the jon-fitness scenario library.

Design principle: a scenario is a *decision problem*, not a phrasing variant. Two
scenarios differ only if a good coach would plausibly answer them differently. The
generator therefore composes from axes that each change the correct answer:

    environment  -> what stimulus already exists
    phase        -> how much headroom there is
    goal         -> what stimulus is actually needed
    training age -> what loading is appropriate
    recovery     -> whether to add anything at all
    constraint   -> what is off the table
    pt frequency -> how much room the coach actually has

Each generated scenario carries its own `expected_priorities`, `traps` and `must_not`,
derived from the combination — so grading is per-scenario, not generic.

Hand-authored adversarial scenarios live in `adversarial.json` and are merged in.

Usage:
    python evals/generate_scenarios.py            # write evals/scenarios/scenarios.json
    python evals/generate_scenarios.py --stats    # summarise the library
"""
from __future__ import annotations

import argparse
import itertools
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "scenarios" / "scenarios.json"
ADVERSARIAL = HERE / "scenarios" / "adversarial.json"

random.seed(20260909)  # deterministic library

# --------------------------------------------------------------------- axes

ENVIRONMENTS = {
    "commercial_unstructured": dict(
        label="commercial gym, no programme",
        stimulus="self-selected, unstructured resistance training",
        already="picks exercises on the day, no progression model",
        family="commercial"),
    "commercial_machines": dict(
        label="commercial gym, mostly machines",
        stimulus="machine-based resistance training",
        already="almost all machines, little free-weight or unilateral work",
        family="commercial"),
    "commercial_programhopper": dict(
        label="commercial gym, changes programme constantly",
        stimulus="resistance training but never the same block twice",
        already="a new programme every 2-3 weeks, nothing run long enough to progress",
        family="commercial"),
    "commercial_sorenesschaser": dict(
        label="commercial gym, trains for soreness",
        stimulus="high-variety, high-fatigue resistance training",
        already="judges sessions by how sore they are the next day",
        family="commercial"),
    "commercial_structured": dict(
        label="commercial gym, follows a written programme",
        stimulus="structured resistance training with progression",
        already="an upper/lower or push-pull-legs split they actually follow",
        family="commercial"),
    "revl": dict(
        label="REVL classes",
        stimulus="REVL group programming (Perform/Move strength + Sweat conditioning + Complete)",
        already="REVL classes",
        family="revl"),
    "revl_plus_commercial": dict(
        label="REVL classes plus solo gym sessions",
        stimulus="REVL group programming plus self-directed gym work",
        already="REVL classes plus extra solo sessions",
        family="mixed"),
    "revl_plus_running": dict(
        label="REVL classes plus running",
        stimulus="REVL group programming plus endurance running",
        already="REVL classes plus a weekly running load",
        family="mixed"),
    "commercial_plus_running": dict(
        label="commercial gym plus running",
        stimulus="resistance training plus endurance running",
        already="gym sessions plus a weekly running load",
        family="mixed"),
    "group_plus_bodybuilding": dict(
        label="group classes plus bodybuilding-style training",
        stimulus="group conditioning plus hypertrophy-focused resistance work",
        already="group classes plus their own bodybuilding split",
        family="mixed"),
    "group_plus_powerlifting": dict(
        label="group classes plus powerlifting-style training",
        stimulus="group conditioning plus heavy barbell work",
        already="group classes plus a squat/bench/deadlift focus",
        family="mixed"),
}

REVL_PHASES = {
    "Volume":      dict(wk="1-3",  headroom="most",     note="loads roughly 40-65%, volume already high"),
    "Build":       dict(wk="4-6",  headroom="limited",  note="loads climbing toward 85-90%"),
    "Deload":      dict(wk="7",    headroom="strength-only", note="strength deloaded, metabolic volume intact"),
    "Peak Wk 1":   dict(wk="8",    headroom="minimal",  note="the heavy wave, to roughly 90-95%"),
    "Peak Wk 2":   dict(wk="9",    headroom="none",     note="1RM and 3RM testing week"),
    "Peak Wk 3":   dict(wk="10",   headroom="none",     note="Sweat Engine/Sprint baseline testing week"),
    "Rebuild":     dict(wk="11-13", headroom="moderate", note="moderate loads, mostly RPE/RIR"),
}

GOALS = {
    "hyp_general":  ("build muscle overall", ["hypertrophy stimulus", "weekly volume per muscle group"]),
    "hyp_upper":    ("build upper-body size", ["upper-body hypertrophy volume"]),
    "hyp_lower":    ("build lower-body size", ["lower-body hypertrophy volume"]),
    "hyp_glutes":   ("develop glutes", ["hip-dominant hypertrophy", "loaded hip extension"]),
    "hyp_back":     ("build a bigger back", ["horizontal and vertical pulling volume"]),
    "hyp_shoulders":("build shoulders", ["vertical push and lateral raise volume"]),
    "hyp_arms":     ("build arms", ["direct elbow flexion/extension volume"]),
    "str_general":  ("get stronger overall", ["heavy compound exposure", "progression model"]),
    "str_squat":    ("increase squat strength", ["squat-specific loading", "spacing from existing squat work"]),
    "str_hinge":    ("increase deadlift strength", ["hinge-specific loading", "axial load management"]),
    "str_press":    ("increase pressing strength", ["press-specific loading"]),
    "str_pull":     ("get their first pull-up / more pulling strength", ["vertical pull progression"]),
    "str_relative": ("get stronger without gaining weight", ["strength at stable bodyweight"]),
    "bodycomp":     ("lose fat while keeping muscle", ["protein/energy referral", "retain training intensity"]),
    "conditioning": ("improve conditioning", ["identify which conditioning quality is missing"]),
    "performance":  ("improve athletic performance", ["power/speed quality", "sport specificity"]),
    "workcapacity": ("increase work capacity", ["aerobic base vs glycolytic capacity"]),
    "movement":     ("move better / fix technique", ["movement screen", "technique at sub-maximal load"]),
    "weakpoint":    ("fix a specific weak point", ["assessment before prescription"]),
    "hybrid_size_classes": ("get bigger without giving up their classes", ["complement, don't duplicate"]),
    "hybrid_str_cond":     ("get stronger without losing conditioning", ["concurrent training interference"]),
    "hybrid_size_fresh":   ("gain size without feeling destroyed every week", ["fatigue-efficient hypertrophy"]),
}

TRAINING_AGE = {
    "complete_beginner": "has never followed a training programme",
    "inconsistent_beginner": "has trained on and off for a year, never consistently",
    "intermediate": "has trained consistently for about two years",
    "experienced": "has trained seriously for five-plus years",
    "returning_athlete": "played sport to a decent level, out of training for three years",
    "long_term_strength": "has been strength training for eight years and is close to their ceiling",
}

RECOVERY = {
    "good": ("sleeps 8 hours, low stress", "normal"),
    "poor_sleep": ("sleeping about 5 hours a night at the moment", "reduce"),
    "work_stress": ("in a very heavy period at work", "reduce"),
    "travel": ("travelling for work most of next month", "adapt"),
    "sore": ("legs are constantly sore", "change pattern"),
    "perf_down": ("numbers have been going backwards for two weeks", "investigate"),
    "fresh_high_volume": ("feels fresh despite training six days a week", "verify then use"),
    "returning_break": ("just back from six weeks off", "re-ramp"),
    "sore_but_improving": ("sore most days but lifts are still going up", "distinguish soreness from fatigue"),
    "motivated_underrecovered": ("very motivated but sleeping badly and stressed", "protect from themselves"),
    "unmotivated_recovered": ("well rested but struggling to stay motivated", "adherence problem, not a load problem"),
}

CONSTRAINTS = {
    "none": "",
    "time_30": "only has 30 minutes per session",
    "time_45": "sessions have to fit in 45 minutes",
    "equip_home": "trains at home with dumbbells and a pull-up bar only",
    "equip_nobar": "the gym has no barbell available at their usual time",
    "wont_drop": "is not willing to drop any of their current classes",
    "wants_more": "keeps asking to add more volume",
    "soreness_belief": "believes a session was wasted if they aren't sore",
    "one_pt": "only has budget for one PT session a week",
    "shoulder_hx": "has an old shoulder issue that flares with overhead pressing",
    "back_hx": "has a history of low-back pain with heavy deadlifts",
    "knee_hx": "gets knee pain with deep knee-dominant work",
}

PT_FREQ = ["1x/week", "2x/week", "3x/week"]
AGE_BANDS = ["early 20s", "late 20s", "30s", "40s", "50s", "60s"]


def priorities_for(env_key, phase, goal_key, age_key, rec_key, con_key, pt):
    """Per-scenario expected programming priorities and traps."""
    env = ENVIRONMENTS[env_key]
    pri, traps, must_not = [], [], []

    # --- what the coach must establish first
    if env["family"] in ("revl", "mixed") and "revl" in env_key:
        pri.append("Identify the REVL phase and week, and what the client actually did last week")
        pri.append("Count REVL's existing stimulus before adding anything (total training load)")
        traps.append("Programming the PT session as if REVL were not happening")
        must_not.append("Assert a specific REVL load/%/rep count as fact")
    if env["family"] == "commercial":
        pri.append("Impose a progression model on unstructured training")
        traps.append("Adding more exercises instead of adding structure")
    if env["family"] == "mixed":
        pri.append("Account for total weekly stress across BOTH activities, not each in isolation")
        traps.append("Treating the two activities as independent")

    # --- phase-driven
    if phase:
        h = REVL_PHASES[phase]["headroom"]
        if h == "none":
            pri.append(f"Recognise {phase} is a testing week — protect it, add nothing load-bearing")
            must_not.append("Add heavy or maximal work during a testing week")
            traps.append("Adding a second heavy exposure during a test week")
        elif h == "minimal":
            pri.append("Recognise Peak leaves minimal headroom; support rather than add")
            traps.append("Stacking a second strength peak on REVL's peak")
        elif h == "strength-only":
            pri.append("Use Deload as the assessment/technique window; do not add metabolic volume")
            traps.append("Treating Deload as a whole-body rest week, or adding conditioning")
        elif h == "most":
            pri.append("Volume phase has the most headroom — the best window for added strength work")

    # --- goal-driven
    pri.extend(GOALS[goal_key][1])
    if goal_key.startswith("hyp"):
        traps.append("Prescribing conditioning or more compounds instead of targeted hypertrophy volume")
    if goal_key.startswith("str"):
        traps.append("Adding strength work without checking existing frequency for that pattern")
    if goal_key in ("conditioning", "workcapacity"):
        pri.append("Identify WHICH conditioning quality is missing before adding any")
        traps.append("Adding intervals to someone already doing 3+ hard conditioning sessions")

    # --- training age
    if age_key in ("complete_beginner", "inconsistent_beginner"):
        pri.append("Movement competence and technique before load")
        must_not.append("Prescribe near-maximal loading to a novice")
    if age_key == "returning_athlete":
        pri.append("Re-ramp tissue tolerance; prior training age is not current capacity")
        traps.append("Programming to their old level rather than their current one")
    if age_key == "long_term_strength":
        pri.append("Accept small margins; specificity and weak points matter more than volume")

    # --- recovery
    action = RECOVERY[rec_key][1]
    if action == "reduce":
        pri.append("Reduce intensity first, then volume — do not simply prescribe rest")
        traps.append("Either ignoring the recovery signal or defaulting to 'take a week off'")
    if action == "investigate":
        pri.append("Investigate the cause before changing the programme")
    if action == "verify then use":
        pri.append("Verify the freshness claim before spending it; freshness is not a reason to add by default")
        traps.append("Adding volume just because the client says they feel fine")
    if action == "distinguish soreness from fatigue":
        pri.append("Separate muscle soreness from performance decrement — performance is improving")
        traps.append("Deloading a client whose performance is actually rising")
    if action == "adherence problem, not a load problem":
        pri.append("Treat this as adherence/behaviour, not as a programming-load problem")
        traps.append("Changing the programme when the issue is motivation")
    if action == "re-ramp":
        pri.append("Re-introduce load gradually; expect rapid early progress")

    # --- constraints
    c = CONSTRAINTS[con_key]
    if con_key.startswith("time"):
        pri.append("Fit the session honestly into the stated time")
        traps.append("Prescribing more work than the time allows")
    if con_key.startswith("equip"):
        pri.append("Respect the equipment actually available")
        must_not.append("Prescribe equipment the client said they do not have")
    if con_key in ("wants_more", "soreness_belief"):
        pri.append("Push back on the 'more/sorer is better' belief with reasoning, not a lecture")
        traps.append("Complying with the client's request for more volume")
    if con_key in ("shoulder_hx", "back_hx", "knee_hx"):
        pri.append("Work around the reported issue; refer out if it is painful or unresolved")
        must_not.append("Ignore the reported injury history")
    if con_key == "one_pt":
        pri.append("With one session a week, pick the single highest-value intervention")
    if con_key == "wont_drop":
        pri.append("Respect that classes stay; complement rather than replace")

    return pri, traps, must_not


def make_prompt(env_key, freq, phase, goal_key, age_key, age_band, rec_key, con_key, pt, name):
    env = ENVIRONMENTS[env_key]
    goal_txt = GOALS[goal_key][0]
    bits = [f"{name}, {age_band},"]
    bits.append(f"{TRAINING_AGE[age_key]}.")
    if env_key.startswith("revl"):
        p = f" They're in the **{phase}** phase (week {REVL_PHASES[phase]['wk']} of the block)." if phase else ""
        bits.append(f"They do REVL {freq}.{p}")
        if env_key == "revl_plus_commercial":
            bits.append("They also do a couple of their own gym sessions on top.")
        if env_key == "revl_plus_running":
            bits.append("They also run about 25 km a week.")
    elif env_key == "commercial_plus_running":
        bits.append(f"They lift {freq} at a commercial gym and run about 25 km a week.")
    elif env_key in ("group_plus_bodybuilding", "group_plus_powerlifting"):
        bits.append(f"They do group classes {freq} plus {env['already']}.")
    else:
        bits.append(f"They train {freq} at a commercial gym — {env['already']}.")
    bits.append(f"They want to {goal_txt}.")
    rec_txt = RECOVERY[rec_key][0]
    if rec_key != "good":
        bits.append(f"Right now they {rec_txt}.")
    c = CONSTRAINTS[con_key]
    if c:
        bits.append(f"They {c}.")
    bits.append(f"I've got them for PT {pt}. What should I do with them?")
    return " ".join(bits)


NAMES = ["Aisha", "Marcus", "Priya", "Tom", "Wen Li", "Sofia", "Daniel", "Hannah", "Rui",
         "Grace", "Omar", "Chloe", "Nathan", "Leila", "Ben", "Yuki", "Sam", "Mia",
         "Kofi", "Elena", "Dev", "Zoe", "Callum", "Nadia", "Theo", "Ivy", "Raj",
         "Freya", "Hugo", "Anika", "Luca", "Maya"]


def build():
    scenarios = []
    sid = 0

    def add(env_key, freq, phase, goal_key, age_key, rec_key, con_key, pt):
        nonlocal sid
        sid += 1
        name = NAMES[sid % len(NAMES)]
        age_band = random.choice(AGE_BANDS)
        pri, traps, must_not = priorities_for(env_key, phase, goal_key, age_key, rec_key, con_key, pt)
        env = ENVIRONMENTS[env_key]
        scenarios.append(dict(
            id=f"SC-{sid:04d}",
            family=env["family"],
            environment=env_key,
            environment_label=env["label"],
            weekly_frequency=freq,
            revl_phase=phase,
            goal=goal_key,
            goal_label=GOALS[goal_key][0],
            training_age=age_key,
            age_band=age_band,
            recovery=rec_key,
            constraint=con_key,
            pt_frequency=pt,
            prompt=make_prompt(env_key, freq, phase, goal_key, age_key, age_band, rec_key, con_key, pt, name),
            expected_priorities=pri,
            traps=traps,
            must_not=must_not,
            source="generated",
        ))

    # ---- 1. REVL across every phase x frequency x a spread of goals ----
    revl_goals = ["hyp_general", "hyp_lower", "hyp_back", "hyp_glutes", "str_general", "str_squat",
                  "str_hinge", "str_press", "conditioning", "workcapacity", "movement",
                  "weakpoint", "performance", "hybrid_size_classes", "hybrid_str_cond",
                  "hybrid_size_fresh", "bodycomp"]
    for phase in REVL_PHASES:
        for freq in ["3x/week", "4x/week", "5x/week"]:
            for goal in revl_goals:
                age = random.choice(list(TRAINING_AGE))
                rec = random.choice(list(RECOVERY))
                con = random.choice(list(CONSTRAINTS))
                add("revl", freq, phase, goal, age, rec, con, random.choice(PT_FREQ))

    # ---- 2. commercial-gym clients without structure ----
    comm_envs = ["commercial_unstructured", "commercial_machines", "commercial_programhopper",
                 "commercial_sorenesschaser", "commercial_structured"]
    comm_goals = ["hyp_general", "hyp_upper", "hyp_lower", "hyp_glutes", "hyp_back",
                  "hyp_shoulders", "hyp_arms", "str_general", "str_squat", "str_hinge",
                  "str_press", "str_pull", "str_relative", "bodycomp", "performance", "movement"]
    for env in comm_envs:
        for freq in ["2x/week", "3x/week", "4x/week", "5x/week", "6x/week"]:
            for goal in random.sample(comm_goals, 5):
                add(env, freq, None, goal,
                    random.choice(list(TRAINING_AGE)), random.choice(list(RECOVERY)),
                    random.choice(list(CONSTRAINTS)), random.choice(PT_FREQ))

    # ---- 3. mixed / concurrent training ----
    mixed_envs = ["revl_plus_commercial", "revl_plus_running", "commercial_plus_running",
                  "group_plus_bodybuilding", "group_plus_powerlifting"]
    for env in mixed_envs:
        for freq in ["3x/week", "4x/week", "5x/week"]:
            for goal in random.sample(list(GOALS), 6):
                phase = random.choice(list(REVL_PHASES)) if env.startswith("revl") else None
                add(env, freq, phase, goal,
                    random.choice(list(TRAINING_AGE)), random.choice(list(RECOVERY)),
                    random.choice(list(CONSTRAINTS)), random.choice(PT_FREQ))

    # ---- 4. recovery-led scenarios (recovery is the decision, not the goal) ----
    for rec in RECOVERY:
        for env in ["revl", "commercial_unstructured", "commercial_structured",
                    "revl_plus_running", "group_plus_powerlifting"]:
            phase = random.choice(list(REVL_PHASES)) if env.startswith("revl") else None
            add(env, random.choice(["3x/week", "4x/week", "5x/week"]), phase,
                random.choice(list(GOALS)), random.choice(list(TRAINING_AGE)),
                rec, random.choice(list(CONSTRAINTS)), random.choice(PT_FREQ))

    # ---- 5. constraint-led scenarios ----
    for con in CONSTRAINTS:
        if con == "none":
            continue
        for env in ["revl", "commercial_unstructured", "group_plus_bodybuilding"]:
            phase = random.choice(list(REVL_PHASES)) if env.startswith("revl") else None
            add(env, random.choice(["3x/week", "4x/week", "5x/week"]), phase,
                random.choice(list(GOALS)), random.choice(list(TRAINING_AGE)),
                random.choice(list(RECOVERY)), con, random.choice(PT_FREQ))

    # ---- merge hand-authored adversarial set ----
    if ADVERSARIAL.exists():
        adv = json.loads(ADVERSARIAL.read_text())
        scenarios.extend(adv)

    return scenarios


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()

    s = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(dict(
        version=1,
        generated_by="evals/generate_scenarios.py",
        count=len(s),
        scenarios=s,
    ), indent=1))

    from collections import Counter
    print(f"wrote {OUT.relative_to(HERE.parent)}  —  {len(s)} scenarios")
    if args.stats:
        for field in ("family", "environment", "revl_phase", "goal", "training_age",
                      "recovery", "constraint", "pt_frequency", "source"):
            c = Counter(x.get(field) for x in s)
            print(f"\n{field}:")
            for k, v in c.most_common():
                print(f"   {str(k):32s} {v}")


if __name__ == "__main__":
    main()
