---
title: Roleplay
guide: nori
quote: "Give me a character with something to want and something to lose. We can make a perfectly respectable mess from there."
---

# Roleplay

Open a character and write together, whether you want a casual conversation or a long-running story.

=== "Computer"

    <figure class="screenshot" markdown>
    [![A demo Roleplay conversation on desktop](../assets/images/screenshots/desktop-roleplay.webp)](../assets/images/screenshots/desktop-roleplay.webp)
    <figcaption>Read the scene, then give the character something to respond to.</figcaption>
    </figure>

=== "Phone"

    <figure class="screenshot screenshot--phone" markdown>
    [![A demo Roleplay conversation on a phone](../assets/images/screenshots/phone-roleplay.webp)](../assets/images/screenshots/phone-roleplay.webp)
    <figcaption>The composer stays beside the conversation.</figcaption>
    </figure>

## Start a scene

1. Open a character and choose **Roleplay**.
2. Open a saved chat or start a new one.
3. Check your persona, then write your first message.

The model can also receive the character card, persona, preset, lore, Author's Note and enabled helpers. If the tone feels wrong, check those instructions before adding more.

## Work with replies

| You want to… | Use… |
| --- | --- |
| Try another answer | **Regenerate** or generate a new swipe |
| Fix a particular sentence | **Edit** |
| Extend the current answer | **Continue**, where available |
| Give a direction for a replacement | Type it, then **Guided Regenerate** |
| Keep the original alongside a guided alternative | **Guided Swipe** |

Choosing a saved swipe doesn't make another model request. Click the swipe counter on a computer, or hold it on a phone, to compare versions. Choose **Show swipe** to use one. Earlier replies can be read, copied or branched into a new chat from this view.

From 1.5.7, **Guided Swipe** and **Guided Impersonate** are beside **Switch chat** in Simple Mode when enabled in Guided Generations. Type a direction before pressing either one. Swipe makes an alternative, keeps the original reply and leaves your direction in the composer. Impersonate drafts a reply as your persona in the composer without sending it. Both ask your model for a reply.

An empty composer makes Guided Regenerate behave like an ordinary regeneration. Stop current work before editing the history it relies on.

If the main reply has finished, **Stop** ends the remaining Agent work and keeps that reply. From 1.5.5, this also covers a server-written reply that runs in several Auto-continue parts. Stopping it keeps the parts that already finished, and a stopped reply stays stopped.

