#!/bin/bash
# Deploy the Daily Pump runtime to ~/DailyPumpData/bin and (re)load the LaunchAgent.
# Why: launchd-run processes are blocked from reading ~/Desktop (macOS privacy), so the job must run from a copy.
# Re-run after any change to the scripts in source/dailypump/.
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
DATA="$HOME/DailyPumpData"; BIN="$DATA/bin"
mkdir -p "$BIN"
cp "$SRC"/dp_common.py "$SRC"/dp_ingest.py "$SRC"/dp_capture.py "$SRC"/dp_report.py "$SRC"/dp_sync_to_repo.py "$SRC"/dp_catchup.sh "$BIN"/
cp "$SRC/../extract_revl.py" "$DATA/extract_revl.py"        # OCR engines, resolved as <bin>/../extract_revl.py
swiftc -O "$SRC/dpui.swift" -o "$BIN/dpui"
chmod +x "$BIN/dp_catchup.sh"
# Wrapper app so macOS privacy permissions (Screen Recording, Accessibility) can be granted ONCE to a real app.
# launchd-run bare binaries cannot be granted these reliably; the app is the "responsible process" for its children.
APP="$DATA/DailyPumpCapture.app"
if [ ! -d "$APP" ]; then
  osacompile -o "$APP" -e 'with timeout of 7200 seconds
  do shell script "/bin/bash \"$HOME/DailyPumpData/bin/dp_catchup.sh\""
end timeout'
  /usr/libexec/PlistBuddy -c "Add :LSUIElement bool true" "$APP/Contents/Info.plist" 2>/dev/null || true
  /usr/libexec/PlistBuddy -c "Add :CFBundleIdentifier string com.jonfitness.dailypumpcapture" "$APP/Contents/Info.plist" 2>/dev/null \
    || /usr/libexec/PlistBuddy -c "Set :CFBundleIdentifier com.jonfitness.dailypumpcapture" "$APP/Contents/Info.plist"
  codesign --force --sign - "$APP" >/dev/null 2>&1 || true
fi
PLIST=com.jonfitness.dailypump-catchup.plist
cp "$SRC/$PLIST" "$HOME/Library/LaunchAgents/$PLIST"
launchctl bootout "gui/$(id -u)/com.jonfitness.dailypump-catchup" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$HOME/Library/LaunchAgents/$PLIST"
echo "deployed to $BIN and loaded com.jonfitness.dailypump-catchup (every 2 h, 09:05-21:05)"
