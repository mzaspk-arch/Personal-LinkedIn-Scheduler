# Breaking-news posts (auto-designed, auto-published)

When an important new tax or technology rule is published in the UAE, Pakistan or another GCC country, Claude designs
a poster and publishes it straight away. It does NOT wait for the queue, the series or the dated slots.
A scheduled task checks twice a day, Monday to Saturday, at about 1:40 PM and 8:40 PM Dubai time.

## 1. Where to look (official sources first)
| Country | Tax | Technology / digital rules |
|---|---|---|
| UAE | FTA (tax.gov.ae): decisions, public clarifications, guides · Ministry of Finance (mof.gov.ae) · uaelegislation.gov.ae | TDRA (tdra.gov.ae) · UAE Cybersecurity Council · Central Bank (centralbank.ae) for digital payments · MoF e-invoicing pages |
| Pakistan | FBR (fbr.gov.pk): SROs, circulars, press releases, Finance Act changes · Provincial revenue authorities (PRA, SRB, KPRA, BRA) | MoITT (moitt.gov.pk) · PTA (pta.gov.pk) · SECP (secp.gov.pk) · State Bank (sbp.org.pk) for digital payments · PSEB |
| Saudi Arabia | ZATCA (zatca.gov.sa) | SDAIA, CST |
| Oman | Tax Authority (taxoman.gov.om) | Ministry of Transport, Communications and IT |
| Bahrain | NBR (nbr.gov.bh) | iGA |
| Qatar | GTA (gta.gov.qa) | MCIT |
| Kuwait | Ministry of Finance (mof.gov.kw) | CITRA |

News sites (Gulf News, Khaleej Times, The National, Dawn, Business Recorder, firm alerts) may be used to FIND an item,
but every fact on the poster must be checked against the official document itself.

## 2. What qualifies
Post only when ALL are true:
- **New and official:** a law, decree, cabinet/ministerial decision, FTA/FBR decision, SRO, circular, public clarification,
  guide, deadline change, rate change, new obligation or new relief, published in the last 72 hours (Dubai time).
- **Useful to the audience:** SME owners, CFOs, accountants, founders, tech buyers in the UAE, Pakistan and the GCC.
  It changes what a business must do, pay, file, claim or build.
- **Not already covered:** not in `news/log.md`, `posted/log.md`, `captions/`, `designer/posts/` or the queued posters.
- **Readable:** Claude could open and read the official text (or official press release) and the key facts are clear.

Skip: speeches, conferences, awards, MoUs, "plans to" stories without an issued text, minor website/portal notices,
anything Claude cannot verify. When in doubt, do not publish; log it as skipped with the reason.

Technology items qualify only when they change obligations or opportunities for businesses, for example data protection,
AI or cybersecurity rules, e-invoicing technical rules, digital payment rules, IT export / freelancer incentives,
software-house registration or tax changes for tech companies.

## 3. Limits
- At most ONE news post per run, so at most two a day. If several items qualify, publish the most important one and log
  the others as "pending" so the next run can take the next one (only while it is still within 7 days of publication).
- Never post within the same run as a correction of an earlier post without saying so clearly in the caption.

## 4. Design
- Use `designer/render.py` and the brand template. Save the spec as `designer/posts/<YYYY-MM-DD>-NEWS-<Topic>.json` and
  render with `--out posters/news`. Caption: `captions/<same id>.txt`.
- Pillar: `TAX • UAE`, `TAX • PAKISTAN`, `TAX • GCC`, `DIGITAL TRANSFORMATION` or `SAAS`.
- Source line starts with "Just released · " then the document name and its date, e.g.
  `Just released · FTA Decision No. 21 of 2026 · 30 Oct 2026`.
- Format: Checklist (what changed, who, when, what to do) or MythVsFact. 2 headline lines + ONE highlight line.
- Vary the look: read the last three specs in `designer/posts/` (by date) and pick a `layout`
  (`classic`, `ghost`, `edge`, `block`, `right`) and a `theme` (`dark`, `light`) different from the most recent post.
  `ghost` and `edge` need a short `kicker` (a number, date or word such as `NEW`, `SRO`, `1 JAN`).
- Disclaimer on: "General information, not tax advice." on tax posts.

## 5. Caption
Follow `CAPTION-RULES.md` (value first, formatting, country hashtags). In addition:
- Line 2 says what was issued, by whom and when.
- Put the official source link on its own line before the question: `Source: <official URL>`.
- Every number, date and document number must match the official text exactly.

## 6. Logging
Append one row per item considered to `news/log.md`:
`| <date> | <country> | <document> | <official URL> | posted / skipped / pending | <LinkedIn link or reason> |`
After publishing, remove the PNG and caption (keep the spec) and add a `NEWS` row to `posted/log.md`.
