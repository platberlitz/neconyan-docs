---
title: Included tools
guide: nori
quote: "Check the sidebar or Extensions → Built-in before installing a second copy. Duplicate extensions can leave one inactive, which is a tedious way to discover it was already here."
---

# Included tools

Find documented macros in the [macro reference](../macros/index.md).

Neconyan ships with a collection of writing, appearance and diagnostic tools. They sit alongside the rest of the workspace in the **Workspace**, **Fine-tuning**, **Characters & Lore**, **Appearance** and **Troubleshooting** sidebar sections. Open **Extensions → Built-in** for their settings pages, or **Extensions → Manage extensions** to inspect versions, authors, licences and enabled states. If a bundled tool is switched off, its sidebar button shows **Off** and opens **Manage extensions** so you can turn it on.

Included code updates with Neconyan. Third-party extensions you install separately have their own update path. A bundled tool can still use a paid model or an external service.

## Writing and prompt work

| Tool | Use it for |
| --- | --- |
| **Guided Generations** | Give a response, swipe, regeneration, correction or impersonation specific guidance |
| **Input History** | Search earlier composer input and pick one to replace your draft |
| **Quick Replies** | Buttons above the message box for saved messages, steering and commands |
| **Deep Swipe** | Work with message alternatives, including supported user-message alternatives |
| **Preset Tools** | Search and organise prompt sections |
| **Chat Completion Tabs** | Switch separate **Parameters** and **Prompts** tabs on and off from the sidebar, or open its settings in **Extensions → Built-in** |
| **Prompt Tags** | Manage tags and defaults for supported prompt sections |
| **Macro Enhanced** | A full page for macros: try them in **Playground**, look them up in **Reference**, save your own in **My macros**, check this chat's saved values in **This chat** and set pronouns in **Setup**. See [Macros](../macros/index.md) |
| **Prompting Lab** | Build prompt tests, compare requests and run selected model comparisons |

Prompt reconstruction and dry diagnostics don't generate replies. Prompting Lab's model comparisons and optional analysis make real requests. Read the action before running a batch.

### Quick Replies

**Quick Replies** is the bundled extension; its settings header says **Quick Reply**. Buttons sit above the message box, and **Show quick reply buttons** turns the bar on. Sets are listed under **Shown in every chat**, **Only in this chat** and **Only with this character**; a character association is kept in your settings, not in the character card.

For a single button, use **Make a quick reply**. For a prepared set, use **Ready-made buttons**. **Edit a set** chooses the set you are editing, **Set options** holds its shared behaviour and **Add quick reply** adds another button to it.

The ready-made sets are **Story controls** (**Continue**, **Try again**, **Write for me**), **Reply directions** (such as **More detail**, **Shorter** and **Time skip**), **Writing helpers** (**Action**, **Speech**, **OOC**) and **Ask privately** (**Recap**, **Ideas**, **Who is here?**). **Add set** creates a set under a unique name, switches the bar on, and links the set to every chat when it isn't linked anywhere yet. Adding a set makes no model request; buttons that generate or ask do.

The builder asks for a **Button label**, **What should it do?** and the text, files the button under **Add it to** and saves it with **Add button**. The modes are **Send it as my message**, **Put it in the message box**, **Steer the next reply**, **Ask the AI privately** and **Run a command**. The chips insert **What I typed**, **Character name** and **My name**.

**Steer the next reply** sends anything already in the message box first, then asks for a reply that follows a one-use note. The note isn't added to the chat. **Ask the AI privately** still makes a model request: the answer appears in a pop-up instead of the chat, and the provider works as usual.

The builder refuses a button that doesn't fit the selected set. A set with **Put replies in the message box instead of sending** or **Add what I typed automatically** only accepts send-type buttons; the notice names the set and your options, and the set's own options are left alone.

## Lore and saved work

**World Info Lab** traces lore activation and supports reviewed batch changes. It and Prompting Lab can open saved chats up to 64 MiB. **Lorebook Distiller** proposes lore entries from a saved chat. **Chat Archive** searches and organises chats; its organisation export doesn't contain the chat contents themselves.

**Card & Lorebook Time Machine** keeps supported snapshots of characters, lorebooks and presets. It isn't a whole-account or chat backup. Compare before restoring, because a restore replaces newer edits.

You can keep chatting and save settings while **Snapshot everything now** runs. Its snapshot update keeps your newer local choices and doesn't count as a settings change from another device. A real change from another device still stops a conflicting save.

If the item changes again after comparison, the restore stops rather than overwriting the intervening edit. Compare the current item again before retrying. A snapshot that fails its integrity check can't be used as a trusted restore source.

Several tools keep accepted work and results on the server. Closing the page stops watching it; use the explicit Stop action when you want to request cancellation.

## Appearance and media

**Dialogue Colors** assigns speaker colours. **Regex Agent Themes** restyles trackers and Companion panels. **CSS Snippets** manages your small visual customisations. **Termeownal UI** offers an optional terminal-style interface with its own command glossary.

**Quick Image Gen** needs its own provider configuration. It can use a manual prompt, a chat scene or supported image tags. Prompt preparation may also call a text model. When a separate connection profile writes those prompts, its **Max Tokens** defaults to 32,000 and goes up to 64,000, so long prompts aren't cut short; an install still on the old 500 default moves to the new one once. **Character Expressions** uses separate sprite artwork and classification settings; a character avatar alone isn't a complete expression set.

Speech, captioning, translation, attachments and galleries each have their own settings. A working text connection doesn't automatically configure all of them.

### Images in replies

**Settings → Appearance → Avatar & Chat Styles** holds **Don't send chat images to the model**, which keeps image files and their saved descriptions out of new automatic replies across the account. Pictures stay visible and existing message text stays text. **Review chat images** opens the review panel for the open chat, where an image can be **Send the image**, **Show only** or **Use a description** and, in Roleplay, **Remove from message**. The account setting and a chat's or branch's own setting override the individual choices.