A [Quick Reply](../helpers/tools.md#quick-replies) can also steer the next answer. It adds a one-use note that isn't added as a chat message.

### When a reply fails or comes back empty {#failed-replies}

These apply from Neconyan 1.5.5. They aren't in 1.5.4 or earlier.

A reply that arrives with no text at all counts as a failed attempt, even when the AI service reported success. Neconyan shows **Reply failed**. For a swipe or regenerate, the previous reply goes back where it was with its Companion notes, and Agents don't run on the failed attempt. It no longer becomes an empty swipe.

When the server writes the reply, swiping or regenerating empties the old reply straight away while the new one is written. The chat stays where you were reading. If the attempt fails or you press **Stop**, the old reply and its notes come back.

Version 1.5.6 smooths this further:

- On a server-written swipe or **Regenerate**, including guided ones, the emptied reply shrinks to a small `...` card at once, so there's no blank gap above the new reply. A Guided Correction still keeps the old reply's height, so your place holds.
- A swipe that fails before any text arrives keeps the existing reply in view. If you'd scrolled up while waiting, your place stays put, and reloading doesn't bring back the temporary `...` message.
- A server-written swipe no longer drops an Agent's rewrite or skips Companion notes when a Memory Shard is set up.
- With the model name shown in message timestamps, it sits on its own line below the date, and long names wrap instead of being cut off.

If a service starts a reply and then sends nothing for five minutes, the attempt ends with **The AI service stopped sending the reply.** The wait for the first words isn't limited, so a slow local model isn't cut off. [Troubleshooting](../help/troubleshooting.md#a-reply-comes-back-empty-or-stops-halfway) covers what to check.

## Run a group scene

Choose how the group takes turns:

- **Natural order** follows the conversation.
- **List order** follows the member order.
- **Pooled order** randomly picks a member, preferring those who haven't spoken since your last message.
- **Manual** lets you choose a speaker.
- **Scene Director** asks a separate model which members should speak. It can choose nobody and falls back to ordinary selection if it fails.

**Let them talk** runs a short exchange between at least two unmuted members. Choose one to eight turns. The default is three. To end it, stop, send a message, switch chats or leave the page. Ensemble writing produces the scene in one request instead of one request per speaker.

Use **Scene** to set the location and mark who is present. **Whisper** reaches members who are present and unmuted. Absent characters don't receive it. A member's **Use as Narrator / GM** option adds a reminder for that speaker. It doesn't give them control over everyone else or unmute them.

??? info "Scene Director requests"

    The director reads the member cards and up to eight recent messages, then chooses up to three speakers. It never picks you. From 1.6.0 it waits up to 30 seconds by default; change **Director timeout** under **Group Controls**, anywhere from 1 to 300 seconds. If it gives no usable answer, the usual order picks instead and a warning says so once per chat. The **Scene** panel shows its last pick and why.

### Who heard what {#who-heard-what}

From 1.6.0, each group member only remembers the lines they were there to hear. Someone who was away, or who wasn't in a whisper, doesn't get that line in their prompt.

- Every message can show a badge such as **Heard by 1 of 3**. Tap it, or choose **More → Who heard this**, to tick or untick members, then **Save**. Apply it to **This message** or **From here on**.
- Switch on **Everyone hears this** in the same editor for a line that every member should know, including members who are away now or join later.
- Long-press a member and open **Memory** to choose what they keep: **What they heard** (the default), **Only with the group**, which keeps a line only while someone else who heard it is in the scene, or **Everything**, which gives them every line except other people's whispers. **Catch up on what was said** fills in a member who missed something, and **Forget everything so far** clears what they heard.
- **Remember from message** in the **Scene** panel sets a memory starting point for the chat. Members forget everything before that message number.

[Mewmory](../helpers/mewmory.md) follows the same rules, so each speaker recalls and saves only what they heard. Group chats from SillyTavern's Presence extension keep who heard what when you bring them over.

??? info "Scene commands and macros"

    Slash commands change who heard what without opening the editor: `/heard-forget Kit 4-9`, `/heard-remember`, `/heard-all`, `/heard-none`, `/heard-everyone 4-9`, `/heard-copy from=3 to=8`, `/heard-transfer name=Kit to=Mira`, `/heard-get 12` and `/heard-from 12`. `/away Kit`, `/back Kit` and `/scene-location The inn` change the scene. Presence command names such as `/presenceForget` still work.

    Prompts and cards can read the scene with `{{groupPresent}}`, `{{groupAway}}`, `{{sceneLocation}}` and `{{groupHeard::12}}`.

## Images in replies

Open **Settings → Appearance → Avatar & Chat Styles → Review chat images** to choose what the model receives:

- **Send the image** needs a model that can read images and **Send inline media** enabled.
- **Use a description** sends the written description.
- **Show only** keeps the image visible without sending either.
- **Remove from message** removes the reference without deleting its file.

Press **Save choice** after choosing. Account or chat settings that say **Don't send** take priority. Changing a choice doesn't alter a request the provider has already accepted. Stop and retry if needed. For a stuck review notice, see [troubleshooting](../help/troubleshooting.md#image-input-needs-attention).

## Chat and writing settings

Start with **Settings → Chat & Writing**:

- **Chat & messages → Chat window** controls chat links and **Reopen your last chat**. Both start off. Links work on your installation and account; they aren't public copies.
- **Chat & messages → Sending** includes whether the keyboard opens automatically.
- **Chat & messages → Messages → Block external media** sets the default for loading images, audio and video from other websites. The character or group's external-media dialog also has **Block external media by default**. **Always allowed** and **Always forbidden** override that default for the selected character or group. Outside sites can see your IP address when their media loads.
- **Replies → Where replies are written** chooses **In the browser** or **On the server**. See [leaving the page](#when-you-leave-the-page) before changing it.

**Name chats automatically** makes a model request once a date-named chat has enough messages and you've sent one. The default is six messages, including the greeting. You can change that number under **Messages before naming** or turn naming off. Assistant chats, temporary chats and Conversation mode aren't named this way.

From 1.6.0, thinking models get room to finish reasoning before they write the title. If naming fails, a **Could not name this chat automatically** message shows the reason once. That chat keeps its dated name and isn't tried again until the page reloads, so name it from the wand button in the chat bar or **Label current** in Chat History instead.

The message timer stops when the main reply finishes. It doesn't count Agent work afterwards. A cut-off reply keeps any text or thinking it received. It doesn't start after-reply Agents as though the answer had completed.

If a reply finishes with thinking but no text, the bundled **Thinking Reply Recovery** Agent can write the missing reply from that thinking and pass it to your other after-reply Agents. It starts switched off; turn it on in Agents. A routine chat save while a long reply is being written no longer makes it skip, and the recovered prose is written into the chat.

## When an Agent fails

A failed Agent shouldn't cost you the main answer. Neconyan keeps the completed reply and successful changes from other helpers. A failed helper may retry once, which can cost another request. If no rewrite succeeds, the original reply remains.

Translation or speech failures also leave the answer intact. If you changed or deleted the source chat while work was running, check its saved request before trying again. See [Agents](../helpers/agents.md#troubleshoot-a-helper).

## Replies saved by the previous version

After an update, Neconyan can recover a completed server reply that wasn't attached to its chat. It checks the original chat first and doesn't ask the model to write it again.

If the chat has changed, inspect **Server requests** rather than resending. Cancelled or dismissed work isn't restored automatically. Recovery waits until normal startup if you're in Safe Mode.

## Keep prompt switches beside the chat

On a computer, Chat Completion prompts can be pinned beside the chat. Pinning makes a switch easier to reach; it doesn't enable the prompt. The panel follows the preset's order and disappears when you unpin the last item.

You can manage pins on a phone, but the beside-chat panel is desktop-only. See [model settings](model-settings.md) for the prompt itself.

## Formatting and scripts

Open the formatting settings for message appearance, find-and-replace rules and scripts. Start with one rule and test it on a saved reply.

Interactive message scripts run in a separate widget. If a browser can't block their network access, **Run anyway** permits access that may send data outside the app. Only use it for scripts you trust. Update an older Android app if it asks for a newer script bridge.

### Find-and-replace rules

1. Describe what you want changed.
2. Choose whether the rule belongs to **Global**, **Preset** or **Character**.
3. Choose a connection and select **Draft**.
4. Read the result in the editor and use **Test Mode** before saving.

**Improve** revises an existing rule. **Show last reply** includes up to 1,500 characters as an example. Each draft or improvement is a model request. A failed request keeps your current rule.

### Regex flags {#regex-flags}

A regular expression is a pattern for finding text. Its flags change what it matches:

| Flag | Meaning |
| --- | --- |
| `g` | Replace every match |
| `i` | Ignore upper and lower case |
| `s` | Let `.` match line breaks |
| `m` | Treat each line as a beginning and end |

Without flags, a normal match is case-sensitive and stops at the first result. The **Options** chips update the pattern for you. Try the recipes in **Test Mode** before using them on a chat.

### Script parser options {#script-parser-options}

**Strict escaping** and **literal variables** start off. A script can set its own behaviour with `/parser-flag` instead of changing the account default. See the [macro and scripting reference](../macros/index.md) for syntax.

These commands help scripts that start replies:

- `/is-generating` checks whether work is active.
- `/wait-generation` waits for it. Its default timeout is 60,000 milliseconds. `0` waits without a limit.
- `/stop` and `/generate-stop` stop generation.
- `/getinput` reads the composer.
- `/trigger`, `/gen` and `/genraw` start writing.

If a composer script fails, its text is restored only while the composer is still empty, so newer typing isn't overwritten.

## Keep the model informed

Put stable character details in the card, world facts in [lorebooks](lorebooks.md), and the current scene direction in Author's Note. [Mewmory](../helpers/mewmory.md) recalls older events. [Scratchpad](../helpers/scratchpad.md) helps plan changes before applying them.

### Author's Note {#authors-note}

With a Roleplay chat open, choose **Chat tools → Author's Note** by the composer. From 1.5.7 you can do this in Simple Mode too. On a keyboard, use Enter or Space to open Chat tools and select the note; closing the editor returns focus to Chat tools.

Author's Note adds a short instruction to the prompt. Its tabs choose where that instruction belongs:

- **This chat:** the current chat's note. Frequency `1` sends it every turn. `0` stops regular insertion. Lore scanning is a separate setting.
- **Character:** private notes for this character. Tick the ones to use and choose Top, Replace or Bottom. **Separate notes for each persona** gives each persona its own note library, not just separate ticks. The list you see and the edits you make follow the equipped persona, so another persona's notes stay out of this list and out of the prompt.
- **Persona:** one active private profile that follows the persona across characters.
- **New chats:** defaults for chats you create later.

Top notes come before the chat note, character first and persona second. Bottom notes follow it in the same order. Conversation mode has its own Author's Note settings.

From 1.6.0, the **Full screen** button beside each note opens a larger editor, which helps with a long note on a phone.

=== "Computer"

    <figure class="screenshot" markdown>
    [![The four Author's Note tabs in Simple Mode on desktop](../assets/images/screenshots/desktop-simple-authors-note.webp)](../assets/images/screenshots/desktop-simple-authors-note.webp)
    <figcaption>The <strong>This chat</strong> tab holds the note and when it's sent.</figcaption>
    </figure>

=== "Phone"

    <figure class="screenshot screenshot--phone" markdown>
    [![The Author's Note editor and its four tabs in Simple Mode on a phone](../assets/images/screenshots/phone-simple-authors-note.webp)](../assets/images/screenshots/phone-simple-authors-note.webp)
    <figcaption>All four tabs stay available in the phone editor.</figcaption>
    </figure>

## Manage saved chats {#saved-chats}

Use **Switch chat** to search and reopen a conversation. For file actions, choose **View chat files** on desktop or **Manage files** in the phone's chat tools.

From there you can start or import a chat, export it, rename it, or delete it. JSONL keeps the chat structure. Plain text and Readable Replies are for reading elsewhere. Importing as a new instance keeps it separate from the original.

**Label** can name the current chat or date-named chats with a model request. For cleanup, choose **Older than** and **Keep newest**, then **Preview** before **Clean**. Cleanup targets date-named chats by default and protects the open chat and newest one. [Back up first](../help/backups.md).

## When you leave the page

**In the browser** is the default for ordinary Roleplay. Most single-character replies can be held by the server if the page disconnects, then recovered when you return. After-reply Agents aren't replayed automatically; use **Rerun agents** if needed. From 1.5.5, the **Agents did not finish** warning carries its own [**Rerun agents** button](../helpers/agents.md#rerun-agents-on-a-reply).

If you return while a reply is still being written, it appears after the last saved message rather than above the greeting. A replacement reply keeps its existing place.

Choose **On the server** when you want supported writing and Agents to continue after closing the page. The server must stay running. Conversation, Notebook writing and supported one-to-one guided replies already use server work. Some group or page-only features still need the browser.

Instructions that require the browser may prevent a server request or send supported work back to the browser. Notebook writing reports unsupported instructions rather than silently dropping them.

If you reconnect during a reply, let Neconyan check the saved request before sending again. Inspect **Server requests** if the result doesn't appear.

??? info "How long browser replies are held"

    The temporary hold is normally 15 minutes, or up to 24 hours with chat context. Restarting the server loses that temporary hold. Explicit server requests use saved jobs instead.
