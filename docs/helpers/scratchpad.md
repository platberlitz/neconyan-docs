---
title: Scratchpad
guide: nori
quote: "Ask the awkward writing question here. Your characters don't need to hear you discussing whether their entire argument should be deleted."
---

# Scratchpad

Scratchpad is a side conversation with an assistant you choose: Miso, Taro, Nori, a copy of a character card or someone you make yourself. Use it to discuss a scene, check continuity, brainstorm or propose edits without adding that discussion to the main story.

Every assistant stays in character while helping. Miso, Taro and Nori keep their own voices, and your own assistants use the personality you give them.

=== "Computer"

    <figure class="screenshot" markdown>
    [![Scratchpad on desktop, open beside a Story Mode chat with a round table of three assistants](../assets/images/screenshots/desktop-scratchpad.webp)](../assets/images/screenshots/desktop-scratchpad.webp)
    <figcaption>A staged round table beside the story. Nothing said here goes into the chat.</figcaption>
    </figure>

=== "Phone"

    <figure class="screenshot screenshot--phone" markdown>
    [![Scratchpad on a phone, with the assistants it is talking with and a reply](../assets/images/screenshots/phone-scratchpad.webp)](../assets/images/screenshots/phone-scratchpad.webp)
    <figcaption>On a phone Scratchpad fills the screen; Back to chat returns to the story.</figcaption>
    </figure>

## Open a discussion

Open **Scratchpad** in the workspace, through the chat tools or through **Ask Scratchpad** in Notebooks. On desktop it can sit beside the chat or use the full width. On a phone it uses the screen and provides a way back to the chat or note.

1. Use **Talking with** to select an assistant.
2. Choose **Same connection as chat** or a separate connection profile.
3. Check **Show preview**, then type your question and send it.

Normal Scratchpad use works without a model's special tool-call support.

Quick prompts fill the composer with requests such as **Read the scene**, **Plot ideas**, **Catch me up**, **Continuity check** and **Lore gaps**. Read or edit the draft, then send it.

Each reply shows its output and thought token counts beside the assistant's name, labelled **Output tokens** and **Thought tokens**. The counts grow while the reply is written and stay on the saved reply. Thought tokens only appear when the provider reports the model's thinking.

## Add your own assistant

Press **Assistants** beside the portraits to open **Your assistants**.

- **Add a new assistant** asks for an **Assistant name** and a **Personality**. **Example dialogue (optional)** and **Choose picture** are optional. Pictures can be PNG, JPEG or WebP, under 16 MB, and are cropped to a square portrait.
- **Use a character card** searches your saved characters. **Add** copies the card's picture, description, personality and example dialogue. It doesn't copy the scenario, greetings, lorebooks or the card's own system instructions. The copy is independent: editing the card later doesn't change the assistant, and editing the assistant doesn't change the card.
- **Use** selects an assistant. In a round table it includes or leaves them out.
- **Edit** changes a saved assistant's name, personality, picture or example dialogue. **Save assistant** applies the changes to future replies across your account. **Delete**, inside **Edit**, removes them from your library after you confirm.

You can save up to 24 assistants. Names keep their first 80 characters, and the personality and example dialogue keep up to 64,000 bytes each, so a very long card is shortened to fit.

Sessions keep their own copy of each assistant they used. A deleted assistant still reads correctly in old sessions and shows **Only in this session** there. Session exports carry those copies, so an imported session keeps its assistants without adding them to your library; use **Edit** to save one.

Your own assistants work everywhere the included three do: round tables, connections, assistant prompts and global instructions. A session-specific prompt still takes priority over personality edits.

## Check exactly what it will read

Use **Show preview** before asking about private or large material. Context controls can include recent or selected chat messages, selected swipes and optional character, persona, Author's Note or lore content.

Selected saved notes follow notebook permissions. Linking to another note doesn't automatically include it. Scratchpad doesn't automatically read Mewmory records or Companion notes.

Story context is rebuilt from the open chat on each send. Saved-note text and permissions are also checked again on the server. The Context list updates when shared notes change during a session. If a note changes while a reply is being prepared, send again using the new version; unavailable, private or expired notes show **Not shared** without their text.

Where notebook AI access is allowed, the preview also lists the notebook's name, access level, permitted actions and readable-note count. That list doesn't include note titles or contents by itself. Removing access can't withdraw material already sent to a model.

A discussion opened from **Ask Scratchpad** in a note is note-specific. It uses the shared note or selection and doesn't silently add the story beside it.

The note is saved before sharing; if autosave is already running, Scratchpad waits for it. The confirmation grants access to the chosen note or selection for 30 minutes without changing permanent notebook permissions. Tick **Allow proposed edits to the shared text** if you want edit suggestions. Use **Stop sharing** under Context to end that temporary access.

## Ask more than one assistant

Round table mode lets you select up to three assistants. **Ask 2** or **Ask 3** sends to the selected assistants, each with its own connection and reply limit.

