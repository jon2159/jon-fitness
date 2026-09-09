#!/usr/bin/env python3
"""
ISA CPT course-notes -> clean per-lesson Markdown + images.

For each source PDF:
  <Semantic Name>/
     <Semantic Name>.md      one "## Page N" section per page, text in reading
                             order, slide text + text read out of the figures/
                             diagrams woven together, textbook page-refs and
                             course boilerplate stripped.
     images/                 every embedded raster image, pageNN_imgMM.<ext>

Text wording is never altered - only whitespace / line-wrapping / bullet glyphs
are normalised, and whole artifact strings (textbook "(Pg 62)" refs, the
"Sports International Academy" logo, the "ISA CERTIFIED / PERSONAL / TRAINER
COURSE" cover lines) are removed.
"""

import difflib
import re
import shutil
import sys
from pathlib import Path

import fitz  # PyMuPDF

SRC_DIR = Path(__file__).parent / "isa-cpt-pdfs"
OUT_DIR = Path(__file__).parent / "out"

# source stem (without "[STUDENT] ") -> semantic folder / file name
SEMANTIC = {
    "CPT V6.Week 1 Chapter 1 16":
        "Week 01 - Role & Scope of Practice + Legal & Business Considerations (Ch 1, 16)",
    "CPT V6.Week 2 Chapter 2":
        "Week 02 - The ACE Integrated Fitness Training (IFT) Model (Ch 2)",
    "CPT V6.Week 2 Chapter 3":
        "Week 02 - Basics of Behavior Change (Ch 3)",
    "CPT V6.Week 2 Chapter 4":
        "Week 02 - Communication, Goal Setting & Stages of the Client Relationship (Ch 4)",
    "CPT V6.Week 3 Chapter 9":
        "Week 03 - Foundations of Anatomy, Kinesiology & Muscular Training (Ch 9)",
    "CPT V6.Week 4 Chapter 5 7 8":
        "Week 04 - Health Screening, Resting Assessments & Cardiorespiratory Training (Ch 5, 7, 8)",
    "CPT V6.Week 5 Chapter 8 11":
        "Week 05 - Cardiorespiratory Program Design & Integrated Exercise Programming (Ch 8, 11)",
    "CPT V6.Week 6 Chapter 10":
        "Week 06 - Muscular Training Assessments (Ch 10)",
    "CPT V6.Week 7 Chapter 10 11":
        "Week 07 - Muscular Training Assessments & Integrated Exercise Programming (Ch 10, 11)",
    "CPT V6.Week 8 Chapter 14":
        "Week 08 - Exercise Across the Lifespan (Ch 14)",
    "CPT V6.Week 9 Chapter 6 12":
        "Week 09 - Nutrition for Health & Fitness + Clients with Obesity (Ch 6, 12)",
    "CPT V6.Week 10 Chapter 13 15":
        "Week 10 - Clients with Chronic Disease & Musculoskeletal Issues (Ch 13, 15)",
}

OCR_DPI = 200
WEBSAFE_EXT = {"png", "jpg", "jpeg", "gif", "bmp", "webp", "tif", "tiff"}
FANCY_BULLETS = "•▪●◦‣⁃∙◆➢➤➣▷▶"
BULLET_RE = re.compile(r"^(\s*)(?:[" + re.escape(FANCY_BULLETS) + r"]\s*|[-*]\s+)")
SENT_END = ('.', '!', '?', ':', ';', '"', "'", ')', ']', '-', '–', '—', ',')

# textbook / slide reference artifacts, removed wherever they appear
REF_RE = re.compile(
    r"""\s*[\(\[]\s*
        (?:pg|pgs?|page|pp)\.?\s*\d[\w\s.,&\-–—]*?   # "Pg 62", "Pg 20, Table 1-3"
        [\)\]]""",
    re.IGNORECASE | re.VERBOSE,
)
REF_ONLY_RE = re.compile(
    r"^[\(\[]?\s*(?:pg|pgs?|page|pp)\.?\s*\d[\w\s.,&\-–—]*?[\)\]]?$",
    re.IGNORECASE,
)

LOGO_WORDS = {"sports", "international", "academy", "internationai",
              "sportsinternationalacademy", "internationalsportsacademy"}
COVER_LINES = {"isa certified", "personal", "trainer course",
               "isa certified personal trainer course"}
AGENDA_KEYS = {"contentcovered", "tableofcontent", "tableofcontents",
               "learningobjectives", "chapterobjectives", "objectives"}


# ----------------------------------------------------------------- OCR (lazy)
_ocr = None


def get_ocr():
    global _ocr
    if _ocr is None:
        from rapidocr_onnxruntime import RapidOCR
        _ocr = RapidOCR()
    return _ocr


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def toks(s):
    return [t for t in re.findall(r"[a-z0-9]+", s.lower()) if len(t) >= 3]


def despace(line):
    """'W E E K  2' -> 'WEEK 2'."""
    s = line.strip()
    ne = [t for t in s.split(" ") if t]
    if len(ne) >= 5 and all(len(t) == 1 for t in ne):
        s = re.sub(r"(?<=[A-Za-z0-9]) (?=[A-Za-z0-9])", "", s)
        s = re.sub(r"\s{2,}", " ", s)
        return s
    return line


