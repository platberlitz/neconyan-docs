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

Yes, through a browser or Home Screen window while Neconyan runs on another computer or host. Follow [Open it on your phone](../start/phone.md). The Android APK doesn't install on iOS.

## Can I keep using my SillyTavern characters?

Compatible cards, chats, lorebooks and other supported files can be imported. Make a backup and follow [Bring your old data](../start/imports.md). Extension compatibility needs a separate check.

## Are my chats public?

They are stored on the Neconyan server you're using, under its account and access setup. Meower doesn't publish posts to a public social network. When you use an online model or service, the material needed for that request is sent to that service.

## Does closing the tab stop a reply?

Accepted server-backed work can keep running while the server is available. Use **Stop** to cancel it; closing the page doesn't request cancellation. Browser-only routes depend on the page staying open, and stopping the whole app interrupts its server.

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
