---
title: Test and share
guide: taro
quote: "Test the state after a reload, not just the toast after a click. A toast is very easy to make confident."
---

# Test and share your extension

Use a disposable test account and the Neconyan version you intend to support. Keep the extension source in its own repository so its changes and releases are independent of the app checkout.

## Test the starter's full lifecycle

For Scene Note, verify these outcomes:

1. The extension appears in Manage extensions and mounts one settings panel.
2. Typing changes the status to **Unsaved changes**.
3. Saving schedules the app's settings save; after a completed save and reload, the note returns.
4. A second account doesn't inherit the first account's note.
5. Disabling and reloading removes the panel.
6. Re-enabling and reloading restores the panel and the saved note.
7. Repeated activation doesn't duplicate the panel or listeners.
8. Text containing HTML marks remains literal note text.

For a feature with chat-specific state, also switch chats while work is pending and confirm the result doesn't save into the new chat. Test errors and cancellation before trying large or paid requests.

## Inspect the browser and server

Use browser developer tools to inspect Console errors and Network requests. A script returning HTML instead of JavaScript often means the asset path is wrong or the server returned an error page.

Neconyan's **Debugger** can capture a diagnostic report and layout snapshot. Server-side failures may require the server terminal's error as well. Keep reports focused on the failing operation and remove private content before publishing them.

If an edited asset looks unchanged, reload with the browser cache disabled during development and inspect the served file. The extension loader adds the app's asset version to entry URLs; it doesn't turn every source edit into a new application release.

## Test the interface

Check phone and desktop sizes, keyboard-only use, light and dark themes, and pale and dark accents. Confirm the page doesn't scroll sideways, labels fit and important actions remain reachable with the phone keyboard open.

Chromium touch emulation is useful but doesn't prove Safari behaviour. For iPhone support, test a real iPhone where possible. Neconyan's repository also includes an iOS emulation helper for the app's platform-specific branches; those results remain emulation.

Capture screenshots of your extension with demonstration data. For a chat or prompt integration, verify every mode you claim to support and say when a mode is outside the extension's scope.

## Package a Git repository

Keep the manifest and its entry files at the repository root:

```text
my-neconyan-extension/
  manifest.json
  index.js
  style.css
  README.md
  LICENSE
```

The README should explain installation, supported Neconyan versions, where the controls appear, what data is stored, any external requests and how to disable the extension. Include dependencies and costs when relevant. Set the manifest's author, version and home page to your own project.

Users can install a Git repository through the app's extension installation controls, subject to server settings and account permissions. Personal installations live in the account's extensions directory. Installing for everyone uses the global extension location and requires administrator permission.

An extracted local starter isn't automatically a Git-managed installation. To distribute updates, publish a proper repository with the manifest at its root and test installation from that repository URL.

## Updating and compatibility

Bump the extension's version when you release changes. Test migrations from an older saved-settings object, including missing fields. Don't overwrite existing settings with defaults every time the module loads.

Avoid an identifier that collides with a bundled tool or another extension. The loader normalises names for some duplicate checks, including case and the third-party prefix. Shipping an old copy of a bundled tool can leave one copy inactive rather than producing the behaviour you expected.

If a change needs new host APIs, document the tested app versions and check for those capabilities at runtime. The manifest's compatibility version isn't a substitute for testing the actual feature.

## Source references

- [Extension loader and lifecycle hooks](https://github.com/platberlitz/Neconyan/blob/33e9d09/public/scripts/extensions.js)
- [Context API](https://github.com/platberlitz/Neconyan/blob/33e9d09/public/scripts/st-context.js)
- [Boot and dependency decisions](https://github.com/platberlitz/Neconyan/blob/33e9d09/public/scripts/extension-boot-lifecycle/index.js)
- [Server installation routes](https://github.com/platberlitz/Neconyan/blob/33e9d09/src/endpoints/extensions.js)
- [Neconyan's design rules](https://github.com/platberlitz/Neconyan/blob/staging/DESIGN.md)

These links pin implementation details to the reviewed source where appropriate. Recheck them against the version you release for.
