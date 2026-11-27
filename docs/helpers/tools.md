---
title: Included tools
guide: nori
quote: "Check the sidebar or Extensions → Built-in before installing a second copy. Duplicate extensions can leave one inactive, which is a tedious way to discover it was already here."
---

# Included tools

Find documented macros in the [macro reference](../macros/index.md).

Neconyan ships with a collection of writing, appearance and diagnostic tools. You'll find them alongside the rest of the workspace, in the **Workspace**, **Fine-tuning**, **Characters & Lore**, **Appearance** and **Troubleshooting** sidebar sections. Open **Extensions → Built-in** for their settings pages. Open **Extensions → Manage extensions** to see versions, authors, licences and which tools are enabled. If a bundled tool is switched off, its sidebar button shows **Off** and opens **Manage extensions** so you can turn it on.

Included code updates with Neconyan. Third-party extensions you install separately update their own way. A bundled tool can still use a paid model or an external service.

## Writing and prompt work

| Tool | Use it for |
| --- | --- |
| **Guided Generations** | Give a response, swipe, regeneration, correction or impersonation specific guidance |
| **Input History** | Search earlier composer input and pick one to replace your draft |
| **Quick Replies** | Buttons above the message box for saved messages, steering and commands |
| **Dice Roller** | Roll d4 to d100 with up to four dice, a bonus, difficulty and advantage or disadvantage, then send the result to the story |
| **Deep Swipe** | Work with message alternatives, including supported user-message alternatives |
| **Preset Tools** | Search and organise prompt sections |
| **Chat Completion Tabs** | Switch separate **Parameters** and **Prompts** tabs on and off from the sidebar, or open its settings in **Extensions → Built-in** |
| **Prompt Tags** | Manage tags and defaults for supported prompt sections |
| **Macro Enhanced** | A full page for macros: try them in **Playground**, look them up in **Reference**, save your own in **My macros**, check this chat's saved values in **This chat** and set pronouns in **Setup**. See [Macros](../macros/index.md) |
| **Prompting Lab** | Build prompt tests, compare requests and run selected model comparisons |

Prompt reconstruction and dry diagnostics don't generate replies. Prompting Lab's model comparisons and optional analysis make real requests. Read the action before running a batch.

On phones, Prompting Lab and World Info Lab use visible section buttons instead of a section dropdown. Tap a section to open its controls without opening the keyboard.

### Quick Replies

**Quick Replies** is the bundled extension. Its settings header says **Quick Reply**. Buttons sit above the message box, and **Show quick reply buttons** turns the bar on. Sets are listed under **Shown in every chat**, **Only in this chat** and **Only with this character**. A link to a character is kept in your settings, not in the character card.

For a single button, use **Make a quick reply**. For a prepared set, use **Ready-made buttons**. **Edit a set** chooses the set you're editing, **Set options** holds its shared behaviour and **Add quick reply** adds another button to it.

The ready-made sets are:

- **Story controls**: **Continue**, **Try again**, **Write for me**
- **Reply directions**: such as **More detail**, **Shorter** and **Time skip**
- **Writing helpers**: **Action**, **Speech**, **OOC**
- **Ask privately**: **Recap**, **Ideas**, **Who is here?**

**Add set** creates a set under a unique name and switches the bar on. If the set isn't linked anywhere yet, it also links it to every chat. Adding a set makes no model request. Buttons that generate or ask do.

The builder asks for a **Button label**, **What should it do?** and the text. **Add it to** chooses the set the button goes in, and **Add button** saves it. The modes are **Send it as my message**, **Put it in the message box**, **Steer the next reply**, **Ask the AI privately** and **Run a command**. The chips insert **What I typed**, **Character name** and **My name**.

**Steer the next reply** sends anything already in the message box first, then asks for a reply that follows a one-use note. The note isn't added to the chat. **Ask the AI privately** still makes a model request. The answer appears in a pop-up instead of the chat, and the provider works as usual.

The builder refuses a button that doesn't fit the selected set. A set with **Put replies in the message box instead of sending** or **Add what I typed automatically** only accepts send-type buttons. The notice names the set and your options, and the set's own options are left alone.

### Dice Roller

**Dice Roller** is a Companion. Every account has it installed but switched off. Turn it on under **Agents → Companions**, then open the **Companion panel** to find the dice. Choose **Notes under replies** in its editor if you'd rather have the dice card under the newest message. The roll happens in your browser and makes no model request.

1. Type what you're attempting.
2. Pick a **Die** from d4 to d100, and up to four **Dice**.
3. Set a **Bonus** from -20 to +20 and a **Difficulty**: Easy, Normal, Hard, Extreme or Custom.
4. Choose **Luck**. Advantage keeps the higher of two rolls, Disadvantage the lower.
5. **Add to message** puts a line such as `🎲 Pick the lock - rolled 17 vs 12 (1d20+2: 15) - SUCCESS` in the message box, and **Send** sends it.

