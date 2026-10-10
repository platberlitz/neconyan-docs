---
title: Scratchpad
guide: nori
quote: "Ask the awkward writing question here. Your characters don't need to hear you discussing whether their entire argument should be deleted."
---

# Scratchpad

Scratchpad is a side conversation with Miso, Taro or Nori. Use it to discuss a scene, check continuity, brainstorm or propose edits without adding that discussion to the main story.

## Open a discussion

Open **Scratchpad** in the workspace, through the chat tools or through **Ask Scratchpad** in Notebooks. On desktop it can sit beside the chat or use the full width. On a phone it uses the screen and provides a way back to the chat or note.

1. Use **Talking with** to select an assistant.
2. Choose **Same connection as chat** or a separate connection profile.
3. Check **Show preview**, then type your question and send it.

Normal Scratchpad use works without a model's special tool-call support.

Quick prompts fill the composer with requests such as Read scene, Plot ideas, Catch up, Continuity check and Lore gaps. Read or edit the draft, then send it.

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

## Sessions and saved results

Scratchpad keeps sessions associated with the current work, with options for new or temporary sessions, searching and export/import. Server-backed replies can continue after the page closes while the server remains available.

Renaming a saved Roleplay chat keeps its Scratchpad sessions, context settings and replies in progress. A different chat that later uses the old name gets its own sessions.

You can save a selection, message or session into a notebook. This copies the discussion text, excluding reasoning and change cards; it doesn't grant ongoing access to that notebook.

See the [full Scratchpad reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/scratchpad.md) for limits, proposal states and detailed context behaviour.
