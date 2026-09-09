#!/usr/bin/env python3
"""Step 2 helper — quantify movement-pattern / quality exposure across the REVL
screenshots, so the written analysis rests on counts rather than impressions.

Reads the OCR produced by extract_revl.py (source/.revl_ocr_cache/) and emits
frequency tables to stdout (and, with --md, a Markdown block ready to paste into
source/revl_programming_analysis.md).

Method, stated plainly so the numbers can be judged:
  - Unit of analysis = one screenshot (= one class session).
  - A pattern is "present in a session" if any of its keywords appears anywhere in
    that session's merged OCR text. Presence, not rep-count — OCR cannot be trusted
    for rep/set arithmetic.
  - Keyword lists are deliberately conservative and are printed with --show-keys.
  - A session can hit many patterns; percentages are share-of-sessions, not shares
    of a total.
Limits: OCR misreads, abbreviations and synonyms are not exhaustive; treat every
number as an approximate lower bound on exposure.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = Path(__file__).resolve().parent
CACHE = SRC / ".revl_ocr_cache"
BLOCK_DIRS = {1: REPO / "REVL Block 1 2026", 2: REPO / "REVL Block 2 programming 2026"}
PHASE_ORDER = ["Volume Wk 1", "Volume Wk 2", "Volume Wk 3",
               "Build Wk 1", "Build Wk 2", "Build Wk 3", "Deload Wk 1",
               "Peak Wk 1", "Peak Wk 2", "Peak Wk 3",
               "Rebuild Wk 1", "Rebuild Wk 2", "Rebuild Wk 3"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

PATTERNS = {
    "Squat (bilateral)":      r"\b(back squat|front squat|bb squat|goblet squat|air squat|cyclist squat|fr squat|thruster|wall ball|dball squat|squat clean|overhead squat|box squat)\b",
    "Hinge (bilateral)":      r"\b(deadlift|rdl|sumo deadlift|good morning|hip thrust|glute bridge|kb swing|swing|clean pull|high pull|back extension|gtos|ground to overhead)\b",
    "Unilateral lower":       r"\b(split squat|bulgarian|lunge|step up|step down|single leg|sl |pistol|cossack|skater|shrimp)\b",
    "Horizontal push":        r"\b(bench press|floor press|push up|dip|chest press|fly)\b",
    "Vertical push":          r"\b(strict press|shoulder press|push press|overhead press|jerk|arnold press|sto|shoulder to overhead|handstand|hspu|devils press)\b",
    "Horizontal pull":        r"\b(bent over row|pendlay|ring row|prone row|chainsaw|inverted row|seal row|renegade row|db row|kb row)\b",
    "Vertical pull":          r"\b(pull up|chin up|pull-up|chin-up|lat pulldown|c2b|scap pull|kip swing|dead ?hang|toes to bar|ttb|k2c|kipping)\b",
    "Carry / loaded hold":    r"\b(carry|farmer|suitcase|front rack hold|fr hold|oh hold|overhead carry|plate oh|waiter|sandbag hold)\b",
    "Rotation / anti-rotation": r"\b(pallof|russian twist|rotation|anti-rotation|windmill|turkish|get ?up|side plank|woodchop|landmine)\b",
    "Core / trunk (non-rot.)": r"\b(plank|hollow|deadbug|dead bug|v-up|sit ?up|superman|leg raise|ab wheel|toes to bar|ttb|k2c|candlestick)\b",
    "Olympic / ballistic":    r"\b(power clean|hang clean|snatch|clean & jerk|clean and jerk|jerk|box jump|broad jump|jump squat|med ?ball|dball power|high pull|kb clean)\b",
    "Erg / machine cardio":   r"\b(ski erg|row erg|bike erg|echo bike|erg|assault|c2|rower|skierg|bikeerg)\b",
    "Running / locomotion":   r"\b(run|shuttle|sprint|jog|km|400m|800m|1000m|200m run)\b",
    "Burpee / mixed metcon":  r"\b(burpee|devils press|man maker|bear crawl|sled|battle rope)\b",
}

QUALITIES = {
    "%1RM prescribed":        r"@\s*\d{1,3}\s*[-–]?\s*\d{0,3}\s*%|\b\d{2}\s*%",
    "RIR prescribed":         r"\bRIR\b",
    "RPE prescribed":         r"\bRPE\s*\d",
    "Tempo / eccentric cue":  r"\b(\d\s*s\s*ecc|ecc|tempo|pause|paused|deadstop|tng|2020|3s)\b",
    "EMOM / interval density": r"\bE\d?MOM\b|\bEvery\s+\d",
    "AMRAP / for-time":       r"\bAMRAP\b|\bfor time\b|\bAFAP\b|\bcap\b",
    "Partner / team format":  r"\bin pairs\b|\bygig\b|\bteams? of\b|\bpartner\b|\bsynchro\b",
    "Unbroken / max-effort":  r"\bunbroken\b|\bmax\b|\bAHAP\b",
}


def sess_key(path: Path) -> str:
    return hashlib.md5(f"{path.relative_to(REPO)}|rapid".encode()).hexdigest()[:16]


def vis_key(path: Path) -> str:
    return hashlib.md5(f"{path.relative_to(REPO)}|vision".encode()).hexdigest()[:16]


def load_text(path: Path) -> str:
    parts = []
    for k, eng in ((sess_key(path), "rapid"), (vis_key(path), "vision")):
        f = CACHE / f"{k}.{eng}.txt"
        if f.exists():
            t = f.read_text(encoding="utf-8", errors="replace")
            if not t.startswith("__"):
                parts.append(t)
    return "\n".join(parts).lower()


def session_type(stem: str) -> str:
    s = stem.lower()
    for t in ("perform total", "perform lower", "perform upper", "move total",
              "sweat sprint baseline", "sweat engine baseline",
              "sweat sprint", "sweat engine", "sweat team", "complete"):
        if t in s:
            return t.title()
    return "Other/Special"


def phase_of(folder: str) -> str:
    return folder.split(" Wk")[0]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--md", action="store_true", help="emit Markdown tables")
    ap.add_argument("--show-keys", action="store_true")
    args = ap.parse_args(argv)

    if args.show_keys:
        for k, v in {**PATTERNS, **QUALITIES}.items():
            print(f"{k}\n    {v}\n")
        return 0

    sessions = []
    for b, root in BLOCK_DIRS.items():
        if not root.is_dir():
            continue
        for folder in sorted((d for d in root.iterdir() if d.is_dir()),
                             key=lambda d: PHASE_ORDER.index(d.name) if d.name in PHASE_ORDER else 99):
            for png in sorted(folder.glob("*.png")):
                txt = load_text(png)
                if not txt:
                    continue
                sessions.append(dict(block=b, folder=folder.name, phase=phase_of(folder.name),
                                     week=PHASE_ORDER.index(folder.name) + 1 if folder.name in PHASE_ORDER else 0,
                                     stem=png.stem, day=png.stem.split(" ")[0].lower(),
                                     stype=session_type(png.stem), text=txt))
    if not sessions:
        print("No OCR cache found — run: python source/extract_revl.py", file=sys.stderr)
        return 1

    def hits(txt, rx):
        return bool(re.search(rx, txt, re.I))

    n = len(sessions)
    out = []
    P = out.append
    P(f"Sessions analysed: {n}  (Block 1: {sum(1 for s in sessions if s['block']==1)}, "
      f"Block 2: {sum(1 for s in sessions if s['block']==2)})\n")

    # --- 1. pattern presence overall
    P("### Movement-pattern presence — share of all sessions\n")
    P("| Pattern | sessions | % |")
    P("|---|--:|--:|")
    for name, rx in PATTERNS.items():
        c = sum(1 for s in sessions if hits(s["text"], rx))
        P(f"| {name} | {c} | {100*c/n:.0f}% |")
    P("")

    # --- 2. pattern by session type
    types = [t for t in ["Perform Total", "Perform Lower", "Perform Upper", "Move Total",
                         "Sweat Sprint", "Sweat Engine", "Sweat Team", "Complete"]
             if any(s["stype"] == t for s in sessions)]
    P("### Movement-pattern presence by session type (% of that type's sessions)\n")
    P("| Pattern | " + " | ".join(f"{t} (n={sum(1 for s in sessions if s['stype']==t)})" for t in types) + " |")
    P("|---" * (len(types) + 1) + "|")
    for name, rx in PATTERNS.items():
        row = []
        for t in types:
            ss = [s for s in sessions if s["stype"] == t]
            c = sum(1 for s in ss if hits(s["text"], rx))
            row.append(f"{100*c/len(ss):.0f}%" if ss else "-")
        P(f"| {name} | " + " | ".join(row) + " |")
    P("")

    # --- 3. pattern by phase
    phases = ["Volume", "Build", "Deload", "Peak", "Rebuild"]
    P("### Movement-pattern presence by phase (% of that phase's sessions)\n")
    P("| Pattern | " + " | ".join(f"{p} (n={sum(1 for s in sessions if s['phase']==p)})" for p in phases) + " |")
    P("|---" * (len(phases) + 1) + "|")
    for name, rx in PATTERNS.items():
        row = []
        for p in phases:
            ss = [s for s in sessions if s["phase"] == p]
            c = sum(1 for s in ss if hits(s["text"], rx))
            row.append(f"{100*c/len(ss):.0f}%" if ss else "-")
        P(f"| {name} | " + " | ".join(row) + " |")
    P("")

    # --- 4. pattern by weekday
    P("### Movement-pattern presence by weekday (% of that day's sessions)\n")
    P("| Pattern | " + " | ".join(f"{d.title()} (n={sum(1 for s in sessions if s['day']==d)})" for d in DAYS) + " |")
    P("|---" * (len(DAYS) + 1) + "|")
    for name, rx in PATTERNS.items():
        row = []
        for d in DAYS:
            ss = [s for s in sessions if s["day"] == d]
            c = sum(1 for s in ss if hits(s["text"], rx))
            row.append(f"{100*c/len(ss):.0f}%" if ss else "-")
        P(f"| {name} | " + " | ".join(row) + " |")
    P("")

    # --- 5. prescription qualities by phase
    P("### Prescription style by phase (% of that phase's sessions)\n")
    P("| Quality | " + " | ".join(f"{p}" for p in phases) + " |")
    P("|---" * (len(phases) + 1) + "|")
    for name, rx in QUALITIES.items():
        row = []
        for p in phases:
            ss = [s for s in sessions if s["phase"] == p]
            c = sum(1 for s in ss if hits(s["text"], rx))
            row.append(f"{100*c/len(ss):.0f}%" if ss else "-")
        P(f"| {name} | " + " | ".join(row) + " |")
    P("")

    # --- 6. observed %1RM tokens per phase (evidence, not arithmetic)
    P("### %1RM-looking tokens seen, by phase (raw OCR strings — approximate)\n")
    for p in phases:
        toks = Counter()
        for s in sessions:
            if s["phase"] != p:
                continue
            for m in re.findall(r"@\s*([\d\-–~ ]{1,25}?)\s*%", s["text"]):
                t = re.sub(r"\s+", "", m)
                if re.fullmatch(r"[\d\-–]{1,24}", t):
                    toks[t] += 1
        top = ", ".join(f"`{k}`×{v}" for k, v in toks.most_common(12)) or "(none legible)"
        P(f"- **{p}:** {top}")
    P("")

    # --- 7. weekly session census
    P("### Sessions per phase-week folder\n")
    P("| Folder | Block 1 | Block 2 |")
    P("|---|--:|--:|")
    for f in PHASE_ORDER:
        c1 = sum(1 for s in sessions if s["folder"] == f and s["block"] == 1)
        c2 = sum(1 for s in sessions if s["folder"] == f and s["block"] == 2)
        P(f"| {f} | {c1} | {c2} |")
    P("")

    text = "\n".join(out)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
