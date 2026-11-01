---
title: Characters and personas
guide: nori
quote: "A character is easier to write when they want something specific. 'Mysterious' is a mood. Hiding a stolen wedding ring is a problem."
---

# Characters and personas

A **character card** describes who the model plays. A **persona** describes who you are in the conversation. Keeping those roles clear helps prevent the model from assigning your character's traits to someone else.

## Create a useful card

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

A card works well for stable identity. Keep changing details, such as a current injury, in the chat or a suitable [writing tool](../helpers/index.md).

Use [lorebooks](lorebooks.md) for world information that should enter context selectively. Use [Notebooks](../helpers/notebooks.md) for material you want to organise before deciding whether a model should see it.

## Set up your persona

Open **Persona** to choose or edit your name, avatar and description. Write what the model needs to know about your role, rather than assuming your account name is a complete character description.

Check the active persona when a conversation seems wrong. Conversation histories are persona-specific, and persona information can also influence prompts in Roleplay.

Each persona can keep its own expression set, separate from the character's set. See [Included tools](../helpers/tools.md#separate-expression-sets-for-a-shared-card) for the setup and background classification.

## Move and copy a card

Characters' **Import** action accepts supported card files, including PNG files with embedded card data. Use **Duplicate Character** when you want a separate version to experiment with.

For chats from another installation, see [Import as new instance](../start/imports.md#bring-chats-from-another-installation). That explicit option creates a separate character instance and chat history rather than attaching foreign history to an existing identity.

**Export and Download** offers PNG or JSON. A card export carries character information; it isn't a complete archive of chats, galleries, connection secrets or settings. Use [the appropriate backup](../help/backups.md) for those.

!!! taro "Taro"
    A portrait is an image. A card is data. Sometimes one PNG contains both. If an import gives you only a picture, inspect the file before accusing the character of amnesia.

## Check the result in a short chat

Ask a question that tests the character's voice, then put them in a small situation that tests their priorities. If their behaviour is wrong, revise the conflicting or vague instruction. A single good reply isn't proof that every field is working.

For help drafting the card, ask [Scratchpad](../helpers/scratchpad.md) for a proposal and review the exact change before saving it.
