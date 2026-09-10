#!/usr/bin/env python3
"""Claude-authored *wildcard* scenarios — the exploratory generalization layer.

Each cycle, a fresh `claude -p` turn (no jon-fitness skill in its context) invents
a small number of brand-new personal-training situations that are NOT in any
library. They are graded like any other scenario but tracked as their own metric.

Why separate from `generalization.json`:
  - generalization.json is DETERMINISTIC and STABLE — the same items over time,
    so a trend line means something.
  - wildcards are NON-DETERMINISTIC and disposable — they probe for failure modes
    we didn't think to encode. A wildcard result is a single sample, not a trend.

Promotion rule (see evals/README.md): a wildcard is never persisted into the
permanent library as-is. If wildcards keep exposing the *same* underlying failure
pattern, a human distils that pattern into a new permanent adversarial scenario —
the pattern, not the exact prompt.

Usage:
    python evals/wildcards.py --n 3                 # print 3 fresh wildcards as JSON
    python evals/wildcards.py --n 3 --save          # also write results/wildcards/<ts>.json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
WILD_DIR = HERE / "results" / "wildcards"

BRIEF = """You are helping build an evaluation set for an AI that advises personal trainers on
programming. Invent {n} BRAND-NEW client situations that a good strength & conditioning coach
would find genuinely tricky to program for.

Requirements for the set:
- Each must be a realistic message a personal trainer would send, in their words, about ONE
  real client. 3-6 sentences. Include the client's training history, what training they already
  do each week, their goal, their current recovery/life context, and any constraint.
- Each must contain a real decision trap — an obvious answer that a sports scientist would
  consider wrong or incomplete.
- Spread them across different goals, environments and traps. Do NOT make them all about
  group classes, and do NOT all be "client wants more volume".
- Avoid anything requiring medical diagnosis or clinical management.
- These must be DIFFERENT from common textbook examples — surprise an experienced coach.

For each scenario output an object with exactly these keys:
  "prompt"              the trainer's message
  "expected_priorities" 3-6 things a strong answer addresses
  "traps"               2-4 wrong turns the scenario baits
  "must_not"            0-3 hard-failure behaviours (fabrication, out-of-scope, ignoring a stated fact)

Reply with ONLY a JSON array of {n} such objects. No prose, no markdown fence."""


def claude(prompt: str, timeout: int = 300) -> str:
    r = subprocess.run(["claude", "-p", prompt, "--permission-mode", "bypassPermissions",
                        "--allowed-tools", ""],
                       capture_output=True, text=True, timeout=timeout, cwd=str(REPO))
    return r.stdout.strip() if r.returncode == 0 else ""


def _extract_array(text: str):
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.M).strip()
    i, j = text.find("["), text.rfind("]")
    if i == -1 or j == -1:
        return None
    try:
        return json.loads(text[i:j + 1])
    except json.JSONDecodeError:
        return None


def generate(n: int = 3, timeout: int = 300):
    raw = claude(BRIEF.format(n=n), timeout=timeout)
    arr = _extract_array(raw)
    if not arr:
        return []
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = []
    for k, o in enumerate(arr, 1):
        if not isinstance(o, dict) or "prompt" not in o:
            continue
        out.append(dict(
            id=f"WILD-{ts}-{k}",
            family="wildcard",
            set="wildcard",
            environment="wildcard",
            revl_phase=None,
            goal="wildcard",
            training_age="unspecified",
            recovery="unspecified",
            constraint="unspecified",
            pt_frequency="unspecified",
            prompt=o["prompt"],
            expected_priorities=o.get("expected_priorities", []),
            traps=o.get("traps", []),
            must_not=o.get("must_not", []),
            source="claude-authored",
        ))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--save", action="store_true")
    ap.add_argument("--timeout", type=int, default=300)
    args = ap.parse_args()
    w = generate(args.n, args.timeout)
    if not w:
        print("wildcard generation failed (no valid JSON)", file=sys.stderr)
        return 1
    if args.save:
        WILD_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        p = WILD_DIR / f"{ts}.json"
        p.write_text(json.dumps({"generated": ts, "scenarios": w}, indent=1))
        print(f"wrote {p.relative_to(REPO)}", file=sys.stderr)
    print(json.dumps(w, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
