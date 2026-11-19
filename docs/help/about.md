---
title: About these docs
guide: taro
quote: "A guide should help you complete the task you came for. If you're still guessing what to press, it needs fixing."
---

# About these docs

This is the official Neconyan handbook, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). It covers getting started, everyday writing, helpers and extension development.

## Version and scope

I reviewed the changed guides against the **Neconyan 1.5.7 staging candidate** (commit **da76c549**) on **20 November 2026**. 1.5.7 isn't published yet; [1.5.6 is the latest published release](https://github.com/platberlitz/Neconyan/releases/tag/v1.5.6).

This edition adds:

- [Author's Note](../workspace/roleplay.md#authors-note), **Guided Swipe** and **Guided Impersonate** in Simple Mode
- [single and batch picture removal](../workspace/index.md#gallery) in Gallery
- [picture and portrait batches](../helpers/scratchpad.md#images-and-portraits) in Scratchpad
- PixAI's updated modes, LoRAs and separate **Negative Prompt** in [Quick Image Gen](../helpers/tools.md#appearance-and-media)
- `jani.com` as BotSearcher's backup address for JanitorAI

The affected guides mark what needs 1.5.7. The 1.5.6 edition covered the shorter Simple Mode setup, **Panels**, Gallery in the workspace, PixAI, saved Scratchpad pictures, new Agents controls, smaller Mewmory recall requests, BotSearcher's JanitorAI lists and the phone Notebooks layout. Notes for earlier versions still describe those releases.

The macro catalogue keeps its reviewed 7 October snapshot. The Scene Note starter and extension styling guide now carry the accent button guidance. The other extension examples are unchanged from their reviewed 7 October snapshots. The macro guides explain which replies are still built on the server and which macros those refuse. The newer Agent-only placeholders are documented separately and don't change the registered macro count.

The practical guides focus on common tasks and link to longer references when you need the details. Those references may change after this edition. Model features still depend on your provider and model supporting them.

## Screenshots and artwork

I captured Simple Mode's guided actions and Author's Note on a computer and a phone viewport on 20 November 2026 from [Neconyan at da76c549](https://github.com/platberlitz/Neconyan/tree/da76c549). I used the default Calico Dark colours, opaque panels and a demonstration chat with Miso. The other workspace screenshots are from 1.5.6 builds, so some details can look different. The Proofreader example uses a fixed sample response through the real edit-history workflow, not a live model conversation.

Miso, Taro and Nori use Neconyan's existing assistant artwork, with male, female and neutral variants. Their handbook dialogue is written guidance, not a live model conversation. Gender preferences stay in the browser when storage is available.

## Credits and licences

Neconyan is maintained by [Platberlitz](https://github.com/platberlitz) and grew from SillyTavern and SillyBunny. Its original documentation and bundled original assets are distributed here under **AGPL-3.0**, with the licence included in the documentation repository.

The site uses Material for MkDocs and MkDocs under their respective licences. **Nunito** and **Fredoka One** are served locally with their SIL Open Font Licence notices. Bundled application tools keep their original authorship and licences. See [the attribution table](https://github.com/platberlitz/Neconyan/blob/staging/docs/neconyan-native-tools.md).

## Improve a guide

Report an incorrect label or workflow with the page address, your app version and what you see instead. For screenshots, use demonstration data and keep credentials out of view. Useful additions explain a task someone can actually complete, including how to recognise a successful result.

The handbook is edited as Markdown. See the documentation repository's README for local preview and publishing instructions. Search runs in the browser over the built documentation. Reading these pages doesn't need a Neconyan login or a model connection.
