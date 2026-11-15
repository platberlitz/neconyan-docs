---
title: Mewmory
guide: taro
quote: "A character's memory can be wrong. Keep the source passage so you can check what actually happened."
---

# Mewmory

Mewmory helps a saved Roleplay chat recall earlier events. **Pawspective** adds what individual characters believe about those events, including things they got wrong.

Mewmory is separate from Conversation summaries, Companion trackers and Scratchpad. Start with one short chat so you can check what it remembers.

!!! info "New in the 1.5.5 candidate"
    The **Story** tab, the Archive tools, the in-chat controls, the estimates and the extra exports below come from the Neconyan 1.5.5 staging candidate at commit **680a05f1**, which I reviewed on 15 November 2026. Version 1.5.5 is not published yet. The current published release is [1.5.4](https://github.com/platberlitz/Neconyan/releases/tag/v1.5.4), where these controls won't appear.

## Set it up for a chat

1. Open a saved Roleplay chat, then **Mewmory**.
2. In **Now → Memory focus and window**, choose what to remember and how much recent chat to keep. **All model settings** opens the detailed connections.
3. Choose a connection for the roles you use, such as **Facts and events** or **Pawspective**. Wait for **Configuration saved**.
4. Turn on **Use Mewmory in this chat**. For earlier messages, open **Settings → Upkeep for this chat**, choose **Update memories for the whole chat** and watch the progress. It shows [an estimate first](#check-the-cost-first).

Settings save automatically. If a change is refused, fix the highlighted value or use **Discard unsaved settings**. The last saved configuration keeps working meanwhile.

### Choose a Jev recall model

**Recall decision model** offers Jev presets and a custom model. Jev scores which saved memories belong in a reply. It doesn't write the reply or replace the model that records events.

Choose a saved connection profile, optionally with a model override, or **Manual endpoint & API key** for a separate service. Enter keys in settings, never in chat. Start with the preset's protocol and score threshold. Choosing a preset doesn't supply model access.

### Keep enough recent chat

**Replace older chat with Mewmory context** starts on. Choose a token allowance, the amount of text the model counts, or a number of messages. The message window starts at ten recent messages, removing older ones in groups of five. At fifteen messages, the oldest five leave only once they're remembered.

**Reply immediately** keeps unrecorded older messages when memory is behind. **Wait for memory** records them first. You can stop waiting.

Removing old text from the next request doesn't hide it on screen. **Also hide omitted messages in the saved chat** is a separate choice. In token mode, automatic hiding has its own threshold and starts off.

## Understand the views

| View | Use it to… |
| --- | --- |
| **Now** | See the memories prepared for the next reply |
| **Story** | Read a recap, open promises and who is connected |
| **Pawspective** | Check what each character believes |
| **Archive** | Find, sort and tidy memories and original passages |
| **Recall** | See what was included or left out |
| **Settings** | Manage connections, processing, jobs and exports |

If a reply misses a fact, check **Recall** first. Was the fact included? If it was, the writing model may have ignored it.

**Picked** shows the actual memory or passage before its selection reason, score and source links. **Included passages and memories** also shows neighbouring passages that were added automatically. I keep the wording from that recall, so editing a memory later doesn't change what this view says was sent. Older recalls that didn't save the text say so. Use **Preview which memories would be picked** to inspect a fresh selection.

## Read the story so far {#story}

Open a saved chat, then **Mewmory → Story**. Everything here is built from memories Mewmory has already saved, so opening the tab makes no model request. If it looks empty or stale, update the chat's memories first.

- **Previously on** lists the most important recent events, oldest first. **See every event** opens the Archive showing events only.
- **Open promises** lists promises and unfinished business. Mewmory reminds the model of one when its cue words come up in the scene. **Mark as kept** closes a promise that was fulfilled. **Set aside** drops one that no longer matters.
- **Who is connected** draws the characters and the links between them, with a plain list of the same information underneath. Press a character to open **Everything about** that character, gathered from Pawspective. **Close** returns to the tab.

**Now** shows the last three events and the number of open promises, with **Open Story**. A wrong event or promise is corrected in the Archive like any other memory.

### Ask Mewmory

Type under **Your question** and press **Ask**, for example to check who promised what. The answer comes only from saved memories and lists the ones it used, so you can check it. It says so when it isn't sure. Each question is one request to the **Facts and events** model and counts towards the [daily token limit](#check-the-cost-first).

### Check for contradictions

**Check for contradictions → Check now** looks for saved memories that disagree. For each pair, mark either side **Only a suspicion** or **Not supported by the story**, or choose **Both are fine**.

Neither tool runs on its own. Both can be wrong when the memories themselves are incomplete. I'd treat the result as a reason to read the sources, not a verdict.

### Share memories with the same character's other chats

Sharing is opt-in for each memory. In **Archive**, tick the memories, then choose **Change ticked memories… → Share with other chats**. Other chats with the same character list them on the Story tab under **From other chats**.

**Bring into this chat** copies one in as your own note in that chat. **Stop sharing** withdraws it. Nothing crosses over until you bring it in, and a memory you already brought in stays if sharing stops later.

## Tidy the Archive {#archive-tools}

Open **Mewmory → Archive** in a saved chat. These tools change how memories are used. They don't touch the chat messages.

| You want to… | Use… |
| --- | --- |
| Change several memories together | Tick them, or **Tick all on this page**, then **Change ticked memories…** |
| Reorder the list | **Sort by**: **Newest in the story first**, **Oldest in the story first**, **Most recently changed** or **Pinned first** |
| Narrow the list | **More filters**: importance, status, a message range, and **Show** for new, pinned, edited, excluded or unused memories |
| Read memories in chat order | **Show as → Timeline by message** |
| Find where a memory came from | **Go to message**, which closes Mewmory and jumps to that message |
| See what an edit changed | **Earlier versions** on a rewritten memory |
| Merge repeats | **Find near-duplicates**, then **Keep this one** |

**Change ticked memories…** applies one change to up to 80 ticked memories: pin or unpin them, stop or resume using them in replies, re-mark their status, or share them with other chats.

The strip above the list counts memories written since you last pressed **Mark all as looked at**, and the ones marked uncertain. Check it for the quickest view of what Mewmory added while you weren't watching.

**Keep this one** folds the other near-duplicates into your choice, adds their sources and people to it, and retires the rest. **Undo last change** on the kept memory brings them back.

## Mewmory in the chat {#in-chat}

With Mewmory on, a reply that drew on saved memory shows a small chip beneath it, such as **Used 4 memories** or **Used 2 earlier passages**. Press it to open Mewmory on that message. The count is saved with the message, and each swipe keeps its own.

A message's **More** menu has **Mewmory for this message**. It opens a **This message** block listing what was remembered from that message and what the reply used, with **Go to message**.

- **Forget this message** stops Mewmory using that message and the memories taken from it. **Remember this message again** puts it back.
- **Keep new messages off the record** is a per-chat switch on the status card, beside **Use Mewmory in this chat**. While it's on, every new message, yours and the replies, carries an **Off the record** chip and Mewmory never reads it. Earlier messages aren't touched. **Put back on the record** clears it for one message.

Both leave the messages in the chat and in later prompts as usual. They only decide what Mewmory records. Simple Mode hides these in-chat controls.

## Source history matters

Check a doubtful memory against its source passage. Correct objective records separately from a character's mistaken belief. Deleted messages and rejected swipes aren't equally current history.

**Link this continuation** deliberately connects an appropriate follow-on chat. Starting an unrelated chat doesn't share everything automatically.

## Processing and waiting

Recording and recalling memories can make model requests. **Backup connections** tries your saved profiles in order when a text role fails. Each attempt can add usage. From the 1.5.5 candidate, a backup also takes over when the first connection answers with an error, not only when it can't be reached. Examples are a refused key, a missing model, a rate limit, a server fault or a time-out. Embeddings, the optional numerical representations used for meaning-based search, don't use those fallbacks. Keyword search works without them.

**Use models running on this computer only** restricts the relevant roles to permitted local addresses. Otherwise, remote providers may receive the material they process.

Background work waits briefly after server startup and can continue while after-reply Agents run. A failed job doesn't count as completed memory. Check the error before pressing **Update memories for the whole chat** again. Changing models can mean processing the same history again.

### Check the cost first {#check-the-cost-first}

**Update memories for the whole chat** and **Review for missed details** no longer start at once. Each shows **Before updating the whole chat** or **Before reviewing for missed details**, with the messages waiting, the number of model requests and the tokens expected. **Start update** or **Start review** begins. **Cancel** leaves everything as it was. The figures are estimates in tokens, not money, and the real total can differ.

To cap background spending, set **Daily token limit for automatic updates** under **Settings → Memory updates**. It starts at 0, which means no limit. Every Mewmory model request is counted per day across all your chats. Once the day's total reaches the limit, automatic updates wait until tomorrow. Buttons you press yourself and the memories picked for a reply still work, so a scene isn't broken halfway. **Upkeep for this chat** shows the day's use and says when the limit has been reached.

The limit counts Mewmory's own requests, including Ask Mewmory. It doesn't count the main reply.

### Find a setting

**Settings** is split into folding sections, with only **Memory updates** open at first. Type in **Search settings** to show just the settings whose name or description matches, and clear the box to see every section again.

Each model role except Embeddings has two optional boxes. **Prefill, optional** starts that role's answer with text you supply, for example `{` when a model keeps wandering off the expected format. **Partial prefill for Kimi K3, optional** is used instead with Kimi K3 and K3.1 Pro models when it isn't blank. Backup connections use the same boxes. Leave both empty unless a role misbehaves.

## Avoid duplicate retrieval

If another search tool also adds old passages, check that both aren't sending the same text. Duplicate context leaves less room for the rest of the scene.

## Export and restore

Open **Settings → Export and restore**. Exports contain the story text and memories, and leave out connection keys.

| Export | What you get |
| --- | --- |
| **Export Mewmory** | This chat's archive, as a file Mewmory can restore |
| **Export as Markdown** | A readable file of this chat's memories grouped by kind, with the message each came from. It's for reading only and can't be restored |
| **Export every chat** | The memory of all your chats in one JSON file. Restoring it in a chat picks out the memories that belong there |

Restore checks for matching source history. It doesn't make deleted or rejected chat content current again.

### Send memories to a lorebook {#send-memories-to-a-lorebook}

**Settings → Send memories to a lorebook** copies this chat's current facts, events and promises into a [lorebook](../workspace/lorebooks.md) you can edit or share. **Lorebook name** starts as 'Mewmory - ' followed by the chat's name. Press **Send memories to this lorebook** when it's right. Sending again updates the same entries instead of adding copies.

Mewmory never reads those entries back, so editing the lorebook doesn't change the memories. Attach the book to a character or chat like any other lorebook if you want it used. If you do, the same facts can reach the model from both Mewmory and the lorebook and take up space twice.

See the [full Mewmory reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/mewmory.md) for connection roles, budgets and recovery details.
