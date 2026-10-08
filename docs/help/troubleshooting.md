---
title: Something went wrong
guide: taro
quote: "Show me the error and tell me what you were trying to do. You don't need to apologise for asking."
---

# Something went wrong

Find the symptom below and start there. Change one relevant thing at a time and keep the original error message.

## The page won't open

Check that the launcher is still running and hasn't stopped with an error. On the computer running Neconyan, open the address printed in the terminal; the default is:

```text
http://127.0.0.1:4433/
```

If another program is using that port, the terminal should report it. Stop the conflicting copy or use a different configured port, then open the matching address.

On a phone, use the **computer's network address**, not localhost. Check that both devices share a network, the server is listening for network connections and the firewall permits access. Follow [the phone guide](../start/phone.md) for authentication and address allow-list settings.

## The page opens but the model won't reply

Open Connections and check the provider, model, key and endpoint. A loaded model list doesn't prove the selected model accepts generation requests.

| Error or symptom | Check first |
| --- | --- |
| Unauthorised, invalid key, 401 | Correct provider, current key and API access |
| Forbidden, 403 | Account permissions, model access or server access rules |
| Rate limited, 429 | Provider limits, available credit and simultaneous helper requests |
| Model not found | Exact model identifier and availability on this endpoint |
| Connection refused or unreachable | Model service running, address and port reachable from the Neconyan server |
| Unsupported parameter or bad request | Requested features and limits supported by that model |
| Context too large | Input size, history, lore, helper context and reserved reply space |

Providers can use error codes differently. The returned message is more useful than the number alone.

## A reply is taking a long time

Look at whether Neconyan is preparing the request, waiting for the provider, receiving output or waiting for a required helper. Focus on the stage that's taking time. For example, changing the writing prompt won't fix a helper waiting for an unavailable connection.

Check [Agent activity](../helpers/agents.md), Mewmory jobs and the selected connection. Try a short request with one character and the minimum relevant helpers to isolate the cause. Before retrying, establish what happened to the previous request.

Streaming displays output as it arrives; it doesn't guarantee that the provider begins immediately. Closing the tab also doesn't cancel work already accepted by the server. Use the explicit Stop control when you want cancellation.

## A chat or note seems missing

Confirm the server address and account. An Android installation and a computer installation have separate data unless you've transferred it. In Conversation, also check the persona and branch.

Try [Search everything](../workspace/index.md#search-everything) with a distinctive phrase. It searches saved chats, notes, character definitions and lorebook entries in the current account. A warning that some content couldn't be searched means results are incomplete. Unsaved drafts aren't included.

For Roleplay, check the selected character or group and saved chat history. Chat Archive can help find saved files, including orphaned files no longer linked to an existing card. Temporary chats aren't saved.

For notes, check the notebook, Trash, history and save status. **Saved on this device only** isn't confirmation that another device can retrieve the note from the server.

## A chat import is refused

For a chat from another installation, read [Import as new instance](../start/imports.md#bring-chats-from-another-installation) and explicitly select it when you want a separate character instance. A normal import doesn't automatically bypass origin checks. Keep the source files and read the error before retrying.

If a saved ZIP import asks for its archive again after reinstalling, select the original ZIP. The browser may remember an import whose uploaded source is no longer on the server.

## A setting or panel looks broken

Try a known bundled theme and disable the specific custom CSS or extension you most recently changed. Reload, then repeat the action that failed. If only one third-party extension triggers the issue, record its version and report it to its author with the Neconyan version.

On a phone, mention the device, browser and whether you're using a Home Screen window or an ordinary tab. Keyboard-open problems need that detail.

## A helper works differently from the chat

Check the helper's own connection and context preview. Scratchpad, Companions, Mewmory, image generation, speech and translation can each have separate configuration. A successful main reply doesn't establish that those configurations work.

If a lore fact is ignored, inspect World Info Lab or the outgoing prompt. If a memory is ignored, inspect Mewmory's Recall view. Establish what reached the model before changing the writing instructions.

## Collect a useful report

Open **Included tools → Debugger → Open**, reproduce the issue, then use **Diagnostic report** to copy or download the report. Read it before sharing. The report omits several sensitive values, but screenshots and surrounding text may still include private information.

Include the app version, device/browser, exact steps, expected result, actual result and error text. Add a screenshot if it explains a layout problem. Remove keys, passwords and private conversation content.

Report reproducible app problems through [Neconyan's issue tracker](https://github.com/platberlitz/Neconyan/issues). For a provider account, payment or service outage, the provider's support is the appropriate contact.
