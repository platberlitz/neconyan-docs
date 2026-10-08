---
title: Lorebooks
guide: nori
quote: "Write the bit the scene needs. The ancient kingdom's complete tax code can wait until somebody actually commits tax fraud."
---

# Lorebooks

Lorebooks hold world information that can be added to a model request when relevant. An entry might describe a place, person, custom, object or rule of the setting.

They help keep a large world usable without placing every detail in every prompt. They still use context space when activated, and the model can still misunderstand what it receives.

## Make your first entry

1. Open **Lorebooks** and create or select a book.
2. Add an entry for one clear subject.
3. Give it a recognisable title and write the facts the model should use.
4. Add activation keys, the words or phrases that should make the entry relevant, where the entry uses keyword activation.
5. Save it and associate or enable the book for the intended chat or character.
6. Test it with a message that should activate the entry, then inspect the resulting context.

For example, an entry about 'Glassmarket Station' might use that name and its common nickname as keys. Its content can describe the station's location, purpose and one important constraint. Unrelated history is easier to maintain in another entry.

## Attach additional books to a character

Open the character editor, then choose **Link to Lorebook** from its management menu. The additional-books picker lets you search for and select several lorebooks, including on phones and tablets. Confirm the dialog to save the selection. Reopen it to check the saved choices or clear them.

To find an entry by its title, keywords or saved text across your account, use [Search everything](index.md#search-everything). Finding an entry doesn't activate it in the current chat.

## Why an entry might not appear

The book must be available to the current chat, the entry must be enabled and its activation conditions must be satisfied. Scanning settings determine which recent text is examined. Budget and ordering settings can also prevent an otherwise relevant entry from fitting.

A constant or always-active entry behaves differently from a keyword-triggered one. Use it deliberately for information that truly belongs in every relevant request, because it consumes space repeatedly.

## Inspect activation with World Info Lab

Open **Included tools → World Info Lab → Open**. In **Scan**, choose the current chat or pasted text, select the reply action to simulate and use **Run scan**.

**Trace** explains why entries activated, were skipped or didn't fit. This diagnostic rebuilds context without generating a reply or editing the lorebook. It's more reliable than asking the model whether it remembers an entry by name.

## Publish from a notebook

In [Notebooks](../helpers/notebooks.md), **Use as lore** can publish a note or section to a lorebook entry. A simple association between a note and a book is only organisational; it doesn't send the note to the model.

Publishing creates or updates content, but doesn't automatically attach or enable the book for every chat. Check the book's usage after publishing. If you use automatic updates from saved note edits, remember that lore settings and the source note remain distinct controls.

## Extract from existing writing

**Lorebook Distiller** can propose entries from a saved chat. Choose the source, connection and destination, then review the saved proposals. Only selected entries are written when you apply them.

Extraction uses a model and can mistake an implication or a character's belief for fact. Compare the proposal with the actual source before adding it to the world.

!!! taro "Taro"
    If two entries disagree, the model has received two disagreeing instructions. Increasing the context limit won't settle the argument.

For recalled events from a long Roleplay history, see [Mewmory](../helpers/mewmory.md). For private planning material, use [Notebooks](../helpers/notebooks.md).
