---
title: Characters and personas
guide: nori
quote: "A character is easier to write when they want something specific. 'Mysterious' is a mood. Hiding a stolen wedding ring is a problem."
---

# Characters and personas

A **character card** describes who the model plays. A **persona** describes who you are in the conversation. Keeping those roles clear helps prevent the model from assigning your character's traits to someone else.

## Create a useful card

For a private workspace where you can draft, ask for help and review changes before saving a card, open [Catelier](../helpers/catelier.md). The ordinary character editor still works for quick edits.

Open **Characters**, create a character and fill in the fields you actually need. Give the character a name, a recognisable voice, a motive and a starting situation. Use the first message to demonstrate the kind of interaction you want.

A practical starting set is:

- **Identity:** who the character is and what they do.
- **Behaviour:** how they respond under pressure, affection or disagreement.
- **Relationship:** what they know about your persona at the start.
- **Situation:** where the scene begins and what is happening.
- **Voice:** a few concrete examples of how they speak.

Put each instruction where it belongs. Duplicating it across fields uses context space and can make future edits inconsistent.

The editor uses **Basics**, **Definition**, **Greetings** and **Advanced** tabs. Creator's Notes are on Basics, and the favourite star sits beside the name. Field token counts show how much text those fields contain; they aren't the size of the complete model request.

## What each card field does {#card-fields}

Each field below is sent to the model in its own place in the request. In Chat Completion presets, **Presets → Prompts** shows where. The matching [macro](../macros/index.md) lets you place a field yourself.

### Description {#description}

**Definition → Description** holds who the character is: appearance, history, abilities, relationships and the way they think. It's sent with every reply, so keep it to lasting facts. Macro: `{{description}}`.

### Personality summary {#personality}

**Definition → Personality summary** is a short summary of temperament, such as 'dry, loyal, slow to trust'. Many cards leave it empty and put personality in the description instead; use one place, not both. Macro: `{{personality}}`.

### Scenario {#scenario}

**Definition → Scenario** describes the circumstances of the conversation: where it happens, what's going on and how the character relates to you at the start. Update it, or start a new chat, when the situation changes for good. Macro: `{{scenario}}`.

### Examples of dialogue {#dialogue-examples}

**Definition → Examples of dialogue** shows the model how the character writes. Start each example on its own line with `<START>`, then write a short exchange:

```text
<START>
{{user}}: Are you coming to the market?
{{char}}: Only if you're carrying the bags. I carried them last week. And the week before.
```

Neconyan adds a missing `<START>` at the very beginning. **Settings → Chat & Writing → Chat & messages → Prompts → Example messages** decides whether examples are sent:

- **Gradual push-out** includes them only while there's room, so they drop out as the chat grows.
- **Always include examples** keeps them in every request.
- **Never include examples** leaves them out.

A few varied examples teach voice better than many similar ones. Examples are also copied faithfully, so don't include facts that shouldn't repeat.

### First message {#first-message}

**Greetings → First message** is the character's opening message in every new chat. It sets the scene, length and style the model will tend to copy, so write it the way you want replies to read.

**Alternate Greetings** offers other openings. They appear as swipes on the first message of a new chat; group members can use them to start the conversation.

## Token counts {#token-counts}

The editor header shows the card's size as **Tokens** and **Permanent**. A token is a piece of text, often part of a word, that models count.

- **Permanent** counts the name, **Description**, **Personality summary**, **Scenario** and **Character's Note**. These are sent with every reply.
- The total also counts **Main Prompt**, **Post-History Instructions**, **Examples of dialogue** and **First message**, which may be dropped or sent only at the start.

A warning sign appears when the total is more than half the connection's context size. A large card leaves less room for chat history, so the model forgets earlier messages sooner. The counts are estimates and don't include presets, lorebooks or the chat itself.

## Keep changing facts out of the permanent description

### Switchable traits with Purrks

**Purrks** are small pieces of character instruction you can turn on separately: a mood, a trait or a scene direction. Open **Character Purrks** in the chat tools, or **Prompts** in Catelier.

Choose **Always active**, **Manual switch**, **Keyword trigger** or **Scene AI director**. Check the placement too: character description, system prompt, after chat history or a chosen depth. System and after-history placements follow the **Prefer character prompt** settings.

