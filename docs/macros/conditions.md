---
title: Conditions
guide: taro
quote: 'Ask a comparison to compare. A sentence that looks like maths can still be treated as text.'
---

# Conditions

These Macro Enhanced macros return `true` or `false`, or choose text from a set of cases. Combine them with the core [if block](basics.md#if):

```text
{{if::{{gte::{{getvar::supplies}}::3}}}}
There are enough supplies for the trip.
{{else}}
The party needs more supplies.
{{/if}}
```

Set `supplies` before using this example. When both values are numbers, the comparison macros compare them as numbers. Otherwise they compare them as text. Keep to one type of value for predictable results.

**Browser prompts only.** The comparison and `switch` macros on this page, and the `expr` macro, only run in the browser. Ordinary Roleplay replies build their prompts there, so they work. Conversation replies, Deep Swipe and replies with a selected Notebook context build their prompts on the server. If one of those prompts uses one of these macros, the reply stops before the model request. Test the macros in the Macro Enhanced Playground. [Macro Enhanced in Roleplay prompts](index.md#macro-enhanced-in-roleplay-prompts) has the full list. The core `if` block works everywhere.

The plain `if` macro treats empty text, `false`, `off` and `0` as false. A sentence such as `0 > 0` is non-empty text, so wrap written comparisons in `expr` or use `gt`, `eq` and the other comparisons below. Macro Enhanced also has an optional setting that works out comparisons directly in if conditions.

<!-- macro-reference: conditions -->
