---
title: Text
guide: nori
quote: 'A missing title should not leave a lonely pair of brackets behind. We have a macro for that.'
---

# Text

These Macro Enhanced macros change or measure text. Positions start at **0**. Where supported, a negative position counts backwards from the end, and the end position is excluded.

**Browser prompts only.** These macros only run in the browser. Ordinary Roleplay replies build their prompts there, so they work. Conversation replies, Deep Swipe and replies with a selected Notebook context build their prompts on the server and stop before the model request if one is used. Test them in the Macro Enhanced Playground, and see [Macro Enhanced in Roleplay prompts](index.md#macro-enhanced-in-roleplay-prompts) for the full list.

Use `default` for a missing value and `wrap` for punctuation that should appear only when there is something inside it.

The token-count helpers use a rough character estimate. For an exact prompt limit, check the selected model’s token count. Text length also follows the app’s string handling, so a visible emoji can take more than one position.

<!-- macro-reference: text -->
