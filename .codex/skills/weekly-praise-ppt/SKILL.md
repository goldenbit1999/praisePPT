---
name: weekly-praise-ppt
description: Build the weekly combined Korean-English worship lyric PowerPoint for this project from the changing files in the 간사모임 input folder and the user's ordered song list.
---

# Weekly Praise PowerPoint

Use this skill when the user asks to prepare the weekly praise deck in this repository.

## Project contract

- Treat '간사모임/' as a changing weekly input drop folder. Inspect its current contents every time; never assume prior filenames, songs, page counts, or formats still apply.
- Treat the user's song list as authoritative for song order, displayed titles, English titles, and keys.
- Do not modify source files in '간사모임/'.
- Use 'praisePPT/template.pptx' and 'praisePPT/generate_weekly_praise.py'.
- Preserve the user's current 'praisePPT/weekly_praise.pptx' unless the request authorizes regenerating it.

## Workflow

1. Inspect all current PPT, PPTX, and PDF files under '간사모임/'.
2. Extract the Korean and English lyrics for only the requested songs.
   - Prefer text already embedded in the supplied files.
   - Inspect image-only score pages visually or with OCR when necessary.
   - Use a web source only to fill or verify missing text, and reconcile it with the supplied score.
3. Pair Korean and English by meaning and performance order.
4. Create numbered UTF-8 files in 'praisePPT/', such as '01_song-name.txt'.
   - The first block is the title slide: Korean title, then English title.
   - Each following block is one lyric slide.
   - Separate blocks with one blank line.
   - Prefer two Korean lines followed by their two English lines per lyric slide.
   - Shorten the grouping before reducing font size.
5. Remove or replace numbered song TXT files from the prior week only when generating a newly authorized weekly deck.
6. From 'praisePPT/', run:

   '../venv/Scripts/python.exe generate_weekly_praise.py'

7. Verify:
   - Song order matches the user's list.
   - Every requested song has one title slide.
   - No verse, chorus, bridge, or intended repeat was silently dropped.
   - Korean and English lines are correctly paired.
   - The deck opens and all slides render.

## Style contract

- Title slides follow slide 1 of the supplied worship deck: centered yellow Malgun Gothic at 60 pt.
- Lyric slides follow the original project style: Korean Malgun Gothic 45 pt in white; English Arial 40 pt in yellow; centered and top-aligned.
- Keep the template background and 16:9 slide size.
- Minor final adjustments made manually in PowerPoint are acceptable and do not need to become general rules unless the user asks.

## Deliverables

- 'praisePPT/weekly_praise.pptx'
- Numbered per-song bilingual TXT files used to reproduce it
- 'praisePPT/weekly_lyrics_mixed.txt', generated as a convenient combined intermediate

Report any lyrics that could not be verified rather than silently inventing them.
