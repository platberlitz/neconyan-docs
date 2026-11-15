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

Most list macros use a comma between items unless you supply another separator. The first item is **0**. Where negative positions are supported, **-1** selects the last item. A slice stops before its end position, which isn't included.

**Browser prompts only.** These macros only run in the browser. Ordinary Roleplay replies build their prompts there, so they work. Conversation replies, Deep Swipe and replies with a selected Notebook context build their prompts on the server. If one of those prompts uses one of these macros, the reply stops before the model request. Test the macros in the Macro Enhanced Playground. [Macro Enhanced in Roleplay prompts](index.md#macro-enhanced-in-roleplay-prompts) has the full list.

**JSON** is a text format for structured data. For example, a saved inventory could contain:

```json
{"items":[{"name":"sword","count":1},{"name":"potion","count":3}]}
```

A path such as `items[0].name` means the name of the first item. Save complicated JSON in a variable, then read it through `getvar` inside the JSON macro. That way an object’s closing braces can't be mistaken for macro punctuation.

<!-- macro-reference: lists -->
