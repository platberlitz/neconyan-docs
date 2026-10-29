---
title: Common questions
guide: miso
quote: "The question you're about to ask is probably a sensible one. Even if the answer turns out to be 'that button is in the other panel'."
---

# Common questions

## Is Neconyan free?

Neconyan's source is available under AGPL-3.0. Model providers, image services, speech services and hosting can have their own costs. The app doesn't include API credits.

## Does it come with an AI model?

No. [Connect a supported provider or local model service](../start/connections.md). The Android app includes the Neconyan server, which is different from including a language model.

## Can I use it on an iPhone?

Yes, through a browser or Home Screen window while Neconyan runs on another computer or host. Follow [Open it on your phone](../start/phone.md). The project also includes a standalone iPhone app that keeps the server and your chats on the phone; it needs iOS 17 or newer and is sideloaded, not installed from the App Store. If a release provides an IPA, use that release's matching file; otherwise, use the browser setup. The Android APK doesn't install on iOS.

## What is Simple Mode?

An optional smaller layout. Existing accounts keep their current layout, and a new account keeps the full sidebar unless Nori's offer is accepted. **Yes, keep it simple** hides power tools such as Mewmory, Chat Archive, Extensions and the other Fine-tuning pages without deleting or switching them off. **Show all features** in the sidebar brings everything back, and **Settings → Appearance → Simple Mode** turns it on again. [Find your way around](../workspace/index.md#keep-the-sidebar-simple) explains what stays.

## Can I keep using my SillyTavern characters?

Compatible cards, chats, lorebooks and other supported files can be imported. Make a backup and follow [Bring your old data](../start/imports.md). Extension compatibility needs a separate check.

## Are my chats public?

They are stored on the Neconyan server you're using, under its account and access setup. Meower doesn't publish posts to a public social network. When you use an online model or service, the material needed for that request is sent to that service.

## Does closing the tab stop a reply?

Not usually. With **In the browser (recommended)** selected under **Settings → Chat & Writing → Chat & messages → Replies → Where replies are written**, ordinary Roleplay replies run in the page, but the server holds most single-character replies when the page closes. Reopen the same chat to collect the result; a finished reply waits for 15 minutes, or 24 hours if the request carried chat context. Agents that run after a reply aren't replayed for a held reply. With **On the server** selected, the ordinary reply and its after-reply Agents keep going after you close the page or your phone sleeps.

Conversation replies, Scratchpad, replies that need a Notebook context and saved server workflows such as Deep Swipe always keep running on the server while it's available. Use **Stop** to cancel any of them; closing the page doesn't request cancellation. Restarting or stopping the whole app interrupts its server and loses held replies.

## Why did my tab reload by itself after an update?

A tab opened before the server was updated keeps running the old page. From 1.3.6, when you come back to that tab or it comes back online, Neconyan checks which version the server now serves. If nothing is happening, it saves your settings and reloads; a reply held on the server while you were away is collected after the reload. If a reply is being written, a message is being edited, a chat is saving or the message box has text in it, nothing is thrown away: an **Update ready** notice says 'Neconyan was updated. Tap here to load the new version.' Tap it when you're ready. Reloading doesn't send anything to the model.

## Why do notices stay on screen longer now?

From 1.3.0, a notice that closes by itself stays up for at least 5 seconds, so you have time to read it. This includes notices from extensions and scripts that ask for a shorter time. Notices that wait for you to close them are unchanged.

## Why doesn't Conversation show my Roleplay messages?

They use separate histories. Conversation also has persona-specific histories and branches. Check the mode, persona, server and account before concluding that data was deleted.

## Do all helpers see all my notes?

No. Notebook access, reference use, lore publication and Scratchpad sharing have distinct controls. Use the relevant context preview. A note link doesn't grant access to the linked note.

## Do Miso, Taro and Nori use different models?

They can use different saved connections in features such as Scratchpad, or share the chat's connection. Their character identity and gender don't select a paid provider automatically. The handbook's written dialogue makes no model requests.

## Why is an answer still wrong if the correct fact is in memory?

First check whether the fact was included in that request. If it was, the model can still misunderstand or ignore it. Source-backed recall improves the available context; it doesn't guarantee factual generation.

## Can I make my own extension?

Yes. Start with [Making extensions](../extensions/index.md), then build the downloadable starter and test it against the Neconyan version you intend to support.

## Where do I report a problem?

Use [troubleshooting](troubleshooting.md) to collect the relevant details, then open a reproducible app issue in [the repository](https://github.com/platberlitz/Neconyan/issues). Remove credentials and private material from reports and screenshots.
