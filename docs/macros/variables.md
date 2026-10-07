---
title: Variables
guide: taro
quote: 'Check where a variable is saved before choosing how to read it. The name alone will not tell you.'
---

# Variables

A **variable** is a saved value with a name, such as `location` containing `Library`.

## Choose a store

| Store | Where the value belongs | Write and read |
| --- | --- | --- |
| Local | This Roleplay chat | `setvar` and `getvar` |
| Global | Your account, across chats | `setglobalvar` and `getglobalvar` |
| Macro Enhanced chat variables | A separate store in this chat | `setchatvar` and `getchatvar` |

The two chat-only stores are separate. A value written with `setchatvar` will not appear through `getvar`.

```text
{{setvar::location::Library}}
The scene takes place in {{getvar::location}}.
```

The setter produces no text. The second line becomes `The scene takes place in Library.`

## Writes can run more than once

A prompt may be evaluated during preview, preparation or a retry. An increment inside it can therefore run more than once for a single visible reply. Use an explicit action to update a story counter when exact timing matters.

## Short spelling for ordinary variables

With newer macro support enabled, a dot reads a local variable and a dollar sign reads a global variable:

```text
{{.location}}
{{$preferred_style}}
```

Use these prefixes for the operations below. Replace `score` with your variable name.

| Example | Meaning | Output |
| --- | --- | --- |
| `{{.score = 3}}` | Save 3 | Nothing |
| `{{.score += 2}}` | Add 2, or append text for text values | Nothing |
| `{{.score -= 1}}` | Subtract a number | Nothing |
| `{{.score++}}` | Add 1 | New value |
| `{{.score--}}` | Subtract 1 | New value |
| `{{.score ?? 5}}` | Use 5 only if the variable is missing | Existing value or 5 |
| `{{.score ??= 5}}` | Save 5 only if missing | Existing value or 5 |
| `{{.score == 3}}` | Compare as text | true or false |
| `{{.score != 3}}` | Check different text | true or false |
| `{{.score > 3}}` | Compare numbers | true or false |
| `{{.score >= 3}}` | At least 3 | true or false |
| `{{.score < 3}}` | Below 3 | true or false |
| `{{.score <= 3}}` | At most 3 | true or false |

The fallback operators below also replace values that count as false, including 0. Their double pipes are valid *within variable shorthand*:

```text
{{.score || 5}}
{{.score ||= 5}}
```

The first reads a fallback without saving it. The second saves the fallback when needed. Use `??` or `??=` when a saved zero must be kept.

## Named macros

The ordinary local and global macros are core features. The six names containing `chatvar` or `ChatVar` belong to Macro Enhanced. In slash-command scripts, use Macro Enhanced’s `/me-chatvar` commands to work with its separate store; similarly named built-in slash commands can use the ordinary store.

<!-- macro-reference: variables -->