# ----------------------------------------------------------------- geometry
def ocr_lines(page):
    """Full-page OCR -> [(y, x, text)] in PDF points."""
    pix = page.get_pixmap(dpi=OCR_DPI)
    res, _ = get_ocr()(pix.tobytes("png"))
    if not res:
        return []
    scale = 72.0 / OCR_DPI
    out = []
    for box, txt, _c in res:
        txt = txt.strip()
        if not txt or norm(txt) in LOGO_WORDS:
            continue
        ys = [p[1] for p in box]
        xs = [p[0] for p in box]
        out.append((min(ys) * scale, min(xs) * scale, txt))
    return out


def native_lines(page):
    """Native text -> [(y, x, text)], reconstructing word gaps from char boxes
    so letter-spaced display type ('W E E K  2') keeps its word boundaries."""
    out = []
    for b in page.get_text("rawdict")["blocks"]:
        if b.get("type") != 0:
            continue
        for ln in b["lines"]:
            chars = [c for sp in ln["spans"] for c in sp["chars"]]
            if not chars:
                continue
            rec = ""
            for i, c in enumerate(chars):
                if i:
                    prev = chars[i - 1]
                    gap = c["bbox"][0] - prev["bbox"][2]
                    pw = prev["bbox"][2] - prev["bbox"][0]
                    if c["c"] != " " and prev["c"] != " " and gap > max(1.4, 0.45 * pw):
                        rec += " "
                rec += c["c"]
            rec = rec.rstrip()
            if rec.strip():
                x0, y0, _x1, _y1 = ln["bbox"]
                out.append((y0, x0, rec))
    return out


def similar(a, b):
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return 0.0
    if na == nb:
        return 1.0
    if (na in nb or nb in na) and min(len(na), len(nb)) / max(len(na), len(nb)) > 0.55:
        return 0.95
    ta, tb = set(toks(a)), set(toks(b))
    jac = len(ta & tb) / len(ta | tb) if (ta | tb) else 0.0
    return max(jac, difflib.SequenceMatcher(None, na, nb).ratio())


def order_reading(lines, page_w):
    """Order [(y,x,text)] as a human reads: header(s), then column by column.

    Chrome (page numbers, textbook refs) is ignored for the column geometry so a
    lone '[PG 12]' in the far corner can't be mistaken for a second column.
    """
    lines = [l for l in lines if not drop_line(strip_line(l[2]))]
    if not lines:
        return []
    by_y = lambda t: (t[0], t[1])
    uniq = sorted({round(x) for _, x, _ in lines})
    split, best = None, 0
    for a, b in zip(uniq, uniq[1:]):
        c = (a + b) / 2
        if 0.16 * page_w < c < 0.74 * page_w and (b - a) > best:
            best, split = b - a, c
    if split and best > 0.12 * page_w:
        left = sorted((l for l in lines if l[1] < split), key=by_y)
        right = sorted((l for l in lines if l[1] >= split), key=by_y)
        if len(left) >= 3 and len(right) >= 3:
            top = min(l[0] for l in right)
            head = [l for l in left if l[0] < top - 8]
            return head + [l for l in left if l[0] >= top - 8] + right
    return sorted(lines, key=lambda t: (round(t[0] / 6), t[1]))


# ----------------------------------------------------------------- cleaning
def strip_line(line):
    line = REF_RE.sub("", line)
    line = line.replace("\t", " ")
    line = despace(line.strip())                          # before collapsing gaps
    line = re.sub(r"(?<=\S) {2,}(?=\S)", " ", line).strip()
    line = re.sub(r"\(\s+", "(", line)
    line = re.sub(r"\s+\)", ")", line)
    line = re.sub(r"\s+([,.;:!?])", r"\1", line)
    m = BULLET_RE.match(line)
    if m:
        line = m.group(1) + "- " + BULLET_RE.sub("", line).strip()
    return line


def drop_line(line):
    n = norm(line)
    if not n:
        return True
    if n in LOGO_WORDS or n in {norm(c) for c in COVER_LINES}:
        return True
    if re.fullmatch(r"\d{1,3}", line.strip()):
        return True
    if REF_ONLY_RE.match(line.strip()):
        return True
    return False


def clean_block(lines):
    """lines: ordered list of raw text strings -> cleaned markdown text."""
    kept = []
    for raw in lines:
        for piece in raw.split("\n"):
            s = strip_line(piece)
            if s and not drop_line(s):
                kept.append(s)
    text = "\n".join(kept)
    text = re.sub(r"([a-z])-\n([a-z])", r"\1\2", text)          # de-hyphenate wraps
    # rejoin a line broken mid-sentence
    out = []
    for ln in text.split("\n"):
        cont = ln[:1].islower() or ln.lstrip()[:1] in "–—"
        if (out and out[-1] and not out[-1].rstrip().endswith(SENT_END)
                and cont and not ln.lstrip().startswith("- ")):
            out[-1] = out[-1].rstrip() + " " + ln.strip()
        else:
            out.append(ln)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()


