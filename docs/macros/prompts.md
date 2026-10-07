---
title: Prompt formatting
guide: taro
quote: 'Most people can leave these alone. They are here for the people building or repairing a preset.'
---

# Prompt formatting

These macros read saved prompt text and formatting markers. They are useful when building a preset or an Instruct template, which describes the text markers a model expects around messages.

All names beginning with `instruct` produce empty text when Instruct mode is disabled. The first-message and last-message prefixes fall back to their ordinary prefix when no special value is set.

Author’s Note macros read their named note. Reasoning macros read configured formatting strings; they do not reveal hidden model content. Repeating any of these in a template can duplicate text that another part of the prompt already includes.

<!-- macro-reference: prompts -->
