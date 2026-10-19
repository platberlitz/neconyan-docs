---
title: Dates and times
guide: miso
quote: 'For a story date, save the date you chose. The real-world clock keeps moving even when your characters take a break.'
---

# Dates and times

Core time macros read the real-world clock. Macro Enhanced adds `dateadd`, `datediff` and `dateformat` for working with a date you supply.

**Browser prompts only.** `dateadd`, `datediff` and `dateformat` only run in the browser. Ordinary Roleplay replies build their prompts there, so they work. Conversation replies, Deep Swipe and replies with a selected Notebook context build their prompts on the server and stop before the model request if one is used. Test them in the Macro Enhanced Playground, and see [Macro Enhanced in Roleplay prompts](index.md#macro-enhanced-in-roleplay-prompts) for the full list. The core time macros work everywhere.

Use an unambiguous date such as `2026-10-07`. Local time and language depend on the environment processing the prompt. A server and a browser can have different time zones.

## Common format parts

| Part | Meaning | Example |
| --- | --- | --- |
| `YYYY` | Four-digit year | 2026 |
| `MM` | Month number | 10 |
| `MMMM` | Month name | October |
| `DD` | Day of the month | 07 |
| `dddd` | Weekday name | Wednesday |
| `HH` | Hour, 24-hour clock | 18 |
| `mm` | Minutes | 05 |
| `ss` | Seconds | 09 |
| `[at]` | Literal text | at |

Capitalisation matters: `MM` is the month, while `mm` is minutes. Names follow the active language. Date arithmetic accepts units such as days, weeks and months; the short unit `M` means months and `m` means minutes.

<!-- macro-reference: dates -->
