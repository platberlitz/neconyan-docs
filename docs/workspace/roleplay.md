---
title: Roleplay
guide: nori
quote: "Give me a character with something to want and something to lose. We can make a perfectly respectable mess from there."
---

# Roleplay

In Roleplay, you exchange messages with a character to develop a scene. It suits both casual character chat and narrated stories.

=== "Computer"

    <figure class="screenshot" markdown>
    [![Roleplay on desktop, showing a saved character conversation and the message composer](../assets/images/screenshots/desktop-roleplay.webp)](../assets/images/screenshots/desktop-roleplay.webp)
    <figcaption>A staged Roleplay conversation. Message controls act on the selected message or alternative.</figcaption>
    </figure>

=== "Phone"

    <figure class="screenshot screenshot--phone" markdown>
    [![Roleplay on a phone, with character messages above the composer](../assets/images/screenshots/phone-roleplay.webp)](../assets/images/screenshots/phone-roleplay.webp)
    <figcaption>The composer stays close to the conversation on a narrow screen.</figcaption>
    </figure>

## Start a scene

Open a character, select Roleplay and choose a saved chat or begin a new one. Check your selected persona, then write a reply that gives the character something concrete to respond to.

Your model may receive more than the visible messages: the card, persona, preset instructions, activated lore, Author's Note and enabled helpers can all contribute. If the writing ignores your intended tone, inspect the full prompt for conflicting instructions.

## Work with replies

**Regenerate or swipe** when you want an alternative. **Edit** when you want a specific correction. **Continue** where available asks the model to extend the current response rather than start a new exchange.

Selecting an existing swipe changes the current text. Generating a new one makes a model request. Read the selected version before continuing, especially if later events depend on a particular detail.

To compare saved swipes, click the swipe counter on a computer or long-press it on a phone. Each version appears as a card you can read in full, copy, branch into a new chat or delete. Choose a card, then **Show swipe** to put it in the chat. On an earlier reply the cards are for reading, copying and branching only.

With **Guided Regenerate** in the composer, type a direction first and the latest AI reply is replaced with one that follows it. An empty composer gives an ordinary regeneration. Use Guided Swipe instead when you want to keep the old reply as an alternative.

Avoid editing an old message while a generation is still relying on it. Stop the current work first and make your intended history clear.

Once the main reply has finished but its after-reply Agents are still running, Stop ends the remaining Agent work and keeps the completed reply: the model isn't asked for the main answer again. Stopping while the main reply is still being written follows the ordinary cancellation rules. [Agents and Companions](../helpers/agents.md#order-and-dependencies) explains which runs each Stop covers.

Quick Replies can put controls such as Continue and steering above the message box. A **Steer the next reply** button asks for a reply that follows a one-use note; unlike an ordinary sent message, the note isn't added to the chat. See [Quick Replies](../helpers/tools.md#quick-replies).

## Run a group scene

A Roleplay group adds character cards as members and gives each turn to a speaker. **Group Controls → Group reply strategy** offers **Natural order**, **List order**, **Pooled order**, **Manual** and **Scene Director**. Scene Director makes a separate small model request before each reply. It reads the member cards and up to eight recent visible messages, then picks 0 to 3 members in speaking order. It never picks you, and it can choose nobody when the scene should wait for you. Its choice replaces the usual order for that turn. **Director model** gives that request its own saved connection profile without changing the model that writes the character replies. If no usable choice arrives within 3 seconds, the usual order picks and a warning explains the fallback once per chat. The **Scene** panel shows the last pick and its reason. Scene Director is not Director's Commentary, the after-reply agent.

**Let them talk** in the group speaker bar lets enabled members take turns among themselves while you listen. **Group Controls → Let them talk: replies** sets the burst from 1 to 8, with 3 as the default. It needs at least two unmuted members and no reply already running. Each reply is saved as it finishes, and the button reads **Stop** while the burst runs. Stop, sending a message, switching chat or leaving the chat ends it. With Scene Director on, the director keeps choosing and is told that you're only listening. **Ensemble replies** writes a whole scene in one request and splits it into character messages, so it spends one request rather than one per turn. **Keep characters to their own lines** cuts a reply where it starts writing another member's part.

The **Scene** button opens the chat's scene strip. **Location** is an optional label up to 300 characters. Tap a member to **Mark away** or **Bring into the scene**; away members miss what is said meanwhile, and shared memory stays out when it could give the scene away. **Message audience** offers **To everyone** or **Whisper to** one present, unmuted member. A whisper records its audience, and other members cannot hear or react to it; later prompts and Agent work follow the same boundary. If the target becomes away or muted, Neconyan asks you to choose someone present or address everyone. Scene state belongs to the current chat, not the whole group.

