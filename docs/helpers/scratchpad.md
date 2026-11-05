---
title: Scratchpad
guide: nori
quote: "Ask the awkward writing question here. Your characters don't need to hear you discussing whether their entire argument should be deleted."
---

# Scratchpad

Scratchpad is a side conversation for ideas, continuity checks and proposed edits. Talk with Miso, Taro, Nori or an assistant of your own. The discussion doesn't become part of the story.

=== "Computer"

    <figure class="screenshot" markdown>
    [![Scratchpad on desktop with a demonstration discussion](../assets/images/screenshots/desktop-scratchpad.webp)](../assets/images/screenshots/desktop-scratchpad.webp)
    <figcaption>Discuss the scene without adding the planning to it.</figcaption>
    </figure>

=== "Phone"

    <figure class="screenshot screenshot--phone" markdown>
    [![Scratchpad on a phone with a demonstration discussion](../assets/images/screenshots/phone-scratchpad.webp)](../assets/images/screenshots/phone-scratchpad.webp)
    <figcaption>Back to chat returns to the story.</figcaption>
    </figure>

## Open a discussion

1. Open **Scratchpad** from the workspace or chat tools, or **Ask Scratchpad** from a notebook note.
2. Choose an assistant under **Talking with** and a connection.
3. Check **Show preview** to see what you're sharing, then send your question.

From Home, **General Scratchpad** starts without hidden chat context. Quick prompts such as **Plot ideas** and **Continuity check** fill the message box for you to edit and send. Ordinary discussions don't need special tool-call support from the model.

## Add your own assistant

Open **Assistants → Your assistants**. **Add a new assistant** takes a name and personality, with an optional picture and example dialogue. **Use a character card** makes an independent assistant copy; later card edits don't change it.

**Edit → Save assistant** changes future replies. Deleting an assistant removes it from your library, but old sessions keep the copy they used. You can keep up to 24 assistants.

## Check exactly what it will read

**Show preview** lists the current context. Choose recent or selected messages and optional cards, persona, notes, lore or Author's Note. Shared character cards are included as saved, including their greetings, examples and instructions.

In Roleplay, **Also share → Current preset** adds your preset separately, with prompts marked on or off. It starts off. Conversation doesn't use these presets.

Important boundaries:

- **General** shares no chat, swipes, lore or preset. You can explicitly share a selected card, persona and permitted notes.
- Picked messages stay tied to their original chat. Switching chats doesn't substitute different messages.
- Scratchpad doesn't automatically read Mewmory or Companion notes.
- A linked note isn't automatically shared. Notebook permissions still apply.
- **Ask Scratchpad** from a note shares that note or selection for 30 minutes after confirmation. It doesn't add the story beside it. Tick **Allow proposed edits to the shared text** for suggestions, or use **Stop sharing** to end access.

Context and note permissions are checked again when you send. Removing permission can't withdraw text already sent to a provider.

## Search the web

Choose a provider under **Context → Web search**. Brave, Exa and Tavily need their own keys; NanoGPT uses your saved key. SearXNG needs an instance with JSON output enabled. Custom search addresses must return supported JSON results.

The globe beside the message box turns search on for the next message. Only that message, trimmed to 400 characters, goes to the search service. Your cards, notes and earlier conversation stay out of the search query.

One search serves the whole round table. Replies cite numbered results and keep a folded **Sources** list. If search fails, the assistants can still answer, with a notice. **Stop** cancels an active search too.

## Ask more than one assistant

Turn on **Round table** and select up to three assistants. Each answers with its own connection and reply limit, without seeing the others' answers from that round. Ask a follow-up to compare their ideas.

**Random** asks just one selected assistant per message. Turn it off to ask everyone again. Each answer can be a separate paid request; **Stop all** stops the round and failed participants can be retried individually.

## Review a proposed change

An assistant can propose changes to supported cards, lorebooks, Roleplay messages and notebook notes. Open **Review**, compare **Now** with **Proposed text**, then choose **Save change**. A proposal appearing is not a save.

You can adjust supported non-notebook proposals before saving. Notebook changes save the exact reviewed proposal, so ask for a revision if needed. If the original changed meanwhile, reopen or regenerate the proposal rather than overwriting newer work.

Message edits apply to Roleplay, not Conversation. Return to the original chat to review them. **Use as draft in the chat box** fills the composer without sending.

## Create a character

Ask for a character and review the **New character card** proposal. Adjust its structured draft if needed, then **Save change**. Wait for **Saved** before looking in Characters.

A generated avatar is optional and needs Quick Image Gen configured. For a dedicated workspace with field-by-field revisions, use [Catelier](catelier.md).

## Images and portraits

**Image idea** drafts a request. **Generate image** starts the image request using Quick Image Gen settings; if prompt review is enabled, approve **Generate reviewed image** first.

Generating a picture doesn't replace a portrait. **Review avatar** compares the pictures and **Save change** applies the replacement to the exact shared card. **Previous avatar** opens the preserved original PNG; it isn't one-click undo.

Image work can continue on the server after you close Scratchpad. **Stop image** requests cancellation. Use **Retry saved job** for retained work rather than buying another image when only local saving failed. An unknown provider outcome isn't automatically purchased again.

Download pictures separately. Session exports keep text and image prompts, not pictures, jobs or approvals.

## Edit an assistant's instructions

Use **Context → Assistant prompts → View or edit…**, then **Save prompt**. These instructions belong to Scratchpad, not the ordinary character card. **Reset to default**, followed by **Save prompt**, restores the built-in wording.

Permission rules still apply. Editing an assistant prompt doesn't grant access to private notes.

## Give every assistant the same instructions

Open **Context → Global user instructions → Edit user instructions**. Choose all assistants or selected ones, write your preferences and **Save instructions**.

These account-wide instructions follow you across devices and discussions. A reply already running keeps its original instructions. Save an empty value to turn them off. Session exports don't include them.

## Streaming and reply length

**Context → Stream replies** shows text and available thinking as they arrive. Fold **Thinking** if you only want the answer. Turn streaming off to wait for the complete reply.

**Longest reply (tokens)** limits output, including thinking on models that count it there. New sessions start at 32,000; existing sessions keep their value. Output and thought counts show what the provider reports.

If **Scratchpad is full** appears, export anything you need, then remove old sessions or long replies. The [full reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/scratchpad.md) lists storage limits.

## Sessions and saved results

Open **Sessions** to find, start, export or import a discussion. Roleplay sessions follow the character across chats; groups have their own list. Conversation keeps separate lists for each persona. Note discussions belong to the note, and General has its own account list.

Server-backed replies can continue after closing the page while the server stays available. Switching chats doesn't redirect an edit proposal to another chat.

**Delete old sessions automatically** starts off. Enabling it asks you to confirm the number to keep across all lists. Deletions are permanent; the open session and active replies are protected. Export first if you may want the discussion again.

You can copy a message, selection or session to a notebook. This saves discussion text, leaving out reasoning and change cards, and grants no ongoing notebook access.
