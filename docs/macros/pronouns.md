---
title: Pronouns
guide: miso
quote: 'Set the pronouns you want to use, then let the sentence follow them.'
---

# Pronouns

Macro Enhanced provides one set of pronouns for your **persona** and another for the **character**. Set the persona’s pronouns in Persona settings or Macro Enhanced; both edit the same saved choice. Character pronouns belong to the card.

The default is **they/them**. A chat-specific override takes priority over the saved choice. These settings are separate from the three guide preferences on this documentation site.

## A sentence that adapts

```text
{{Sub}} {{pverb::is::are}} ready. Give {{obj}} {{poss}} bag.
```

With she/her, this becomes:

```text
She is ready. Give her her bag.
```

With they/them:

```text
They are ready. Give them their bag.
```

Capitalise the first letter of a pronoun macro to capitalise its result. The character equivalents begin with `char`, such as `Charsub` and `charpverb`.

## Forms at a glance

| Form | Example sentence | She/her | He/him | They/them |
| --- | --- | --- | --- | --- |
| Subject | ___ arrived. | she | he | they |
| Object | I saw ___. | her | him | them |
| Possessive before a noun | ___ bag | her | his | their |
| Standalone possessive | The bag is ___. | hers | his | theirs |
| Reflexive | Did it by ___. | herself | himself | themself |

You can use a preset such as `she/her`, `he/him`, `they/them` or `it/its`, or supply all five forms:

```text
{{setpronouns::xe/xem/xyr/xyrs/xemself}}
```

A custom set can end in `/plural` or `/singular` to choose verb agreement. Clear a chat override with an empty argument:

```text
{{setpronouns::}}
```

In a group, a character-specific context may be unavailable. Character pronouns then fall back to they/them unless a chat override supplies another set. Check the prepared prompt before relying on these macros for several speakers.

<!-- macro-reference: pronouns -->
