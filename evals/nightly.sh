#!/usr/bin/env bash
# jon-fitness nightly evaluation — orchestrator called by the cloud routine
# (and runnable by hand). One invocation = one evaluation cycle + housekeeping.
#
#   1. git pull (cloud checkout may be behind)
#   2. regenerate the scenario library (cheap, deterministic)
#   3. run ONE eval cycle (25 scenarios: ~7 benchmark + ~18 rotated)
#   4. every 3rd cycle: run the optimizer in analyse-only mode -> PROPOSALS.md
#   5. weekly-ish (Sunday): run the GUARDED optimizer --apply (regression-tested)
#   6. commit results + push
#
# Skill edits are only ever made by step 5's guarded, regression-tested path.
# Steps 1-4 never touch the skill.
set -uo pipefail
cd "$(dirname "$0")/.."

log(){ printf '[%s] %s\n' "$(date -u +%H:%M:%S)" "$*"; }

log "pull"
git pull --ff-only --quiet origin main || log "pull failed (continuing on local)"

log "regenerate scenarios"
python3 evals/generate_scenarios.py >/dev/null

CYCLE=$(python3 -c "import json,os;p='evals/results/rotation_state.json';print(json.load(open(p)).get('cycle',0) if os.path.exists(p) else 0)")
NEXT=$((CYCLE+1))
log "running cycle $NEXT"
set -o pipefail
python3 evals/run_cycle.py --n "${EVAL_N:-15}" --label "nightly" 2>&1 | tail -40
RC=$?
set +o pipefail

if [ "$RC" -ne 0 ]; then
  log "cycle exited $RC (0 scored / hard failure) — skipping optimizer, commit and push"
  log "done (cycle $NEXT NOT recorded, run_cycle rc=$RC)"
  exit "$RC"
fi

if [ $((NEXT % 3)) -eq 0 ]; then
  log "optimizer: analyse"
  python3 evals/optimize.py 2>&1 | tail -10
fi

if [ "$(date -u +%u)" = "7" ]; then          # Sunday UTC
  log "optimizer: guarded apply (weekly)"
  python3 evals/optimize.py --apply 2>&1 | tail -20
fi

log "prune cycle transcripts older than 30 days"
find evals/results/cycles -name '*.json' -type f -mtime +30 -delete 2>/dev/null || true

log "commit + push"
git add -A evals/results evals/scenarios/scenarios.json
if ! git diff --cached --quiet; then
  git commit -q -m "eval: nightly cycle $NEXT

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FHeBbPq2DUV8b9bysbJqwJ" || true
fi
git push --quiet origin main 2>&1 | tail -5 || log "push failed"
log "done (cycle $NEXT, run_cycle rc=$RC)"
