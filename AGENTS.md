# Praise PPT Project

## Purpose

This repository creates one combined 16:9 PowerPoint deck for a weekly worship set. Each song receives:

1. A Korean/English title slide.
2. Korean and English lyric slides paired by meaning and performance order.

The user normally provides the ordered song list after a meeting. The supporting scores, lyric decks, and PDFs are then placed in the '간사모임/' folder.

## Use the project skill

For weekly deck creation or related maintenance, read and follow:

'.codex/skills/weekly-praise-ppt/SKILL.md'

That skill is the authoritative workflow for this repository.

## Repository layout

- '간사모임/': changing weekly source material. Its contents and filenames are not stable. Inspect it fresh every time and never modify its source files.
- 'praisePPT/template.pptx': the visual template used for generated slides.
- 'praisePPT/generate_weekly_praise.py': the canonical PPT generator.
- 'praisePPT/NN_song-name.txt': ordered bilingual song inputs for the current deck.
- 'praisePPT/weekly_lyrics_mixed.txt': generated combined text intermediate.
- 'praisePPT/weekly_praise.pptx': current completed deck. This may contain small manual finishing edits by the user.
- 'praisePPT/requirements.txt': Python dependencies.
- 'venv/': local Python environment used to run the generator.

## Standard workflow

1. Read the user's ordered song list, including Korean title, English title, and key.
2. Inspect all current PPT, PPTX, and PDF materials under '간사모임/'.
3. Extract and verify the requested Korean and English lyrics.
4. Pair the lyrics and divide them into readable slide-sized blocks.
5. Create or replace numbered song files in 'praisePPT/'.
6. Run from the 'praisePPT/' directory:

   '../venv/Scripts/python.exe generate_weekly_praise.py'

7. Verify song order, title slides, verse/chorus/bridge completeness, Korean-English pairing, and that the generated deck opens.
8. Preserve minor manual edits in 'weekly_praise.pptx' unless the user explicitly asks to regenerate or overwrite it.

## Song text format

The first blank-line-separated block is the title slide:

    한글 곡 제목
    English Song Title

Each later block is one lyric slide. Prefer:

    한글 가사 첫 줄
    한글 가사 둘째 줄
    English lyric line one
    English lyric line two

Separate slides with one blank line. Number filenames to establish song order, such as '01_first-song.txt' and '02_second-song.txt'.

## Style

- Title: centered yellow Malgun Gothic, 60 pt.
- Korean lyrics: centered white Malgun Gothic, 45 pt.
- English lyrics: centered yellow Arial, 40 pt.
- Lyric text is top-aligned.
- Preserve the template background and 16:9 dimensions.

Small PowerPoint adjustments made by the user are acceptable finishing work. Do not overfit the generator to incidental manual changes unless requested.

## Preservation and cleanup

- Never treat the current contents of '간사모임/' as permanent examples or hard-code their filenames.
- Do not delete or edit '간사모임/' source materials.
- Do not overwrite 'weekly_praise.pptx' during analysis or testing.
- Use a temporary output path for comparisons.
- Keep the generator, template, current numbered TXT inputs, dependency file, and final deck.
- Remove only clearly obsolete experiments, caches, lock files, and temporary comparison artifacts.
