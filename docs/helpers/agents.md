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
4. Open **Quick settings** for common controls, or **Edit** for the full configuration.
5. Check its connection and output limit.
6. Enable it and try one short saved chat turn.
7. Inspect the result and activity before making it automatic everywhere.

The global **Agents On/Off** control affects whether configured Agents run. An individual Agent's enabled state is another thing to check.

**Manage agents** holds the list, with All, Pinned, Before reply, After reply and Companions views, search and a category filter. **Connections & defaults** holds the shared settings. On each card, **More actions** contains less frequent actions such as Export and Delete.

The version beside an installed Agent's name describes that saved Agent. **Browse library** shows the available template's version beside its name, so you can compare them before updating.

Quick settings includes the connection, model override, run timing and order. An empty model override uses the connection's model. **Save changes** applies your edits; **Open full editor** saves them before opening the complete editor. For several selected Agents, fields stay unchanged unless you change them. Tick **Set model for selected agents** to apply a shared model override.

## Bundled reply rewriters

These helpers are installed but disabled initially. Enable only the ones you need. Each enabled model-based rewrite adds a request after the main reply, so it can increase waiting and cost.

| Helper | Intended job |
| --- | --- |
| **Continuity Corrector** | Repair contradictions with established scene facts, such as location, injuries, clothing or possessions |
| **Proofreader** | Correct prose and formatting while preserving meaning and tracker blocks; this replaces the older Prose Polisher |
| **Dialogue Humaniser** | Make spoken lines sound natural and fit the exchange |
| **Format Fixer** | Repair formatting without changing the scene |
| **User Agency Guard** | Remove actions, thoughts or decisions invented for the user |
| **Knowledge Guard** | Remove claims a character shouldn't know |
| **Character Authenticity Checker** | Repair out-of-character lines while preserving earned character growth |
| **Friction Keeper** | Correct unearned agreement and preserve believable disagreement, leaving tracker blocks intact |
| **Repetition Breaker** | Reduce repeated phrasing, gestures and beats |
| **Length Trimmer** | Shorten a reply towards its configured **Target length** |
| **NSFW Enhancer** | Make sex scenes explicit and specific, without fading to black or hedging |

These are instructions to a model, not guarantees. Review the result before continuing the scene. They rewrite the new reply, not earlier messages. **Recent messages to read** provides up to 30 earlier messages as read-only context; zero means the helper receives only the reply being processed.

Character Authenticity Checker uses the card, example dialogue, group cards and available Mewmory context. Its instructions put story-earned growth ahead of the original card and distinguish a character's interview opinions from events that happened. It edits the reply, not the saved card.

Continuity Corrector starts with 12 recent messages as context. It can also use active lore, the Author's Note, saved tracker values and prepared Mewmory facts. Its instructions favour established recent events and ask it to leave a consistent reply alone. This is an after-reply rewrite; **Continuity Pins**, below, prepares a short note before the writer answers.

When the **Continuity Companion** is enabled too, the two work together. The Corrector reads the Companion's latest note as a list of things to check, and confirms each one against the chat before changing anything. The Companion is told what the Corrector fixed in the current reply, so its card opens with a line starting **Fixed:** and doesn't report those slips again. With either one switched off, nothing passes between them. With **Run companions at the same time as after-reply agents** on, the Companion starts before the Corrector finishes, so it can't list the fixes.

Knowledge Guard can read the card, persona, active lore, Author's Note and saved Secrets Tracker values. Its `{{secrets-tracker}}` placeholder reads enabled saved tracker templates, including renamed copies, without rerunning the tracker. A fact existing in lore doesn't mean every character knows it. Unchanged bundled copies update to version 2 automatically; customised copies keep your edits and offer **Update**.

If a helper answers with a refusal instead of the text, Neconyan discards it, keeps the original and tells you which helper refused. Refusal wording already in the original reply doesn't count, so a character can still say no in the story. The switch is **Keep the original when an Agent refuses** under **Connections & defaults → Context & notifications**, and it starts on.

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

## Bundled maps and trackers

Two bundled Companions keep a record of where people are. **Position Tracker** and **Visual Map** both arrive disabled. Turn on **Agents On/Off** and the Companion you want, then run a reply; their notes open in the **Companion panel**, not under the reply. Neither changes the reply text.

