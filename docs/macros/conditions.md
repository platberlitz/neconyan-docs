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

The plain `if` macro treats empty text, `false`, `off` and `0` as false. A sentence such as `0 > 0` is non-empty text, so wrap written comparisons in `expr` or use `gt`, `eq` and the other comparisons below. Macro Enhanced also offers an optional setting to work out comparisons directly in if conditions.

<!-- macro-reference: conditions -->
