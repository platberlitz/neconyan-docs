---
title: Make it yours
guide: miso
quote: "You can change the colours without changing the model. You can also hide the decorative cats. I am being extremely brave about that second option."
---

# Make it yours

Open **Settings → Appearance** to change how Neconyan looks. Appearance controls don't make model requests, and a visual theme is separate from a model preset.

## Appearance controls

| Control | What it changes |
| --- | --- |
| **UI Theme** | A broader saved appearance preset, with import, export and save controls |
| **Accent Profiles** | Accent palettes and custom primary/secondary colours |
| **Shell Style** | The shape and treatment of controls, panels and navigation |
| **Chat Style** | Message presentation |
| **Desktop response controls** | Whether swipe arrows and the counter sit inside the bubble or below it on wide screens |
| **Theme Colors** | Individual colour values, including ordinary quoted text |

Colour edits apply immediately. **Save as a new theme** stores a broader named theme; **Save Current** under saved accent pairs stores the accent pair. Those are separate saves.

## Choose a style

Calico is the familiar Neconyan look. **Kittyless** removes decorative cats, ears and paws while retaining your chats and installed characters. You can also use **Hide cats (Kittyless)** beneath the style choices while keeping another shell style.

Other choices include Windows Aero, Windows XP, Windows 98, macOS Minimal and several quieter styles. Windows 98 gives bundled assistant artwork a pixel-art treatment; it doesn't replace the portraits of characters you've imported.

For a dark olive Windows XP look, choose the **Windows XP** shell and **Windows XP Olive Green Dark** under UI Theme. Shell Style and UI Theme are separate selections.

**Shell Style → Your cat** and **Character cat** choose the sleeping-cat coat on each side of the chat. **Pair** sets both at once; changing either afterwards selects **Your own mix**. These choices apply immediately and are saved in this browser. **Hide cats (Kittyless)** hides them with the other decorations.

## Make text comfortable to read

Start with a bundled light or dark theme and a readable font size. Check a real chat, the composer and a settings panel after changing colours. Neconyan adjusts some theme colours for contrast, but custom CSS and message-level colour tags can override the result.

**AMOLED Black** is available under UI Theme for a pure-black interface. Switch to another theme if you want its hidden wallpaper and cloud artwork back.

## Visual Toggles

**Visual Toggles** groups its switches into **Comfort**, **Message details**, **Chat layout**, **Characters**, and **Settings and sliders**. Read the description beside a switch to see which part of the interface it affects. These display choices are separate from the sending and generation controls in **Chat & Writing**.

Use **Reduced Motion** to disable interface animations and transitions. Supported styles also respect the operating system's reduced-motion preference.

## Movable panels

Open **Appearance → Movable panels** to enable dragging and resizing supported pop-outs. Drag a panel by its top edge to move it, or its corner to resize it.

The built-in layouts are **Pop-outs on the Right**, **Writing Desk**, **Centred Card** and **Compact Corner**. They place supported pop-outs such as Author's Note, CFG and token probabilities. They don't move the main chat or workspace side panels. Save your own layout after arranging the pop-outs you use.

## Change dialogue colours

For one ordinary quotation colour, use **Theme Colors → Quote Text**. Accent Profiles can replace this colour when you apply an accent.

For different named speakers, use **Included tools → Dialogue Colors → Settings → Characters**. Select a speaker's swatch or add the missing name. **Colors saved** chooses Per chat, Per card or Global scope.

Per-card settings aren't automatically embedded in an exported character file. Use the tool's explicit **Save to card** action when you want that transfer. Its local display mode and modes that store colour tags also have different effects on saved text.

## Small custom changes

**CSS Snippets** manages named visual rules, with global, theme and chat scopes. CSS is the language that controls the page's appearance. Keep changes small and test them on a phone as well as a desktop.

**Appearance → Custom CSS → Generate CSS with AI** asks a model for a visual change. **Replace** requests a complete updated stylesheet; **Append** requests additions to the existing rules. This uses a model request. The result applies only if the saved CSS hasn't changed while the request runs. Keep a copy of your rules before trying a generated change.

If something becomes unreadable or stops responding after a visual change, disable the relevant snippet or return to a known theme before changing model settings. See [troubleshooting](../help/troubleshooting.md).