Open a member's menu from their avatar in the speaker bar or Scene panel and choose **Use as Narrator / GM**, or **Use as character** to switch back. A Narrator gets a reminder to describe the setting, consequences and supporting characters, advance the scene when it needs an event, leave the members' choices to their own replies, and respect presence and whisper boundaries. It does not add a separate narrator model, narrate while the member is muted or away, or give that member control of the others. To hear the same turn in another voice, regenerate it as a different member.

For a messaging-style group, see [Conversation](conversation.md); for a cast feed, see [Meower](meower.md).

## Images in replies

Pictures in a chat can join future automatic replies as the image itself, as a description, or not at all. Open **Settings → Appearance → Avatar & Chat Styles → Review chat images**, then choose per image:

- **Send the image** sends the file with the request. It also needs **Send inline media** and a connection that accepts images.
- **Use a description** sends a saved or typed description instead of the file.
- **Show only** keeps the picture visible and sends the model neither the file nor its saved description.
- **Remove from message** removes the reference; the saved image file and the chat backup remain.

Press **Save choice** to apply one, or tick several with **Select this image** and use **Save choices for selected images**. The account setting **Don't send chat images to the model** and the chat setting **Don't send this chat's images to the model** override the individual choices.

Show only changes only what new automatic replies may include. Your own written text, existing memories and already displayed messages stay as they are. Work already accepted keeps the input it captured; use **Stop** to cancel it. Writing a caption by hand and pointing a tool at a specific image are separate actions.

If a send is refused because an image needs a choice, a **Review needed before replying** notice opens the review for that chat directly.

