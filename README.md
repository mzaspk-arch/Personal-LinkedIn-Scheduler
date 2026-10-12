# Personal LinkedIn Scheduler

Zubair Akbar's LinkedIn poster queue. Claude scheduled tasks post twice a day, Monday to Saturday,
at about 11:00 AM and 5:00 PM (Dubai time). No posts on Sunday.

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