Replies get a short system note telling the model to write that outcome as settled fact without mentioning dice or numbers. Continuing or swiping keeps it. It works with browser and server replies.

**Roll options** holds **Critical rolls**, **Partial successes** and **Roll when the Companion panel opens**. From 1.6.0 it also has two switches, both off to begin with:

- **Auto roll** rolls fresh dice after every reply, so a roll is always waiting for your next message.
- **Auto send** adds the waiting roll as a 🎲 line after each message you send, without putting it in the message box. A message that already has a roll from **Add to message** keeps that one. Slash commands, continues and empty sends get no roll.

With **Auto send** on, a choice from **CYOA Choices with Skill Checks** or **Doors with Fate Checks** gets its own d100 roll against that choice's target. Tap the choice in the reply or the **Companion panel**, or start your message with its number. A 1 is a critical success and 100 a critical failure. Rolling 10 or more under the target succeeds, and up to 10 over is a partial success.

## Lore and saved work

**Pawthfinder** chooses relevant lore with a separate decision model. In its settings, choose a **Jev / decision model preset**, then connect its endpoint or a saved profile. Jev scores which entries to retrieve. Summary writing still uses your chat model. **Decision protocol** must match the provider's decision endpoint or chat-completion service.

From 1.5.6, the presets include Nano-GPT's decision models, such as Jev, Kev, d3 and SubQ. A Nano-GPT preset fills in its address and model. Save your Nano-GPT key under **API key for this endpoint**. It needs Nano-GPT API access and credits.

If you want Pawthfinder to choose the lore by itself, enable **Disable World Info keyword activation**. Otherwise ordinary keyword matches can add entries too. Start with the preset's threshold and change one setting at a time.

**Reuse the lore when swiping** is on by default and needs **Tool Mode** or **Predictive Pipeline**. A swipe or regenerate then keeps the lore Pawthfinder already picked for the reply you're changing. You don't pay its decision model to choose that lore again. Turn it off to pick lore fresh for every swipe. Lore is still picked again after a changed message, a changed lorebook, a different chat or a failed retrieval. The reused answer is kept in the open page, so the first swipe after a reload asks again.

**World Info Lab** traces lore activation and supports reviewed batch changes. It and Prompting Lab can open saved chats up to 64 MiB. **Lorebook Distiller** proposes lore entries from a saved chat. **Chat Archive** searches and organises chats. Its organisation export doesn't contain the chat contents themselves.

**Card & Lorebook Time Machine** keeps supported snapshots of characters, lorebooks and presets. It doesn't back up your whole account or your chats. Its window now has a list and a detail view, with snapshot cards, kind filters, a history timeline and field-by-field comparisons. On a phone it switches between the list and one snapshot instead of squeezing both in. Compare before restoring, because a restore replaces newer edits.

You can keep chatting and save settings while **Snapshot everything now** runs. Its snapshot update keeps your newer local choices and doesn't count as a settings change from another device. A real change from another device still stops a conflicting save.

If the item changes again after you compare, the restore stops rather than overwriting that newer edit. Compare the current item again before retrying. A snapshot that fails its integrity check can't be used as a trusted restore source.

Several tools keep accepted work and results on the server. Closing the page only stops you watching the work. Use the explicit Stop action when you want to request cancellation.

## Appearance and media

**Dialogue Colors** assigns speaker colours. **Regex Agent Themes** restyles trackers and Companion panels. **CSS Snippets** manages your small visual customisations. **Termeownal UI** offers an optional terminal-style interface with its own command glossary.

**Quick Image Gen** needs its own provider configuration. Its panel is built around one **Create** card, which holds status, prompt, **Style**, **Configuration** and **Generate**. **Gallery**, **History**, **Logs** and **Quick setup** sit underneath, and settings are behind tabs. It can use a manual prompt, a chat scene or supported image tags. Preparing a prompt may also call a text model. When a separate connection profile writes those prompts, its **Max Tokens** defaults to 32,000 and goes up to 64,000, so long prompts aren't cut short. An install still on the old default of 500 moves to the new one once.

