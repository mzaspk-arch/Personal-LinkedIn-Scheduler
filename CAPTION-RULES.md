# Caption rules (used by Claude when a poster has no caption file)

Write the caption from what the poster says. The caption and the image must say the same thing.

## Value first (every post must teach something)
The goal is that a reader learns something useful in 30 seconds and wants to follow Zubair for more.
- Lead with the reader's problem or the change that affects them, not with news for its own sake.
- Give practical, specific knowledge: what changed, who it affects, the deadline or amount, and what to do now.
- Explain one idea well rather than many ideas briefly. Translate legal wording into plain business language.
- End with 1–2 clear action steps and a question that invites people to share their experience.
- Helpful, not salesy: no hard selling; mention Zubair's services in at most 2 of every 10 posts.

## Voice: a trusted senior advisor
- Line 1 is the hook: under 12 words, a problem, a number or a bold claim. No emoji in the hook.
- One idea per line, a blank line between paragraphs (list items stay on consecutive lines). 120–220 words in total.
- Specific: real numbers, deadlines, decision or clarification numbers exactly as on the poster.
- Max 2 emoji, only as bullets (✅ or ▶). Usually two ✅ action lines near the end.
- End with a question, then a blank line, then "General information, not tax advice." (tax posts), then 3–5 hashtags on the last line.
- No client names or client figures. No invented stories: if a post needs a personal story that is not on the poster, do not invent one.
- Never use "synergy", "game-changer" or similar buzzwords.

## Formatting (bold headings and bullets)
Write caption files in this simple format; `tools/linkedin_format.py` turns `**...**` into bold text when the post is published.
- Line 1 (the hook) is bold: `**Hook text here.**`
- A short lead-in line before a list is bold and ends with a colon: `**Key points:**`
- List items start with `▶ ` and sit on consecutive lines (no blank line between items).
- If an item has a label, bold the label: `▶ **Transport:** home-to-work, client sites or job duties.`
- Bold only headings and labels, never whole paragraphs, hashtags or the disclaimer.
- Action lines start with `✅ ` (max 2), each followed by a blank line.

## Tax accuracy
- Every figure, date and decision number must match the poster.
- For tax posts, check the key facts against current FTA / Ministry of Finance guidance with a web search. If something on the poster looks wrong or out of date, do NOT publish: skip the post, keep it in the queue, and report the problem.
- If a deadline on the poster has already passed on the posting date, do not publish it; report it instead.

## Hashtags (pick 3–5, matching the country of the post)
First decide the post's country from the poster: UAE (FTA, Ministry of Finance, AED, EmaraTax, Corporate Tax/VAT in the UAE) or Pakistan (FBR, PKR, IRIS, IPO Pakistan, Pakistani law).

- **UAE posts: UAE hashtags only.** #UAECorporateTax #UAEVAT #SMEsUAE #UAEBusiness #FTA
- **Pakistan posts: Pakistan hashtags only.** #PakistanTax #FBR #SMEsPakistan #PakistanBusiness #OverseasPakistanis (the last one only when the post is about overseas Pakistanis)
- **General hashtags (can be added to either):** #CFO #Odoo #ERP #DigitalTransformation #Entrepreneurship #Automation #SaaS

- **Other GCC posts (Saudi Arabia, Oman, Bahrain, Qatar, Kuwait): GCC hashtags only.** #GCCTax #SaudiArabia #ZATCA #Oman #Bahrain #Qatar #Kuwait (pick the country concerned) plus general hashtags.
- **Technology posts:** general hashtags plus the country set of the country concerned.

Never put a UAE hashtag on a Pakistan post or a Pakistan hashtag on a UAE post. If a post covers both countries, use only general hashtags plus one from each country set.

## Example structure (from approved posts in this repository)
**6 employee benefits where you can now recover VAT.**

FTA Decision No. 17 of 2026 took effect on 1 October.

It covers goods and services you give employees free of charge.

▶ **Transport:** home-to-work, client sites or job duties, with no cash-allowance option.
▶ **Food and drinks:** only where staff are at remote sites with no food facilities nearby.
▶ ...

✅ Check your employment contracts first.

✅ Then line up your policies and receipts before your next VAT return.

Which of these benefits does your business provide today?

General information, not tax advice.

#UAEVAT #SMEsUAE #CFO
