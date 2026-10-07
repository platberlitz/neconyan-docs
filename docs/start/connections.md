---
title: Connect a model
guide: taro
quote: "One working connection first. Then we can argue about sampling settings with the appropriate amount of misplaced confidence."
---

# Connect a model

Neconyan sends your conversation to a model and displays the reply. You choose the service, model and credentials through **Connections** in the workspace sidebar.

## Choose the kind of connection

| Connection | What you need | Where the writing runs |
| --- | --- | --- |
| Online provider | An account with API access, any required credit and an API key | The provider's servers |
| Local model service | A running model service and its supported connection address | Your own hardware |
| Compatible custom endpoint | Its API format, address, model name and any required key | Wherever that endpoint is hosted |

An endpoint is the address of a service Neconyan can send requests to. 'OpenAI-compatible' describes an API format; it doesn't mean the service is operated by OpenAI or accepts an OpenAI key.

## Make the first connection

1. Open **Connections**. On a phone, open the workspace navigation first.
2. Select the API type and provider that match the service you're using.
3. Enter its API key when required. Copy the key from that provider's account page, without extra spaces.
4. Choose an available model, or enter its exact identifier if the connection requires it.
5. If you're using a custom or local endpoint, enter the address in the format that connection expects. Follow its example rather than adding an extra path by habit.
6. Connect, then try a short message with a bundled character.

A model list loading successfully checks only part of the connection. A real reply confirms that the selected model accepts a generation request with your current settings.

!!! miso "Miso"
    Try a tiny request first: 'Give me one cosy scene idea.' Once that works, we can add your lorebook.

## Save a connection profile

A connection profile remembers a model setup so you can return to it or assign it to a helper. Give it a useful name that includes the provider and purpose, such as 'Local writing' or 'Quick summaries'.

The main chat and background helpers can use different connections. [Scratchpad](../helpers/scratchpad.md), [Agents](../helpers/agents.md) and [Mewmory](../helpers/mewmory.md) each have their own connection choices. Check those separately if the main chat works but a helper fails.

Switching profiles can also change the model and related request settings. Read the active connection before sending a long or expensive request.

## Using a local model

Start the model service before connecting Neconyan. Confirm which API formats it offers, the port it's listening on and which model is loaded. Neconyan is the chat interface; your model service manages the actual model files and hardware.

The endpoint must be reachable **from the machine running the Neconyan server**. If the server is on your computer and you're visiting from a phone, the endpoint is still interpreted from the computer. If Neconyan itself runs on Android, a localhost address refers to the phone.

## Understand the limits

**Context capacity** is how much input and output the model can handle together. **Reply limit** is the maximum output you ask it to produce. A larger reply limit doesn't enlarge its context capacity and can leave less room for history.

Start with settings the provider supports. Some models reject particular sampling options, image inputs, tools or requested output sizes. If you see a request error, use its exact wording to identify the unsupported setting rather than changing everything at once.

## Costs and privacy

The connected service receives the material included in the request: relevant chat history, character information and any enabled context. Helpers and image generation may make additional requests. Check your provider's pricing and data policy, and use context previews where a feature offers them.

Keys are credentials. Don't paste them into a character card, public screenshot or bug report. For errors, share the provider type, model identifier and redacted error message instead.

Next: [Your first chat](first-chat.md). If a request is failing, see [Something went wrong](../help/troubleshooting.md).
