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

Avoid editing an old message while a generation is still relying on it. Stop the current work first and make your intended history clear.

## Chat and writing settings

**Settings → Chat & Writing** separates controls into **Chat & messages**, **Characters**, **Auto-swipe & auto-continue**, **Autocomplete** and **Fine-tuning**. Start with the drawer that matches the behaviour you want to change. Script controls live under Fine-tuning; appearance-only switches live under [Appearance](appearance.md).

For reopening and linking chats, use **Chat & messages → Chat window**. **Reopen your last chat** and **Chat links in address bar** are separate choices, initially off. A chat link refers to a chat on that installation and account; it isn't a public copy of the conversation.

You can also use **Copy chat link** in desktop Recent Chats, or open **Chat link settings** from the phone's chat tools.

## Keep the model informed

- Put stable character traits in the [character card](characters.md).
- Put relevant world facts in [lorebooks](lorebooks.md).
- Use an Author's Note for short guidance about the current scene or style.
- Use [Mewmory](../helpers/mewmory.md) when a long saved history needs structured recall.
- Use [Scratchpad](../helpers/scratchpad.md) for planning you don't want inserted as a story message.

Adding context uses space. More instructions aren't automatically better if they contradict each other or push useful history out of the request.

## When you leave the page

Most server-backed Roleplay work can finish after the browser disconnects. Reopening the chat lets the interface recover accepted work and saved results. The server and provider still need to be available; browser-only model or speech routes can require the page to stay open.

If a reply seems stuck, inspect its status before sending another. [Troubleshooting](../help/troubleshooting.md) explains the difference between slow preparation, a pending provider request and a failed connection.

!!! taro "Taro"
    A tracker displayed under a reply may be an Agent or Companion result. The main model didn't necessarily write it. Check which request you're actually diagnosing.

Prefer a messaging-app rhythm? Try [Conversation](conversation.md). Prefer uninterrupted prose? Try [Story Mode](story-mode.md).
