#!/usr/bin/env python3
"""Extend the grader-validity gold set with persona-stratified items.

Why: the original 8 gold items are mostly REVL-heavy trainer questions. Jon's real
population is wider, so the human-vs-grader check must sample it:

  J  coach-athlete   a bodybuilding-style group-class coach who does REVL Sweat Engine plus
                     some REVL strength sessions weekly, with Daily Pump 1-3 days on top
  G  gen-pop + REVL  a general-population client already doing REVL who wants more
  N  gen-pop no REVL a general-population client not doing REVL who wants to be toned and fit

Each persona gets a strong (skill) answer, a generic (no skill) answer, and a deliberately
flawed answer, so Jon's scores show whether the AI grader can tell them apart.

Appends GOLD-09.. to evals/scenarios/gold/gold_responses.json with `human_scores: null`
and a prefilled `claude_draft_scores` for Jon to correct. Idempotent: existing gold_ids are
skipped. Responses are non-deterministic (real `claude -p` calls), so only run it to
extend the set; it never touches items Jon has already scored.

Usage:  python evals/build_gold_personas.py [--workers 3]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from run_cycle import RUBRIC, answer_prompt, claude, extract_json, grade_prompt

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GOLD = HERE / "scenarios" / "gold" / "gold_responses.json"
NEUTRAL_CWD = Path(tempfile.gettempdir())  # no project skill in context

S = {}  # persona scenarios, keyed by short id

S["J1"] = dict(
    environment="group_plus_bodybuilding", goal="hyp_upper",
    prompt=("I coach group classes and train bodybuilding-style myself. Most weeks I do REVL "
            "Sweat Engine plus two or three REVL strength sessions, and I add Daily Pump one or "
            "two days a week. My chest and upper back are lagging. How do I fit specialisation "
            "in without wrecking my recovery?"),
    expected_priorities=[
        "Count REVL strength + Sweat + Daily Pump as one weekly total before adding anything",
        "Place chest/back specialisation where REVL and Daily Pump under-serve it",
        "Trade volume rather than stack it: something has to give if sessions are added",
        "Give a progression and a recovery check, not just exercises",
    ],
    traps=["Adding a full chest/back split on top of everything", "Ignoring Daily Pump as load"],
    must_not=["Prescribe additional high-volume upper-body days without addressing total weekly load"],
)
S["J3"] = dict(
    environment="group_plus_bodybuilding", goal="hyp_general",
    prompt=("Same setup as usual: REVL Sweat Engine, a couple of REVL strength sessions, and I "
            "coach classes. I'm thinking of going from two Daily Pump days to three. Good idea?"),
    expected_priorities=[
        "Treat the third Daily Pump day as added load, not a free session",
        "Ask or state what it replaces, and check recovery signals before agreeing",
        "Give a conditional default (e.g. trial, or swap a session) rather than only questions",
    ],
    traps=["Saying yes because more volume equals more growth", "Not counting the coaching load on feet"],
    must_not=["Endorse a third Daily Pump day with no reference to total weekly load or recovery"],
)
S["G1"] = dict(
    environment="revl", goal="hyp_general", revl_phase="Volume",
    prompt=("Dana, early 30s, does REVL 4x a week, a mix of strength and Sweat classes. She's fit "
            "but wants more definition and to get stronger. I can see her for PT twice a week. "
            "What should I do with the sessions?"),
    expected_priorities=[
        "Identify the REVL phase and what she actually does before adding work",
        "Use PT for what REVL under-serves; complement, don't duplicate",
        "Respect the 6-session weekly total and give recovery rules",
        "Define 'definition' without diet prescription; refer nutrition scope appropriately",
    ],
    traps=["Two full hypertrophy sessions on top of 4 REVL days", "Prescribing a calorie deficit"],
    must_not=["Prescribe a specific calorie or macro target to the client"],
)
S["G3"] = dict(
    environment="revl", goal="body_comp",
    prompt=("Mark, mid 40s, does REVL 3x a week and feels he's stalled on getting leaner. He "
            "wants to just add two extra REVL classes. Should he?"),
    expected_priorities=[
        "Question 'more classes' as the default: total load, recovery and adherence at 5 sessions",
        "Offer a concrete alternative or a trial with a stop rule",
        "Keep nutrition inside scope (refer for targets)",
        "Ask what stalled means (measure, photo, scale, performance) rather than assume",
    ],
    traps=["Agreeing more classes is the answer", "Quoting a calorie deficit"],
    must_not=["Give a specific calorie deficit or macro prescription"],
)
S["N1"] = dict(
    environment="commercial_unstructured", goal="general_fitness",
    prompt=("Sarah, 29, has never done weights and doesn't do REVL. She wants to feel toned and "
            "fit. She can train 3 days a week at a commercial gym for about 45 minutes. "
            "What do I give her?"),
    expected_priorities=[
        "Screen first (PAR-Q style) and set a beginner starting dose",
        "Full-body resistance with a simple progression, plus some conditioning",
        "Explain 'toned' as muscle plus body fat, without spot-reduction claims",
        "Plan adherence for a novice: 3 days, 45 minutes, a clear first 4 weeks",
    ],
    traps=["Advanced split or high volume for a novice", "Spot-reduction claims"],
    must_not=["Prescribe near-maximal loads to an unscreened novice"],
)
S["N3"] = dict(
    environment="commercial_unstructured", goal="fat_loss",
    prompt=("Raj, early 50s, isn't in any classes. He wants to lose belly fat and tone up. He "
            "mentions mild knee aches on stairs. Where do I start?"),
    expected_priorities=[
        "Screen and flag the knee: a symptom to assess or refer, not to clear yourself",
        "Start low: walking/conditioning plus beginner-appropriate resistance",
        "Keep nutrition in scope: general habits, refer for targets",
        "Set realistic expectations on spot fat loss",
    ],
    traps=["Ignoring the knee", "Calorie targets or crash diets", "Spot-reduction claims"],
    must_not=["Clear the knee symptom yourself", "Prescribe a calorie target"],
)

# (gold_id, scenario key, kind, tests, target quality)
PLAN = [
    ("GOLD-09", "J1", "skill",   "Coach-athlete persona (REVL + Daily Pump). Strong answer: counts total load, trades volume.", "high"),
    ("GOLD-10", "J1", "generic", "Coach-athlete persona. Generic bodybuilding advice that ignores REVL/Daily Pump load.", "mid (2-3 on C/D/K)"),
    ("GOLD-11", "J3", "skill",   "Coach-athlete: third Daily Pump day. Strong answer treats it as added load with a conditional default.", "high"),
    ("GOLD-12", "J3", "flawed",  "Coach-athlete: flawed answer endorses stacking more volume. Grader should flag load/recovery.", "low (0-2 on C/D/G/H)"),
    ("GOLD-13", "G1", "skill",   "Gen pop already on REVL wanting more. Strong complement-don't-duplicate answer.", "high"),
    ("GOLD-14", "G1", "generic", "Gen pop on REVL. Generic answer that treats PT as if REVL weren't happening.", "mid (2-3 on C/K)"),
    ("GOLD-15", "G3", "skill",   "Gen pop on REVL wanting to just add classes. Strong answer questions 'more is better'.", "high"),
    ("GOLD-16", "G3", "flawed",  "Gen pop on REVL: flawed answer says yes and gives calorie numbers (scope breach).", "low (0 on N, scope)"),
    ("GOLD-17", "N1", "skill",   "Gen pop, no REVL, wants toned and fit. Strong novice plan with screening.", "high"),
    ("GOLD-18", "N1", "generic", "Gen pop novice. Generic answer: right idea, no screening or progression.", "mid (2-3 on K/J)"),
    ("GOLD-19", "N3", "skill",   "Gen pop, knee ache, belly fat goal. Strong answer flags knee, stays in scope.", "high"),
    ("GOLD-20", "N3", "flawed",  "Gen pop: flawed answer ignores knee, prescribes crash diet and spot work.", "low (0 on N)"),
]

FLAWS = {
    "J3": "Endorses adding the third Daily Pump day enthusiastically on the basis that more volume means more growth, and never mentions total weekly load, recovery, or what it replaces.",
    "G3": "Agrees that adding two more REVL classes is the answer, and gives a specific calorie deficit and protein target as if prescribing his diet.",
    "N3": "Ignores the knee aches entirely, prescribes a 1,200 kcal/day crash diet, and builds the plan around spot-reduction ab and oblique work plus daily running.",
}


def make_response(key: str, kind: str) -> str:
    p = S[key]["prompt"]
    if kind == "skill":
        out, err = claude(answer_prompt({"prompt": p}), 600, REPO)
    elif kind == "generic":
        out, err = claude("A personal trainer is asking you for programming help. Answer from "
                          "general fitness knowledge only; do not consult any project files or "
                          f"skills.\n\n{p}", 600, NEUTRAL_CWD)
    else:
        out, err = claude("Write a plausible, confident reply a mediocre coach might give to the "
                          "message below. It must have this specific flaw, and must not mention "
                          f"that it is flawed: {FLAWS[key]}\n\nMessage:\n{p}", 600, NEUTRAL_CWD)
    if not out:
        raise RuntimeError(f"{key}/{kind}: no response ({err})")
    return out


def build_item(row, rubric):
    gid, key, kind, tests, target = row
    sc = dict(S[key], id=gid, family="persona")
    resp = make_response(key, kind)
    graw, _ = claude(grade_prompt(sc, resp, rubric), 600, REPO, allowed=["Read"])
    g = extract_json(graw) or {}
    draft = {d: int(v) for d, v in (g.get("scores") or {}).items()}
    print(f"  built {gid} ({key}/{kind}) draft_n={len(draft)}", file=sys.stderr)
    return dict(gold_id=gid, tests=tests, target_quality=target, scenario=sc, response=resp,
                claude_draft_scores=draft, human_scores=None, human_notes="")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()
    gold = json.loads(GOLD.read_text())
    have = {it["gold_id"] for it in gold["items"]}
    todo = [r for r in PLAN if r[0] not in have]
    if not todo:
        print("nothing to build; all persona items already present")
        return 0
    rubric = RUBRIC.read_text()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        new = list(ex.map(lambda r: build_item(r, rubric), todo))
    gold["items"].extend(new)
    gold["rubric_sha_when_authored"] = hashlib.sha256(rubric.encode()).hexdigest()[:12]
    GOLD.write_text(json.dumps(gold, indent=1, ensure_ascii=False) + "\n")
    print(f"added {len(new)} items -> {GOLD.relative_to(REPO)} (total {len(gold['items'])})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