Older messages may need attention before Show only can be applied; [Something went wrong](../help/troubleshooting.md#image-input-needs-attention) explains the repair and recovery controls.

## Chat and writing settings

**Settings → Chat & Writing** separates controls into **Chat & messages**, **Characters**, **Auto-swipe & auto-continue**, **Autocomplete** and **Fine-tuning**. Start with the drawer that matches the behaviour you want to change. Script controls live under Fine-tuning; appearance-only switches live under [Appearance](appearance.md).

For reopening, linking and naming chats, use **Settings → Chat & Writing → Chat & messages → Chat window**. **Reopen your last chat** and **Chat links in the address bar** are separate choices, initially off. A chat link refers to a chat on that installation and account; it isn't a public copy of the conversation. Under **Chat & messages → Sending**, **Open keyboard when a chat opens** focuses the message box when you open or switch to a chat so you can type straight away.

You can also use **Copy chat link** in desktop Recent Chats, or open **Chat link settings** from the phone's chat tools.

**Name chats automatically** in the same **Chat window** group is on by default, with **Messages before naming** set to **6** (from 1 to 100). It counts visible non-system messages with text, including the greeting, after you've sent at least one message of your own. When the open chat still has its date-and-time name and Neconyan is idle, it asks the current model for a short title; this usually takes one request, though a failed structured attempt on Chat Completion can retry once as plain text. Names you chose yourself are kept, and temporary chats, built-in assistants and Conversation are skipped.

**Settings → Chat & Writing → Chat & messages → Replies → Where replies are written** chooses the default path for new ordinary replies. **In the browser (recommended)** shows the reply directly in the tab. **On the server** sends ordinary Roleplay replies through a saved server job. Both show text as it arrives. Conversation, replies that need a selected Notebook context, one-to-one guided corrections and Deep Swipe always use the server. Built-in assistant chats, group guided actions and some group turns stay in the browser. Changing the setting doesn't start a reply or make a model request.

Server-run Roleplay replies keep running while you're watching the chat as well as when the tab is hidden. **Writing reply…** is the live job's status. [When you leave the page](#when-you-leave-the-page) explains what happens if you close it. With **Settings → Appearance → Visual Toggles → Message Timer** enabled, elapsed seconds keep ticking between incoming chunks and stop when the main reply finishes, even if Agents are still working.

While a streamed reply has no text or visible reasoning yet, a **Thinking...** label stays above the empty message. It clears when either appears and isn't saved in the chat.

If a stream ends early, stalls, loses its connection or hits **Max Response Length** while the model is still reasoning, Neconyan keeps the partial prose or thinking-only reply that arrived, explains why it stopped, and skips automatic after-reply Agents on the incomplete turn so they don't rewrite a cut-off answer. Making room for a new held reply never cancels one that is still being written, and a refused or failed swipe unlocks swiping again.

For OpenRouter and custom OpenAI-compatible connections, **Interleaved Thinking** sits below **Enable function calling** in the Chat Completion settings. Turn on **Request model reasoning** to use it. **Since Last User Message** and **Active Tool Chain** send each saved tool call's own reasoning with later calls; a neighbouring message's thinking is used only when the call has none.

The live bubble stays visible until the saved reply is ready to replace it, and the handover preserves your reading position. Cancelling a replacement restores the original reply. While the tab is hidden, the live preview pauses to save battery and catches up when you come back.

Completed Agent changes appear while the remaining Agents are still working. Parallel rewrites that need combining show their combined result once it's ready; appended blocks and completed Companion notes can appear earlier. Reopening a running reply restores Stop and keeps Send unavailable until that work settles. When a later Companion note updates under a saved reply, your reading position stays where it was instead of jumping to the newest message.

## When an Agent fails

A finished reply isn't thrown away because a helper after it failed. Neconyan retries a failed after-reply Agent or Companion once while the chat and its accepted Agent settings still match. The retry is another request to that helper's connection, so it can add usage. The main reply isn't requested again.

If the retry fails too, the reply is added with the completed helper changes that can still be applied. If applying those changes fails, for example after restarting with an edited Agent definition, the reply is saved as the main model wrote it. Optional translation and automatic speech are still attempted; either can fail without discarding the reply. If a restart interrupts either step after the main reply is ready, the reply is still saved and that unfinished step isn't requested again. You don't need to regenerate.

A real change to the chat, such as editing or deleting the message the reply is answering, can still stop that reply from being added. [Agents and Companions](../helpers/agents.md#order-and-dependencies) explains which runs Stop covers.

## Replies saved by the previous version

Version 1.3.4.1 kept finished replies that couldn't be added to their chat in the **Recovered reply** card. The first normal start after updating handles those old copies automatically: Neconyan protects the saved copy before routine job cleanup can remove it, checks that the chat still matches, and saves the reply once using the already-paid result. It doesn't ask the main model again and doesn't show a second recovery card or a restore button.

If the chat changed since that reply, or its saved model result is missing or doesn't match, the old copy stays in job history instead of overwriting your edit. Nothing is sent again. Replies you cancelled or dismissed yourself stay that way, and safe mode waits until you start normally. A completed upgrade isn't repeated on later restarts.

## Keep prompt switches beside the chat

For Chat Completion connections, open **Presets → Prompts** and use **Pin** beside a prompt you often switch on or off. On a computer, **Pinned prompts** then appears beside or above the Roleplay chat. Its switches change the prompt's enabled state without opening the preset again.

The outer prompt list stays open. Individual prompt sections can still be folded, and their lock controls fill the section row's height.

Pinning alone doesn't enable a prompt or edit its text. Pins belong to the selected preset and follow its prompt order. Switching presets changes the list; **Collapse pinned prompts** keeps a compact control in view. Use **Unpin** in the prompt list to remove one. Removing the last pin removes the panel.

You can manage pins in the phone's prompt list, but the chat-side panel is desktop-only. It isn't shown in Conversation, Story Mode, Meower or Text Completion.

## Formatting and scripts

**Allow card scripts** controls interactive card content. Scripts run in an isolated embedded page with restricted Neconyan access and checked slash commands; only the interactive widget the script drives is placed in that sandbox, leaving the surrounding message prose in the chat. Automatic runs require a browser that can block direct connections. If yours can't, each card needs **Run anyway** and could send its own content or anything you type into it to outside servers. Only run cards you trust. An older Android app with an unrestricted native bridge asks you to update instead of offering that override.

**Fine-tuning → Formatting** groups controls into **Context & cleanup**, **Instruct template**, **System prompt**, **Reasoning** and **Reply controls**. Use the section for the request or reply behaviour you want to change. Instruct templates define message markers for supported local-model connections; Chat Completion prompt lists still belong to that connection's preset controls. **Tour** explains the page, and [Model and prompt settings](model-settings.md) covers sampling, formatting, stopping strings and the tokenizer in more detail.

### Find-and-replace rules

**Fine-tuning → Regexes** holds find-and-replace rules for messages and prompts. You don't need to know the pattern language to make one:

1. In **Draft a rule with a model** at the top of the page, describe the change in plain words, for example 'turn lines starting with OOC: into small grey text'.
2. Choose where it's saved with **Save to**: **Global**, **Preset** or **Character**.
3. Choose a **Connection**: a saved connection profile or **Current connection**. Neconyan remembers the choice.
4. Press **Draft rule**.

The editor opens with the rule filled in, a short explanation and **Test Mode** running on an example. Nothing is saved until you press **Save**. The editor has the same panel under **Describe it and let a model write it**: once a pattern exists its button reads **Improve rule** and sends the current rule back for revision, and **Show it my last reply** adds the latest message, up to 1,500 characters, as sample text. Each draft is one request on the chosen connection, and a failed draft leaves the form as it was. **Write a rule yourself** opens an empty editor, and **Manage** holds **Import**, **Select several** and the **Debugger**.

### Regex flags {#regex-flags}

Flags are letters after the closing slash of a pattern that change how it matches. **Find Regex** accepts either form:

- `/pattern/flags`, such as `/colour/gi`, uses the flags you list.
- A plain pattern without slashes, such as `colour`, uses no flags: it changes only the first match and treats capital and small letters as different.

The **Options** row under **Find Regex** sets them for you. Turning a chip on or off rewrites the box as `/pattern/flags`, adding the slashes if the pattern didn't have them.

| Chip | Flag | What it does |
| --- | --- | --- |
| **Every match** | `g` | Changes every match, not just the first one |
| **Ignore case** | `i` | Treats capital and small letters as the same |
| **Dot matches new lines** | `s` | Lets `.` match line breaks, so a match can span lines |
| **^ and $ per line** | `m` | Makes `^` and `$` match the start and end of every line, not only the whole text |

The line under the box confirms the result, for example **Applies to all matches** and **Case insensitive**, or **Invalid Find Regex** when the pattern can't be read. Most rules want **Every match**; without it, a rule meant to tidy a whole reply stops after the first change. **Start from a recipe** fills in common patterns with suitable flags already set, and **Test Mode** shows the effect before you save.

STscript, Neconyan's slash-command scripting language, can run commands from the composer while a reply is being written. These commands help coordinate it:

| Command | What it does |
| --- | --- |
| `/is-generating` | Returns whether a solo or group reply is being generated |
| `/wait-generation timeout=60000` | Waits up to 60 seconds for the current reply; returns false on timeout. Use `timeout=0` to wait indefinitely |
| `/stop` | Stops the current reply; `/generate-stop` is an alias |
| `/getinput` | Reads the existing composer draft without changing it |
| `/trigger` | Requests another reply without sending or clearing the draft |

Use a wait before triggering another reply when the current one may take time. **Stop script** cancels a script's wait. Checking and waiting don't request a reply; generating does.

From a Quick Reply or automation, this replaces the existing draft with uppercase text:

```text
/getinput | /upper | /setinput
```

Typing and submitting that script directly in the composer clears the submitted script before it runs, so it can't recover an earlier draft. `/trigger`, `/gen` and `/genraw` preserve text already in the composer. A failed submitted command is restored only if the composer is still empty, keeping text you've since typed.

### Script parser options {#script-parser-options}

Two switches in **Settings → Chat & Writing → Fine-tuning** change how STscript reads a script. Both start off, and most scripts don't need them.

- **STscript: strict escaping** makes a backslash escape any separator, including another backslash. With it on, `/echo abc \| /echo def` shows one message, `abc | /echo def`, because `\|` is a plain pipe rather than the start of a new command. `\\|` is a literal backslash followed by a real separator. Without it, older, looser escaping rules apply.
- **STscript: literal variables** stops `{{getvar::}}` and `{{getglobalvar::}}` from running macros stored inside a variable. Turn it on when a variable holds text with `{{` braces that should be read as written, not filled in a second time.

A single script can switch either option for itself with `/parser-flag STRICT_ESCAPING on` or `/parser-flag REPLACE_GETVAR on` at the start.

## Keep the model informed

- Put stable character traits in the [character card](characters.md).
- Put relevant world facts in [lorebooks](lorebooks.md).
- Use an [Author's Note](#authors-note) for short guidance about the current scene or style.
- Use [Mewmory](../helpers/mewmory.md) when a long saved history needs structured recall.
- Use [Scratchpad](../helpers/scratchpad.md) for planning you don't want inserted as a story message.

Adding context uses space. More instructions aren't automatically better if they contradict each other or push useful history out of the request.

### Author's Note {#authors-note}

Open **Chat tools → Author's Note** to steer the current scene, tone or style without editing the character card. A summary line at the top shows which notes are active in the open chat, and four tabs separate where each note lives:

- **This chat**: the open conversation's note, placement, depth, role and **Insertion Frequency** (`1` sends on every reply, `0` disables the Author's Note for this chat), plus the shared **Include in World Info Scanning** switch used across all chats.
- **Character**: private notes saved for this character or group and left out when you export the card. Add several notes with **New note**, tick every note you want in the mix, and tap a name to edit its text and whether it sits at the **Top of Author's Note**, **Replace Author's Note** or **Bottom of Author's Note**. Tick **Separate notes for each persona** so each persona keeps its own set of ticked notes for this character.
- **Persona**: a private note that follows your active persona across characters. It keeps named profiles (one active at a time) and its own Top, Replace or Bottom placement. You can also open it straight from **Persona** (**Author's Note** or **Edit note**) or from the **Author's Note → Edit** button inside the composer's persona picker.
- **New chats**: the default text, placement and frequency copied into new chats when they start.

When both Character and Persona notes are switched on, Top notes run before the chat note (or before any Replace notes), and Bottom notes run after it, with ticked character notes in list order before the persona note. Conversation mode has its own Author's Note setting.

## Manage saved chats {#saved-chats}

To switch quickly without leaving the composer, press the current chat's name on the chat bar above the message box (its tooltip and accessible label read **Switch chat**). It opens a searchable popup for the current character or group, showing each chat's title, last-message date, message count, token estimate and a short preview; **Current** marks the open chat.

For the full file manager, open **View chat files** in the bottom chat actions row (shown or hidden with **Show chat actions** / **Hide chat actions**), from the chat tools sheet on a phone, or with **Chat tools → Manage chat files**. The window is titled with the character's name, for example **Miso Chat History**.

- Click a chat to open it. **Search...** filters the list.
- **New Chat** starts a fresh chat with the character's first message. **Import Chat** brings in a chat file.
- **Import from another instance → Import as new instance** makes a separate copy of the character that holds the chats chosen in **Import Chat**. Nothing is merged into the existing character.

Each chat row has its own buttons:

| Button | What it does |
| --- | --- |
| **Rename** | Renames the chat file |
| **JSONL** | Downloads the chat file, which Neconyan can import again |
| **Plain text** | Downloads the chat as a plain text document |
| **Readable** | Downloads a transcript laid out for reading |
| **Replies** | Downloads only the character's replies |
| **Delete** | Deletes the chat file |

**Label current** asks the model to give the open chat a descriptive name, and **Label dated** does the same for chats still named with the date they started. **Cancel** stops a labelling run. Each label uses one request on your connection, or two if a structured Chat Completion attempt falls back to plain text. To have dated chats named in the background once they reach a message threshold, keep **Name chats automatically** on under **Settings → Chat & Writing → Chat & messages → Chat window**.

To clear out old chats, set **Older than** and **Keep newest**, then press **Preview** to see which chats match. **Dated only**, on by default, limits the clean-up to chats still named with their start date, so chats you've renamed stay. The open chat and the newest chats you asked to keep are never removed. **Clean** asks before it deletes, and deleted chats can't be restored from this window, so make a [backup](../help/backups.md) first if you might want them back.

## When you leave the page

With **In the browser** selected, ordinary Roleplay replies, swipes, **Continue**, group turns and **Guided** replies run in the page. If you close or leave it mid-reply, the server holds most single-character replies: reopen the same chat to collect and save the result without another paid request. A finished reply waits 15 minutes, or 24 hours when the request carried chat context, and a server restart loses it. Agents that run after a reply aren't replayed for a held reply; use [**Rerun agents**](../helpers/agents.md#rerun-agents-on-a-reply) from the message menu if you want them.

With **On the server** selected, the same ordinary replies use a saved job, so they keep writing after you close the page or your phone sleeps, and their after-reply Agents still run. A browser-only macro stops a server reply with an error instead of sending it. A page instruction the server cannot carry falls back to the browser only when no Notebook context requires the server.

A reply that needs a selected Notebook context always goes to the server, even when **In the browser** is selected. The server builds that prompt from saved material, so it can't always include everything the page would. When the route can't include your page prompts, Neconyan explains why and doesn't generate a reply missing those instructions. Fix or remove the page-only instruction, or clear the Notebook context for that reply, then send again.

Replies that use a selected Notebook context, **Deep Swipe** replacements and protected **Guided** corrections run as saved server jobs and keep going, Agents included, after the browser disconnects. After a suspended phone tab returns, the page reconnects to the current saved job, refreshes a stale preview or readback first and only shows the result once that refresh succeeds. The server and provider still need to be available; browser-only model or speech routes can require the page to stay open.

If a reply seems stuck, inspect its status before sending another. [Troubleshooting](../help/troubleshooting.md) explains the difference between slow preparation, a pending provider request and a failed connection.

!!! taro "Taro"
    A tracker displayed under a reply may be an Agent or Companion result. The main model didn't necessarily write it. Check which request you're actually diagnosing.

Prefer a messaging-app rhythm? Try [Conversation](conversation.md). Prefer uninterrupted prose? Try [Story Mode](story-mode.md).
