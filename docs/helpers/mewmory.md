---
title: Mewmory
guide: taro
quote: "A character's memory can be wrong. Keep the source passage so you can check what actually happened."
---

# Mewmory

Mewmory helps a saved Roleplay chat recall earlier events. **Pawspective** adds what individual characters believe about those events, including things they got wrong.

It is separate from Conversation summaries, Companion trackers and Scratchpad. Start with one short chat so you can check what it remembers.

## Set it up for a chat

1. Open a saved Roleplay chat, then **Mewmory**.
2. In **Now → Memory focus and window**, choose what to remember and how much recent chat to keep. **All model settings** opens the detailed connections.
3. Choose a connection for the roles you use, such as **Facts and events** or **Pawspective**. Wait for **Configuration saved**.
4. Turn on **Use Mewmory in this chat**. For earlier messages, choose **Backfill this chat** and watch the progress.

Settings save automatically. If a change is refused, fix the highlighted value or use **Discard unsaved settings**. The last saved configuration keeps working meanwhile.

### Choose a Jev recall model

**Recall decision model** offers Jev presets and a custom model. Jev scores which saved memories belong in a reply; it doesn't write the reply or replace the model that records events.

Choose a saved connection profile, optionally with a model override, or **Manual endpoint & API key** for a separate service. Enter keys in settings, never in chat. Start with the preset's protocol and score threshold. Choosing a preset doesn't supply model access.

### Keep enough recent chat

**Replace older chat with Mewmory context** starts on. Choose a token allowance, the amount of text the model counts, or a number of messages. The message window starts at ten recent messages, removing older ones in groups of five. At fifteen messages, the oldest five leave only once they're remembered.

**Reply immediately** keeps unrecorded older messages when memory is behind. **Wait for memory** records them first; you can stop waiting.

Removing old text from the next request doesn't hide it on screen. **Also hide omitted messages in the saved chat** is a separate choice. In token mode, automatic hiding has its own threshold and starts off.

## Understand the views

| View | Use it to… |
| --- | --- |
| **Now** | See the memories prepared for the next reply |
| **Pawspective** | Check what each character believes |
| **Archive** | Find original passages and recorded events |
| **Recall** | See what was included or left out |
| **Settings** | Manage connections, processing, jobs and exports |

If a reply misses a fact, check **Recall** first. Was the fact included? If it was, the writing model may have ignored it.

**Picked** shows the actual memory or passage before its selection reason, score and source links. **Included passages and memories** also shows neighbouring passages that were added automatically. I keep the wording from that recall, so editing a memory later doesn't change what this view says was sent. Older recalls that didn't save the text say so; use **Preview which memories would be picked** to inspect a fresh selection.

## Source history matters

Check a doubtful memory against its source passage. Correct objective records separately from a character's mistaken belief. Deleted messages and rejected swipes aren't equally current history.

**Link this continuation** deliberately connects an appropriate follow-on chat. Starting an unrelated chat doesn't share everything automatically.

## Processing and waiting

Recording and recalling memories can make model requests. **Backup connections** tries your saved profiles in order when a text role fails; each attempt can add usage. Embeddings, the optional numerical representations used for meaning-based search, don't use those fallbacks. Keyword search works without them.

**Use models running on this computer only** restricts the relevant roles to permitted local addresses. Otherwise, remote providers may receive the material they process.

Background work waits briefly after server startup and can continue while after-reply Agents run. A failed job doesn't count as completed memory. Check the error before repeatedly backfilling. Changing models can mean processing the same history again.

## Avoid duplicate retrieval

If another search tool also adds old passages, check that both aren't sending the same text. Duplicate context leaves less room for the rest of the scene.

## Export and restore

Use Mewmory's export controls for its records. Exports leave out connection keys. Restore checks matching source history; it doesn't make deleted or rejected chat content current again.

See the [full Mewmory reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/mewmory.md) for connection roles, budgets and recovery details.