Quick Image Gen's **Generated images in replies** chooses what a new picture does: **Show only**, **Use a description** or **Send the image**. **Use a description** sends the prompt that made the picture, as text. A new Roleplay picture defaults to **Show only**; a Conversation picture defaults to **Send the image**. **Library images in replies** defaults to **Send the image** and offers **Use a description**, which sends the library image's saved description. Sending an image also needs **Send inline media** and a connection that accepts images.

See [Roleplay](../workspace/roleplay.md#images-in-replies) for the per-message controls, [Conversation](../workspace/conversation.md#review-image-input) for its review panel, and [Something went wrong](../help/troubleshooting.md#image-input-needs-attention) for repair and recovery.

### Separate expression sets for a shared card

Open a chat, then **Characters & Lore → Character Expressions**. The image list is the **Expression images** section. Under **Character in this card**, use **Add character** to give each person in a multi-character card a separate expression set. **Whole card** selects the shared set. This is separate from group-chat membership and the card's avatar.

Under **Character appearance**, enter **Appearance notes for image generation**, then **Save appearance**. **Follow the first named speaker in each reply** picks a set from explicit speaker names or `Name:` dialogue labels, not an ordinary mention. If no name matches, it uses your chosen set. Selecting a set manually turns following off. **Remove character set** removes the choice from the card but leaves its image folder.

Use **Add expressions** for several labels separated by commas or new lines. **Find an expression** searches the list, and **All**, **Ready** and **Missing** filter it. A label doesn't create artwork: use **Generate missing** with Quick Image Gen, or add files under **More image tools** with **Upload character sheet** or **Upload ZIP**. **Export ZIP** downloads every image in the selected set, even those hidden by the current search or filter, with the original names and formats; it doesn't include the card, description or chats. Image files are named after the expression, with an optional suffix such as `joy.png` and `joy-2.png`.

**Create expressions for** offers **Chat character** and a **Persona:** entry for each saved persona. Persona generation uses the saved persona name and description, and every persona keeps its own set, even when two personas share a display name. Choosing an image for a persona sets it for that persona's latest user message and as the starting choice for future messages; older messages keep their saved expression. **Clear persona expression** clears the choice without deleting artwork. With **Classifier API → In-Chat Agent** and the **Expressions Agent** running automatically, a new persona message without a saved expression is also classified in the background against that persona's own set; the character's reply doesn't wait for the result. That classification is a separate request on the Agent's connection. A valid result replaces the hand-picked image on that new message; an invalid result keeps it.

Under **How expressions are picked → Image generation and cleanup**, **Sprite generation mode** offers **Separate images** or **Character sheet (auto-split)**. Separate images devote more pixels to each expression, and generation size still follows Quick Image Gen. **Sprite framing** offers **Bust portrait (consistent close-up)** and **Full body (consistent standing pose)**.

**Generation background** offers **Green (recommended)**, **Magenta (for green characters)** and **White or transparent**. Green is the default; choose a colour that doesn't appear on the character. Green and magenta are removed automatically, while **Also remove white or other plain backgrounds** is a separate switch. Changing this setting doesn't touch images you already have; it applies to the next generation or cleanup pass. Cleanup smooths white fringes, keeps each tile's full edges without clipping the artwork, and can't reliably tell every background apart from the character, so check the result.

**AI background removal (optional)** downloads a verified anime cut-out model of about 176 MB once and then processes images on the Neconyan server. **Enlarge after cleanup (optional)** offers **Off**, **2x larger** and **4x larger**, using a model of about 2.5 MB in small overlapping sections and keeping transparency. Both start off. Only the model downloads contact the model host; Quick Image Gen still uses your configured provider for new pictures.

**More image tools → Redo cleanup** reprocesses the existing set and, after a confirmation, overwrites the files, so **Export ZIP** first. Repeated cleanup with enlargement still on enlarges again. **Stop** cancels the run, and images that fail are reported as failed rather than cleaned. As measurements from the project's ARM test server, not promises: background removal took around 22 seconds and about 1 GB of memory for a 256 by 205 pixel image, and 2x enlargement of that size took around 21 seconds with a measured peak of 188 MiB including decoding. Generating images can incur provider charges.

**Display and choices → Show expressions in phone chat** shows each reply's saved expression above its text on phones, in any chat style, including styles that hide ordinary avatars. Ripple keeps its side portrait. The switch is display-only and doesn't reclassify messages.

## Find characters or diagnose a problem

**BotSearcher** searches supported card sources. Available filters, accounts and downloads depend on the source site. External-site errors can occur independently of your model connection. A failed JannyAI link import names its reason, such as a missing login on the server or a hidden card definition. Logging in to JannyAI in your own browser doesn't count; use **Refresh status** or **Open JannyAI login window** in BotSearcher.

**JannyAI card blocks proxies** means the creator has hidden the definition and disabled proxy access. Logging in again won't remove that setting. If JannyAI offers a card download, download it there and import the file; not every hidden card offers one.

**Debugger** provides a diagnostic report and layout snapshot. Reproduce the problem first, then open its report, read it and copy or download it. **Prompt Inspector** helps inspect supported outgoing requests; those prompts may contain private chat material.

!!! taro "Taro"
    'Included' means the code is here. You'll still need to configure any external service it uses and check that service's charges.

Original authors, source links and licence details are recorded in the [included-tools attribution table](https://github.com/platberlitz/Neconyan/blob/staging/docs/neconyan-native-tools.md) and beside the bundled source. Want to make your own tool? Start with [Making extensions](../extensions/index.md).
