---
title: How to write macros
guide: taro
quote: 'The punctuation matters. Fortunately, most of it is two braces and a pair of colons.'
---

# How to write macros

## A name between braces

A macro starts with two opening braces and ends with two closing braces:

```text
{{char}}
```

## Give it an input

An **argument** is a value you give a macro. Put two colons before each argument:

```text
{{upper::hello}}
```

This produces `HELLO`. A macro with several arguments reads them in order:

```text
{{replace::the red door::red::blue}}
```

This produces `the blue door`.

Optional arguments can be left off the end. To leave an earlier argument empty while supplying a later one, keep its separators:

```text
{{dateadd::::2::days}}
```

The empty starting date means now; the result is two days later. Macro Enhanced is required for these examples.

## Put one macro inside another

The inner result supplies an argument to the outer macro:

```text
{{upper::{{char}}}}
```

With Miso selected, this produces `MISO`.

## Use a block for longer text

A block has an opening macro and a matching closing macro with a slash:

```text
{{if::{{hasvar::location}}}}
The scene takes place in {{getvar::location}}.
{{else}}
Ask where the scene takes place.
{{/if}}
```

Only the chosen branch is evaluated. Match each closing tag to its opening tag, especially when nesting conditions.

Most blocks trim whitespace at their edges. A `#` flag preserves it when the layout needs it:

```text
{{#trim}}  Keep these edge spaces.  {{/trim}}
```

## Leave yourself a comment

```text
{{// This note is removed before the prompt is sent.}}
```

For a longer comment:

```text
{{//}}
Notes about how this prompt works.
These lines are removed together.
{{///}}
```

## Common punctuation mistakes

- Use ordinary straight braces and colons. A rich-text editor can change punctuation while pasting.
- A literal `::` separates arguments. Use a simpler separator in your input text when possible.
- A literal pipe can be interpreted as filter syntax. Use the [or macro](conditions.md#or) for either/or conditions.
- JSON objects end in braces too. For complicated JSON, save it in a variable and pass that variable into the macro.

The parser recognises some proposed flags whose behaviour is not implemented in this version. Do not rely on `!`, `?`, `~` or `>` before a macro name to change its timing or filter its output. The `!` *inside an if condition* is a separate feature that reverses that condition.

## An old preset uses different spelling

You may see angle-bracket names such as `<USER>`, `<CHAR>`, `<BOT>` and `<GROUP>`, or arguments separated by spaces or a single colon. These come from older prompt formats. Keep a backup when updating a preset and test it in the version you use.

Use the double-brace, double-colon examples in this handbook for new work. A supported alias, such as `description` for `charDescription`, appears in the entry’s **Arguments and other names** section.
