#!/usr/bin/env python3
"""Extra evaluation layers used by run_cycle.py, kept in their own module so the
core cycle logic stays small:

  - generalization set selection  (held-out benchmark, scenarios/generalization.json)
  - wildcard scenario generation  (delegates to wildcards.generate)
  - the training-science CONSISTENCY pass (an independent 2nd grader call that
    only checks whether a response is internally physiologically coherent)

None of this feeds the optimizer. Generalization + wildcard rows are a
read-only scoreboard; optimize.py filters them out.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
GEN = HERE / "scenarios" / "generalization.json"
GEN_STATE = RESULTS / "generalization_state.json"
WILD_DIR = RESULTS / "wildcards"


# ------------------------------------------------------------------ generalization

def select_generalization(n):
    """Least-recently-run n from the held-out set. Its own rotation state so it
    never perturbs the primary rotation."""
    if n <= 0 or not GEN.exists():
        return []
    scen = json.loads(GEN.read_text())["scenarios"]
    st = {}
    if GEN_STATE.exists():
        st = json.loads(GEN_STATE.read_text()).get("last_run", {})
    scen.sort(key=lambda s: (st.get(s["id"], 0), s["id"]))
    picked = scen[:n]
    for s in picked:
        s["set"] = "generalization"
    return picked


def mark_generalization_run(ids):
    st = {"last_run": {}}
    if GEN_STATE.exists():
        st = json.loads(GEN_STATE.read_text())
        st.setdefault("last_run", {})
    now = int(time.time())
    for i in ids:
        st["last_run"][i] = now
    GEN_STATE.parent.mkdir(exist_ok=True)
    GEN_STATE.write_text(json.dumps(st, indent=1))


# ------------------------------------------------------------------ wildcards

def make_wildcards(n, timeout=300):
    if n <= 0:
        return []
    try:
        from wildcards import generate
    except ImportError:
        return []
    w = generate(n, timeout=timeout)
    for s in w:
        s["set"] = "wildcard"
    if w:
        WILD_DIR.mkdir(parents=True, exist_ok=True)
        ts = w[0]["id"].split("-", 1)[1].rsplit("-", 1)[0]
        (WILD_DIR / f"{ts}.json").write_text(json.dumps({"scenarios": w}, indent=1))
    return w


# ------------------------------------------------------------------ consistency pass

CONSISTENCY_CHECKS = [
    "Claims recovery is poor / compromised but still increases volume or intensity.",
    "Claims high fatigue or soreness in a body area, then prescribes another high-volume "
    "session for that same area without justifying it.",
    "Adds hypertrophy or strength volume without accounting for the client's existing "
    "REVL / class / concurrent training exposure.",
    "Treats muscle soreness as automatically meaning rest is needed.",
    "Treats absence of soreness as evidence the training was ineffective.",
    "Adds a Russian / max-strength protocol mainly because the client asked, without "
    "running the eligibility gate and the total-load dosing decision.",
    "Treats REVL / BFT / group training as something that must always be reduced, rather "
    "than integrated.",
    "Prescribes a physiologically sound plan that does not fit the client's stated "
    "schedule, time, or equipment.",
    "Prescribes an intensity that contradicts the stated training age or REVL phase.",
    "States a physiological mechanism or number as fact without support.",
]


def consistency_prompt(s, response):
    checks = "\n".join(f"{i+1}. {c}" for i, c in enumerate(CONSISTENCY_CHECKS))
    return f"""You are a sports scientist auditing ONE thing: is this training recommendation
INTERNALLY CONSISTENT? Not whether it is the best possible plan — only whether it contradicts
itself or basic exercise physiology given the client's situation.

CLIENT MESSAGE:
{s['prompt']}

RECOMMENDATION:
{response}

Check for these contradictions specifically:
{checks}

Also flag any other clear internal contradiction (e.g. "deload" then a harder week; "keep it
short" then 12 exercises; "we don't know their max" then a %1RM prescription).

Reply with ONLY this JSON, no prose, no fence:
{{
  "consistency_score": 0-5,   // 5 = fully coherent; 3 = one soft contradiction; 0 = incoherent or self-cancelling
  "contradictions": ["<each contradiction found, one sentence, quote the offending bit>"],
  "coherent_strengths": ["<places the reasoning holds together well>"]
}}"""


def run_consistency(s, response, claude_fn, extract_json_fn, timeout, repo):
    """claude_fn / extract_json_fn passed in from run_cycle to avoid a circular import."""
    raw, err = claude_fn(consistency_prompt(s, response), timeout, repo, allowed=["Read"])
    g = extract_json_fn(raw)
    if not g or "consistency_score" not in g:
        return {"consistency_score": None, "contradictions": [], "consistency_error": err or "parse failed"}
    try:
        score = int(g["consistency_score"])
    except (TypeError, ValueError):
        score = None
    return {
        "consistency_score": score,
        "contradictions": g.get("contradictions", []) or [],
        "coherent_strengths": g.get("coherent_strengths", []) or [],
    }
