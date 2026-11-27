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

### If the address isn't on the allowed host list {#host-not-allowed}

If a **Forbidden** page says Neconyan only opens at addresses on its allowed host list, the server turned away the name you typed. The check stops other websites reaching your server by pointing a name of theirs at it. `localhost`, `127.0.0.1` and your computer's IP address always open.

If you open Neconyan through your own domain, a reverse proxy, a tunnel or a local network name such as a Tailscale MagicDNS name, add that name to your actual **config.yaml** and restart:

```yaml
hostWhitelist:
  hosts:
    - st.example.com
```

The page shows these lines with the name it refused. A leading dot, such as `.example.com`, also covers its subdomains. The file is the one on the **Using config path** line Neconyan prints when it starts. In Docker that line says `./config.yaml`, which is inside the container: the file to edit on your computer is `config.yaml` in the folder you mounted as the config folder (`docker/config/config.yaml` with the bundled `docker-compose.yml`).

If your configuration came from an older version, where host checking was off, the first start after updating switches it on once and keeps the old file, comments included, beside it as **config.yaml.before-host-check**. To keep the check off, set `enabled: false` under `hostWhitelist`. It stays off after that, because the updated file also records the switch as `upgraded: true` under `hostWhitelist`. The copy doesn't have that line, so if you put the copy back and want the check to stay off, add `upgraded: true` under `hostWhitelist` in it, or set `enabled: false` in the updated file instead.

If the `SILLYTAVERN_HOSTWHITELIST_ENABLED` environment variable is set, it decides whether host checking is on, whatever the file says, and the one-time switch waits. Once you remove the variable, the next start switches an old file on as above.

### If Neconyan cannot finish loading {#if-neconyan-cannot-finish-loading}

When startup fails in a way the page can catch, Neconyan shows **Neconyan could not finish loading** with the recorded error, **Retry startup** and **Read report**. **Retry startup** reloads the page and keeps saved browser data. It doesn't clear the cache or start a reload loop. **Read report** opens the saved error even though the app didn't finish starting.

If the same error returns, read the report and check the launcher terminal before clearing site data. Clearing browser storage can remove the report and other saved settings. A failure that stops the page before this panel can run still uses the recovery screen or saved crash report described below.

### If two starts do not finish

When two browser starts in a row don't finish, the next load shows **Neconyan could not finish starting** instead of the app, with the time of the last recorded activity when one exists. The buttons are:

- **Start Neconyan** continues a normal start.
- **Read crash report** opens the saved report before any application work begins.
- **Clear frontend cache and reload** removes cached frontend files, resets the failed-start count and reloads.
- **Start in low-memory mode** saves that choice before starting.

On an iPhone or iPad, a startup crash loop turns low-memory mode on automatically unless you set it off. That setting is saved, so low-memory mode stays on until you change it in Settings. When automatic mode is on, the button reads **Start without low-memory mode**. Any start that finishes loading clears the failed-start count. A clean close or a new tab doesn't inherit another tab's crash loop.

### If the data folder is already owned {#data-root-owned}

Neconyan keeps a small ownership record, the `.neconyan-root-owner` folder inside your **data** folder, so two copies can't write to the same data at once. If the record belongs to a copy that still seems to be running, the terminal stops with `DATA_ROOT_OWNED` and 'The data folder is already owned by a running process.'

In 1.5.5 this could happen on Windows after a few days off, once another program had been given the old server's process number. From 1.5.6, Neconyan checks when that process started. A program that started after the record was written can't be the old server, so the stale record is cleared and the terminal logs **Reclaimed a stale data folder lease**.

If it still happens, close every copy of Neconyan first, including other terminal windows and any second installation that uses the same data folder. With Neconyan closed, deleting the `.neconyan-root-owner` folder inside the data folder clears the stale lock. Then start Neconyan again. Don't delete it while another copy might still be running.

### If a phone app stops at startup

The Android and iPhone apps keep a small ownership record inside their data folder, so two copies can't write to it at once. A run that Android or iOS closed without warning can leave that record behind. Both apps now clear a record left by their own earlier run and log **Reclaimed a stale data folder lease** in `server.log`. Both still refuse when the earlier server may be running or when the record holds something the app never writes.

On Android, the recovery screen names the lock fields that differ. Close Neconyan from the recent apps screen or force stop it in Android settings, then press **Try again**. Include the message in a bug report if it comes back. Save a backup from that screen when it says the lock needs checking. On iPhone, **Try again** and **Share startup log** stay available, and the shared report ends with the last part of the server log.