**Extract from card** finds supported traits without a model request and adds them switched off. **Generate Purrks** asks a model, so it can cost credits. The import setting **Create switchable Purrks on import** also starts extracted traits off. Existing Orb fragments are converted regardless of that switch.

The Purrks travel with the card; their current chat switches belong to the chat. Keep long-term facts in the description and use Purrks for details you want to control separately.

A card works well for stable identity. Keep changing details, such as a current injury, in the chat or a suitable [writing tool](../helpers/index.md).

Use [lorebooks](lorebooks.md) for world information that should enter context selectively. Use [Notebooks](../helpers/notebooks.md) for material you want to organise before deciding whether a model should see it.

## Set up your persona

Open **Persona** to choose or edit your name, avatar and description. Write what the model needs to know about your role, rather than assuming your account name is a complete character description.

Check the active persona when a conversation seems wrong. Conversation histories are persona-specific, and persona information can also influence prompts in Roleplay.

Each persona can keep its own expression set, separate from the character's set. See [Included tools](../helpers/tools.md#separate-expression-sets-for-a-shared-card) for the setup and background classification.

## Organise tags and folders {#tag-management}

Open **Manage tags** (the gear button in the tag filter bar on **Characters**) to open **Tag Management**. It uses the tags already on your cards, shows a live summary of tags, folders and notes at the top, and needs no model request.

- **Tags & Folders**: search tag names and notes, or type `c:` followed by a character or group name (such as `c:Narrator`) to find tags assigned to them; a leading `-` excludes a term and commas mean either. Filter by folder state, **Unused** or **With notes**, and sort manually (drag the grip) or by name or usage count. Create a tag with **No folder**, **Open folder** (shows its characters in the main library even when the folder isn't selected) or **Closed folder** (hides its characters from the main library until you open the folder). Each tag row lets you edit its name, folder type, card visibility, colours, tag note and assigned characters or groups. Under **Folder and bulk tools**, tick **Group library by folder tags** to use folders in the library, **Merge tags** to fold selected tags and their notes into a kept tag, or **Delete tags** to remove several at once.
- **Characters & Groups**: search cards by name, `t:tag`, `f:folder`, `a:text` (searches the whole card: name, description, personality, scenario, first message, creator's notes, organiser note and tags), `n:note` (organiser note) or `-term`, with quotes keeping a phrase together and commas meaning either. Filter by type, tagged or untagged, folder state, notes or **Favourites**. Each row lets you add or remove tags, write an organiser **Notes** entry, or **Open** the card. Use **Select shown** or tick individual rows, then open **Bulk assign tags** to **Assign tags** or **Remove tags** across the selection at once.

At the top of **Tag Management**, **Prune** removes unused tags plus references and organiser notes left behind by deleted characters or groups, **Backup** downloads a JSON file of your tags, assignments and notes, and **Restore** imports a tag backup or notes file (asking whether to **Overwrite** or **Keep Existing** when items overlap). After a delete, merge or prune, the **Undo** banner at the top of the window restores the previous state.

## Move and copy a card

Characters' **Import** action accepts supported card files, including PNG files with embedded card data. Use **Duplicate Character** when you want a separate version to experiment with.

For chats from another installation, see [Import as new instance](../start/imports.md#bring-chats-from-another-installation). That explicit option creates a separate character instance and chat history rather than attaching foreign history to an existing identity.

**Export and Download** offers PNG or JSON. A card export carries character information; it isn't a complete archive of chats, galleries, connection secrets or settings. Use [the appropriate backup](../help/backups.md) for those.

!!! taro "Taro"
    A portrait is an image. A card is data. Sometimes one PNG contains both. If an import gives you only a picture, inspect the file before accusing the character of amnesia.

## Check the result in a short chat

Ask a question that tests the character's voice, then put them in a small situation that tests their priorities. If their behaviour is wrong, revise the conflicting or vague instruction. A single good reply isn't proof that every field is working.

For help drafting the card, ask [Scratchpad](../helpers/scratchpad.md) for a proposal and review the exact change before saving it.