| Companion | What its note shows |
| --- | --- |
| **Position Tracker** | People grouped by place, with their exact spot, what they are doing and their distance from you: **In scene**, **Nearby**, **Away** or **Unknown**. It also lists recent moves. Up to 10 characters and 6 places. |
| **Visual Map** | An illustrated map with your place at the centre, other places laid out by direction, character pins, a travel trail and a compass. Up to 8 places and 10 characters. |

Each note reads the latest reply first, then up to 10 recent messages, with the character card, persona, active lore and Author's Note available. It starts from the previous map, so someone the story leaves alone keeps their last position. Each Companion is a separate model request; running both adds two requests to a reply unless you [batch compatible Companions](#batch-companions-and-share-notes).

## Instructions or extra requests?

| Behaviour | What happens | Cost implication |
| --- | --- | --- |
| Prompt instructions | Extra text joins the main request | More input tokens, without necessarily adding a separate request |
| Reply processing or rewriting | Supported processing acts on a reply | A model-based rewrite can make another request |
| Companion | A separate model reads its configured context and writes a result | Another request, with its own input and output |

Tokens are the text units a model counts for limits and charging. An Agent's visible prompt count doesn't necessarily include every later Companion request.

## Rerun agents on a reply

When an after-reply rewrite came out wrong, or you've changed an Agent's prompt, open the reply's message menu and press **Rerun agents** (the circular arrow). It only appears while **Agents On** is set and at least one enabled after-reply Agent has a prompt. Companions aren't rerun; they keep their own controls.

The rerun follows **After-reply agents** under **Connections & defaults**: **Run together** starts every Agent on the same reply, and **Run one at a time** passes each result to the next. It starts from the reply as it was before the earlier rewrites, so rewrites are redone rather than stacked, and appended blocks are replaced rather than added twice. Your own edits and **Fix trackers** repairs are kept as the starting point. Activation chance is ignored, because you asked for it.

If an Agent fails or you press **Stop**, the reply stays as it was. If you edit, swipe or leave the reply while the rerun is working, its result is thrown away. The reply's Agent change history keeps the rerun, and its **Undo** button restores the exact text from before it. Each Agent is another model request, so a rerun costs the same as the original run.

## Choose connections deliberately

Use **Connections & defaults** for shared choices. An Agent's own connection can override the Companion default, which can override the general default. If one helper fails while the chat works, inspect that helper's actual selection.

A cheaper or faster model may suit a simple structured tracker. Check its output quality rather than assuming the main writing model is required for every job.

## Repair a tracker

Use **Fix trackers** at the top of Agents, beside **Agents On/Off**. It checks the current chat's eligible inline and Companion trackers. Agents and the relevant trackers must be enabled. You don't need to open **More tools** to reach it.

Some repairs, such as putting recognised fields back in order, need no model request. Others ask a model to repair the tracker and can cost another request. A repair succeeds only when its result also matches the display rules that render the tracker: a block whose tags close but that would still show as raw tags isn't accepted, existing blocks must survive, and a tracker with no clear boundaries is refused rather than guessed at. Invalid, blank or cut-short repairs are rejected, the previous text stays and the failure is reported. The same display-aware checks apply to automatic Companion tracker cleanup. Check the saved result afterwards.

Under **Connections & defaults → Connection profiles**:

- **Fix trackers connection profile** starts at **Each tracker's usual connection**. Choose a separate profile to use its model for repairs without changing ordinary Agent runs.
- Add fallback connections in the order you want them tried. An empty repair fallback list uses the tracker's usual fallbacks.
- **Fix trackers time limit (seconds)** starts at **180** for each connection. A timed-out request moves to the next available fallback. **0** removes the time limit; the largest setting is **3600** seconds.

The button shows progress while repairs run. If every connection fails, check the reported error and connection settings before trying again.

## Order and dependencies

**Connections & defaults → Execution rhythm → After-reply agents** decides how the helpers that work on a finished reply are scheduled. This replaces the earlier **Reply passes** and **Append agents** labels. **Run together**, the starting choice, sends every pass the original reply at once. If two or more rewriters return different versions, one extra request combines them, using the last rewriting helper's connection; it appears as **Combined reply**. If that combined version comes back empty or cut short, the original reply is kept.

**Run one at a time** follows **Order** instead, so each rewriter works on the previous rewrite. It takes longer, but it avoids the combining request.

