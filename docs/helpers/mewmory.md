---
title: Mewmory
guide: taro
quote: "A character's memory can be wrong. Keep the source passage so you can check what actually happened."
---

# Mewmory

Mewmory helps saved Roleplay chats recall earlier events using their source passages. **Pawspective** adds a character's interpretation of that history, including beliefs that may be mistaken.

It is separate from Conversation's summaries, Companion trackers and Scratchpad context. Enabling one doesn't enable the others.

## Set it up for a chat

1. Open a saved Roleplay chat, then **Mewmory** in the workspace.
2. In **Settings**, configure the roles you want to use, such as **Facts and events** or **Pawspective**.
3. Choose saved connection profiles or configure supported endpoints directly.
4. Save and wait for **Configuration saved**.
5. Turn on **Use Mewmory in this chat**.
6. For an existing history, use **Backfill this chat**, then watch the job and coverage status.

Original passages remain useful even without every model-powered role enabled. Optional meaning search uses embeddings, numerical representations that help match related wording. Keyword search works without embeddings.

Remote models are allowed by default. **Only use models on this computer** restricts the relevant configuration to permitted local addresses. Choose this based on where you actually want the processing to run.

## Understand the views

| View | What to inspect |
| --- | --- |
| **Now** | The current cast and memory material prepared for the chat |
| **Pawspective** | Character-specific interpretations and source-backed knowledge |
| **Archive** | Original passages and objective records |
| **Recall** | What was included, rejected or left out by the budget |
| **Settings** | Connections, jobs, coverage, processing and export/restore controls |

Use **Recall** when the model appears to miss a fact. First establish whether that fact was selected and included. Then judge whether the writing model used it correctly.

## Source history matters

Mewmory follows accepted saved revisions. Rejected swipes and later-deleted material shouldn't be treated as equally current truth. Use its source views, corrections, exclusions and pins when a record needs attention.

A Pawspective record can be a character's mistaken interpretation. Keep that distinction when correcting the objective history.

Starting an unrelated chat doesn't silently share all memory. **Link this continuation** is the deliberate way to connect an appropriate continuation. Branches depend on their matching source history.

## Processing and waiting

Extraction and some AI-assisted recall can run in the background. The current reply may use local or already completed selections while newly prepared AI results become available to later replies.

Failed jobs don't count as completed coverage. Check the job error and model configuration before repeatedly backfilling. Changing models or processing settings can require work to run again and incur more charges.

Context limits still apply. Mewmory can refuse a request that would overflow protected input rather than silently remove material you meant to preserve.

!!! miso "Miso"
    Try it on a short history first. Check one remembered event against the original messages, then let it handle the longer story.

## Avoid duplicate retrieval

If you also use another meaning-based search tool, such as Vectorization, check whether both tools add the same passages. Duplicate passages consume context space. Mewmory can search by keywords, meaning or a combination of both; inspect the result to see what was included.

## Export and restore

Use Mewmory's export and restore controls for its records. Exports exclude connection keys. Restoration still checks matching source history; it doesn't revive deleted or rejected chat content as current memory.

See the [full Mewmory reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/mewmory.md) for connection roles, budgets, continuation matching and recovery details.
