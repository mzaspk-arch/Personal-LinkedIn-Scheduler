# Personal LinkedIn Scheduler

Zubair Akbar's LinkedIn poster queue. Claude scheduled tasks post Monday to Saturday (Dubai time).
No posts on Sunday.

| Slot | Time | What is posted |
|---|---|---|
| MORN | about 8:30 AM | Only designed series posts in `posters/dated/` named `<date>-MORN-...`. If there is none for the day, nothing is posted. |
| AM | about 11:00 AM | A dated `<date>-AM-...` post if there is one, otherwise your next queued poster. |
| PM | about 5:00 PM | A dated `<date>-PM-...` post if there is one, otherwise your next queued poster. |
| NEWS | about 1:40 PM and 8:40 PM checks | Breaking official tax/technology updates (UAE, Pakistan, GCC), designed and published immediately when something new qualifies. Rules: `NEWS-RULES.md`. |

The MORN slot never takes posters from your own queue, so adding a series does not push your posters back.

### Current series in the MORN slot
**UAE Tax 2026–27** (themes from PwC's Annual Tax Conference 2026): 30 posts, 2 November to 8 December 2026
(no posts on 2–3 December, UAE National Day). Specs are in `designer/posts/*-MORN-*.json`, captions in `captions/`.
To skip one, delete its PNG from `posters/dated/` and its caption from `captions/`. To edit one, change its
caption file, or change the spec and re-render with `python3 designer/render.py <spec> --out posters/dated`.

## How to add posters
1. Put the PNG in the `posters` folder (1080 × 1350).
2. Name it with a number so it sorts after the others, e.g. `19-VAT-Refunds.png`.
   Posters go out in name order: the lowest number first.
3. A post with several pages (a carousel): give all pages the SAME number and end
   each name with the page, e.g. `26. APA-Post-Pg-1.png` and `26. APA-Post-Pg-2.png`.
   They are posted together as one post with several images.
4. Caption (optional): add `captions/<same name>.txt`. If there is no caption,
   Claude writes one from the poster the evening before, following `CAPTION-RULES.md`,
   and sends you a preview.

## What happens after posting
The poster and its caption are removed from `posters/` and `captions/`, and a line is
added to `posted/log.md` with the date and the LinkedIn link. Old files stay in the
GitHub history if you ever need them.
