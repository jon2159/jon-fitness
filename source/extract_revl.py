#!/usr/bin/env python3
"""Step 1 of the REVL reference build — extract the text off the REVL workout
screenshots into one traceable Markdown file.

Input   : the two screenshot libraries on disk (git-ignored, local only):
              REVL Block 1 2026/
              REVL Block 2 programming 2026/
          each with 13 phase-week subfolders (Volume Wk 1 .. Rebuild Wk 3) and one
          PNG per session, named "<day> <session>.png".

Engines : two independent readers, so disagreement is visible instead of a silent
          guess:
            A. rapidocr-onnxruntime  (pure-Python, CPU)
            B. Apple Vision  (VNRecognizeTextRequest) via a tiny Swift helper this
               script compiles on first run — used automatically when `swiftc` is
               present (macOS). Skipped gracefully otherwise.

Output  : source/revl_raw_data.md
            - one section per screenshot, in chronological order
              (Block -> phase-week -> day/session)
            - phase / week / day / session headers inferred from the folder + file
              name (flagged as inferred)
            - the merged reading, then each engine's raw output
            - a light structured parse (sections, exercise-looking lines,
              set/rep/load/tempo/rest/cap tokens) marked LOW-CONFIDENCE
            - explicit [?] flags on lines the two engines disagree on or that look
              partially illegible
          Per-image engine output is cached under source/.revl_ocr_cache/.

This file is the raw evidence layer. It deliberately does NOT interpret the
programming — that is Step 2 (source/revl_programming_analysis.md).

Usage :
    python source/extract_revl.py                 # full run, both blocks
    python source/extract_revl.py --limit 8        # smoke test (writes partial)
    python source/extract_revl.py --blocks 1       # one block only
    python source/extract_revl.py --no-vision      # rapidocr only
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import os
import re
import subprocess
import sys
import textwrap
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = Path(__file__).resolve().parent
BLOCK_DIRS = {
    1: REPO / "REVL Block 1 2026",
    2: REPO / "REVL Block 2 programming 2026",
}
OUT = SRC / "revl_raw_data.md"
CACHE = SRC / ".revl_ocr_cache"
VISION_BIN = CACHE / "revl_vision_ocr"
VISION_SRC = CACHE / "revl_vision_ocr.swift"

PHASE_ORDER = [
    "Volume Wk 1", "Volume Wk 2", "Volume Wk 3",
    "Build Wk 1", "Build Wk 2", "Build Wk 3",
    "Deload Wk 1",
    "Peak Wk 1", "Peak Wk 2", "Peak Wk 3",
    "Rebuild Wk 1", "Rebuild Wk 2", "Rebuild Wk 3",
]
DAY_ORDER = ["monday", "tuesday", "wednesday", "thursday", "friday",
             "saturday", "sunday", "qld", "albury", "coaches"]

VISION_SWIFT = r'''
import Foundation
import Vision
import AppKit

for path in CommandLine.arguments.dropFirst() {
    var out = ""
    if let img = NSImage(contentsOfFile: path),
       let tiff = img.tiffRepresentation,
       let bmp = NSBitmapImageRep(data: tiff),
       let cg = bmp.cgImage {
        let req = VNRecognizeTextRequest()
        req.recognitionLevel = .accurate
        req.usesLanguageCorrection = false
        let handler = VNImageRequestHandler(cgImage: cg, options: [:])
        do {
            try handler.perform([req])
            if let obs = req.results {
                out = obs.compactMap { $0.topCandidates(1).first?.string }.joined(separator: "\n")
            }
        } catch { out = "__VISION_ERROR__ \(error)" }
    } else { out = "__LOAD_ERROR__" }
    try? out.write(toFile: path + ".visiontxt", atomically: true, encoding: .utf8)
}
'''

# --------------------------------------------------------------------------- infer

def phase_week_num(folder: str) -> int:
    try:
        return PHASE_ORDER.index(folder) + 1
    except ValueError:
        return 99


def parse_phase_week(folder: str):
    m = re.match(r"(Volume|Build|Deload|Peak|Rebuild)\s+Wk\s+(\d+)", folder, re.I)
    if m:
        return m.group(1).title(), int(m.group(2))
    return folder, None


def day_key(fname: str):
    stem = fname.lower().rsplit(".", 1)[0]
    first = stem.split(" ")[0]
    di = DAY_ORDER.index(first) if first in DAY_ORDER else 50
    return (di, stem)


def parse_day_session(stem: str):
    words = stem.split(" ")
    day = words[0].title() if words and words[0] in DAY_ORDER else None
    session = " ".join(words[1:]).title() if len(words) > 1 else stem.title()
    return day, session


# --------------------------------------------------------------------------- OCR

_rapid = None


def rapid():
    global _rapid
    if _rapid is None:
        from rapidocr_onnxruntime import RapidOCR
        _rapid = RapidOCR()
    return _rapid


def ocr_rapid(path: Path) -> str:
    try:
        res, _ = rapid()(str(path))
        return "\n".join(x[1] for x in res) if res else ""
    except Exception as exc:  # noqa: BLE001
        return f"__RAPID_ERROR__ {exc}"


_vision_ok = None


def vision_available(no_vision: bool) -> bool:
    global _vision_ok
    if no_vision:
        return False
    if _vision_ok is not None:
        return _vision_ok
    if not _which("swiftc"):
        _vision_ok = False
        return False
    CACHE.mkdir(exist_ok=True)
    if not VISION_BIN.exists():
        VISION_SRC.write_text(VISION_SWIFT)
        r = subprocess.run(["swiftc", "-O", str(VISION_SRC), "-o", str(VISION_BIN)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f"  (Vision helper failed to compile; rapidocr only)\n  {r.stderr[:200]}",
                  file=sys.stderr)
            _vision_ok = False
            return False
    _vision_ok = True
    return True


def _which(name: str):
    from shutil import which
    return which(name)


def ocr_vision(path: Path) -> str:
    tmp = CACHE / (hashlib.md5(str(path).encode()).hexdigest()[:16] + ".png")
    side = Path(str(tmp) + ".visiontxt")
    try:
        if not tmp.exists():
            tmp.write_bytes(path.read_bytes())
        subprocess.run([str(VISION_BIN), str(tmp)], capture_output=True, timeout=60)
        txt = side.read_text(encoding="utf-8") if side.exists() else "__VISION_NO_OUTPUT__"
    except Exception as exc:  # noqa: BLE001
        txt = f"__VISION_ERROR__ {exc}"
    finally:
        for p in (tmp, side):
            try:
                p.unlink()
            except OSError:
                pass
    return txt


def cached_ocr(path: Path, engine: str, no_vision: bool) -> str:
    CACHE.mkdir(exist_ok=True)
    key = hashlib.md5(f"{path.relative_to(REPO)}|{engine}".encode()).hexdigest()[:16]
    cf = CACHE / f"{key}.{engine}.txt"
    if cf.exists() and cf.stat().st_mtime >= path.stat().st_mtime:
        return cf.read_text(encoding="utf-8")
    if engine == "rapid":
        txt = ocr_rapid(path)
    elif engine == "vision" and vision_available(no_vision):
        txt = ocr_vision(path)
    else:
        txt = "__ENGINE_UNAVAILABLE__"
    cf.write_text(txt, encoding="utf-8")
    return txt


# --------------------------------------------------------------- merge + structure

def norm_line(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def merge_readings(a: str, b: str):
    """Return (merged_lines, disagreement_flags). Lines only one engine saw, or
    that differ between engines, get a [?] flag."""
    la = [ln.strip() for ln in a.splitlines() if ln.strip()]
    lb = [ln.strip() for ln in b.splitlines() if ln.strip()]
    if not lb or b.startswith(("__ENGINE_UNAVAILABLE__", "__VISION")):
        return la, ["single-engine (rapidocr only) — treat all as low confidence"]
    if not la:
        return lb, ["single-engine (vision only) — treat all as low confidence"]
    sm = difflib.SequenceMatcher(None, [norm_line(x) for x in la], [norm_line(x) for x in lb])
    merged, flags = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            merged += la[i1:i2]
        elif tag == "replace":
            for x in la[i1:i2]:
                merged.append(f"{x}  [?]")
            for y in lb[j1:j2]:
                merged.append(f"{y}  [? vision]")
            flags.append(f"engines differ near: {la[i1] if i1 < i2 else lb[j1]!r}")
        elif tag == "delete":
            for x in la[i1:i2]:
                merged.append(f"{x}  [? rapid only]")
        elif tag == "insert":
            for y in lb[j1:j2]:
                merged.append(f"{y}  [? vision only]")
    return merged, flags


SECT = re.compile(r"^\s*(WARM ?UP|COOL ?DOWN|S\d\.?|SCORE|FINISHER|A\d?\.|B\.|C\.|"
                  r"BLOCK\s*\d|PART\s*\d|EMOM|E\d?MOM|AMRAP|FOR TIME|BUY[- ]?IN)\b", re.I)
PRESCR = re.compile(r"(@\s*\d{1,3}\s*%|\d{1,3}\s*%|@?\s*\d\s*-\s*\d\s*RIR|RIR|RPE\s*\d|"
                    r"\bx\s*\d|\d+\s*x\s*\d+|\d+-\d+-\d+|:\d{2}\b|\d{1,2}:\d{2}|"
                    r"EMOM|E\d?MOM|AMRAP|\bCap\b|TNG|Deadstop|Ecc|Tempo|\bAHAP\b|\bAFAP\b)", re.I)
EXL = re.compile(r"[A-Za-z].*(Deadlift|Squat|Bench|Press|Row|Pull ?Up|Chin ?Up|Lunge|"
                 r"Clean|Snatch|Jerk|Thruster|Swing|Carry|Erg|Bike|Ski|Run|Burpee|"
                 r"Wall ?Ball|Plank|Hold|Stretch|Bridge|Curl|Extension|Raise|Fly|"
                 r"Push ?Up|Dip|Get ?Up|Step|Hinge|RDL|GHD|KB|DB|BB|DBall)", re.I)


def structure(lines):
    out = []
    for ln in lines:
        clean = ln.replace("  [?]", "").replace("  [? vision]", "").replace(
            "  [? rapid only]", "").replace("  [? vision only]", "")
        tags = []
        if SECT.match(clean):
            tags.append("SECTION")
        if EXL.search(clean):
            tags.append("exercise?")
        pres = PRESCR.findall(clean)
        if pres:
            tags.append("prescription?")
        flagged = "[?]" in ln or "[? " in ln
        if tags or flagged:
            mark = " / ".join(tags) if tags else "uncertain"
            out.append(f"- ({mark}) {ln}")
    return out


# --------------------------------------------------------------------------- main

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--blocks", type=int, nargs="+", choices=[1, 2], default=[1, 2])
    ap.add_argument("--no-vision", action="store_true")
    args = ap.parse_args(argv)

    missing = [str(BLOCK_DIRS[b]) for b in args.blocks if not BLOCK_DIRS[b].is_dir()]
    if missing:
        print("ERROR: screenshot folder(s) not found:\n  " + "\n  ".join(missing), file=sys.stderr)
        print("These folders are git-ignored — they must be present locally to extract.", file=sys.stderr)
        return 1

    vision = vision_available(args.no_vision)
    o = []
    o.append("# REVL programming — raw extracted screenshot data (Step 1)\n")
    o.append("Auto-generated by `source/extract_revl.py`. Two independent readers per image:")
    o.append(f"**rapidocr-onnxruntime** and **Apple Vision** "
             f"({'both active' if vision else 'Vision unavailable — rapidocr only'}).\n")
    o.append("> **How to read this file.** These posters use heavily stylised type over")
    o.append("> photos. Both engines misread numbers, drop small print and lose word")
    o.append("> spacing. Lines the two engines disagree on are marked `[?]`. The")
    o.append("> *Structured parse* is a keyword heuristic, **LOW CONFIDENCE** by design.")
    o.append("> Downstream analysis must treat any specific load, %, rep count, tempo or")
    o.append("> cap here as *approximate* — cross-check against the image, never state as")
    o.append("> fact. Phase / week / day / session headers are **inferred from folder and")
    o.append("> file names** (flagged `[inferred]`).\n")

    counts = {}
    err = 0
    processed = 0
    for b in args.blocks:
        root = BLOCK_DIRS[b]
        o.append(f"\n---\n\n# Block {b}  (`{root.name}/`)\n")
        folders = sorted((d for d in root.iterdir() if d.is_dir()),
                         key=lambda d: phase_week_num(d.name))
        n = 0
        for folder in folders:
            phase, wk = parse_phase_week(folder.name)
            wknum = phase_week_num(folder.name)
            o.append(f"\n## Block {b} — {folder.name}  (programme week {wknum}) [inferred]\n")
            o.append(f"- **Phase:** {phase}  ·  **Phase-week:** {wk}  ·  "
                     f"**Overall week:** {wknum}   _(inferred from folder name)_\n")
            for png in sorted(folder.glob("*.png"), key=lambda p: day_key(p.name)):
                n += 1
                if args.limit and processed >= args.limit:
                    o.append(f"### {png.stem} — _(skipped: --limit {args.limit})_\n")
                    continue
                processed += 1
                day, session = parse_day_session(png.stem)
                ra = cached_ocr(png, "rapid", args.no_vision)
                vi = cached_ocr(png, "vision", args.no_vision) if vision else "__ENGINE_UNAVAILABLE__"
                if ra.startswith("__") and "ERROR" in ra:
                    err += 1
                merged, flags = merge_readings(ra, vi)
                struct = structure(merged)

                o.append(f"### {png.stem}")
                o.append(f"`{png.relative_to(REPO)}`  ·  day **{day or '?'}** [inferred]  ·  "
                         f"session **{session}** [inferred]\n")
                if flags:
                    o.append("_Reader notes:_ " + "; ".join(flags) + "\n")
                o.append("**Merged reading** (`[?]` = engines disagree / one-engine-only):\n")
                o.append("```")
                o.append("\n".join(merged) if merged else "(no text detected)")
                o.append("```\n")
                o.append("<details><summary>structured parse — LOW CONFIDENCE keyword heuristic</summary>\n")
                o.append("\n".join(struct) if struct else "_(nothing matched)_")
                o.append("\n</details>\n")
                o.append("<details><summary>raw — rapidocr</summary>\n\n```\n"
                         + ra.strip() + "\n```\n</details>\n")
                if vision:
                    o.append("<details><summary>raw — Apple Vision</summary>\n\n```\n"
                             + vi.strip() + "\n```\n</details>\n")
                if processed % 20 == 0:
                    print(f"  ...{processed} images", file=sys.stderr)
        counts[b] = n

    o.append("\n---\n\n## Extraction summary\n")
    o.append(f"- Blocks: {', '.join(map(str, args.blocks))}")
    for b in args.blocks:
        o.append(f"- Block {b}: {counts[b]} screenshots")
    o.append(f"- Total screenshots: {sum(counts.values())}")
    o.append(f"- OCR'd this run: {processed}" + (f"  (--limit {args.limit})" if args.limit else ""))
    o.append(f"- Engines: rapidocr" + (" + Apple Vision" if vision else " only (no Vision)"))
    o.append(f"- rapidocr errors: {err}")
    o.append(f"- Cache: `{CACHE.relative_to(REPO)}/`  (git-ignored)")
    o.append("\nNext: Step 2 reads this file to build `source/revl_programming_analysis.md`.\n")

    OUT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)}  ({OUT.stat().st_size // 1024} KB, "
          f"{sum(counts.values())} screenshots, {processed} processed, {err} errors, "
          f"engines: rapidocr{'+vision' if vision else ''})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
