# Poster designer

Claude designs posters in Zubair's personal brand style (Personal Brand Kit) and adds them to the queue.

- `template.html` — the brand layout: grey gradient, faint network lines, slate bar, Montserrat headline in capitals
  with ONE light-blue line, Inter body, round headshot footer, disclaimer.
- `render.py` — turns a post spec (JSON) into a 1080 × 1350 PNG. Run: `python3 designer/render.py designer/posts/<file>.json`
  It stops with an error if the text does not fit; shorten the text and run again.
- `posts/` — the specs Claude wrote (kept so a poster can be re-rendered after an edit).
- `samples/` — one sample per format.
- `fonts/`, `assets/` — Montserrat and Inter (Open Font License) and the headshot.

Formats: MythVsFact, Checklist, LessonLearned, BuildInPublic, HotTake.
LessonLearned and BuildInPublic need a real story or a real number from Zubair; Claude never invents them.
