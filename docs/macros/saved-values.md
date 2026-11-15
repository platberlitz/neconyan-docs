---
title: Saved choices and counters
guide: nori
quote: 'Choose the weather once and let it rain for a scene. I can find other ways to cause trouble.'
---

# Saved choices and counters

These Macro Enhanced macros keep choices stable or read counters recorded in the current chat.

**Browser prompts only.** These macros, including `freeze`, `listpick` and `rollonce`, only run in the browser. Ordinary Roleplay replies build their prompts there, so they work. Conversation replies, Deep Swipe and replies with a selected Notebook context build their prompts on the server. If one of those prompts uses one of these macros, the reply stops before the model request. Test the macros in the Macro Enhanced Playground. [Macro Enhanced in Roleplay prompts](index.md#macro-enhanced-in-roleplay-prompts) has the full list.

## Pick the right lifetime

| Need | Use |
| --- | --- |
| Keep a result until you clear it | `freeze` |
| Keep a dice roll until you clear it | `rollonce` |
| Refresh after several user messages | `sticky` |
| Refresh when the calendar day changes | `daily` |
| Choose consistently from a list without saving a value | `listpick` |

A **key** is the name of a saved choice, such as `opening-weather`. Use a different key for an independent choice. Reusing a key can bring back the earlier value even after you change the macro’s content.

## Stable prompts and costs

Some providers reuse an unchanged beginning of a prompt and charge less for it. Keeping values stable can help, but eligibility and discounts depend on the provider. Changing a value near the start can reduce how much the provider can reuse. These macros don't guarantee cheaper requests.

## What the counters count

Message, swipe and generation counters track events observed by Macro Enhanced. They don't reconstruct every event in an imported chat. Reading a counter doesn't increase it.

<!-- macro-reference: saved-values -->
