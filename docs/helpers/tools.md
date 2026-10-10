---
title: Included tools
guide: nori
quote: "Check Included tools before installing a second copy. Duplicate extensions can leave one inactive, which is a tedious way to discover it was already here."
---

# Included tools

Find documented macros in the [macro reference](../macros/index.md).

Neconyan ships with a collection of writing, appearance and diagnostic tools. Open **Included tools** to reach them, or **Extensions → Manage extensions** to inspect versions, authors, licences and enabled states.

Included code updates with Neconyan. Third-party extensions you install separately have their own update path. A bundled tool can still use a paid model or an external service.

## Writing and prompt work

| Tool | Use it for |
| --- | --- |
| **Guided Generations** | Give a response, swipe, regeneration, correction or impersonation specific guidance |
| **Input History** | Search earlier composer input and pick one to replace your draft |
| **Deep Swipe** | Work with message alternatives, including supported user-message alternatives |
| **Preset Tools** | Search and organise prompt sections |
| **Chat Completion Tabs** | Separate parameter and prompt controls |
| **Prompt Tags** | Manage tags and defaults for supported prompt sections |
| **Macro Enhanced** | Look up and manage supported placeholders and pronoun controls |
| **Prompting Lab** | Build prompt tests, compare requests and run selected model comparisons |

Prompt reconstruction and dry diagnostics don't generate replies. Prompting Lab's model comparisons and optional analysis make real requests. Read the action before running a batch.

## Lore and saved work

**World Info Lab** traces lore activation and supports reviewed batch changes. It and Prompting Lab can open saved chats up to 64 MiB. **Lorebook Distiller** proposes lore entries from a saved chat. **Chat Archive** searches and organises chats; its organisation export doesn't contain the chat contents themselves.

**Card & Lorebook Time Machine** keeps supported snapshots of characters, lorebooks and presets. It isn't a whole-account or chat backup. Compare before restoring, because a restore replaces newer edits.

If the item changes again after comparison, the restore stops rather than overwriting the intervening edit. Compare the current item again before retrying. A snapshot that fails its integrity check can't be used as a trusted restore source.

Several tools keep accepted work and results on the server. Closing the page stops watching it; use the explicit Stop action when you want to request cancellation.

## Appearance and media

**Dialogue Colors** assigns speaker colours. **Regex Agent Themes** restyles trackers and Companion panels. **CSS Snippets** manages your small visual customisations. **Termeownal UI** offers an optional terminal-style interface with its own command glossary.

**Quick Image Gen** needs its own provider configuration. It can use a manual prompt, a chat scene or supported image tags. Prompt preparation may also call a text model. **Character Expressions** uses separate sprite artwork and classification settings; a character avatar alone isn't a complete expression set.

Speech, captioning, translation, attachments and galleries each have their own settings. A working text connection doesn't automatically configure all of them.

### Separate expression sets for a shared card

Open a chat, then **Fine-tuning → Character Expressions → Sprites for this character**. Under **Character in this card**, use **Add character** to give each person in a multi-character card a separate expression set. **Whole card** selects the shared set. This is separate from group-chat membership and the card's avatar.

Under **Character appearance**, enter **Appearance notes for image generation**, then **Save appearance**. **Follow the first named speaker in each reply** picks a set from explicit speaker names or `Name:` dialogue labels, not an ordinary mention. If no name matches, it uses your chosen set. Selecting a set manually turns following off. **Remove character set** removes the choice from the card but leaves its image folder.

Use **Add expressions** for several labels separated by commas or new lines. **Find an expression**, **With images** and **Missing images** help find the ones you need. A label doesn't create artwork: open **Import, generate and manage images** to upload a sprite pack or character sheet, or **Generate missing sprites** with Quick Image Gen.

Under **How expressions are picked → Image generation and cleanup**, **Sprite generation mode** offers separate images or an automatically split character sheet. **Sprite framing** chooses a bust or full-body view. Use **Remove background (white/solid-color sheets only)** only for a plain background; leave it off when the artwork fills the image. **Redo crop/cleanup** processes the existing set. Generating images can incur provider charges.

## Find characters or diagnose a problem

**BotSearcher** searches supported card sources. Available filters, accounts and downloads depend on the source site. External-site errors can occur independently of your model connection. A failed JannyAI link import names its reason, such as a missing login on the server or a hidden card definition. Logging in to JannyAI in your own browser doesn't count; use **Refresh status** or **Open JannyAI login window** in BotSearcher.

**JannyAI card blocks proxies** means the creator has hidden the definition and disabled proxy access. Logging in again won't remove that setting. If JannyAI offers a card download, download it there and import the file; not every hidden card offers one.

**Debugger** provides a diagnostic report and layout snapshot. Reproduce the problem first, then open its report, read it and copy or download it. **Prompt Inspector** helps inspect supported outgoing requests; those prompts may contain private chat material.

!!! taro "Taro"
    'Included' means the code is here. You'll still need to configure any external service it uses and check that service's charges.

Original authors, source links and licence details are recorded in the [included-tools attribution table](https://github.com/platberlitz/Neconyan/blob/staging/docs/neconyan-native-tools.md) and beside the bundled source. Want to make your own tool? Start with [Making extensions](../extensions/index.md).
