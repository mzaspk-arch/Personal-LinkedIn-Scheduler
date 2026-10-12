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

## Background variations
Every poster keeps the same brand base (grey gradient, slate bar, one light-blue line, same footer).
Three variations rotate automatically so the feed doesn't look repetitive (or set "variant" in the spec):
- `top` — glow at the top centre, network lines top right
- `left` — glow top left, network lines bottom right
- `panel` — the list or number sits on a steel-blue panel

## Weekly designed posts
Zubair's own posters in `posters/` always go first. Every Sunday Claude counts them: when fewer than 6 are left,
it designs posters for the remaining days of the coming week (Monday to Saturday). Designed posters are saved in
`posters/dated/` with the posting date at the start of the name (e.g. `2026-12-10-UAE-Input-VAT-Checks.png`)
and are posted on that date.
