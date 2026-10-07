---
title: Saved choices and counters
guide: nori
quote: 'Choose the weather once and let it rain for a scene. I can find other ways to cause trouble.'
---

# Saved choices and counters

These Macro Enhanced macros keep choices stable or read counters recorded in the current chat.

## Pick the right lifetime

| Need | Use |
| --- | --- |
| Keep a result until you clear it | `freeze` |
| Keep a dice roll until you clear it | `rollonce` |
| Refresh after several user messages | `sticky` |
| Refresh when the calendar day changes | `daily` |
| Choose consistently from a list without saving a value | `listpick` |

A **key** is the name of a saved choice, such as `opening-weather`. Use a different key for an independent choice. Reusing a key can retrieve the earlier value even after you change the macro’s content.

## Stable prompts and costs

Some providers reuse an unchanged beginning of a prompt and charge less for it. Keeping values stable can help, but eligibility and discounts depend on the provider. Changing a value near the start can reduce the amount it can reuse. These macros do not guarantee cheaper requests.

## What the counters count

Message, swipe and generation counters track events observed by Macro Enhanced. They are not a reconstruction of every event in an imported chat. Reading a counter does not increase it.

<!-- macro-reference: saved-values -->
