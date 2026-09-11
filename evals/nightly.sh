#!/usr/bin/env bash
# jon-fitness nightly evaluation — orchestrator called by the cloud routine
# (and runnable by hand). One invocation = one evaluation cycle + housekeeping.
#
#   1. git pull (cloud checkout may be behind)
#   2. regenerate the scenario library (cheap, deterministic)
#   3. run ONE eval cycle (EVAL_N scenarios, default 15: ~7 benchmark + rotated)
#   4. every 3rd cycle: run the optimizer in analyse-only mode -> PROPOSALS.md
#   5. weekly-ish (Sunday): run the GUARDED optimizer --apply (regression-tested)
#   6. commit results + push
#
# Skill edits are only ever made by step 5's guarded, regression-tested path.
# Steps 1-4 never touch the skill.
#
# Scheduled 2x/night (22:30 + 05:30 SGT, cron 30 14,21 * * *), not 3x. A 3rd
# fire spaced only 4h after the first collided with Anthropic's rolling
# 5-hour usage window and produced nothing (2026-09-10: fires at 22:37/02:38/
# 06:38 SGT scored 2/3 nights -- the 02:38 fire failed outright). 2 fires
# spaced ~7h apart reliably start with a clear window; see evals/README.md.
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
if git diff --cached --quiet; then
  log "nothing to commit (no result files changed) — sync trivially OK"
  log "done (cycle $NEXT, run_cycle rc=$RC)"
  exit 0
fi
git commit -q -m "eval: nightly cycle $NEXT

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FHeBbPq2DUV8b9bysbJqwJ"

# Push with retry: origin/main can move between our pull at the top and now
# (another routine fire, a manual run, or a person committing). A plain push
# failure must never mean "results only exist locally" -- retry against a
# fresh fetch, and if a real merge conflict shows up, resolve it in favour of
# THIS run's result files (they're what we're trying to land) rather than
# leaving the repo in a half-merged state for the next scheduled fire.
PUSHED=0
for attempt in 1 2 3; do
  # Capture output and check git push's OWN exit code -- piping straight into
  # `tail` here would make `if` see tail's exit status (always 0) instead of
  # push's, silently treating every failed push as a success.
  PUSH_OUT=$(git push origin main 2>&1)
  PUSH_RC=$?
  echo "$PUSH_OUT" | tail -5
  if [ "$PUSH_RC" -eq 0 ]; then
    PUSHED=1
    break
  fi
  log "push attempt $attempt failed -- fetching origin/main and retrying"
  git fetch --quiet origin main
  if ! git merge --no-edit -q origin/main; then
    CONFLICTS=$(git diff --name-only --diff-filter=U)
    OUTSIDE_EVALS=$(echo "$CONFLICTS" | grep -vE '^evals/(results/|scenarios/scenarios\.json$)' || true)
    if [ -n "$OUTSIDE_EVALS" ]; then
      # Never auto-resolve a conflict outside the results/scenario files this
      # script owns (e.g. a skill file a human or the guarded optimizer
      # touched concurrently) -- that's exactly the kind of silent clobber
      # the "never weaken skill edits" rule exists to prevent. Bail loudly.
      git merge --abort
      log "merge conflict OUTSIDE evals/results -- refusing to auto-resolve: $OUTSIDE_EVALS"
      log "results are committed locally but NOT pushed; needs a human to resolve"
      PUSHED=0
      break
    fi
    log "merge conflict -- resolving results files"
    # history.jsonl is the permanent scored-results record: a plain "ours" or
    # "theirs" pick would silently DROP whichever side's scenario rows lost,
    # so union both sides' lines instead (dedup exact repeats, keep order).
    if echo "$CONFLICTS" | grep -qx "evals/results/history.jsonl"; then
      git show :2:evals/results/history.jsonl > /tmp/nightly_ours_history.jsonl 2>/dev/null || true
      git show :3:evals/results/history.jsonl > /tmp/nightly_theirs_history.jsonl 2>/dev/null || true
      awk '!seen[$0]++' /tmp/nightly_ours_history.jsonl /tmp/nightly_theirs_history.jsonl \
        > evals/results/history.jsonl
      rm -f /tmp/nightly_ours_history.jsonl /tmp/nightly_theirs_history.jsonl
      git add evals/results/history.jsonl
    fi
    # Everything else that's still conflicted is regenerated or low-stakes
    # (rotation_state.json, REPORT.md, scenarios.json, PROPOSALS.md) -- keep
    # our side; it self-corrects on the next cycle.
    for f in $(git diff --name-only --diff-filter=U); do
      git checkout --ours -- "$f" 2>/dev/null || true
      git add "$f"
    done
    git commit --no-edit -q || true
  fi
  sleep 5
done

# Never trust the push exit code alone -- confirm origin/main actually points
# at what we just committed before calling this a successful sync.
git fetch --quiet origin main
LOCAL_HEAD=$(git rev-parse HEAD)
REMOTE_HEAD=$(git rev-parse origin/main 2>/dev/null || echo "unknown")
if [ "$PUSHED" -eq 1 ] && [ "$LOCAL_HEAD" = "$REMOTE_HEAD" ]; then
  log "SYNC OK — origin/main == $LOCAL_HEAD (cycle $NEXT results are live on GitHub)"
  log "done (cycle $NEXT, run_cycle rc=$RC)"
  exit 0
else
  log "SYNC FAILED after 3 attempts — local HEAD=$LOCAL_HEAD origin/main=$REMOTE_HEAD"
  log "Cycle $NEXT results are committed LOCALLY in this container but NOT synced to your repo."
  log "done (cycle $NEXT, run_cycle rc=$RC, SYNC FAILED)"
  exit 1
fi
