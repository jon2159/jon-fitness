#!/usr/bin/env python3
"""Run one jon-fitness evaluation cycle.

    answer  -> a fresh headless Claude runs the scenario with the skill available
    grade   -> a second, independent headless Claude scores it 0-5 on 15 dimensions
    record  -> append to results/history.jsonl, write results/cycles/<ts>.json,
               refresh results/REPORT.md

Scenario selection rotates: least-recently-run standard scenarios first, plus a
fixed slice of the permanent benchmark (adversarial) suite every cycle so
regressions are always visible.

Usage
-----
    python evals/run_cycle.py                     # 25 scenarios (18 rotated + 7 benchmark)
    python evals/run_cycle.py --n 10              # smaller cycle
    python evals/run_cycle.py --only ADV-001 SC-0007
    python evals/run_cycle.py --benchmark-only    # full regression run
    python evals/run_cycle.py --dry-run           # show selection, run nothing
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SKILL_DIR = REPO / ".claude" / "skills" / "jon-fitness"
SCEN = HERE / "scenarios" / "scenarios.json"
RUBRIC = HERE / "rubric.md"
RESULTS = HERE / "results"
HISTORY = RESULTS / "history.jsonl"
CYCLES = RESULTS / "cycles"
STATE = RESULTS / "rotation_state.json"
REPORT = RESULTS / "REPORT.md"

DIMS = list("ABCDEFGHIJKLMNO")
DIM_NAMES = {
    "A": "goal_alignment", "B": "training_specificity", "C": "total_training_load",
    "D": "volume_management", "E": "intensity_management", "F": "frequency_management",
    "G": "fatigue_management", "H": "recovery_compatibility", "I": "exercise_selection",
    "J": "progression", "K": "individualisation", "L": "practicality",
    "M": "long_term_coherence", "N": "safety_caution", "O": "communication",
}
COMPOSITES = {
    "goal_alignment": ["A", "B"],
    "load_management": ["C", "D", "E", "F"],
    "recovery": ["G", "H"],
    "individualisation": ["K", "L"],
    "programming_quality": ["I", "J"],
    "long_term_planning": ["M"],
    "safety": ["N"],
}


# ------------------------------------------------------------------ provenance

def skill_version():
    """Exact skill/reference state used for this cycle: the commit it sits on,
    whether the tree is dirty, and a content hash over every skill markdown file
    (so an uncommitted edit still produces a distinct, comparable fingerprint)."""
    def _git(*a):
        try:
            return subprocess.run(["git", *a], capture_output=True, text=True,
                                  cwd=str(REPO)).stdout.strip()
        except Exception:
            return ""
    files = sorted(SKILL_DIR.rglob("*.md"))
    h = hashlib.sha256()
    for f in files:
        h.update(f.relative_to(REPO).as_posix().encode())
        h.update(b"\0")
        h.update(f.read_bytes())
        h.update(b"\0")
    dirty = bool(_git("status", "--porcelain", "--", str(SKILL_DIR)))
    return {
        "commit": _git("rev-parse", "--short", "HEAD"),
        "skill_dirty": dirty,
        "skill_hash": h.hexdigest()[:16],
        "skill_files": len(files),
    }


# ------------------------------------------------------------------ claude call

def claude(prompt: str, timeout: int, cwd: Path, allowed=None) -> tuple[str, str]:
    """Run a headless Claude turn. Returns (text, error)."""
    cmd = ["claude", "-p", prompt, "--permission-mode", "bypassPermissions"]
    if allowed:
        cmd += ["--allowed-tools", ",".join(allowed)]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           cwd=str(cwd), stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return "", f"timeout after {timeout}s"
    except FileNotFoundError:
        return "", "claude CLI not found on PATH"
    if r.returncode != 0:
        return r.stdout.strip(), f"exit {r.returncode}: {r.stderr.strip()[:300]}"
    return r.stdout.strip(), ""


# ------------------------------------------------------------------ selection

def load_scenarios():
    d = json.loads(SCEN.read_text())
    return d["scenarios"]


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"last_run": {}, "cycle": 0}


def select(scenarios, n, benchmark_slice, only=None, benchmark_only=False):
    if only:
        want = set(only)
        return [s for s in scenarios if s["id"] in want]
    bench = [s for s in scenarios if s.get("benchmark")]
    if benchmark_only:
        return bench
    st = load_state()["last_run"]
    std = [s for s in scenarios if not s.get("benchmark")]
    std.sort(key=lambda s: (st.get(s["id"], 0), s["id"]))          # least-recently-run first
    bench.sort(key=lambda s: (st.get(s["id"], 0), s["id"]))
    k = min(benchmark_slice, len(bench), n)
    return bench[:k] + std[: max(0, n - k)]


# ------------------------------------------------------------------ prompts

def answer_prompt(s):
    return (
        "A personal trainer is asking you for programming help. Answer as you normally "
        "would, using whatever project skills apply.\n\n"
        f"{s['prompt']}"
    )


def grade_prompt(s, response, rubric):
    return f"""You are grading a personal-trainer AI's programming response as a senior strength &
