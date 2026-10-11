---
title: Lists and JSON
guide: taro
quote: 'For a short inventory, a comma-separated list is enough. Use a structured object when the items need their own details.'
---

# Lists and JSON

These Macro Enhanced macros work with lists such as:

```text
sword,shield,potion
```

Most list macros use a comma between items unless you supply another separator. The first item is **0**; **-1** selects the last item where negative positions are supported. The end position of a slice is excluded.

**Not for Roleplay prompts.** These macros only run in the browser. If a Roleplay prompt uses one, the reply stops before the model request. Test them in the Macro Enhanced Playground, and read [Macro Enhanced in Roleplay prompts](index.md#macro-enhanced-in-roleplay-prompts) before putting them in a card, preset or lorebook entry.

**JSON** is a text format for structured data. For example, a saved inventory could contain:

```json
{"items":[{"name":"sword","count":1},{"name":"potion","count":3}]}
```

A path such as `items[0].name` means the name of the first item. Save complicated JSON in a variable, then read it through `getvar` inside the JSON macro. This avoids confusing an object’s closing braces with macro punctuation.

<!-- macro-reference: lists -->
