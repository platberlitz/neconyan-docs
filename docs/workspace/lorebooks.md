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

## Inclusion groups {#inclusion-groups}

An inclusion group lets only one of several related entries in at a time. Use it for alternatives that would contradict each other, such as three versions of the weather or a character's moods.

Give each entry the same label in **Inclusion Group**. An entry can belong to several groups; separate the labels with commas. When more than one entry from a group activates in the same request, Neconyan keeps one:

1. Entries still active from **Sticky** win over newly activated ones. Entries waiting out a cooldown or delay are left out.
2. With group scoring on, only the entries that matched the most keywords stay in the running. Turn it on for every book with **Use Group Scoring** in **Global Lorebook activation settings**, or per entry with **Group Scoring**, where **Use global** follows that switch.
3. If an entry from the group was already added earlier in the same request, the others are skipped.
4. An entry with **Prioritize** ticked wins. If several are, the one with the highest **Order** is chosen.
5. Otherwise Neconyan picks at random. **Group Weight**, 100 by default, sets each entry's chance: an entry with 200 is twice as likely as one with 100.

Entries without a group label aren't affected. If an entry you expected is missing, check whether another member of its group won; [World Info Lab](#inspect-activation-with-world-info-lab) shows what activated.

## Search a whole book by meaning

**Entry tools → Vectorize all** marks entries in the selected book for meaning-based retrieval. This needs the **Vectorization** tool enabled and an embeddings connection configured. Embeddings are numerical descriptions of text used to compare relevance.

1. Open the book, then **Entry tools → Vectorize all**.
2. Review the entry counts. The action covers the whole book, including entries hidden by search or on another page. Existing keywords stay intact, and disabled entries stay disabled.
3. Leave **Include constant entries** off to keep those entries always active. Turning it on makes them depend on keyword or meaning-based selection instead.
4. If offered, check **Turn on lorebook retrieval in replies** deliberately: it affects all active lorebooks, not only this book.
5. Confirm, then use **Index active lorebooks** or let a reply build the required index. Inspect the resulting context as you would with keyword activation.

Marking entries doesn't enable a disabled Vectorization tool. If **Search all enabled entries** is already on, it also searches enabled entries that haven't been individually marked.

## Inspect activation with World Info Lab

Press **World Info Lab** in the Lorebooks library or in an open book. You can also use **Characters & Lore → World Info Lab** in the sidebar. Closing the workspace, or pressing ++escape++, returns you to the book you were in. In **Scan**, choose the current chat or pasted text, select the reply action to simulate and use **Run scan**.

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
