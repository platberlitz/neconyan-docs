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

Set `supplies` before using this example. The comparison macros treat two numeric values as numbers and other values as text. Use consistent value types for predictable results.

**Not for Roleplay prompts.** The comparison and `switch` macros on this page, and the `expr` macro, only run in the browser. If a Roleplay prompt uses one, the reply stops before the model request. Test them in the Macro Enhanced Playground, and read [Macro Enhanced in Roleplay prompts](index.md#macro-enhanced-in-roleplay-prompts) before putting them in a card, preset or lorebook entry. The core `if` block itself still works in Roleplay.

The plain `if` macro treats empty text, `false`, `off` and `0` as false. A sentence such as `0 > 0` is non-empty text, so wrap written comparisons in `expr` or use `gt`, `eq` and the other comparisons below. Macro Enhanced also offers an optional setting to work out comparisons directly in if conditions.

<!-- macro-reference: conditions -->