They answer concurrently, without seeing one another's answers from that round. Ask a follow-up if you want them to compare the ideas after the answers are available.

Each answer can mean a separate paid request. **Stop all** stops the round, and failed participants can be retried separately.

Turn on **Random** beside **Round table** for one reply per message. The send button becomes **Ask 1**, and one of the selected assistants answers at random, with their own personality and connection. **Try again** keeps the assistant who gave the answer you are replacing. Random is saved with the session; turn it off to ask everyone selected again.

Before you send anything, an empty session shows the portraits of every selected assistant.

!!! miso "Miso"
    Give each assistant a different job. A continuity check and a proposed complication will give you more to compare than duplicate requests.

## Review a proposed change

Scratchpad can offer change cards for supported characters, lorebooks, Roleplay messages and notebook notes. Open **Review** and read **Now** against **Proposed text**. **Changes** highlights additions and removals and updates as you edit the proposed text. Nothing is saved merely because a card appeared.

For supported non-notebook proposals, you can adjust the proposed text before **Save change**. Notebook proposals save the exact reviewed proposal; ask for a revised proposal if it needs changing. Scratchpad always requires review for notebook changes.

If the target changed after the proposal was prepared, saving is refused so an old suggestion doesn't overwrite newer work. Reopen or regenerate the proposal against the current content.

Message-edit proposals are available for Roleplay, not Conversation. **Use as draft in the chat box** places text in the composer without sending it.

## Create a character

Ask Scratchpad to create a character, including while discussing a shared notebook note. It returns a **New character card** proposal. Open **Review**, adjust the fields in the JSON draft, the structured text used for the card, then choose **Save change**. Check that the proposal says **Saved** before looking for the new card.

The draft can include the character's name, description, personality, scenario, first message, example dialogue, instructions and alternate greetings. Leave `avatarPrompt` empty for the default picture. An explicitly requested generated avatar needs Quick Image Gen configured and can cost an image request.

Compatible Chat Completion models can use a creation tool. Models without tool calling can still return a change card for you to review and save.

## Edit an assistant's instructions

Open **Context → Assistant prompts**, then **View or edit Miso's prompt**, or the equivalent for Taro or Nori. **Save prompt** applies the complete instructions to that assistant in the current session. New sessions in that chat inherit the choice. To restore the built-in instructions, choose **Reset to default**, then **Save prompt**.

These instructions belong to Scratchpad, not the assistant's ordinary character card. The product-help reference and notebook permission rules are still added automatically; editing the prompt doesn't grant access to private notes.

## Give every assistant the same instructions

For preferences you want everywhere, such as 'answer in British English', open **Context → Global user instructions → Edit user instructions**. Choose **All assistants**, or **Selected assistants** and tick the ones you want. Write your text in **User instructions**, then **Save instructions**.

These instructions belong to your account, not one chat. They are saved on the server, so they follow you across devices. They apply to existing and new sessions, round tables and note discussions. A reply already being written keeps the instructions it started with. Leave the text blank and save to turn them off. Session exports don't include them.

## Streaming and reply length

**Context → Stream replies** is on by default. It shows the reply, and any thinking the model sends, as they arrive. Fold the **Thinking** block if you only want the answer while it updates. Turn the switch off to wait for the finished reply instead. The choice is saved with the session and applies to every assistant in a round table.

**Longest reply (tokens)** starts at 32000 for new sessions, which leaves room for models that count thinking towards their output. Existing sessions keep their saved limit.

Scratchpad saves up to 2 MiB each of answer and thinking, so long replies are no longer cut off early. Each chat's Scratchpad file holds up to 32 MiB. If it fills up, a **Scratchpad is full** message asks you to delete old sessions or long replies before it saves more. With automatic cleanup on, it deletes the oldest sessions to make room instead.

## Sessions and saved results

Scratchpad keeps sessions associated with the current work, with options for new or temporary sessions, searching and export/import. Server-backed replies can continue after the page closes while the server remains available.

**Sessions → Delete old sessions automatically** is one setting for your whole account, and it starts off. **Sessions to keep per chat** can be 1 to 40 and starts at 10. Turning cleanup on, or lowering the number while it is on, asks you to confirm with **Apply to all chats**. Older sessions are deleted for good. The open session, the one that just got a reply and any session with a reply in progress are never deleted. Cleanup runs in other chats the next time their Scratchpad saves. Earlier per-chat cleanup choices aren't carried over, so turn it on once if you used it before.

Renaming a saved Roleplay chat keeps its Scratchpad sessions, context settings and replies in progress. A different chat that later uses the old name gets its own sessions.

You can save a selection, message or session into a notebook. This copies the discussion text, excluding reasoning and change cards; it doesn't grant ongoing access to that notebook.

See the [full Scratchpad reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/scratchpad.md) for limits, proposal states and detailed context behaviour.
