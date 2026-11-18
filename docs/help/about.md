---
title: About these docs
guide: taro
quote: "A guide should help you complete the task you came for. If you're still guessing what to press, it needs fixing."
---

# About these docs

This is the official Neconyan handbook, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). It covers getting started, everyday writing, helpers and extension development.

## Version and scope

I've reviewed these guides against the **Neconyan 1.5.6 staging candidate at 00be4b8e** on **18 November 2026**. This candidate is **not yet published**. [1.5.5 is the latest published release](https://github.com/platberlitz/Neconyan/releases/tag/v1.5.5), reviewed at **680a05f1** on 15 November 2026.

This edition adds:

- Simple Mode's first run: Miso, Taro and Nori in your character list, the **Memory** and **Updates** buttons and **Dialogue Colors**
- **Settings → Appearance → Panels**, which replaces Background Visibility, and **Scroll long labels** for the top bar
- **Gallery** in the workspace, with saved Scratchpad pictures
- Scratchpad's **Feedback tone**, **Current preset** in General and saved pictures for vision models
- **Clothing Tracker**, **Skip user messages**, the bulk Companion picker and **Rerun agents** on interrupted replies
- Mewmory's smaller recall requests and the Nano-GPT decision models, also in Pawthfinder
- BotSearcher's JanitorAI lists and **Sources and logins**
- the phone Notebooks layout
- failed swipes, the **Session expired** notice and reasoning effort fixes

Some controls described here won't appear in 1.5.5. The affected guides say which. The 1.5.5 edition covered Mewmory's Story tab, Scratchpad's quick prompts and branching, the Translator Agent, the reworked Presets page, the Conversation messenger layout, failed and empty replies and the Device sync fixes; those notes still describe 1.5.5.

The macro catalogue keeps its reviewed 7 October snapshot. The Scene Note starter and extension styling guide now carry the accent button guidance. The other extension examples are unchanged from their reviewed 7 October snapshots. The macro guides explain which replies are still built on the server and which macros those refuse. The newer Agent-only placeholders are documented separately and don't change the registered macro count.

The practical guides focus on common tasks and link to longer references when you need the details. Those references may change after this edition. Model features still depend on your provider and model supporting them.

## Screenshots and artwork

I refreshed the workspace screenshots on 18 November 2026 from [Neconyan at 6b6a8696](https://github.com/platberlitz/Neconyan/tree/6b6a8696), a 1.5.6 staging build. They use the default Calico Dark colours, Background Visibility at 0%, demonstration content and the bundled assistants. The two Notebooks screenshots were retaken later that day for the new phone layout and copied from the app README. The 1.5.6 candidate replaces Background Visibility with **Panels**, so panel transparency can look slightly different. Some details, including the Catline Extensions icon, look different in the published 1.5.5 release. The Proofreader example uses a fixed sample response through the real edit-history workflow, with edit, Undo and Redo checked at both widths. It isn't a live model conversation.

Miso, Taro and Nori use Neconyan's existing assistant artwork, with male, female and neutral variants. Their handbook dialogue is written guidance, not a live model conversation. Gender preferences stay in the browser when storage is available.

## Credits and licences

Neconyan is maintained by [Platberlitz](https://github.com/platberlitz) and grew from SillyTavern and SillyBunny. Its original documentation and bundled original assets are distributed here under **AGPL-3.0**, with the licence included in the documentation repository.

The site uses Material for MkDocs and MkDocs under their respective licences. **Nunito** and **Fredoka One** are served locally with their SIL Open Font Licence notices. Bundled application tools keep their original authorship and licences. See [the attribution table](https://github.com/platberlitz/Neconyan/blob/staging/docs/neconyan-native-tools.md).

## Improve a guide

Report an incorrect label or workflow with the page address, your app version and what you see instead. For screenshots, use demonstration data and keep credentials out of view. Useful additions explain a task someone can actually complete, including how to recognise a successful result.

The handbook is edited as Markdown. See the documentation repository's README for local preview and publishing instructions. Search runs in the browser over the built documentation. Reading these pages doesn't need a Neconyan login or a model connection.
