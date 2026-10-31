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
Zubair's own posters in `posters/` always go first. There are 12 posting slots a week (Monday to Saturday,
11 AM = AM and 5 PM = PM). Every Sunday Claude counts his posters: when fewer than 12 are left, it designs
posters for the slots they don't cover. AM slots are UAE topics; PM slots are Pakistan tax or SaaS/ERP/digital topics.
Designed posters are saved in `posters/dated/` named `<YYYY-MM-DD>-<AM|PM>-<Topic>.png` and posted in that slot.

## Series (MORN slot, about 8:30 AM)
Themed series are planned in one go and saved as `posters/dated/<YYYY-MM-DD>-MORN-<Topic>.png`, with the spec in
`posts/` and the caption in `captions/` under the same name. The MORN slot only posts these files; it never uses
Zubair's queue. The weekly design run does not count MORN files and does not design for that slot.