From 1.5.6, **Gallery** also shows pictures saved in Scratchpad, and you can open it straight from the workspace. See [Open Gallery](../workspace/index.md#gallery). Its **Clear local history** button, called **Clear Gallery** in 1.5.5, clears only this device's history.

**Character Expressions** uses separate sprite artwork and classification settings. A character avatar alone isn't a complete expression set.

With the **GPT Image (OpenAI)** provider, **Model** accepts a model ID the proxy provides, and **Proxy URL** points at that proxy. When your proxy offers `gpt-image-2.6-sunburst` or `gpt-image-2.6-flare`, those names are sent through its Responses image route, as the 2.5 names already were. They then generate a picture instead of failing on the plain images endpoint.

From 1.5.6, Quick Image Gen can also use **PixAI**. Under **Image Provider & Output**, set **Provider** to **PixAI** and paste your key into **PixAI API Key**. Keys need a PixAI membership. Create one under **My API Keys** in your pixai.art profile's API settings, or email api@withpixai.art. PixAI charges for every image from your PixAI balance, so check your credits before a batch.

**Model** offers **Tsubaki.3 (default)**, **Tsubaki.2**, **Haruka v2** and **Hoshino v2**. For anything else, choose **Custom model version ID** and type the **Model version ID**, which is the last number in that model version's address on pixai.art. From 1.5.7, **Mode** offers **Pro** (default) and **Ultra** for Tsubaki.3, and **Lite**, **Standard** (default), **Pro** and **Ultra** for Tsubaki.2. Other models don't offer modes. Some modes need a higher PixAI plan. Steps, CFG and sampler only apply to Haruka v2 and Hoshino v2, the SDXL models. Width and height snap to the nearest size PixAI supports.

From 1.5.7, **LoRAs** takes PixAI LoRA version links or IDs for the selected model, separated by commas. Add `:0.5`, for example, after an entry to change its weight. The range is 0 to 1 and leaving the weight out uses 1. How many LoRAs you can use depends on your PixAI plan and model. **Negative Prompt** sends what to avoid separately from the main prompt.

**Prompt helper** starts at **Off (send my prompt as written)**. PixAI's own helper rewrites your prompt and costs extra, so it stays off unless you pick one of the other choices. Finished pictures are saved like any other Quick Image Gen picture. From 1.5.7 Neconyan can recover a finished picture when its first download address fails. PixAI can't cancel a task, so stopping only stops Neconyan waiting for it, and the picture still finishes at PixAI. The key only goes to PixAI's API and isn't included when you export Quick Image Gen settings.

Speech, captioning, translation, attachments and galleries each have their own settings. A working text connection doesn't set all of them up for you.

### Images in replies

**Settings → Appearance → Avatar & Chat Styles** holds **Don't send chat images to the model**. It keeps image files and their saved descriptions out of new automatic replies across the account. Pictures stay visible and existing message text stays text. **Review chat images** opens the review panel for the open chat. There, each image can be set to **Send the image**, **Show only** or **Use a description**. In Roleplay there's also **Remove from message**. The account setting and a chat's or branch's own setting override the individual choices.

Quick Image Gen's **Generated images in replies** chooses what a new picture does: **Show only**, **Use a description** or **Send the image**. **Use a description** sends the prompt that made the picture, as text. A new Roleplay picture defaults to **Show only**. A Conversation picture defaults to **Send the image**. **Library images in replies** defaults to **Send the image** and offers **Use a description**, which sends the library image's saved description. Sending an image also needs **Send inline media** and a connection that accepts images.

See [Roleplay](../workspace/roleplay.md#images-in-replies) for the per-message controls, [Conversation](../workspace/conversation.md#review-image-input) for its review panel, and [Something went wrong](../help/troubleshooting.md#image-input-needs-attention) for repair and recovery.

### Separate expression sets for a shared card

Open a chat, then **Characters & Lore → Character Expressions**. The image list is the **Expression images** section. Under **Character in this card**, use **Add character** to give each person in a multi-character card a separate expression set. **Whole card** selects the shared set. These sets are separate from group-chat membership and the card's avatar.

Under **Character appearance**, enter **Appearance notes for image generation**, then **Save appearance**. **Follow the first named speaker in each reply** picks a set from explicit speaker names or `Name:` dialogue labels. An ordinary mention doesn't count. If no name matches, it uses your chosen set. Selecting a set by hand turns following off. **Remove character set** removes the choice from the card but leaves its image folder.

Use **Add expressions** for several labels separated by commas or new lines. **Find an expression** searches the list, and **All**, **Ready** and **Missing** filter it. A label doesn't create artwork. Use **Generate missing** with Quick Image Gen, or add files under **More image tools** with **Upload character sheet** or **Upload ZIP**. **Export ZIP** downloads every image in the selected set, even those hidden by the current search or filter, with the original names and formats. It doesn't include the card, description or chats. Image files are named after the expression, with an optional suffix, such as `joy.png` and `joy-2.png`.

**Create expressions for** offers **Chat character** and a **Persona:** entry for each saved persona. Persona generation uses the saved persona name and description. Every persona keeps its own set, even when two personas share a display name. Choosing an image for a persona sets it for that persona's latest user message, and as the starting choice for future messages. Older messages keep their saved expression. **Clear persona expression** clears the choice without deleting artwork.

A new persona message without a saved expression can also be classified for you. That needs **Classifier API → In-Chat Agent** and the **Expressions Agent** running automatically. The classification runs in the background against that persona's own set, and the character's reply doesn't wait for the result. It makes a separate request on the Agent's connection. A valid result replaces the hand-picked image on that new message. An invalid result keeps it.

Under **How expressions are picked → Image generation and cleanup**, **Sprite generation mode** offers **Separate images** or **Character sheet (auto-split)**. Separate images give each expression more pixels. Generation size still follows Quick Image Gen. **Sprite framing** offers **Bust portrait (consistent close-up)** and **Full body (consistent standing pose)**.

**Generation background** offers **Green (recommended)**, **Magenta (for green characters)** and **White or transparent**. Green is the default. Choose a colour that doesn't appear on the character. Green and magenta are removed automatically, while **Also remove white or other plain backgrounds** is a separate switch. Changing this setting doesn't touch images you already have. It applies to the next generation or cleanup pass. Cleanup smooths white fringes and keeps each tile's full edges without clipping the artwork. It can't reliably tell every background apart from the character, so check the result.

**AI background removal (optional)** downloads a verified anime cut-out model of about 176 MB once, then processes images on the Neconyan server. **Enlarge after cleanup (optional)** offers **Off**, **2x larger** and **4x larger**. It uses a model of about 2.5 MB, works in small overlapping sections and keeps transparency. Both start off. Only the model downloads contact the model host. Quick Image Gen still uses your configured provider for new pictures.

**More image tools → Redo cleanup** processes the existing set again. After you confirm, it overwrites the files, so use **Export ZIP** first. If enlargement is still on, a repeated cleanup enlarges the images again. **Stop** cancels the run, and images that fail are reported as failed rather than cleaned.

These are measurements from the project's ARM test server, not promises. Background removal took around 22 seconds and about 1 GB of memory for a 256 by 205 pixel image. Enlarging an image of that size 2x took around 21 seconds, with a measured peak of 188 MiB including decoding. Generating images can incur provider charges.

**Display and choices → Show expressions in phone chat** shows each reply's saved expression above its text on phones. It works in any chat style, including styles that hide ordinary avatars. Ripple keeps its side portrait. The switch only changes the display and doesn't reclassify messages.

## Find characters or diagnose a problem

**BotSearcher** searches supported card sources. Available filters, accounts and downloads depend on the source site. An external site can fail even when your model connection works. A failed JannyAI link import names its reason, such as a missing login on the server or a hidden card definition. Logging in to JannyAI in your own browser doesn't count. Use **Refresh status** or **Open JannyAI login window** in BotSearcher.

**JannyAI card blocks proxies** means the creator has hidden the definition and disabled proxy access. Logging in again won't remove that setting. If JannyAI offers a card download, download it there and import the file. Not every hidden card offers one.

The JannyAI panel stays inside BotSearcher's workspace on phones and desktop, including its login and status controls.

From 1.5.6:

- **Sources and logins**, beside **Filters**, opens a page inside the BotSearcher window. Tick the sites you want, sign in to BotBooru, Saucepan.ai or JannyAI, or press **All BotSearcher settings** for everything else. Back or Esc returns to the same search with your words, site and ticks kept. If you changed which sites are on, the results reload. When every site is off, **Choose sources** opens the same page.
- A **JanitorAI** source lists JanitorAI's own **Trending 24h**, **Trending 7d**, **Popular** and **Latest** cards from its sort menu. **SFW only** switches to JanitorAI's SFW list. JanitorAI can't search by text, so it stays out of **All sources**, and its search box takes a card URL. Anyone signed in can browse the lists. Importing needs the server's JanitorAI browser window, which only an administrator can sign in, as with JannyAI. If that window is signed out or not set up, BotSearcher says which.
- In Simple Mode, BotSearcher is called **Find characters**, and a card you add opens its chat straight away.

From 1.5.7, **JanitorAI** also accepts `jani.com` card links and can try that address if `janitorai.com` stops answering for lists or imports. There's still one **Open JannyAI login window** control for an administrator to use under **Sources and logins**. If the backup address needs a sign-in, finish it in that window. **JannyAI** remains a separate source in the picker.

**Debugger** provides a diagnostic report and layout snapshot. Reproduce the problem first, then open its report, read it and copy or download it. **Prompt Inspector** helps inspect supported outgoing requests. Those prompts may contain private chat material.

!!! taro "Taro"
    'Included' means the code is here. You'll still need to configure any external service it uses and check that service's charges.

Original authors, source links and licence details are recorded in the [included-tools attribution table](https://github.com/platberlitz/Neconyan/blob/staging/docs/neconyan-native-tools.md) and beside the bundled source. Want to make your own tool? Start with [Making extensions](../extensions/index.md).
