# `source/` — raw material & extraction scripts

## ISA CPT course notes

The 12 original course PDFs live in `isa-cpt-pdfs/`.

`build.py` / `polish.py` / `strip_images.py` turn those PDFs into clean per-lesson
Markdown (one `## Page N` section per slide, text in reading order, figure/diagram
text woven in, textbook page-refs and course boilerplate stripped).

**The canonical extracted text is `.claude/skills/jon-fitness/references/isa-cpt/`** —
that is what the `jon-fitness` skill reads. This folder only holds the PDFs and the
reproduction scripts; regenerate into the skill's `references/isa-cpt/` if the notes
ever change.

12 lessons · 577 slides · ~31,877 words.

| Lesson | Slides | Words |
|---|--:|--:|
| Week 01 - Role & Scope of Practice + Legal & Business Considerations (Ch 1, 16) | 36 | 2,488 |
| Week 02 - Basics of Behavior Change (Ch 3) | 20 | 1,164 |
| Week 02 - Communication, Goal Setting & Stages of the Client Relationship (Ch 4) | 18 | 914 |
| Week 02 - The ACE Integrated Fitness Training (IFT) Model (Ch 2) | 14 | 534 |
| Week 03 - Foundations of Anatomy, Kinesiology & Muscular Training (Ch 9) | 42 | 1,679 |
| Week 04 - Health Screening, Resting Assessments & Cardiorespiratory Training (Ch 5, 7, 8) | 81 | 4,820 |
| Week 05 - Cardiorespiratory Program Design & Integrated Exercise Programming (Ch 8, 11) | 48 | 2,243 |
| Week 06 - Muscular Training Assessments (Ch 10) | 84 | 4,821 |
| Week 07 - Muscular Training Assessments & Integrated Exercise Programming (Ch 10, 11) | 49 | 2,417 |
| Week 08 - Exercise Across the Lifespan (Ch 14) | 25 | 1,655 |
| Week 09 - Nutrition for Health & Fitness + Clients with Obesity (Ch 6, 12) | 35 | 2,414 |
| Week 10 - Clients with Chronic Disease & Musculoskeletal Issues (Ch 13, 15) | 125 | 6,728 |
| **Total** | **577** | **31,877** |

## How the extraction works

- **Reading order** — text flows title → left column → right column per slide.
- **Wording** — verbatim from each slide's text layer where it has one. Text that lived
  only inside a picture was OCR'd and can lose spaces between words (e.g. `FattyAcids`)
  or, on a dense data table, come through as a flat list of cell values.
- **Removed** — textbook page/figure references (`(Pg 62)`, `[PG 341-346]`,
  `(Refer to Figure 5-4)`…); the *Sports International Academy* logo; the
  *ISA Certified Personal Trainer Course* cover lines; slide numbers; image links.
  *Content Covered* / agenda slides are omitted (the `## Page N` heading stays so
  numbering still matches the PDF).

## Regenerating

```
python build.py           # PDFs -> ./out/<lesson>/<lesson>.md  (+ per-slide images/)
python polish.py           # strip leftover citation parentheticals in ./out
python strip_images.py     # drop the per-slide images/ folders (skill uses text only)
# then copy ./out/*/*.md into ../.claude/skills/jon-fitness/references/isa-cpt/
```

`build.py` reads `isa-cpt-pdfs/` (path is set near the top of the file) and needs
`PyMuPDF` (`fitz`). The image folders it emits are intentionally discarded — nothing
references them. `image-audit.md` records the check that confirmed this.

---

## REVL programming — screenshot extraction

`extract_revl.py` OCRs the two REVL workout-screenshot libraries
(`../REVL Block 1 2026/` and `../REVL Block 2 programming 2026/`, git-ignored, local
only) into **`revl_raw_data.md`** — every session's text, grouped block → phase-week →
session. It uses `rapidocr-onnxruntime` and caches per-image results under
`.revl_ocr_cache/` (git-ignored).

```
python extract_revl.py                # full run (264 screenshots)
python extract_revl.py --limit 6      # quick smoke test (writes a partial file)
python extract_revl.py --blocks 1     # one block only
```

`revl_raw_data.md` is the raw evidence layer behind
`../.claude/skills/jon-fitness/references/revl-class-integration.md` (which teaches the
`jon-fitness` skill how to program 1-on-1 PT around REVL). **OCR of the stylised posters
is approximate** — that reference file must never present a specific REVL load, rep or
percentage as fact.
