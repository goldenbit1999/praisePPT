"""Build one weekly praise deck from numbered bilingual lyric text files.

Input files are discovered in filename order:
    01_*.txt, 02_*.txt, 03_*.txt, ...

The first blank-line-separated block in each file is the song title:
    Korean title (key)
    English title

Every following block becomes one lyric slide.
"""

from pathlib import Path
import re

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor


BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_FILE = BASE_DIR / "template.pptx"
COMBINED_FILE = BASE_DIR / "weekly_lyrics_mixed.txt"
OUTPUT_FILE = BASE_DIR / "weekly_praise.pptx"


def add_empty_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    for shape in list(slide.shapes):
        element = shape.element
        element.getparent().remove(element)
    return slide


def add_title_slide(prs, lines):
    """Match slide 1 of '09_19_26 BEDTS 찬양.pptx'."""
    slide = add_empty_slide(prs)
    box = slide.shapes.add_textbox(
        0,
        642938,
        prs.slide_width,
        1904367,
    )
    frame = box.text_frame
    frame.word_wrap = True

    for index, line in enumerate(lines):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        paragraph.text = line
        paragraph.alignment = PP_ALIGN.CENTER
        for run in paragraph.runs:
            run.font.name = "Malgun Gothic"
            run.font.size = Pt(60)
            run.font.color.rgb = RGBColor(255, 255, 0)


def add_lyric_slide(prs, lines):
    """Use the original make_from_mixed.py lyric-slide style."""
    slide = add_empty_slide(prs)
    box = slide.shapes.add_textbox(
        Inches(0),
        Inches(0.5),
        prs.slide_width,
        prs.slide_height - Inches(1),
    )
    frame = box.text_frame
    frame.word_wrap = True
    frame.vertical_anchor = MSO_ANCHOR.TOP

    for index, line in enumerate(lines):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        paragraph.text = line
        paragraph.alignment = PP_ALIGN.CENTER

        is_korean = bool(re.search(r"[\uac00-\ud7a3]", line))
        for run in paragraph.runs:
            run.font.name = "Malgun Gothic" if is_korean else "Arial"
            run.font.size = Pt(45 if is_korean else 40)
            run.font.color.rgb = (
                RGBColor(255, 255, 255)
                if is_korean
                else RGBColor(255, 220, 60)
            )


def main():
    song_files = sorted(BASE_DIR.glob("[0-9][0-9]_*.txt"))
    if not song_files:
        raise FileNotFoundError("No numbered song files were found.")

    song_texts = [
        path.read_text(encoding="utf-8").strip()
        for path in song_files
    ]
    COMBINED_FILE.write_text("\n\n".join(song_texts) + "\n", encoding="utf-8")

    prs = Presentation(TEMPLATE_FILE)
    for song_text in song_texts:
        blocks = [
            block for block in song_text.split("\n\n")
            if block.strip()
        ]
        add_title_slide(prs, blocks[0].splitlines())
        for block in blocks[1:]:
            add_lyric_slide(
                prs,
                [line.strip() for line in block.splitlines() if line.strip()],
            )

    prs.save(OUTPUT_FILE)
    print(f"Created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
