---
title: Lorebook macros
guide: nori
quote: 'Ask for the entry you need. Your character probably does not need the city’s entire drainage history at breakfast.'
---

# Lorebook macros

These Macro Enhanced macros read lorebooks. An entry can be found by its title, stored as its memo or comment, or by its numeric identifier. Supplying the book name helps when several books contain the same title.

Without a book name, the usual search order is the chat’s book, the character’s books, then global books. Loading happens in the background, so a first lookup can be empty while the book is being loaded.

**Not for Roleplay prompts.** These macros only run in the browser. If a Roleplay prompt uses one, the reply stops before the model request. Test them in the Macro Enhanced Playground, and read [Macro Enhanced in Roleplay prompts](index.md#macro-enhanced-in-roleplay-prompts) before putting them in a card, preset or lorebook entry. Ordinary lorebook activation still works in Roleplay.

## Reading lore is different from activating it

`lore` inserts entry content directly. Ordinary [lorebook activation](../workspace/lorebooks.md) selects entries using keywords, conditions and the available budget. A direct macro lookup can duplicate an entry already included elsewhere.

`loreactive` and the active counts describe the **last generation**. They do not predict what will activate on the next reply. An entry’s existence alone does not mean it was included.

<!-- macro-reference: lorebooks -->
