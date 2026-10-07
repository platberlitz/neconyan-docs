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
2. Use **Browse library** for a bundled starting point, or **Create agent** for your own.
3. Read its purpose and running conditions.
4. Open **Settings** for common controls, or **Edit** for the full configuration.
5. Check its connection and output limit.
6. Enable it and try one short saved chat turn.
7. Inspect the result and activity before making it automatic everywhere.

The global **Agents On/Off** control affects whether configured Agents run. An individual Agent's enabled state is another thing to check.

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

**Run together** allows parallel work, which can reduce waiting but increases simultaneous requests and may hit provider limits. Running one at a time uses the configured order.

A **wait for** relationship makes a helper depend on another helper's result. Use this when the result is required; list order alone doesn't express that dependency. Keep chains short until you've verified each stage.

## History and visibility

Options such as **Keep in history**, recent-message limits and Companion note history decide what later requests can read. Showing or hiding a note in the interface is separate from feeding it back into context.

Use **More tools → Activity & companions** to inspect what ran. Saved setups let you return to a known combination of helpers, but changing a setup doesn't erase the cost or effects of requests already sent.

!!! nori "Nori"
    A 'notice continuity errors' helper and an 'invent a surprise' helper may disagree about a scene. Give each a clear job before asking both to run.

## Troubleshoot a helper

Check its trigger, global and individual switches, selected connection, context, output limit and recent activity. If a main reply is waiting, establish whether the delay is preparation, the provider or a helper that must complete first.

For every editor field and scheduling option, see the [Agent control reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/in-chat-agents-glossary.md). For recalled story events rather than a tracker, see [Mewmory](mewmory.md).