Manually started after-reply Agents run one at a time regardless of that automatic setting. Later rewrites wait, then read the saved result of the earlier rewrite. Their queue is separate from Companions, so a slow Companion doesn't hold up a manual rewrite. **Stop** ends the active work and clears waiting runs. Once the main reply has finished, Stop keeps that completed reply and saves it without another main request; requests already sent to a provider aren't refunded. Stopping before the main reply finishes follows the ordinary cancellation rules for the reply itself.

A failed after-reply Agent or Companion is retried once, with finished results kept and the main reply not requested again. If it fails again, the reply is saved with the changes that finished and without the failed one, like Stop during Agents; translation and speech still run. [Roleplay](../workspace/roleplay.md#when-an-agent-fails) describes the result you see and when a changed chat can still stop the reply from joining it.

Appended blocks are kept separate from the body being rewritten and restored around the finished reply. Neconyan cleans repeated blocks and copied reply text from supported append results. Check the final output when combining custom helpers.

Parallel work can reduce waiting but increases simultaneous requests and may hit provider limits. The Companion parallel setting is separate from this reply-processing choice.

A **wait for** relationship makes a helper depend on another helper's result. Use this when the result is required; list order alone doesn't express that dependency. Keep chains short until you've verified each stage.

## Batch Companions and share notes

Select at least two Companions in **Manage agents**, then choose **Batch & connect**. **Batch in one request** links them for shared requests when their connections, models and context settings are compatible. They must still be enabled and scheduled to run; incompatible Companions run separately.

**Share latest notes → Share between selected companions** lets them read each other's latest completed notes. It doesn't wait for a new note. For one Companion, **Quick settings → Companion connections** offers **Shares one request with**, **Sends notes to** and **Runs after**. Turn on **Wait for linked companions** when a scheduled dependency must finish first, then **Save changes**.

Agent prompts can also read prepared Mewmory context and group-card fields through [place-specific placeholders](../macros/placeholders.md#agents-and-companions). Those placeholders don't perform a fresh memory search.

## History and visibility

Automatic tracker Companions clean their output down to the tracker block. If a model returns story prose, Neconyan can regenerate once; a broken tracker can also receive one repair pass. These extra requests count towards usage. If repair still produces invalid output, check the reported failure rather than treating the note as a valid tracker.

Companions finish at their own speeds. Each completed note appears as soon as that companion finishes, while the slower ones keep running. A note shown this way carries the **Live reply** label: it's a preview of the reply being written, so its edit, rerun and Send to lorebook actions wait until the note becomes saved history. When a later note updates under a saved reply, your reading position stays where it was instead of jumping to the newest message.

Options such as **Keep in history**, recent-message limits and Companion note history decide what later requests can read. **Where kept notes go**, in the editor's **Companion notes** tab and in **Quick settings**, chooses whether kept notes ride on the **Newest reply**, stay with **Each note's own reply**, or gather in **One labelled block** placed by the helper's Position and Depth. Showing or hiding a note in the interface is separate from feeding it back into context.

The **Director's Commentary** Companion is a sceptical critic rather than a fan. It points out what's ridiculous, such as melodrama, convenient coincidences or lines that are funny by accident, says plainly when a moment falls flat or drags, and gives credit only where it's earned. Copies of Director's Commentary, Continuity Companion and Continuity Corrector whose prompt still matches the earlier built-in wording get the new wording automatically, even if you saved them in the editor. A prompt you rewrote keeps your wording.

Use **More tools → Companion activity** to inspect what ran. Saved setups let you return to a known combination of helpers, but changing a setup doesn't erase the cost or effects of requests already sent.

The **Companion panel** opens from its floating or top bar button, or with **Open Companion panel** in Companion activity. Its **Search companions and notes** box filters by companion name or the text of the latest note, and the status counts the matches. Searching changes only the view: it doesn't run a helper or change its switches.

Companion notes and their panel show the model saved with each result. Agent change history also names the model and, when recorded, its connection profile. These labels describe the completed run, not the model selected now. **Settings → Appearance → Visual Toggles → Short Model Name** controls shortening here too. Older results may not have recorded a model.

!!! nori "Nori"
    A 'notice continuity errors' helper and an 'invent a surprise' helper may disagree about a scene. Give each a clear job before asking both to run.

## Troubleshoot a helper

Check its trigger, global and individual switches, selected connection, context, output limit and recent activity. If a main reply is waiting, establish whether the delay is preparation, the provider or a helper that must complete first.

For every editor field and scheduling option, see the [Agent control reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/in-chat-agents-glossary.md). For recalled story events rather than a tracker, see [Mewmory](mewmory.md).
