---
title: Start with macros
guide: miso
quote: 'Start with a name. You can make the complicated bits later, when you actually need them.'
---

# Start with macros

A macro is a short placeholder that Neconyan replaces with text. For example, this greeting uses the current persona and character names:

```text
Hello, {{user}}. I'm {{char}}.
```

If your persona is Alex and the character is Miso, it becomes:

```text
Hello, Alex. I'm Miso.
```

You can use macros in fields that prepare prompts, such as character descriptions, greetings, preset prompts and lorebook entries. The field decides when the text is processed. Pasting a macro into an ordinary notebook note does not automatically run it.

## Try one

1. Open a test character with a saved Roleplay chat.
2. Add the greeting above to its first message.
3. Start a new chat with that character.
4. Check that both names appear correctly.

Changing a card’s greeting affects new chats; it does not rewrite a greeting already saved in a transcript.

## Find what you need

| I want to… | Read |
| --- | --- |
| Insert a name or character detail | [Names and character cards](characters.md) |
| Read a message or a token limit | [Messages and chat settings](chat.md) |
| Control spacing or choose text at random | [Spacing and choices](basics.md) |
| Remember a value | [Variables](variables.md) |
| Include text only when a condition is met | [Conditions](conditions.md) |
| Change the case or length of text | [Text](text.md) |
| Work with several items | [Lists and JSON](lists.md) |
| Calculate a number | [Maths](maths.md) |
| Use a date or time | [Dates and times](dates.md) |
| Keep a random choice stable | [Saved choices and counters](saved-values.md) |
| Read lorebook content | [Lorebooks](lorebooks.md) |
| Use the right pronouns | [Pronouns](pronouns.md) |
| Build a model’s prompt format | [Prompt formatting](prompts.md) |
| Use a placeholder in an Agent or script | [Place-specific placeholders](placeholders.md) |
| Save a reusable template | [Make your own macros](custom.md) |

For a complete example, start with [ready-to-use examples](recipes.md). For punctuation and nested macros, read [how to write them](syntax.md).

## Core macros and Macro Enhanced

Simple names such as `{{user}}` and `{{char}}` are built in. Many of the text, maths, pronoun and saved-choice tools come from **Macro Enhanced**, an included extension. Ordinary Roleplay replies can use them; a few kinds of reply build their prompts on the server and can't. See [below](#macro-enhanced-in-roleplay-prompts).

Open **Fine-tuning → Macro Enhanced** in the sidebar. It opens a full page with five tabs:

| Tab | What it's for |
| --- | --- |
| **Playground** | Try a macro and see what it expands to, without asking a model for a reply |
| **Reference** | Search what your installed version supports, with examples to copy or try |
| **My macros** | Make reusable text with named arguments, saved for everywhere, this browser, a character or one chat |
| **This chat** | Check saved macro values, chat variables and pronoun overrides for the open chat |
| **Setup** | Saved pronouns for personas and characters, and two switches for imported syntax |

If its notice asks you to enable experimental macro support, follow the named setting in **User Settings**, then return.

## Macro Enhanced in Roleplay prompts

Ordinary Roleplay replies build their prompts in the browser. That covers new replies, swipes, regenerations, **Continue**, group turns, **Guided Response** and **Guided Swipe**, so the 102 Macro Enhanced macros in this reference, and macros you make yourself, work in them.

A few kinds of reply still build their prompts on the server, where only core macros run:

- Conversation replies, including assistants
- Roleplay replies that use a selected Notebook context
- Protected **Guided** corrections and **Deep Swipe** replacements
- Background requests

If one of those prompts uses a Macro Enhanced macro, for example in a character description, preset prompt, lorebook entry or earlier message, the reply stops before anything is sent to the model:

```text
The {{name}} macro is browser-only in Macro Enhanced and cannot run in a server prompt. Remove it or use a supported core macro.
```

Macro Enhanced's settings for working out comparisons in conditions and fixing imported syntax are refused in the same way when a server prompt relies on them.

In server prompts, core macros such as `{{user}}`, `{{char}}`, `{{getvar}}` and `{{setvar}}` still work. Local variable writes are saved together with the accepted reply; a failed request doesn't save them. Global variables can be read, but writing one is refused. Lorebook scanning can read variables but not change them, so put a write in a preset prompt or a message instead. See [Variables](variables.md#in-roleplay-prompts).

The Macro Enhanced page shows **Most macros here are browser-only.** Its **Server prompts and saved variables** help gives the full explanation.

!!! taro "Taro"
    If a card leans on Macro Enhanced, keep to ordinary Roleplay replies with it. A Deep Swipe or a reply with a selected Notebook context will stop with the error above.

## What this reference covers

These pages cover **all 201 primary macros registered by the reviewed Neconyan build**, including **102 from Macro Enhanced**, plus their registered alternative names. Each entry has an example; open **Arguments and other names** for input details and aliases.

The reference was checked against the development version dated **7 October 2026**. Older releases, disabled tools and other extensions can change what is available. Macros you create yourself have names and behaviour chosen by you, so the [custom macro guide](custom.md) explains those separately.

!!! taro "Taro"
    If a macro stays visible as braces, check its spelling, the field you put it in and whether its included tool is active. Paying for another model reply will not fix a missing macro.
