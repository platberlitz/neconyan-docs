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

Simple names such as `{{user}}` and `{{char}}` are built in. Many of the text, maths, pronoun and saved-choice tools come from **Macro Enhanced**, an included extension.

Open **Included tools → Macro Enhanced → Settings**. If its notice asks you to enable experimental macro support, follow the named setting in **User Settings**, then return. The **Reference** in Macro Enhanced shows what your installed version currently supports. The **Macro Workbench** provides a Playground for checking expansions without asking a model for a reply.

## What this reference covers

These pages cover **all 201 primary macros registered by the reviewed Neconyan build**, including **102 from Macro Enhanced**, plus their registered alternative names. Each entry has an example; open **Arguments and other names** for input details and aliases.

The reference was checked against the development version dated **7 October 2026**. Older releases, disabled tools and other extensions can change what is available. Macros you create yourself have names and behaviour chosen by you, so the [custom macro guide](custom.md) explains those separately.

!!! taro "Taro"
    If a macro stays visible as braces, check its spelling, the field you put it in and whether its included tool is active. Paying for another model reply will not fix a missing macro.
