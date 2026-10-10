---
title: Place-specific placeholders
guide: taro
quote: 'A placeholder can be valid in one editor and have no meaning in another. Check who supplies its value.'
---

# Place-specific placeholders

Some features supply extra values while processing their own templates. These are separate from the 201 generally registered macros. Use them in the named feature.

## Agents and Companions

An Agent run can supply the text it is currently processing under these equivalent names:

```text
{{currentMessage}}
{{lastMessage}}
{{latestMessage}}
{{response}}
{{currentResponse}}
{{latestResponse}}
{{assistantMessage}}
```

For a reply rewrite or a Companion, this is commonly the reply being processed. Other stages can supply a larger context or an empty value. Here, `lastMessage` can replace the ordinary chat macro of the same name.

Other Agent values are:

| Placeholder | Meaning |
| --- | --- |
| `{{assistantName}}` | Name attached to the supplied message, when available |
| `{{agentName}}` | Name of the Agent running |
| `{{generationType}}` | Kind of request, such as normal, swipe or continue |
| `{{full-mewmory}}` | The combined NPC and memory context prepared for the writer, not the whole memory archive |
| `{{mewmory-facts}}` | Prepared character sheets, story records and source passages |
| `{{mewmory-interview}}` | Prepared interviews and subjective character views |
| `{{group-cards}}` | Every group member's description, personality and scenario, in group order, including muted members marked as muted |

The Mewmory values are empty when it is off for the chat and don't start a fresh search. Group cards are empty outside a group. A character's interview opinions aren't automatically established story events. These are Agent-specific values added in 1.2.5; they don't change the generally registered macro catalogue's count.

Keep the Agent’s [run timing](../helpers/agents.md) in mind. A prompt prepared before a reply exists cannot read that future reply.

## Slash-command scripts

A slash-command script can use:

```text
{{pipe}}
{{var::name}}
{{var::name::index}}
```

`pipe` reads the previous command’s output. `var` reads a variable in that script’s scope, with an optional index. These are script values, separate from the ordinary chat and global stores. Script closures can also supply additional local macro names.

## Image caption templates

```text
{{caption}}
```

The caption feature supplies this value while turning an image caption into a message. It is not a general way to caption an image from any prompt field.

## Custom macro arguments

A [custom macro](custom.md) can use the argument names you define, along with positional names:

```text
{{arg1}}
{{arg2}}
```

They exist while that custom template is being expanded. Another person needs the custom definition, its arguments and any referenced variables to reproduce the result.

## Similar-looking syntax

Regex replacement fields can use capture references such as `$1`. Prompt templates can have their own fields, and extensions can add others. Those formats are not interchangeable with a globally registered macro. Use the reference beside the editor you are working in.
