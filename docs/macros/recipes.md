---
title: Ready-to-use examples
guide: miso
quote: 'Pick the example that solves your problem. You can leave the rest for another day.'
---

# Ready-to-use examples

Try these in a test chat. The first uses core macros; the remaining examples use Macro Enhanced too. Macros that save values change the chat when evaluated.

## A greeting that follows the selected names

Put this in a character greeting:

```text
Hello, {{user}}. I'm {{char}}. What brings you here today?
```

## A location with a fallback

Read a saved location, or use a default if it is missing:

```text
Location: {{default::{{getvar::location}}::the village square}}.
```

To set it explicitly:

```text
{{setvar::location::the library}}
```

Save the value once when the scene changes. Keeping the setter in a repeated prompt would reset the location on each evaluation.

## Weather that stays fixed

```text
Weather: {{freeze::scene-weather::{{random::rainy::clear::misty}}}}.
```

The first evaluation chooses the weather. Later evaluations in this chat keep it. Use a new key for an independent scene, or clear the saved value through Macro Enhanced’s unfreeze command.

## A character sentence with matching pronouns

```text
{{Charsub}} {{charpverb::has::have}} {{charposs}} own reasons to stay.
```

For she/her, this reads `She has her own reasons to stay.` Set the character’s pronouns first; see [pronouns](pronouns.md) for defaults and group-chat limits.

## Keep a number in range

```text
Energy: {{clamp::{{getvar::energy}}::0::100}} / 100.
```

This displays a number between 0 and 100. It does not save the limited value back to `energy`.

## A short conditional instruction

```text
{{if::{{eq::{{getvar::weather}}::rain}}}}
Include the sound of rain when it matters to the scene.
{{else}}
Use the established weather.
{{/if}}
```

The condition compares the saved value to the text `rain`. It inserts one branch into the prompt; the model then uses that instruction when writing.

## Find a problem

If the result is empty, check the input value and the selected chat. If braces remain visible, check the spelling, the macro’s required tool and whether the field processes macros. For a wrong result, test the innermost macro by itself, then add the outer layers back one at a time.
