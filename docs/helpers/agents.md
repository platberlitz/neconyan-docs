---
title: Agents and Companions
guide: taro
quote: "Try a helper on one reply before letting it run automatically. A small amount of supervision beats a large amount of regret."
---

# Agents and Companions

An Agent combines instructions with rules for when to run and where its output goes. Some affect the main request; others make separate requests to perform work around a reply.

A **Companion** is a separate helper request, often run after a reply, that produces a note or tracker. Its result doesn't replace the main character's reply.

## Start with one helper

1. Open **Agents** in the workspace.
2. Choose an installed helper, use **Browse library** for another starting point, or **Create agent** for your own.
3. Read its purpose and running conditions.
4. Open **Settings** for common controls, or **Edit** for the full configuration.
5. Check its connection and output limit.
6. Enable it and try one short saved chat turn.
7. Inspect the result and activity before making it automatic everywhere.

The global **Agents On/Off** control affects whether configured Agents run. An individual Agent's enabled state is another thing to check.

## Bundled reply rewriters

These helpers are installed but disabled initially. Enable only the ones you need. Each enabled model-based rewrite adds a request after the main reply, so it can increase waiting and cost.

| Helper | Intended job |
| --- | --- |
| **Proofreader** | Edit prose while preserving its meaning; this replaces the older Prose Polisher |
| **Dialogue Humaniser** | Make spoken lines sound natural and fit the exchange |
| **Format Fixer** | Repair formatting without changing the scene |
| **User Agency Guard** | Remove actions, thoughts or decisions invented for the user |
| **Knowledge Guard** | Remove claims a character shouldn't know |
| **Friction Keeper** | Correct unearned agreement and preserve believable disagreement |
| **Repetition Breaker** | Reduce repeated phrasing, gestures and beats |
| **Length Trimmer** | Shorten a reply towards its configured **Target length** |
| **NSFW Enhancer** | Make sex scenes explicit and specific, without fading to black or hedging |

These are instructions to a model, not guarantees. Review the result before continuing the scene. They rewrite the new reply, not earlier messages. **Recent messages to read** provides read-only context; zero means the helper receives only the reply being processed.

If a helper answers with a refusal instead of the text, Neconyan discards it, keeps the original and tells you which helper refused. Refusal wording already in the original reply doesn't count, so a character can still say no in the story. The switch is **Keep the original when an Agent refuses** under Agents settings → **Context & notifications**, and it starts on.

## Short notes before a reply

Five more bundled helpers are installed disabled. Each makes an extra model request before the main reply and supplies a short prompt note, with a 400-token output limit by default.

| Helper | What its note covers |
| --- | --- |
| **Intent Reader** | What the latest user message is asking for |
| **Continuity Pins** | Up to three immediate facts the next reply should preserve |
| **Repeat Spotter** | Recent phrasing or beats to avoid repeating |
| **Beat Planner** | A concise plan for the next story beat |
| **Pace Setter** | Reply length and where to stop |

They don't rewrite the whole prompt or produce a separate Companion note. Start with one. Intent Reader and Beat Planner can overlap; Repeat Spotter with Repetition Breaker, or Pace Setter with Length Trimmer, may also duplicate work. Deleted bundled helpers can be added again from **Browse library**.

## Instructions or extra requests?

| Behaviour | What happens | Cost implication |
| --- | --- | --- |
| Prompt instructions | Extra text joins the main request | More input tokens, without necessarily adding a separate request |
| Reply processing or rewriting | Supported processing acts on a reply | A model-based rewrite can make another request |
| Companion | A separate model reads its configured context and writes a result | Another request, with its own input and output |

Tokens are the text units a model counts for limits and charging. An Agent's visible prompt count doesn't necessarily include every later Companion request.

## Choose connections deliberately

Use **Connections & defaults** for shared choices. An Agent's own connection can override the Companion default, which can override the general default. If one helper fails while the chat works, inspect that helper's actual selection.

A cheaper or faster model may suit a simple structured tracker. Check its output quality rather than assuming the main writing model is required for every job.

## Order and dependencies

**Execution rhythm → Reply passes** decides how the helpers that work on a finished reply are scheduled. **Run together**, the starting choice, sends every pass the original reply at once. If two or more rewriters return different versions, one extra request combines them, using the last rewriting helper's connection; it appears as **Combined reply**. If that combined version comes back empty or cut short, the original reply is kept.

**Run one at a time** follows **Order** instead, so each rewriter works on the previous rewrite. It takes longer, but it avoids the combining request.

Appended blocks are kept separate from the body being rewritten and restored around the finished reply. Neconyan cleans repeated blocks and copied reply text from supported append results. Check the final output when combining custom helpers.

Parallel work can reduce waiting but increases simultaneous requests and may hit provider limits. The Companion parallel setting is separate from this reply-processing choice.

A **wait for** relationship makes a helper depend on another helper's result. Use this when the result is required; list order alone doesn't express that dependency. Keep chains short until you've verified each stage.

## History and visibility

Automatic tracker Companions clean their output down to the tracker block. If a model returns story prose, Neconyan can regenerate once; a broken tracker can also receive one repair pass. These extra requests count towards usage. If repair still produces invalid output, check the reported failure rather than treating the note as a valid tracker.

Options such as **Keep in history**, recent-message limits and Companion note history decide what later requests can read. **Where kept notes go**, in the Companion part of the editor and in **Agent settings**, chooses whether kept notes ride on the **Newest reply**, stay with **Each note's own reply**, or gather in **One labelled block** placed by the helper's Position and Depth. Showing or hiding a note in the interface is separate from feeding it back into context.

Use **More tools → Activity & companions** to inspect what ran. Saved setups let you return to a known combination of helpers, but changing a setup doesn't erase the cost or effects of requests already sent.

!!! nori "Nori"
    A 'notice continuity errors' helper and an 'invent a surprise' helper may disagree about a scene. Give each a clear job before asking both to run.

## Troubleshoot a helper

Check its trigger, global and individual switches, selected connection, context, output limit and recent activity. If a main reply is waiting, establish whether the delay is preparation, the provider or a helper that must complete first.

For every editor field and scheduling option, see the [Agent control reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/in-chat-agents-glossary.md). For recalled story events rather than a tracker, see [Mewmory](mewmory.md).
