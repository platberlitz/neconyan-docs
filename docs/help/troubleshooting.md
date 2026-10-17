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

If a Guided Generations preview seemed stuck on 'Writing reply…' after you switched tabs, update to 1.3.0. The preview now reconnects when you return and catches up with the server's text.

## A Roleplay reply stops with a macro error

This message means a Roleplay prompt uses a macro that only works in the browser:

```text
The {{name}} macro is browser-only in Macro Enhanced and cannot run in a server prompt. Remove it or use a supported core macro.
```

Roleplay builds its prompts on the server, so the reply stops before anything is sent to the model. Find the named macro in the card, preset, lorebook entry or message and replace it with a core macro, or remove it. See [Macro Enhanced in Roleplay prompts](../macros/index.md#macro-enhanced-in-roleplay-prompts) for what still works.

## The page freezes after a reply in a long chat

Before 1.3.0, a long chat with a lot of Agent history could freeze the page for minutes after each reply, long enough for Android to close the app. Update to 1.3.0, then try the chat again. If it still freezes, collect a report as described below.

## A chat or note seems missing

Confirm the server address and account. An Android installation and a computer installation have separate data unless you've transferred it. In Conversation, also check the persona and branch.

Try [Search everything](../workspace/index.md#search-everything) with a distinctive phrase. It searches saved chats, notes, character definitions and lorebook entries in the current account. A warning that some content couldn't be searched means results are incomplete. Unsaved drafts aren't included.

For Roleplay, check the selected character or group and saved chat history. Chat Archive can help find saved files, including orphaned files no longer linked to an existing card. Temporary chats aren't saved.

For notes, check the notebook, Trash, history and save status. **Saved on this device only** isn't confirmation that another device can retrieve the note from the server.

## A chat import is refused

For a chat from another installation, read [Import as new instance](../start/imports.md#bring-chats-from-another-installation) and explicitly select it when you want a separate character instance. A normal import doesn't automatically bypass origin checks. Keep the source files and read the error before retrying.

If a saved ZIP import asks for its archive again after reinstalling, select the original ZIP. The browser may remember an import whose uploaded source is no longer on the server.

## Chats stopped opening after copying folders

Copying data folders into an installation by hand can break the records Neconyan uses to track saved files, even when the chat text is fine.

1. Open **Settings → System & Device → Import & Restore → Repair transferred data**.
2. Press **Check transferred data** and read the report. Nothing changes yet.
3. Press **Back up and repair**. Neconyan backs up your chats, character cards, groups and tracking records first, then accepts the files on disk.
4. Press **Reload repaired account** before opening or saving chats.

A chat or character card that can't be read, or whose file name ends in a space or a full stop, no longer blocks the whole repair. The report lists it under 'Repair will leave out this file and keep it unchanged on disk:', and everything else is repaired. Rename or fix the file, then check and repair again to include it. A broken group file still blocks the repair, because it affects the whole group list. Leftover import uploads and saved backup downloads are skipped. Any other refusal names the file it couldn't check.

For future transfers, use **Import Folder** or **Import Backup ZIP** instead of copying files into a running installation.

## Image input needs attention

An image input notice means a saved picture can't join new automatic replies yet, usually because its choice needs review or the referenced file changed. Open **Settings → Appearance → Avatar & Chat Styles → Review chat images**, or click the **Review needed before replying** notice itself.

For Roleplay, the review has three views. **Current chat** lists every attachment location in the open chat; choose **Send the image**, **Use a description**, **Show only** or **Remove from message** per image and press **Save choice**. **Choose chats** reviews several saved chats, with **Stop sending images in selected chats** and **Save copies of images stored in selected chats** for a batch. Each chat is saved separately with its own backup, so a chat that fails doesn't undo the ones that already finished, and copy-only changes keep the existing descriptions and choices.

**Change history** holds earlier changes: **Finish this change** completes a prepared change, **Discard unfinished change** drops one whose preparation did not finish, **Download backup** exports the chat as it was before that change, **Undo change** restores it, and **Delete backup** ends undo availability while keeping image files and compatible copies. Undo is refused once the chat has changed since; download the backup instead. A missing original image can't be reconstructed by undo.

Older saved messages may embed images that need a prompt-sized compatible copy first. **Prepare a converted copy** prepares one and shows the result before anything changes; choose a local replacement instead of downloading the original from its website, and note that the download asks for confirmation first because the website may refuse browser access. **Save a copy as it is** saves an embedded image as a compatible copy without converting it, **Use the copy already on this server** points at a matching account file, and **Make this the gallery's chosen image** fixes a gallery reference. The displayed picture normally stays as it is; tick **Also show this copy in the chat instead of the original** in the preview to adopt it, or use **Show the compatible copy in the chat** once a copy exists. **Save choices for selected images** applies the ticked rows, and **Save copies of selected images stored in the chat** prepares copies for several embedded images at once. Opening the review and scanning a chat doesn't contact external image websites.

Limits: a replacement you choose can be up to 16 MiB, and a prepared copy is a still PNG, JPEG or WebP of at most 1 MiB and 2048 pixels per side. Changes apply to at most 128 images at once; review larger chats in smaller groups.

## A setting or panel looks broken

Try a known bundled theme and disable the specific custom CSS or extension you most recently changed. Reload, then repeat the action that failed. If only one third-party extension triggers the issue, record its version and report it to its author with the Neconyan version.

On a phone, mention the device, browser and whether you're using a Home Screen window or an ordinary tab. Keyboard-open problems need that detail.

## A helper works differently from the chat

Check the helper's own connection and context preview. Scratchpad, Companions, Mewmory, image generation, speech and translation can each have separate configuration. A successful main reply doesn't establish that those configurations work.

If a lore fact is ignored, inspect World Info Lab or the outgoing prompt. If a memory is ignored, inspect Mewmory's Recall view. Establish what reached the model before changing the writing instructions.

## Read saved crash reports

If the browser finds an unfinished record from its previous visible page, **Read report** opens the retained details, even if the server is offline or Debugger is disabled. Background closures stay available for manual reading. An ordinary reload doesn't repeat a notice you've already seen. A missing close record alone doesn't prove a crash.

Open **Extensions → Built-in → Debugger → Saved crash reports** to read browser reports without turning on live debugging. Each has Copy and Download actions. Administrators can also read retained server reports; other accounts can't. **Android crash reports** opens the APK's native reader.

I keep these reports on your installation; nothing is uploaded automatically. They record errors and bounded activity measurements, without deliberately collecting chat text, prompts or credentials. An error message or system trace can still contain private text, so read it before sharing. Recent activity shows what was happening, not what caused the failure. Severe memory loss or unavailable storage can prevent a report from being saved. The [crash diagnostics reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/crash-diagnostics.md) explains the limits.

## Collect a useful report

Open **Troubleshooting → Debugger** in the sidebar, reproduce the issue, then use **Diagnostic report** in **Extensions → Built-in → Debugger** to copy or download the report. Read it before sharing. The report omits several sensitive values, but screenshots and surrounding text may still include private information.

Include the app version, device/browser, exact steps, expected result, actual result and error text. Add a screenshot if it explains a layout problem. Remove keys, passwords and private conversation content.

Report reproducible app problems through [Neconyan's issue tracker](https://github.com/platberlitz/Neconyan/issues). For a provider account, payment or service outage, the provider's support is the appropriate contact.
