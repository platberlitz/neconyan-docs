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
4. Choose an available model from the searchable list, or enter its exact identifier if the connection requires it.
5. If you're using a custom or local endpoint, enter the address in the format that connection expects. Follow its example rather than adding an extra path by habit.
6. Connect, then try a short message with a bundled character.

A model list loading successfully checks only part of the connection. A real reply confirms that the selected model accepts a generation request with your current settings.

!!! miso "Miso"
    Try a tiny request first: 'Give me one cosy scene idea.' Once that works, we can add your lorebook.

## Find a model in a long list

Every chat and text-completion connection with a single model choice shows its models as a list of buttons, with a **Search by name or model ID…** box above it. The list works the same on a phone and a computer.

Type any part of a name or ID to narrow it. Every word you type has to match, and case doesn't matter. **Escape** clears the search, **Enter** chooses the first match when the box has text, and the arrow keys move through the rows. Choosing a row selects that model straight away.

Models marked as favourites move into a **Favourites** group with a star at the right edge. The rest are grouped by family worked out from their IDs, so a new version such as `gemini-3.5-flash` joins **Gemini 3.5** without waiting for an update. OpenRouter and ElectronHub can keep their own vendor groups. NanoGPT labels start with the source, such as **Google/Gemma 4 31B**, because the same model can come from more than one organisation.

The list shows every model the provider returns; scroll to browse or search to narrow it. Searching only changes the view. It saves nothing and makes no model request.

## Save a connection profile

A connection profile remembers a model setup so you can return to it or assign it to a helper. Give it a useful name that includes the provider and purpose, such as 'Local writing' or 'Quick summaries'.

The main chat and background helpers can use different connections. [Scratchpad](../helpers/scratchpad.md), [Agents](../helpers/agents.md) and [Mewmory](../helpers/mewmory.md) each have their own connection choices. Check those separately if the main chat works but a helper fails.

Switching profiles can also change the model and related request settings. Read the active connection before sending a long or expensive request.

## Using a local model

Start the model service before connecting Neconyan. Confirm which API formats it offers, the port it's listening on and which model is loaded. Neconyan is the chat interface; your model service manages the actual model files and hardware.

The endpoint must be reachable **from the machine running the Neconyan server**. If the server is on your computer and you're visiting from a phone, the endpoint is still interpreted from the computer. If Neconyan itself runs on Android, a localhost address refers to the phone.

## Provider notes {#provider-notes}

### OpenAI {#openai}

Choose **Chat Completion**, then `OpenAI` under **Chat Completion Source**. Create a key on the API keys page of your OpenAI platform account; a ChatGPT subscription doesn't include API access or credit. Paste the key into **OpenAI API key**, connect, then pick a model from **Available Models** or type its exact **Model ID**.

**View API Usage Metrics** opens your usage on OpenAI's site. If you're connecting through a proxy, use its **Proxy Password** field; the key box is ignored.

### DreamGen {#dreamgen}

Choose **Text Completion**, then `DreamGen` as the **API Type**. Create an API key in your DreamGen account and paste it into **DreamGen API key**. The **DreamGen Model** list reads `-- Connect to the API --` until the connection succeeds, then lists the models your account can use.

Neconyan doesn't include a DreamGen template. Check DreamGen's documentation for the prompt format its model expects and match it in [Formatting](../workspace/model-settings.md#formatting).

### NovelAI and AI Horde {#novelai-and-ai-horde}

Neconyan no longer offers NovelAI, AI Horde or KoboldAI Classic as reply connections. If saved settings still name one, Neconyan switches to Chat Completion; choose another provider there or under Text Completion. NovelAI is still available for pictures in **Quick Image Gen**.

AI Horde ran requests on computers lent by volunteers, who could see what was sent. Bear that in mind with any shared or community-run service: don't send anything you wouldn't want a stranger to read.

### Where keys are kept {#where-keys-are-kept}

After you connect, the key box empties and shows **Key saved**, or **Missing key** if there's none. Keys are stored by the Neconyan server for your account, not in the page. The key button beside each box opens **Manage API keys**, where you can keep several labelled keys for one provider and choose which is used.

**View hidden API keys** at the bottom of Connections only works if the server owner has allowed it in `config.yaml`. Data imports never bring keys or passwords with them.

## Understand the limits

**Context capacity** is how much input and output the model can handle together. **Reply limit** is the maximum output you ask it to produce. A larger reply limit doesn't enlarge its context capacity and can leave less room for history.

Start with settings the provider supports. Some models reject particular sampling options, image inputs, tools or requested output sizes. If you see a request error, use its exact wording to identify the unsupported setting rather than changing everything at once.

## Costs and privacy

The connected service receives the material included in the request: relevant chat history, character information and any enabled context. Helpers and image generation may make additional requests. Check your provider's pricing and data policy, and use context previews where a feature offers them.

Keys are credentials. Don't paste them into a character card, public screenshot or bug report. For errors, share the provider type, model identifier and redacted error message instead.

Next: [Your first chat](first-chat.md). If a request is failing, see [Something went wrong](../help/troubleshooting.md).