Read the reason on the screen before pressing either button. [Install on Android](../start/android.md#if-the-app-wont-open) and [Open it on your phone](../start/phone.md#use-the-standalone-iphone-app) cover the screens in full.

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

Check which stage Neconyan is in: preparing the request, waiting for the provider, receiving output or waiting for a required helper. Focus on the stage that's taking time. For example, changing the writing prompt won't fix a helper waiting for an unavailable connection.

Check [Agent activity](../helpers/agents.md), Mewmory jobs and the selected connection. Try a short request with one character and as few helpers as the test needs, to narrow down the cause. Before retrying, find out what happened to the previous request.

Streaming shows output as it arrives. It doesn't guarantee that the provider begins immediately. Closing the tab also doesn't cancel work already accepted by the server. Use the explicit Stop control when you want cancellation.

If a Guided Generations preview seemed stuck on 'Writing reply…' after you switched tabs, update to 1.3.0. The preview now reconnects when you return and catches up with the server's text.

## A reply comes back empty or stops halfway

From Neconyan 1.5.5, an empty Roleplay reply shows **Reply failed** and leaves the chat as it was. A swipe or regenerate puts the previous reply back instead of saving an empty one. An empty reply usually comes from the model or its filters. Try again, check the connection's model and maximum reply length, and look at the service's own status page.

**The AI service stopped sending the reply.** means the service began a reply and then sent nothing for five minutes. That usually points to an overloaded service or a dropped connection, not your prompt. The wait for the first words isn't limited, so a slow local model isn't affected.

If **Agents did not finish** appears instead, your reply was saved and only the helper work is missing. Use the **Rerun agents** button under the warning; see [Agents](../helpers/agents.md#rerun-agents-on-a-reply).

From 1.5.6, **Reply interrupted** offers the same button when the text written so far was saved and there are Agents to run on it.

In 1.5.5, editing your persona or changing Shell Style while a server reply was running could make its after-reply Agents fail and bring up **Agents did not finish**, even though the reply itself was fine. Version 1.5.6 no longer counts those changes as a changed connection.

## You were signed out {#session-expired}

From 1.5.6, when the server uses a login and your session runs out, Neconyan shows a **Session expired** notice. It says: 'Your login session has expired. Copy any unsaved text, then reload this page to sign in again.' The notice stays until you close it, and your page and draft stay where they are. Copy anything you haven't sent, then reload. A refused provider key doesn't trigger this notice, and several failed requests still show it only once.

## A server reply says there is no room

When a server reply, save or import reports that protected Roleplay evidence has no room, it has reached the fixed 16 MiB protected-record capacity, not a disk-space limit. Your chat isn't necessarily damaged.

A reply you stopped releases its reservation once the server records the stop. Retry after it settles. A reply that failed or was interrupted keeps its reservation until its job leaves saved history, because it may still be collected or retried. Each admission reserves about 72 KiB (64 KiB plus an 8 KiB receipt) while it can still be saved.

## A reply stops with a macro error

This message means a prompt built on the server uses a macro that only works in the browser:

```text
The {{name}} macro is browser-only in Macro Enhanced and cannot run in a server prompt. Remove it or use a supported core macro.
```

Ordinary Roleplay replies build their prompts in the browser and can use it. Conversation replies, Deep Swipe replacements, protected Guided corrections and Roleplay replies with a selected Notebook context build theirs on the server, so the reply stops before anything is sent to the model. That includes an ordinary reply when **On the server** is selected under **Settings → Chat & Writing → Chat & messages → Replies → Where replies are written**. To fix it, find the named macro in the card, preset, lorebook entry or message. Replace it with a core macro, or remove it. See [Macro Enhanced in Roleplay prompts](../macros/index.md#macro-enhanced-in-roleplay-prompts) for what still works.

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

A chat or character card that can't be read, or whose file name ends in a space or a full stop, no longer blocks the whole repair. The report lists it under 'Repair will leave out this file and keep it unchanged on disk:'. Everything else is repaired. Rename or fix the file, then check and repair again to include it. A broken group file still blocks the repair, because it affects the whole group list. Leftover import uploads and saved backup downloads are skipped. Any other refusal names the file it couldn't check.

For future transfers, use **Import Folder** or **Import Backup ZIP** instead of copying files into a running installation.

## Image input needs attention

An image input notice means a saved picture can't join new automatic replies yet, usually because its choice needs review or the referenced file changed. Open **Settings → Appearance → Avatar & Chat Styles → Review chat images**, or click the **Review needed before replying** notice itself.

A refused reply built in the browser now shows that notice too, and a nested or group call shows one notice rather than several. Each new Send can still show its own notice. Deep Swipe and Guided Correction don't add a second error toast for the same refusal, and Prompt Manager's background prompt count ignores it instead of raising a hidden error. Opening the review doesn't save the current chat first; it opens the chat that was refused.

For Roleplay, the review has three views:

- **Current chat** lists every attachment location in the open chat. Choose **Send the image**, **Use a description**, **Show only** or **Remove from message** per image and press **Save choice**.
- **Choose chats** reviews several saved chats, with **Stop sending images in selected chats** and **Save copies of images stored in selected chats** for a batch. Each chat is saved separately with its own backup, so a chat that fails doesn't undo the ones that already finished. Copy-only changes keep the existing descriptions and choices.
- **Change history** holds earlier changes.

In **Change history**:

- **Finish this change** completes a prepared change.
- **Discard unfinished change** drops one whose preparation didn't finish.
- **Download backup** exports the chat as it was before that change.
- **Undo change** restores it.
- **Delete backup** ends undo availability while keeping image files and compatible copies.

Undo is refused once the chat has changed since. Download the backup instead. A missing original image can't be reconstructed by undo.

Older saved messages may embed images that need a prompt-sized compatible copy first:

- **Prepare a converted copy** prepares one and shows the result before anything changes. Choose a local replacement instead of downloading the original from its website. The download asks for confirmation first, because the website may refuse browser access.
- **Save a copy as it is** saves an embedded image as a compatible copy without converting it.
- **Use the copy already on this server** points at a matching account file.
- **Make this the gallery's chosen image** fixes a gallery reference.
- **Save choices for selected images** applies the ticked rows.
- **Save copies of selected images stored in the chat** prepares copies for several embedded images at once.

The displayed picture normally stays as it is. To adopt the copy, tick **Also show this copy in the chat instead of the original** in the preview, or use **Show the compatible copy in the chat** once a copy exists. Opening the review and scanning a chat doesn't contact external image websites.

Limits: a replacement you choose can be up to 16 MiB. A prepared copy is a still PNG, JPEG or WebP of at most 1 MiB and 2048 pixels per side. Changes apply to at most 128 images at once, so review larger chats in smaller groups.

## A setting or panel looks broken

Try a known bundled theme and turn off the custom CSS or extension you changed most recently. Reload, then repeat the action that failed. If only one third-party extension triggers the issue, record its version and report it to its author with the Neconyan version.

On a phone, mention the device, browser and whether you're using a Home Screen window or an ordinary tab. Keyboard-open problems need that detail.

## A helper works differently from the chat

Check the helper's own connection and context preview. Scratchpad, Companions, Mewmory, image generation, speech and translation can each have separate configuration. A successful main reply doesn't show that those configurations work.

If a lore fact is ignored, look in World Info Lab or the outgoing prompt. If a memory is ignored, look in Mewmory's Recall view. Find out what reached the model before changing the writing instructions.

## Read saved crash reports

If the browser finds an unfinished record from its previous visible page, **Read report** opens the saved details, even if the server is offline or Debugger is disabled. Background closures stay available for manual reading. An ordinary reload doesn't repeat a notice you've already seen. A missing close record alone doesn't prove a crash.

Open **Extensions → Built-in → Debugger → Saved crash reports** to read browser reports without turning on live debugging. Each has Copy and Download actions. Administrators can also read saved server reports. Other accounts can't. **Android crash reports** opens the APK's native reader.

I keep these reports on your installation. Nothing is uploaded automatically. They record errors and a limited set of activity measurements, and don't deliberately collect chat text, prompts or credentials. An error message or system trace can still contain private text, so read it before sharing. Recent activity shows what was happening, not what caused the failure. Severe memory loss or unavailable storage can prevent a report from being saved. The [crash diagnostics reference](https://github.com/platberlitz/Neconyan/blob/staging/docs/crash-diagnostics.md) explains the limits.

## The server runs out of memory {#server-memory}

From 1.6.0, when Node.js stops because it ran out of memory, the saved server crash report says so and points you to **Server → Server Memory (Node.js)**. The card sits between **Updates & Restart** and **Thumbnail Quality** and is marked **Experimental**. It shows the **Current heap limit** and the **Device RAM**. Choose a **Heap cap**, then **Save memory cap** or **Save & Restart**, because the new cap only applies after a restart. **Auto** uses Node.js defaults on a computer and scales by itself on Android, such as in Termux.

The card warns you before you save a cap lower than the current limit or more than half the device's RAM. If `NODE_OPTIONS` or `--max-old-space-size` already sets a cap, that one wins and the card says so. The card is hidden when Neconyan runs under Bun and in the Android and iPhone apps.

## Collect a useful report

Open **Troubleshooting → Debugger** in the sidebar, reproduce the issue, then use **Diagnostic report** in **Extensions → Built-in → Debugger** to copy or download the report. Read it before sharing. The report omits several sensitive values, but screenshots and surrounding text may still include private information.

Include the app version, device/browser, exact steps, expected result, actual result and error text. Add a screenshot if it explains a layout problem. Remove keys, passwords and private conversation content.

Report reproducible app problems through [Neconyan's issue tracker](https://github.com/platberlitz/Neconyan/issues). For a provider account, payment or service outage, contact the provider's support.
