---
title: Your first extension
guide: miso
quote: "We'll make a note box that keeps your text after a reload. I do enjoy a button that does what it says."
---

# Your first extension

This starter adds **Scene Note** to the extension settings. It saves one short note for the current account. The note isn't inserted into prompts or tied to an individual chat.

[Download the starter ZIP](../assets/downloads/scene-note.zip){ .md-button .md-button--primary }

The archive contains the exact source shown below, a short README and the licence. You can also download the [manifest](../assets/downloads/scene-note/manifest.json), [JavaScript](../assets/downloads/scene-note/index.js) and [stylesheet](../assets/downloads/scene-note/style.css) separately.

## 1. Install it in a test account

Extract the ZIP. Put the **scene-note** folder inside the test account's extensions directory. In a default single-user installation, the result is:

```text
Neconyan/
  data/
    default-user/
      extensions/
        scene-note/
          manifest.json
          index.js
          style.css
          README.txt
          LICENSE
```

If your installation uses a custom data root or another account handle, use that account's actual extensions directory. The manifest must be directly inside the extension folder, not hidden inside another extracted wrapper folder.

Reload Neconyan. Check **Extensions → Manage extensions** for Scene Note, enable it if necessary and open its settings through Extensions. Type a note, select **Save note**, wait for normal settings saving, then reload and confirm the text returns.

## 2. Describe the extension

The manifest tells the loader which files to load and which exported functions handle activation and removal.

```json title="manifest.json"
--8<-- "docs/assets/downloads/scene-note/manifest.json"
```

The JavaScript entry is loaded as a module. The named hooks refer to exported functions in that module. The starter performs its setup through **activate**, rather than starting work merely because another lifecycle action imported the file.

Before publishing a derivative, give it your own name, author, project URL and unique settings key. Keep the applicable original licence notices.

## 3. Build and save the panel

```javascript title="index.js"
--8<-- "docs/assets/downloads/scene-note/index.js"
```

The compatibility object is still named **SillyTavern**. That is the actual API name, even in Neconyan. The code asks it for the current context instead of guessing a new global name.

The panel uses normal DOM elements and assigns user text through a textarea's value. It doesn't interpret the note as HTML. Its settings live under one unique key in **extensionSettings**, and the app's debounced settings writer schedules the save.

**Save requested** is intentional wording. This helper schedules saving; it isn't an acknowledgement from the server that writing has finished. A production feature that promises confirmed persistence needs a suitable confirmed-save path and failure handling.

## 4. Style only your panel

```css title="style.css"
--8<-- "docs/assets/downloads/scene-note/style.css"
```

Every rule belongs to the extension's own root. The button uses Neconyan's accent and on-accent text variables, has a touch-friendly height and keeps a visible keyboard focus indicator.

## 5. Understand startup and cleanup

**activate** subscribes to **APP_READY** once. Neconyan's event source remembers that readiness event, so a listener added after readiness also runs. **deactivate** removes the exact listener and the panel; it leaves the user's saved note intact.

The activation guard prevents duplicate panels and subscriptions. Disabling or deleting should stop runtime behaviour, not silently erase settings. If you later add a separate data-cleaning action, explain that destructive action explicitly.

!!! taro "Taro"
    After testing the happy path, disable it, reload, enable it and reload again. One successful click is an encouraging start. It is not a lifecycle test.

Next: [APIs and lifecycle](api.md), then [Test and share](testing.md).
