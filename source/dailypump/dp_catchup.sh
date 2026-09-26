#!/bin/bash
# Daily Pump catch-up: capture the current week's missing days, then OCR + index. Idempotent and local-only.
# Runs from launchd (see com.jonfitness.dailypump-catchup.plist). Log: ~/DailyPumpData/catchup.log
#   DP_SKIP_IDLE=1  skip the "wait until the Mac is idle" step (used for testing)
set -u
BIN="$(cd "$(dirname "$0")" && pwd)"   # runs from ~/DailyPumpData/bin (deployed copy), NOT from ~/Desktop (TCC-protected)
DATA="${DP_DATA_ROOT:-$HOME/DailyPumpData}"
LOG="$DATA/catchup.log"
LOCK="$DATA/.catchup.lock"
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
mkdir -p "$DATA"
exec >>"$LOG" 2>&1
echo "=== $(date '+%F %T') catch-up start"

# single-instance lock (a lock older than 3 h is treated as stale)
if [ -d "$LOCK" ] && [ -n "$(find "$LOCK" -maxdepth 0 -mmin +180 2>/dev/null)" ]; then rmdir "$LOCK" 2>/dev/null; fi
if ! mkdir "$LOCK" 2>/dev/null; then echo "another run is in progress ($LOCK); exiting"; exit 0; fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

# do not take over the pointer while the user is at the Mac: wait until idle >= 120 s (up to 30 min per run)
idle=0
if [ "${DP_SKIP_IDLE:-0}" != "1" ]; then
  for _ in $(seq 1 30); do
    idle=$(ioreg -c IOHIDSystem | awk '/HIDIdleTime/ {print int($NF/1000000000); exit}')
    [ "${idle:-0}" -ge 120 ] && break
    sleep 60
  done
  if [ "${idle:-0}" -lt 120 ]; then echo "Mac was in use for 30 min; skipping this run (next run will catch up)"; exit 0; fi
fi

cd "$DATA" || exit 1
# cheap pre-check (files only): if nothing is missing for this ISO week, do not touch the app at all
python3 "$BIN/dp_capture.py" --check && { echo "nothing missing; done"; exit 0; }
/usr/bin/caffeinate -u -t 3 ; /usr/bin/caffeinate -i python3 "$BIN/dp_capture.py" || echo "capture exited non-zero"
"$DATA/.venv/bin/python" "$BIN/dp_ingest.py" || echo "ingest exited non-zero"
python3 "$BIN/dp_report.py" || echo "report exited non-zero"
python3 "$BIN/dp_sync_to_repo.py" || echo "sync-to-repo exited non-zero"
echo "=== $(date '+%F %T') done"
