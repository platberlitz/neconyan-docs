---
title: Making extensions
guide: taro
quote: "Start with one visible action that works. We can add the spectacularly complicated part after the Save button survives a reload."
---

# Making extensions for Neconyan

An extension adds JavaScript and optional CSS to Neconyan's browser interface. You can add settings, respond to chat events, provide writing utilities or integrate another service. Neconyan retains much of SillyTavern's extension format and exposes a compatibility context for extension code.

You should know basic JavaScript, HTML and CSS before modifying live chat behaviour. This section starts with a small working example and explains where Neconyan differs from assumptions an older extension might make.

## The route through this section

1. **[Your first extension](first-extension.md):** install and understand a downloadable Scene Note example. It adds a settings panel and saves one account-wide note.
2. **[APIs and lifecycle](api.md):** get the current app context, store settings, subscribe to events and clean up when disabled.
3. **[Fit the interface](interface.md):** make controls work with accents, phones, drawers and chat sanitisation.
4. **[Test and share](testing.md):** check behaviour against the app and package a repository people can install.

## Browser extension code and server work

These are **Neconyan frontend extensions**, not Firefox or Chrome add-ons. Their scripts run inside the app page. They don't get Node.js filesystem access just because Neconyan's server uses Node.js or Bun.

A frontend request also doesn't automatically become durable background work. If the feature must keep running after a page closes, it needs an appropriate server-side design. Treat that as a separate integration, with explicit account ownership, saved results, cancellation and recovery.

Don't copy an arbitrary bundled tool's server route and assume it is a public extension API. Several included tools have app-specific server support.

## Develop with disposable data

Use a separate test installation or test data root with demonstration characters. Install your extension for that account while developing it. You can then test reloads, malformed settings and interrupted work without involving the library you write in every day.

A frontend extension runs with access to the app page and the signed-in account's permitted actions. Tell users what it reads, sends and changes. Keep credentials out of source files, ordinary settings objects, screenshots and published example data.

## What compatibility means here

The reviewed source uses a SillyTavern compatibility version of **1.18.1**, separately from Neconyan's own release number. This is an API compatibility signal, not proof that every old extension's selectors, prompt interception or layout will work.

Check the actual functions you use and test the modes you support. [The compatibility notes](api.md#version-and-dependency-checks) explain the manifest fields and their limits.
