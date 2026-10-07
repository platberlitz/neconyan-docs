---
title: Make your own macros
guide: nori
quote: 'Give a repeated template a name. You can spend the time saved on the scene instead.'
---

# Make your own macros

Macro Enhanced lets you save a text template as a macro. Arguments let you reuse it with different inputs, and the template can call other macros.

## Make a scene label

1. Open **Included tools → Macro Enhanced → Settings** and find custom macros.
2. Create a macro named `scene_label`.
3. Give it one argument named `place`.
4. Use this template:

    ```text
    Current location: {{place}}.
    ```

5. Save it in the scope you want, then try it in the Workbench Playground:

    ```text
    {{scene_label::Library}}
    ```

The result is:

```text
Current location: Library.
```

The first argument is also available as `arg1`, the second as `arg2`, and so on. An optional argument can have a default value for calls that leave it empty.

## Choose where it belongs

| Scope | Available to |
| --- | --- |
| Global | Your account’s chats |
| Character | The selected character; the definition can travel with the card |
| Chat | This chat |

If the same custom name exists in several scopes, **Chat wins over Character, then Global**. Use a distinctive name so a shared card’s macro is easy to recognise.

Macro Enhanced avoids replacing another tool’s registered macro. Its built-in functions also have `me-` aliases, such as `me-upper`, for resolving name conflicts. Check the Reference to see which name was registered in your installation.

## Test it before using it in a prompt

Try a normal value, an empty value and a value containing spaces. Check the output before sending a paid request.

The Playground uses temporary ordinary variable and saved-value state. Some shorthand operations briefly touch live state before it is restored, so use a disposable test chat for templates that write values or interact with other extensions.

A template that calls itself, directly or through another custom macro, is stopped. Nesting deeper than ten custom expansions is also stopped. Simplify the definition if it reaches that limit.

## Share the definition

When sharing a preset, include its custom macro definitions and say which scope they belong in. List any required included tools and variables. The text `{{scene_label::Library}}` alone does not contain the definition that makes it work.