# ----------------------------------------------------------------- images
def save_images(doc, page, page_no, img_dir):
    saved, seen = [], set()
    for idx, info in enumerate(page.get_images(full=True), 1):
        xref = info[0]
        if xref in seen:
            continue
        seen.add(xref)
        name = f"page{page_no:02d}_img{idx:02d}"
        try:
            d = doc.extract_image(xref)
            ext, data = d["ext"].lower(), d["image"]
        except Exception:
            ext = data = None
        if ext in WEBSAFE_EXT and data:
            fp = img_dir / f"{name}.{'jpg' if ext == 'jpeg' else ext}"
            fp.write_bytes(data)
        else:
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha >= 4:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                fp = img_dir / f"{name}.png"
                pix.save(fp)
            except Exception as e:
                print(f"    ! page {page_no} img {idx}: {e}")
                continue
        saved.append(fp.name)
    return saved


# ----------------------------------------------------------------- per PDF
def process(pdf_path, stats):
    name = SEMANTIC[pdf_path.stem[len("[STUDENT] "):].strip()]
    folder = OUT_DIR / name
    img_dir = folder / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    md = [f"# {name}", ""]
    n_pages = doc.page_count
    n_img = n_ocr = 0

    for i, page in enumerate(doc):
        page_no = i + 1
        pw = page.rect.width
        nat = native_lines(page)
        och = ocr_lines(page)

        nat_norm_bag = set()
        for _, _, t in nat:
            nat_norm_bag.update(toks(t))

        added = []
        for y, x, t in och:
            if any(similar(t, nt) >= 0.82 for _, _, nt in nat):
                continue
            tk = toks(t)
            if tk and sum(1 for w in tk if w in nat_norm_bag) / len(tk) >= 0.85:
                continue
            added.append((y, x, t))
        # de-dup added lines
        seen, uniq = set(), []
        for y, x, t in sorted(added, key=lambda z: (z[0], z[1])):
            if norm(t) in seen:
                continue
            seen.add(norm(t))
            uniq.append((y, x, t))
        if uniq:
            n_ocr += 1

        ordered = order_reading(nat + uniq, pw)
        raw_lines = [t for _, _, t in ordered]

        # agenda / TOC / objectives slide -> drop its body entirely
        first = norm(raw_lines[0]) if raw_lines else ""
        is_agenda = any(first == k or first.startswith(k) for k in AGENDA_KEYS)
        body = "" if is_agenda else clean_block(raw_lines)

        md.append(f"## Page {page_no}")
        md.append("")
        if body.strip():
            md.append(body)
            md.append("")

        imgs = save_images(doc, page, page_no, img_dir)
        n_img += len(imgs)
        for j, fn in enumerate(imgs, 1):
            md.append(f"![page {page_no} image {j}](images/{fn})")
        if imgs:
            md.append("")

    heads = sum(1 for l in md if re.fullmatch(r"## Page \d+", l))
    assert heads == n_pages, (name, heads, n_pages)
    (folder / f"{name}.md").write_text("\n".join(md).rstrip() + "\n", encoding="utf-8")
    doc.close()
    stats.append((name, n_pages, n_img, n_ocr))
    print(f"   {n_pages} pages, {n_img} images, {n_ocr} pages gained figure text")


def main():
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)
    pdfs = sorted(SRC_DIR.glob("*.pdf"))
    if len(pdfs) != len(SEMANTIC):
        sys.exit(f"expected {len(SEMANTIC)} PDFs, found {len(pdfs)}")
    stats = []
    for p in pdfs:
        print(f"-> {p.name}")
        process(p, stats)
    rep = ["# Extraction report", "",
           "| Lesson | Pages | Images | Pages with figure text added |",
           "|--------|------:|-------:|:---------------------------:|"]
    for name, pg, im, oc in stats:
        rep.append(f"| {name} | {pg} | {im} | {oc} |")
    rep += ["",
            f"Totals: {sum(s[1] for s in stats)} pages, {sum(s[2] for s in stats)} images.",
            "",
            "Notes:",
            "- Page text is in reading order: slide text plus any text read out of "
            "the slide's figures/diagrams (via OCR of the page image), woven together.",
            "- Removed: textbook page references e.g. \"(Pg 62)\" / \"[PG 341-346]\"; "
            "the \"Sports International Academy\" logo; the \"ISA Certified Personal "
            "Trainer Course\" cover lines; lone page numbers. Agenda / \"Content "
            "Covered\" slides are reduced to their title.",
            "- OCR of the slide display font can drop spaces between words on the "
            "few graphics-only pages; wording from the PDF text layer is used "
            "verbatim wherever it exists."]
    (OUT_DIR / "_extraction_report.md").write_text("\n".join(rep) + "\n", encoding="utf-8")
    print(f"\n{sum(s[1] for s in stats)} pages, {sum(s[2] for s in stats)} images -> {OUT_DIR}")


if __name__ == "__main__":
    main()