conditioning coach and sports scientist. Be strict and specific. Reward correct decisions and
sound trade-off reasoning; do NOT reward length, exercise variety, or making a session sound hard.

=== RUBRIC ===
{rubric}

=== SCENARIO ===
id: {s['id']}
family: {s.get('family')}
environment: {s.get('environment_label') or s.get('environment')}
REVL phase: {s.get('revl_phase') or 'n/a'}
goal: {s.get('goal_label') or s.get('goal')}
training age: {s.get('training_age')}
recovery context: {s.get('recovery')}
constraint: {s.get('constraint')}
PT frequency available: {s.get('pt_frequency')}

CLIENT MESSAGE THE AI RECEIVED:
{s['prompt']}

EXPECTED PROGRAMMING PRIORITIES (a strong answer hits most of these):
{chr(10).join('- ' + p for p in s.get('expected_priorities', []))}

TRAPS THIS SCENARIO BAITS (falling in should cost marks):
{chr(10).join('- ' + t for t in s.get('traps', [])) or '- (none specified)'}

HARD FAILURES (any of these => score 0 on the affected dimension, and note it):
{chr(10).join('- ' + m for m in s.get('must_not', [])) or '- (none specified)'}

=== RESPONSE TO GRADE ===
{response}

=== OUTPUT ===
Reply with ONLY a JSON object, no prose before or after, no markdown fence:
{{
  "scores": {{ "A": 0-5, "B": 0-5, "C": 0-5, "D": 0-5, "E": 0-5, "F": 0-5, "G": 0-5,
               "H": 0-5, "I": 0-5, "J": 0-5, "K": 0-5, "L": 0-5, "M": 0-5, "N": 0-5, "O": 0-5 }},
  "priorities_hit": ["<expected priorities the response actually addressed>"],
  "priorities_missed": ["..."],
  "traps_fallen_into": ["..."],
  "hard_failures": ["..."],
  "major_strengths": ["..."],
  "major_errors": ["..."],
  "missed_opportunities": ["..."],
  "duplication_or_overtraining_risk": "<none|low|moderate|high> - one line why",
  "recommended_skill_improvement": "<one concrete change to SKILL.md or a reference file, or 'none'>",
  "failure_category": "<missing_knowledge|ambiguous_instruction|conflicting_instruction|poor_decision_hierarchy|excessive_rigidity|insufficient_individualisation|poor_load_management|poor_context_interpretation|none>"
}}"""


def extract_json(text):
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.M).strip()
    i, j = text.find("{"), text.rfind("}")
    if i == -1 or j == -1:
        return None
    try:
        return json.loads(text[i:j + 1])
    except json.JSONDecodeError:
        return None


# ------------------------------------------------------------------ scoring

def composites(scores):
    out = {}
    for name, dims in COMPOSITES.items():
        vals = [scores[d] for d in dims if d in scores]
        out[name] = round(statistics.mean(vals), 3) if vals else None
    vals = [scores[d] for d in DIMS if d in scores]
    out["overall"] = round(statistics.mean(vals), 3) if vals else None
    return out


# ------------------------------------------------------------------ main

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=25)
    ap.add_argument("--benchmark-slice", type=int, default=7)
    ap.add_argument("--only", nargs="+")
    ap.add_argument("--benchmark-only", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--answer-timeout", type=int, default=420)
    ap.add_argument("--grade-timeout", type=int, default=240)
    ap.add_argument("--label", default="", help="tag this cycle (e.g. 'post-fix-C3')")
    args = ap.parse_args(argv)

    scenarios = load_scenarios()
    picked = select(scenarios, args.n, args.benchmark_slice, args.only, args.benchmark_only)
    print(f"cycle: {len(picked)} scenarios "
          f"({sum(1 for s in picked if s.get('benchmark'))} benchmark)", file=sys.stderr)
    if args.dry_run:
        for s in picked:
            print(f"  {s['id']:9s} {s.get('family'):12s} {s['prompt'][:90]}")
        return 0

    RESULTS.mkdir(exist_ok=True)
    CYCLES.mkdir(exist_ok=True)
    rubric = RUBRIC.read_text()
    state = load_state()
    state["cycle"] = state.get("cycle", 0) + 1
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    version = skill_version()
    print(f"skill version: {version['commit']}"
          f"{' +dirty' if version['skill_dirty'] else ''} "
          f"hash={version['skill_hash']} ({version['skill_files']} files)", file=sys.stderr)

    rows = []
    for i, s in enumerate(picked, 1):
        t0 = time.time()
        print(f"[{i}/{len(picked)}] {s['id']} ...", file=sys.stderr, flush=True)
        resp, err = claude(answer_prompt(s), args.answer_timeout, REPO)
        if err or not resp:
            rows.append(dict(scenario_id=s["id"], error=err or "empty response",
                             cycle=state["cycle"], ts=ts))
            print(f"      ! {err or 'empty response'}", file=sys.stderr)
            continue
        used_skill = bool(re.search(r"jon-fitness|ISA CPT|Wk\d+ Ch\d+|Table 9-12|revl-class-integration",
                                    resp, re.I))
        graw, gerr = claude(grade_prompt(s, resp, rubric), args.grade_timeout, REPO,
                            allowed=["Read"])
        g = extract_json(graw)
        if not g or "scores" not in g:
            rows.append(dict(scenario_id=s["id"], error=f"grade parse failed: {gerr or graw[:200]}",
                             cycle=state["cycle"], ts=ts, response=resp))
            print("      ! grading failed", file=sys.stderr)
            continue
        sc = {d: int(g["scores"].get(d, 0)) for d in DIMS if d in g.get("scores", {})}
        comp = composites(sc)
        row = dict(
            ts=ts, cycle=state["cycle"], label=args.label,
            commit=version["commit"], skill_hash=version["skill_hash"],
            skill_dirty=version["skill_dirty"],
            scenario_id=s["id"], family=s.get("family"), environment=s.get("environment"),
            revl_phase=s.get("revl_phase"), goal=s.get("goal"),
            training_age=s.get("training_age"), recovery_context=s.get("recovery"),
            constraint=s.get("constraint"), pt_frequency=s.get("pt_frequency"),
            benchmark=bool(s.get("benchmark")),
            scores=sc, **comp,
            skill_referenced=used_skill,
            priorities_hit=g.get("priorities_hit", []),
            priorities_missed=g.get("priorities_missed", []),
            traps_fallen_into=g.get("traps_fallen_into", []),
            hard_failures=g.get("hard_failures", []),
            major_strengths=g.get("major_strengths", []),
            major_errors=g.get("major_errors", []),
            missed_opportunities=g.get("missed_opportunities", []),
            duplication_risk=g.get("duplication_or_overtraining_risk"),
            recommended_improvement=g.get("recommended_skill_improvement"),
            failure_category=g.get("failure_category"),
            seconds=round(time.time() - t0, 1),
            response=resp,
        )
        rows.append(row)
        state["last_run"][s["id"]] = int(time.time())
        with HISTORY.open("a") as _f:                       # incremental: survive a mid-cycle kill
            _f.write(json.dumps({k: v for k, v in row.items() if k != "response"}) + "\n")
        STATE.write_text(json.dumps(state, indent=1))
        print(f"      overall {comp['overall']}  ({row['seconds']}s)", file=sys.stderr)

    scored = [r for r in rows if "overall" in r]
    (CYCLES / f"{ts}.json").write_text(json.dumps(dict(
        ts=ts, cycle=state["cycle"], label=args.label, skill_version=version,
        n_selected=len(picked), n_scored=len(scored), rows=rows), indent=1))
    STATE.write_text(json.dumps(state, indent=1))

    if scored:
        print(f"\ncycle {state['cycle']}: {len(scored)}/{len(picked)} scored | "
              f"overall {statistics.mean(r['overall'] for r in scored):.2f}", file=sys.stderr)
    write_report()
    return 0


def write_report():
    if not HISTORY.exists():
        return
    rows = [json.loads(l) for l in HISTORY.read_text().splitlines() if l.strip()]
    if not rows:
        return
    by_cycle = {}
    for r in rows:
        by_cycle.setdefault(r["cycle"], []).append(r)

    L = ["# jon-fitness — evaluation performance history\n",
         f"_Auto-written by `evals/run_cycle.py`. {len(rows)} scored scenario runs "
         f"across {len(by_cycle)} cycles._\n",
         "## Cycle history\n",
         "| Cycle | When (UTC) | n | Overall | Goal | Load mgmt | Recovery | Individ. | Prog. | Long-term | Safety | Label |",
         "|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|"]
    for c in sorted(by_cycle):
        rs = by_cycle[c]
        m = lambda k: f"{statistics.mean([r[k] for r in rs if r.get(k) is not None]):.2f}"
        L.append(f"| {c} | {rs[0]['ts']} | {len(rs)} | **{m('overall')}** | {m('goal_alignment')} | "
                 f"{m('load_management')} | {m('recovery')} | {m('individualisation')} | "
                 f"{m('programming_quality')} | {m('long_term_planning')} | {m('safety')} | "
                 f"{rs[0].get('label','')} |")

    latest = by_cycle[max(by_cycle)]
    L += ["\n## Latest cycle — weakest dimensions\n",
          "| Dim | Name | Mean |", "|---|---|--:|"]
    dmeans = []
    for d in DIMS:
        vals = [r["scores"][d] for r in latest if d in r.get("scores", {})]
        if vals:
            dmeans.append((statistics.mean(vals), d))
    for mean, d in sorted(dmeans)[:6]:
        L.append(f"| {d} | {DIM_NAMES[d]} | {mean:.2f} |")

    from collections import Counter
    fc = Counter(r.get("failure_category") for r in latest
                 if r.get("failure_category") and r["failure_category"] != "none")
    if fc:
        L += ["\n## Latest cycle — failure categories\n", "| Category | n |", "|---|--:|"]
        for k, v in fc.most_common():
            L.append(f"| {k} | {v} |")

    traps = Counter(t for r in latest for t in r.get("traps_fallen_into", []))
    if traps:
        L += ["\n## Latest cycle — most-hit traps\n"]
        for t, v in traps.most_common(8):
            L.append(f"- ({v}×) {t}")

    hard = [(r["scenario_id"], h) for r in latest for h in r.get("hard_failures", [])]
    if hard:
        L += ["\n## Hard failures in the latest cycle\n"]
        for sid, h in hard:
            L.append(f"- **{sid}** — {h}")

    bench = [r for r in rows if r.get("benchmark")]
    if bench:
        bc = {}
        for r in bench:
            bc.setdefault(r["cycle"], []).append(r["overall"])
        L += ["\n## Benchmark (regression) trend\n", "| Cycle | n | Benchmark overall |", "|---|--:|--:|"]
        for c in sorted(bc):
            L.append(f"| {c} | {len(bc[c])} | {statistics.mean(bc[c]):.2f} |")

    REPORT.write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
