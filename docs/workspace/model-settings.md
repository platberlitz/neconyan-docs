---
title: Model and prompt settings
guide: taro
quote: "Change one setting, send one test message, then decide. Changing nine at once is how you end up blaming the moon."
---

# Model and prompt settings

These controls change how a request is built and how the model is asked to write. None of them are needed for a first chat. Start with the connection's defaults, change one thing at a time and judge it from a short test reply.

| What you want to change | Where it lives |
| --- | --- |
| Randomness, repetition and other sampler values | **Fine-tuning → Sampling** |
| How much the model thinks before replying | **Presets → Advanced & Reasoning → Reasoning Effort**, or the brain button beside the message box |
| How messages are merged before sending | **Connections → Prompt Post-Processing** |
| Templates, system prompts, stop strings, token counting and Structured Prefill | **Fine-tuning → Formatting** |
| Tools that extensions can let the model call | **Presets → Advanced & Reasoning → Enable function calling** |

**Context Size** and **Max Response Length** stay on **Presets**. For Chat Completion they're in the **Token Budget** drawer; for Text Completion they're near the top of the page as **Context (tokens)** and **Response (tokens)**. [Understand the limits](../start/connections.md#understand-the-limits) explains how the two relate.

## Sampling {#sampling}

Sampling settings decide how the model picks each next word from the options it considers likely. **Fine-tuning → Sampling** shows the controls for the active connection under **Sampling Backend**, labelled **Chat Completions** or **Text Completions**.

On Chat Completion, a control only appears when the selected provider and model accept it. If the model accepts none, the page says it uses fixed sampling and the provider chooses its own values. Text Completion offers many more controls, because local backends usually accept them.

The settings people change most:

| Setting | What it does |
| --- | --- |
| **Temperature** | Higher values make less likely words more probable, so replies vary more and can wander. Lower values make replies steadier and more repetitive. |
| **Top P** | Keeps only the most likely words whose chances add up to this share. Lower values narrow the choice. |
| **Top K** | Keeps only this many of the most likely words. 0 switches it off. |
| **Min P** | Drops words much less likely than the top choice. It trims nonsense while leaving variety. |
| **Repetition Penalty** | Makes recently used words less likely. Too high and the model avoids words it actually needs. |
| **Frequency Penalty** and **Presence Penalty** | Discourage words the reply has already used often, or at all. |
| **Seed** | The same seed with the same request can repeat a result. -1 picks a new one each time. |

**Neutralize Samplers** resets the sampler values to settings that leave the model's own choices unchanged. It's a good starting point when replies have become strange and you don't know which value did it.

Sampler values are saved with the preset. Switching presets or connection profiles can change them.

## Reasoning effort {#reasoning-effort}

Some Chat Completion models can think before writing their reply. **Reasoning Effort** asks for more or less of that thinking: **None**, **Minimum**, **Low**, **Medium**, **High**, **Extra High** or **Maximum**. More effort usually means a slower reply and more billed tokens. It doesn't guarantee a better one.

Set it in **Presets → Advanced & Reasoning**, or press the brain button beside the message box and pick a short label such as **Low** or **Med**. Both change the same setting.

Across **NanoGPT**, **OpenRouter** and supported native connections (**OpenAI**, **Google AI Studio** on `v1beta`, **Google Vertex AI**, **DeepSeek**, **Moonshot**, **Z.AI**, **MiniMax**, **MistralAI**, **Groq**, **AIMLAPI** and **Fireworks**), Neconyan filters the menu and the composer picker to the effort levels declared or documented for the selected model:

- If your saved choice isn't supported by the current model, the control warns you and lists the valid choices so you can pick one before sending.
- When an OpenRouter model doesn't expose an effort setting, the **Reasoning Effort** selector is disabled with a note that your saved choice is kept for other models, and the brain button beside the message box is hidden.
- When a model requires reasoning, **None** isn't offered.
- On native **DeepSeek**, **None** turns thinking off for **DeepSeek v4 Pro** and **DeepSeek Flash**. **DeepSeek Flash** offers only **None**, **Low**, **High** and **Maximum**; with no effort sent it still thinks, so its reply keeps reasoning room. Through a reverse proxy, **None** isn't sent and DeepSeek's default applies.
- **Claude** and **Gemini 2.5** models turn the level into a thinking budget, a share of **Max Response Length**. A higher response limit therefore allows a longer think. Newer Claude and Gemini 3 models receive the level name instead.
- For unlisted native models or custom proxies where supported levels aren't known, the full list remains available; **Minimum** is sent as `'minimal'` where required, and **None** is only sent where supported.

If a reply fails after changing the level, choose one of the model's supported levels or set it back to **None** where available and test again.

**Request model reasoning** in the same drawer asks the provider to return the thinking so Neconyan can show it. Some providers think without returning anything you can read. **Fine-tuning → Formatting → Reasoning** controls how returned thinking is shown and whether it's added to later prompts.

## Prompt post-processing {#prompt-post-processing}

**Prompt Post-Processing** sits in the Chat Completion section of **Connections**, just above **Connect**. Some providers reject a request unless the messages follow strict rules, such as starting with your message or never sending two messages from the same side in a row. This setting rewrites the request on the server to fit.

| Option | What it changes |
| --- | --- |
| **None** | Sends the messages as built. |
| **Merge consecutive roles** | Joins back-to-back messages from the same side, with speaker names written into the text. |
| **Semi-strict (alternating roles)** | Merges as above and turns any system message after the first into a user message. |
| **Strict (user first, alternating roles)** | Does the same and adds a short opening user message when the chat would otherwise start with the model. |
| **Single user message (no tools)** | Sends the whole request as one user message. |

Most options come in **with tools** and **no tools** versions. The **no tools** versions turn earlier tool results into plain text, and [function tools](#function-tools) stop working while one is selected.

Leave it on **None** unless the provider's error asks for alternating or user-first messages.

## Formatting {#formatting}

**Fine-tuning → Formatting** shapes the request text for Text Completion connections, where Neconyan builds one long prompt instead of a list of messages. It has five standard drawers:

- **Context & cleanup**: the context template, its story string, example separators and clean-up switches such as **Trim Incomplete Sentences**.
- **Instruct template**: the markers that tell a local model where each message starts and ends. Use the template made for the model you're running.
- **System prompt**: instructions placed before the chat, plus **Post-History Instructions** placed after it.
- **Reasoning**: how thinking blocks are recognised, shown and reused.
- **Reply controls**: reply prefixes, [stopping strings](#stopping-strings) and the [tokenizer](#tokenizer).

Below the five drawers is a separate **Structured Prefill** section, not a sixth drawer. It applies to Chat Completion, and [Structured Prefill](#structured-prefill) covers it. With a Chat Completion connection, the page hides the Text Completion-only sections and says so. Cleanup switches, **Reasoning**, **Custom Stopping Strings** and **Structured Prefill** still apply. Chat Completion prompts are edited in **Presets → Prompts** instead.

A wrong instruct template is a common cause of a local model writing your lines, repeating markers or never stopping. Check it before changing samplers.

## Stopping strings {#stopping-strings}

**Formatting → Reply controls → Custom Stopping Strings** ends a reply as soon as the model writes one of the listed strings. Enter them as a list in brackets, each in double quotes:

```json
["\n{{user}}:", "[OOC"]
```

**Replace Macro in Stop Strings**, on by default, turns [macros](../macros/index.md) such as `{{user}}` into their current values first. An entry that isn't valid in that format is ignored.

Use stopping strings when the model keeps writing past its turn, for example by starting a line as you. Keep them specific: a common word in the list will cut replies short.

## Tokenizer {#tokenizer}

A token is a piece of text, often part of a word, that models count instead of characters. **Formatting → Reply controls → Tokenizer** chooses how Neconyan counts them for Text Completion connections. The count decides how much chat history fits in the context and what token counters show. It doesn't change the model or what it receives.

**Best match (recommended)** uses the backend's own counter when it offers one, or picks a counter from the model's name. Choose a specific tokenizer only when you know the model's family and the counts are clearly wrong.

**Token Padding** adds a safety margin to each count, 64 by default, so a request estimated close to the limit still fits.

Chat Completion connections ignore this setting and count with each model's own tokenizer where Neconyan has one.

## Structured Prefill {#structured-prefill}

Structured Prefill turns the last assistant prefill into a reply pattern. Give the model a short opening and rules for the first part of the reply, and it writes the rest. It's for Chat Completion connections, starts switched off and doesn't need an extension. Open **Fine-tuning → Formatting → Structured Prefill**, the last section on that page.

It's useful when a model keeps opening the same way, slips out of the format you asked for, or starts with a canned refusal. It won't fix a weak prompt, and it can't make a provider accept something its safety rules block.

### Try a bundled example first {#structured-prefill-example}

1. Open **Fine-tuning → Formatting → Structured Prefill**.
2. Under **Ready-to-use preset**, choose **Dialogue first** or **Action first**. The five examples fill the controls but don't save a preset or switch the feature on.
3. Review **Starter template** and the controls it filled.
4. Tick **Use Structured Prefill**, send a test reply, then read the status under the controls.

**Dialogue first** opens with a spoken line. **Action first** opens with a short action. **Choose a mood** offers three openings. **Private scene note** writes a short note, hides it and removes it from the saved reply. **Starter model** asks a separate saved connection to write the opening; that adds one model request.

The **Saved prefill preset** list is your own and starts empty. Use **Save preset** under **Prefill presets** to add the current controls under a name. **Import prefill presets** adds its names to this list; importing or choosing a saved preset doesn't turn the feature on.

### Write a small pattern {#structured-prefill-pattern}

A short pattern is easier to debug than a long one. For example:

```text
I feel [[opt:calm|curious]]. [[keep]]
```

The model chooses 'calm' or 'curious', then continues the reply. With **Hide the starter in chat** on, everything before `[[keep]]` is hidden. Without `[[keep]]`, the whole starter is hidden. Hiding alone keeps the text in saved history and later prompts. **Also remove the starter from saved chat** removes the generated prefix from new replies instead; later edits aren't stripped again. Neither option rewrites older replies, and changing presets later doesn't change what an older reply hides.

The pattern starts from the last assistant prefill by default. Tick **Use a separate starter template** and write the opening in **Starter template** when you want to set it here instead.

| Slot | What it allows |
| --- | --- |
| `[[w:2-5]]` or `[[words:2-5]]` | Two to five words. |
| `[[opt:calm,curious]]` or `[[options:calm,curious]]` | One listed choice. |
| `[[re:[A-Z]+]]` or `[[regex:[A-Z]+]]` | A regular expression. Keep it small. |
| `[[free]]` | Free text. Follow it with a literal separator when the end is ambiguous. |
| `[[name]]` | A name from the chat, or a capitalised name when none are supplied. |
| `[[emotion]]` or `[[mood]]` | An emotion word. |
| `[[action]]` and `[[thought]]` | Short word groups. |
| `[[line]]`, `[[line:2]]` or `[[lines:2-4]]` | One line, or a number of lines. |
| `[[num]]`, `[[num:-2-10]]` or `[[number:1-5]]` | An integer or an inclusive range, up to 1,001 possible integers. |
| `[[end]]`, `[[stop]]` or `[[eos]]` | End the reply there. |
| `[[pg]]` | Text from the separate starter model. |
| `[[keep]]` | Where the hidden starter ends and the visible reply begins. |

Unknown slots and invalid ranges stop with an error. **Minimum characters after the starter** rejects very short replies. **Banned phrases (one per line)** takes one phrase per line; entries starting with a letter or digit match at the start of a word, so 'gaze' blocks 'gazed' but not 'stargaze'. The list uses a negative lookahead, which some providers reject. Remove the list or use **Instructions (best effort)** if your provider doesn't support that regex feature.

Leave **Newline marker** at `<NL>` unless a provider returns that text literally.

### Choose an output method {#structured-prefill-output}

**Provider schema** sends a JSON schema, a set of rules for the reply. Neconyan uses the native format for Claude, Gemini (AI Studio and Vertex AI), Cohere and OpenAI Responses, and the compatible schema where an OpenAI-compatible connection supports it. Your provider and model must accept and enforce its text pattern.

**Instructions (best effort)** asks the model to return the same format without a schema parameter. It works on all Chat Completion connections, including connections such as DeepSeek and AI21 that don't offer the required schema format. Following the pattern is up to the model.

Schema support and regex syntax vary by model. Claude rejects lookaheads, and Cohere rejects anchors and lookaheads; use **Instructions (best effort)** for unsupported patterns. A provider that ignores a rule can't be forced to enforce it by this option. Text Completion connections don't use Structured Prefill. Quiet helper requests, tool or web-search calls, image requests and requests with their own schema keep their usual behaviour.

### Check the result {#structured-prefill-result}

The status records the provider, model and output method. A status of **Provider accepted the request. Reply matches the full pattern.** means the provider returned text and Neconyan's complete check passed: the starter, minimum length and banned phrases. It doesn't prove that the provider enforced those rules internally.

A mismatch keeps the reply and reports that it didn't match. Rejected requests, skipped requests, incomplete replies, invalid JSON and checks too costly to finish have separate statuses. Starter-model warnings appear with the result. Saved replies keep their recorded check when you change settings or reopen the chat.

### Continue and saved presets {#structured-prefill-continue}

Neconyan decodes the JSON response as it arrives. The JSON wrapper doesn't appear in chat, and newline markers become real line breaks. A saved reply remembers its own hidden prefix, including after a browser reconnect or a server-generated reply.

**Continue overlap (characters)** repeats the last few characters of the existing reply in the requested pattern, then removes that repetition from the returned text. A mismatched overlap returns an error instead of appending unrelated text. Set it to zero to request only new text. Continue treats the existing reply literally, even when it contains text that looks like a template slot.

If a provider stops with malformed JSON, already decoded reply text is kept with an error. A token-limited response can keep its partial text without a closing JSON wrapper.

Open **Starter model** and choose a saved Chat Completion profile under **Starter connection profile** to use `[[pg]]`. Its own request runs first, with the conversation and optional **Starter instructions**. You can set **Starter token limit**, **Starter timeout (milliseconds)** and **Starter stops (one per line)**. Generated text is inserted literally, so a starter containing `[[keep]]` doesn't become a template command. If that request fails or times out, the main request continues with an empty slot and a recorded warning. **Stop** still cancels the request.

Under **Prefill presets**, use **Save preset**, **Delete preset**, **Export presets** and **Import prefill presets**. Importing adds names to the list and replaces a saved preset with the same name; it doesn't enable the feature. Selecting a saved preset keeps your current on/off choice. The slash commands are `/sp-preset My starter` and `/sp-preset-list`; their longer forms are `/structuredprefill-preset` and `/structuredprefill-preset-list`.

### Refusal steering {#structured-prefill-refusal}

One practical use is refusal steering. If a model keeps opening with the same canned refusal, a locked opening and restricted first choices make that opening much less likely where the provider enforces the schema. **Instructions (best effort)** is only a request. Provider safety blocks still stop the reply, and an off-pattern refusal comes back as a mismatch rather than being rewritten. It isn't a policy bypass, and it can't guarantee a reply.

## Function tools {#function-tools}

A function tool lets the model ask Neconyan to run an action, such as a search or an image request, and read the result before finishing its reply. Extensions add these tools. In **Download Extensions & Assets**, a **Tool** tag marks an extension that adds one.

Turn on **Presets → Advanced & Reasoning → Enable function calling** to make the tools available to Chat Completion models that support them. An icon beside the switch shows whether the current provider accepts tools. **Tool Call Recurse Limit**, 5 by default, caps how many tool calls in a row one reply can make.

Each tool call is another model request and can add usage. Tools are unavailable while [Prompt Post-Processing](#prompt-post-processing) uses a **no tools** option.
