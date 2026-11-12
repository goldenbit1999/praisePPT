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
- Preserve the user's current dated deck ('praisePPT/YYYYMMDD_간사모임_악보.pptx') unless the request authorizes regenerating it.
- The top of 'praisePPT/' holds only the generator, template, dependency file, and the current week's set. Past weeks live in 'praisePPT/archive/YYYYMMDD/', one folder per week.
- Keep verification artifacts (rendered slide images, OCR output, helper package installs) in a temporary directory outside the repository.
- If the deck is open in PowerPoint (a '~$' lock file sits next to it), ask the user to close it before regenerating. Never force-close PowerPoint.

## Workflow

1. Inspect all current PPT, PPTX, and PDF files under '간사모임/'.
2. Extract the Korean and English lyrics for only the requested songs.
   - Prefer text already embedded in the supplied files.
   - Inspect image-only score pages visually or with OCR when necessary.
   - Use a web source only to fill or verify missing text, and reconcile it with the supplied score.
3. Pair Korean and English by meaning and performance order.
4. Before writing the new song files, archive the previous week's set:
   - The previous set is what sits at the top of 'praisePPT/': its numbered TXT files, 'weekly_lyrics_mixed.txt', and its dated deck 'YYYYMMDD_간사모임_악보.pptx'.
   - Move the whole set into 'praisePPT/archive/YYYYMMDD/', named with that previous deck's date. Use 'git mv' for tracked files. Never delete past outputs.
   - If the existing deck already has this week's date, this is a rework of the same week: do not archive; replace the TXT files in place and keep the user's manual deck edits unless regenerating is authorized.
   - If the previous week's date cannot be determined, ask the user.
5. Create numbered UTF-8 files in 'praisePPT/', such as '01_song-name.txt'.
   - The first block is the title slide: Korean title, then English title.
   - Never include the song key, such as '(G)', in either title line, even when the song list or score gives one.
   - Each following block is one lyric slide.
   - Separate blocks with one blank line.
   - Prefer two Korean lines followed by their two English lines per lyric slide.
   - Shorten the grouping before reducing font size.
6. From 'praisePPT/', run:

   '../venv/Scripts/python.exe generate_weekly_praise.py YYYYMMDD'

   - Take YYYYMMDD from the date in this week's '간사모임/' source filename, normalized from any format (for example, 'DTS Staff Setlist 2026.11.14.pdf' gives '20261114'; '20261010_간사모임_악보.pptx' gives '20261010').
   - The deck is saved as 'praisePPT/YYYYMMDD_간사모임_악보.pptx'.
   - If the source filename has no date, or this week's files disagree, ask the user.

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

- 'praisePPT/YYYYMMDD_간사모임_악보.pptx', dated from this week's '간사모임/' source filename
- Numbered per-song bilingual TXT files used to reproduce it
- 'praisePPT/weekly_lyrics_mixed.txt', generated as a convenient combined intermediate

Report any lyrics that could not be verified rather than silently inventing them.
