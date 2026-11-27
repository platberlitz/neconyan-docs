---
title: About these docs
guide: taro
quote: "A guide should help you complete the task you came for. If you're still guessing what to press, it needs fixing."
---

# About these docs

This is the official Neconyan handbook, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). It covers getting started, everyday writing, helpers and extension development.

## Version and scope

I reviewed the changed guides for [Neconyan 1.6.0](https://github.com/platberlitz/Neconyan/releases/tag/v1.6.0) on **27 November 2026**, released at [`f03401f3`](https://github.com/platberlitz/Neconyan/tree/f03401f32a0d71e26a6e45836b7672e73df45bf3).

This edition adds:

- [who heard what](../workspace/roleplay.md#who-heard-what) in Roleplay group chats, with scene commands and macros, and a longer [Scene Director](../workspace/roleplay.md#run-a-group-scene) wait
- Mewmory [following the scene](../helpers/mewmory.md#group-chats) in group chats
- [Edit members](../workspace/conversation.md#open-or-create-a-conversation) and [lore in a conversation](../workspace/conversation.md#conversation-lore)
- Scratchpad's [checks for cards, presets, lorebooks and the app](../helpers/scratchpad.md#check-a-card-preset-or-lorebook), [Try first and Undo](../helpers/scratchpad.md#try-or-undo), **Talk mode**, **Queue follow-up**, **Compare with a second connection** and the new **Context** tabs
- the docked Companions panel, the Memory Shard editor and Plot Compass directions in [Agents](../helpers/agents.md)
- **Auto roll** and **Auto send** for the [Dice Roller](../helpers/tools.md#dice-roller), whose guide now describes it as the Companion it has been since 1.5.0
- [folder tabs and Sort with AI](../workspace/characters.md#folder-tabs) for characters
- [lorebook Health and missing links](../workspace/lorebooks.md#lorebook-health), and [macro warnings](../macros/index.md#macro-warnings) under text fields
- **Hide unsupported reasoning levels** for [Custom connections](../workspace/model-settings.md#reasoning-effort)
- the [Server Memory (Node.js)](troubleshooting.md#server-memory) card, **What's new** on [Home](../workspace/index.md#tours-and-everyday-navigation), Turkish in the [Language list](../workspace/index.md#settings) and the Author's Note [full screen editor](../workspace/roleplay.md#authors-note)

The affected guides mark what needs 1.6.0. The 1.5.7 edition covered Author's Note and the guided actions in Simple Mode, Gallery deletion, Scratchpad picture batches, PixAI modes and BotSearcher's JanitorAI backup address. Notes for earlier versions still describe those releases.

The macro catalogue keeps its reviewed 7 October snapshot. The group scene macros new in 1.6.0, such as `{{groupPresent}}`, are described in the [Roleplay guide](../workspace/roleplay.md#who-heard-what) instead. The Scene Note starter and extension styling guide now carry the accent button guidance. The other extension examples are unchanged from their reviewed 7 October snapshots. The macro guides explain which replies are still built on the server and which macros those refuse. The newer Agent-only placeholders are documented separately and don't change the registered macro count.

The practical guides focus on common tasks and link to longer references when you need the details. Those references may change after this edition. Model features still depend on your provider and model supporting them.

## Screenshots and artwork

I retook every workspace screenshot on a computer and a phone viewport on 27 November 2026 from the 1.6.0 release branch, whose app code matched [Neconyan at 73555b9c](https://github.com/platberlitz/Neconyan/tree/73555b9c888a11d32519b179e56c860b89ec6cff) apart from a later Conversation save fix that doesn't change how these screens look. I used the default Calico Dark colours, opaque panels and demonstration chats, notes and posts with the bundled assistants. The Proofreader example runs the real edit-history workflow with a fixed sample response from a local test service, not a live model conversation.

Miso, Taro and Nori use Neconyan's existing assistant artwork, with male, female and neutral variants. Their handbook dialogue is written guidance, not a live model conversation. Gender preferences stay in the browser when storage is available.

## Credits and licences

Neconyan is maintained by [Platberlitz](https://github.com/platberlitz) and grew from SillyTavern and SillyBunny. Its original documentation and bundled original assets are distributed here under **AGPL-3.0**, with the licence included in the documentation repository.

The site uses Material for MkDocs and MkDocs under their respective licences. **Nunito** and **Fredoka One** are served locally with their SIL Open Font Licence notices. Bundled application tools keep their original authorship and licences. See [the attribution table](https://github.com/platberlitz/Neconyan/blob/staging/docs/neconyan-native-tools.md).

## Improve a guide

Report an incorrect label or workflow with the page address, your app version and what you see instead. For screenshots, use demonstration data and keep credentials out of view. Useful additions explain a task someone can actually complete, including how to recognise a successful result.

The handbook is edited as Markdown. See the documentation repository's README for local preview and publishing instructions. Search runs in the browser over the built documentation. Reading these pages doesn't need a Neconyan login or a model connection.
