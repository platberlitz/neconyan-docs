---
title: APIs and lifecycle
guide: taro
quote: "Read the current context when you need it. Yesterday's selected chat is not a sensible destination for today's asynchronous save."
---

# APIs and lifecycle

The extension context exposes the app's current data and supported helpers. The surface is broad and still contains legacy compatibility names. Check the implementation at the Neconyan revision you support rather than treating every imported function as a permanent public contract.

## Get the current context

```javascript
function currentContext() {
  return globalThis.SillyTavern.getContext();
}

const { extensionSettings, saveSettingsDebounced } = currentContext();
```

Retrieve changing values again at the moment of use. Character, group and chat selections can change while an asynchronous operation is running. A previously captured chat identifier doesn't establish that the user still has that chat open.

The context is defined in [st-context.js](https://github.com/platberlitz/Neconyan/blob/33e9d09/public/scripts/st-context.js). The browser global is established in [script.js](https://github.com/platberlitz/Neconyan/blob/33e9d09/public/script.js). You can also import the compatibility getter from the app's extension module when you deliberately target its served path.

## Choose the right storage

| Storage | Intended scope | Practical rule |
| --- | --- | --- |
| **extensionSettings** | Account settings | Use one unique namespace and the settings save helper |
| **chatMetadata** | The current Roleplay chat's metadata | Verify chat identity and use the provided metadata save path |
| **accountStorage** | Browser storage scoped to the account | Useful for local preferences; not a server backup |
| Your server integration | Explicit server-owned records | Define ownership, validation, saving and recovery yourself |

Don't put secrets in ordinary extension settings. Don't save large file libraries into a small settings object. Keep data migrations explicit and preserve unknown or newer data rather than replacing it with defaults on every start.

The sample's **saveSettingsDebounced** batches nearby changes. It doesn't return proof of a completed server save. **saveMetadataDebounced** protects against several chat-switch and reload races, but a feature doing longer work still needs to validate its original target before applying a result.

## Subscribe to events

```javascript
const context = currentContext();
const onChatChanged = () => {
  const latest = currentContext();
  console.debug('[My extension] Current chat:', latest.chatId);
};

context.eventSource.on(context.eventTypes.CHAT_CHANGED, onChatChanged);

// During teardown, remove the same function reference.
context.eventSource.removeListener(
  context.eventTypes.CHAT_CHANGED,
  onChatChanged,
);
```

Useful event names include **APP_READY**, **CHAT_CHANGED**, **CHAT_LOADED**, **MESSAGE_SENT**, **MESSAGE_RECEIVED**, **MESSAGE_EDITED** and **GENERATION_ENDED**. See [events.js](https://github.com/platberlitz/Neconyan/blob/33e9d09/public/scripts/events.js) for the current list.

Event names alone don't define their payloads or timing. Read the call sites that emit an event before relying on its arguments. A message-received event can occur before rendering or saving finishes. Background helpers may also still be running.

The event emitter awaits asynchronous listeners during emission. Keep work short and handle failures; an unrelated slow request in a frequently emitted event can delay the app. Avoid logging private prompt content in production diagnostics.

## Activation and teardown

The manifest can name hooks for **install**, **update**, **delete**, **enable**, **disable**, **activate** and **clean**. Each names a function exported from the JavaScript entry. Hooks may return a Promise, but the loader only waits for a bounded period, currently five seconds. A timeout doesn't cancel your Promise.

Use **activate** to start runtime behaviour, with an idempotent guard: repeated activation should have no additional effect. Disable/delete cleanup should remove listeners, disconnect observers, stop timers, cancel your own pending work where possible and remove your UI.

Enabling and disabling commonly requires a reload. Don't rely on an enable hook alone to recreate an entire app session. Don't perform destructive data removal as a side effect of a normal disable.

## Requests and generation

The context includes **getRequestHeaders** for authenticated app requests and helpers for supported chat generation, token counts, popups, slash commands and request services. Read each helper's arguments and mode assumptions in the source before using it.

Use **SlashCommandParser.addCommandObject** for new slash commands rather than the deprecated registration helper. Use asynchronous token counting where offered, since synchronous counting can block the interface.

For a server request, check the HTTP result and parse the expected response. For a model request, prevent accidental duplicate submission and provide an explicit stop or cancellation path when supported. Don't silently retry an unknown paid outcome.

## Neconyan's mode and background boundaries

The familiar **chat**, **chatId** and Roleplay generation hooks aren't universal access to Conversation's separate store, Meower's timeline or every durable server workflow. A browser-side prompt listener may not run for work reconstructed and resumed entirely on the server.

Declare which modes your extension supports. If it changes prompts or saved messages, test the real request path, reconnect behaviour and current selected swipe. Don't claim that an extension continues after a tab closes unless its work really is owned and recoverable on the server.

## Version and dependency checks

**minimum_client_version** is checked against the SillyTavern compatibility version when running Neconyan. In the reviewed source that is **1.18.1**, from [neconyan-version-map.js](https://github.com/platberlitz/Neconyan/blob/33e9d09/public/scripts/neconyan-version-map.js), rather than Neconyan's release number.

Use **dependencies** as an array of extension identifiers for actual extension dependencies. The loader checks availability and disabled state, and uses dependencies when coordinating activation. **loading_order** sorts initial activation but isn't a substitute for a declared dependency or a readiness contract.

Legacy **requires** and **optional** fields appear in many manifests. Don't use them as a substitute for **dependencies** in this loader. Feature-detect the actual API you require, show a useful error when absent and document the Neconyan versions you've tested.
