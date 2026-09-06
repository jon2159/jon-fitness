#!/usr/bin/env python3
"""Second pass over out/*.md: strip textbook page / figure / table references
that survived the first clean - including OCR-mangled ones ('[PG\\n394]',
'[PG 411; 413]', 'Pg473') and citation parentheticals.

Only the token 'pg' / 'pgs' is treated as a page marker - never 'page', so the
'## Page N' section headings are untouched.  Dry-run with no args prints a diff
summary; pass --write to apply.
"""
import re
import sys
from pathlib import Path

OUT = Path(__file__).parent / "out"

JOIN_OPEN = re.compile(r"[\[\(]\s*[Pp][Gg]s?\.?[ \t]*\n[ \t]*")
PAREN_PGNUM = re.compile(r" *\([^)\n]*\bpgs?\.? *\d[^)\n]*\)", re.I)
PAREN_CITE = re.compile(
    r" *\((?:see|refer(?:ence)?s?\s*to|from)\s*"
    r"(?:fig(?:ure)?|table|tbl|chart|diagram|appendix|chapter|ch)\b[^)\n]*\)",
    re.I,
)
INLINE_REF = re.compile(
    r"[ \t]*\b(?:on|see|refer(?:ence)?\s+to|per)\s+pgs?\.?\s*\d[\d\s\-–—]*", re.I)
BRACKET_REF = re.compile(
    r" *[\[\(]? *(?<![A-Za-z])pgs?\.? *\d[\d \t.,;:x&/\-–—]*[\]\)]?", re.I)
# a short line that is only digits/ranges/operators trailing a bracket = a
# leftover fragment of a split '[PG 195 & 203-209]' ref
NUM_FRAG = re.compile(r"^[\d]{1,4}[\d\s.,;:&x×/\-–—]*[\]\)]$")
STRAY = {"", "[", "]", "()", "[]", "( )", "-", "•", "–", "—", ";", ":", ",", ".", "[ ]"}


def polish(text):
    text = JOIN_OPEN.sub("[PG ", text)
    text = PAREN_PGNUM.sub("", text)
    text = PAREN_CITE.sub("", text)
    text = INLINE_REF.sub("", text)
    text = BRACKET_REF.sub("", text)
    text = re.sub(r"[ \t]+([,.;:)])", r"\1", text)
    text = re.sub(r"\(\s*\)", "", text)
    out = []
    for ln in text.split("\n"):
        s = ln.strip()
        out.append("" if (s in STRAY or NUM_FRAG.match(s)) else ln.rstrip())
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def main():
    write = "--write" in sys.argv
    changed = 0
    for md in sorted(OUT.glob("*/*.md")):
        old = md.read_text()
        new = polish(old)
        h_old = len(re.findall(r"^## Page \d+$", old, re.M))
        h_new = len(re.findall(r"^## Page \d+$", new, re.M))
        assert h_old == h_new, f"{md.name}: headings {h_old} -> {h_new}"
        assert len(new) > 0.7 * len(old), f"{md.name}: shrank too much"
        if new != old:
            changed += 1
            if write:
                md.write_text(new, encoding="utf-8")
        left = re.findall(r"(?<![A-Za-z])[Pp][Gg]s?\.? *\d|\((?:see|refer)[^)\n]*\)", new, re.I)
        if left:
            print(f"  {md.parent.name}: leftover {left[:5]}")
    print(f"{'wrote' if write else 'would change'} {changed} files")


if __name__ == "__main__":
    main()
