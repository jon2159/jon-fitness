#!/usr/bin/env python3
"""Remove every image link from the lesson .md files and tidy the result:
strip image links, drop the '[EXTRA]'-style PPT tag lines, rejoin numbered-list
items whose marker ('1.') was split onto its own line, mark the omitted agenda
slides. Page headings stay so numbering still matches the PDF."""
import re
import sys
from pathlib import Path

# Run after build.py + polish.py; operates on their ./out folder in place.
# Copy out/<lesson>/<lesson>.md into ../.claude/skills/jon-fitness/references/isa-cpt/ afterward.
DST = Path(__file__).parent / "out"
IMG = re.compile(r"^!\[[^\]]*\]\(images/[^)]*\)\s*$", re.M)
STRAY = re.compile(r"^\s*[\[\]();:,.•–—-]?\s*$")
AGENDA = '*(agenda / "Content Covered" slide — omitted)*'


def clean(text):
    text = IMG.sub("", text)
    text = re.sub(r"^\[[A-Z][A-Z ]{2,}\][ \t]*\n?", "", text, flags=re.M)   # [EXTRA] etc.
    lines = ["" if STRAY.match(ln) else ln.rstrip() for ln in text.split("\n")]
    text = "\n".join(lines)
    text = re.sub(r"^(\d{1,2}[.)])[ \t]*\n(?=\S)", r"\1 ", text, flags=re.M)  # rejoin "1.\nItem"
    text = re.sub(r"\n\d{1,2}[.)]\n(?=\n## Page |\n*\Z)", "\n", text)         # drop dangling "9."
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"(## Page \d+)\n\n+(?=## Page )", r"\1\n\n", text)
    text = re.sub(r"(## Page \d+\n)\n(?=## Page |\Z)", rf"\1\n{AGENDA}\n\n", text)
    return text.strip() + "\n"


def main():
    write = "--write" in sys.argv
    for md in sorted(DST.glob("Week*/*.md")):
        old = md.read_text()
        new = clean(old)
        h1 = len(re.findall(r"^## Page \d+$", old, re.M))
        h2 = len(re.findall(r"^## Page \d+$", new, re.M))
        assert h1 == h2, f"{md.name}: {h1}->{h2}"
        assert "](images/" not in new, md.name
        if write and new != old:
            md.write_text(new, encoding="utf-8")
        print(f"{'wrote' if write else 'dry'}  {md.parent.name[:48]:50}  "
              f"{len(old.splitlines()):5d} -> {len(new.splitlines()):5d} lines")


if __name__ == "__main__":
    main()
