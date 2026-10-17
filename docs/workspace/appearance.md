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

Character tags in the library and character editor follow the selected accent colours too.

## Choose a style

Calico is the familiar Neconyan look. **Kittyless** removes decorative cats, ears and paws while retaining your chats and installed characters. You can also use **Hide cats (Kittyless)** beneath the style choices while keeping another shell style.

Other choices include Windows Aero, Windows XP, Windows 98, macOS Minimal and several quieter styles. Windows 98 gives bundled assistant artwork a pixel-art treatment; it doesn't replace the portraits of characters you've imported.

For a dark olive Windows XP look, choose the **Windows XP** shell and **Windows XP Olive Green Dark** under UI Theme. Shell Style and UI Theme are separate selections.

**Shell Style → Your cat** and **Character cat** choose the sleeping-cat coat on each side of the chat. **Pair** sets both at once; changing either afterwards selects **Your own mix**. These choices apply immediately and are saved in this browser. **Hide cats (Kittyless)** hides them with the other decorations.

There are 34 coats and 21 ready-made pairs. 1.3.0 added Birman, Snowshoe, Cinnamon, Fawn, Caracal and Lynx, with pairs such as **Snow mittens: Birman and Snowshoe** and **Tufted twins: caracal and lynx**. Every coat has pixel-art frames for the Windows 98 style.

To change the picture behind the app, open **Appearance → Background**. The bundled dark backgrounds include **Neconyan - Velvet Moon**, **Neconyan - Rainy Lantern Loft**, **Neconyan - Mosslight Grotto**, **Neconyan - Indigo Tide**, **Neconyan - Ember Hearth** and **Neconyan - Starlit Snow**.

## Make text comfortable to read

Start with a bundled light or dark theme and a readable font size. Check a real chat, the composer and a settings panel after changing colours. Neconyan adjusts some theme colours for contrast, but custom CSS and message-level colour tags can override the result.

**AMOLED Black** is available under UI Theme for a pure-black interface. Switch to another theme if you want its hidden wallpaper and cloud artwork back.

## Visual Toggles

**Visual Toggles** groups its switches into **Comfort**, **Message details**, **Chat layout**, **Characters**, and **Settings and sliders**. Read the description beside a switch to see which part of the interface it affects. These display choices are separate from the sending and generation controls in **Chat & Writing**.

**Visual Toggles → Chat layout** holds **Compact Input Area**, marked **Phones only**. On a phone, on keeps the message box and its controls to a single row; off places a full-width message box above them. It applies immediately, is saved, and is separate from the shell's **Compact Mode** and from **Bottom Bar Size**.

Pages move from the control you pressed: a top-bar shortcut drops its page down from under the bar, and a desktop sidebar page slides out from behind the sidebar. Opening a chat lets the messages rise into place, and swiping slides the next or previous reply in from the side you are moving towards.

Use **Reduced Motion** to disable interface animations and transitions, including these. Supported styles also respect the operating system's reduced-motion preference.

## Bottom bar width on a computer

**Settings → Appearance → Interface → Bottom Bar Size** sets the width of the bottom chat bar on desktop, from 70 to 150. It works separately from **Page Width**. If the bar is wider than the space available, it scrolls sideways. When the message form is narrower than 300 pixels, the message box moves below its buttons.

On a phone, the setting keeps the phone layout but changes the control size. Increase it if the slim default buttons feel too small. In the standard phone layout, Send is 38 pixels at 100 and grows to 44 pixels at 150.

## Movable panels

Open **Appearance → Movable panels** to enable dragging and resizing supported pop-outs. Drag a panel by its top edge to move it, or its corner to resize it.

The built-in layouts are **Pop-outs on the Right**, **Writing Desk**, **Centred Card** and **Compact Corner**. They place supported pop-outs such as Author's Note, CFG and token probabilities. They don't move the main chat or workspace side panels. Save your own layout after arranging the pop-outs you use.

## Change dialogue colours

For one ordinary quotation colour, use **Theme Colors → Quote Text**. Accent Profiles can replace this colour when you apply an accent.

For different named speakers, use **Appearance → Dialogue Colors → Characters** in the sidebar. Select a speaker's swatch or add the missing name. **Colors saved** chooses Per chat, Per card or Global scope.

Under **Settings → Automation**, **Don't color a Narrator card** is on by default. It keeps a character card named `Narrator` in the normal text colour even when the model wraps its lines in a colour, stops `Narrator` being added to the speaker list and tells the model not to colour it.

If a scenario card such as `'Your Wife Wants To Divorce You'` or a titled label such as `'Leonard | Actor'` is being coloured as a speaker, add it under **Not characters** with **Add** or **Add this card's name**, or open the speaker row's **More** actions and choose **Not a character**. Listed names leave the character list, are never added or sent to the model as speakers, and their model-written colours render in the normal text colour. Use the Undo notice to put one back immediately, or remove its chip from the list to let it be coloured again.

Under **Settings → Process**, **Clean messages** removes stored colour markup from every character message and swipe in the open chat while leaving your own messages and system or tool messages alone. Choose **Color lines** in **What to remove** to strip standalone `[COLORS: ...]` lines, or **Color lines and tags** to also remove colour-only tags wrapped around dialogue, then confirm with **Remove lines** or **Remove lines and tags**. Click the Undo notice to restore the messages as they were.

Per-card settings aren't automatically embedded in an exported character file. Use the tool's explicit **Save to card** action when you want that transfer. Its local display mode and modes that store colour tags also have different effects on saved text.

While a server-run Roleplay reply is still being written, its live preview receives dialogue colours as the text arrives. That display pass doesn't save the unfinished message or its speaker overrides.

If your preset uses `{{dialoguecolors}}`, the page resolves its current colour instructions before submitting the reply. The saved job keeps that value when you close the tab, and through group turns and retries. LLM colouring still depends on the model following those instructions; Local (DOM-only) colours the displayed text instead.

## Tracker themes

**Appearance → Regex Agent Themes → Browse themes** previews and applies themes for trackers and Companion panels. This is separate from the whole application's UI Theme.

Search with **Search by name, colour or motion**, then filter with **All**, **Dark**, **Light**, **Animated**, **Adaptive**, or **Custom** once you've saved custom themes. **Theme family** narrows the list further, and **Clear filters** resets it.

**Previous**, **Next** and **Surprise me** only move the preview within the filtered list. **Apply this theme** makes the previewed theme the default; **Show current** returns the preview to the current default.

1.3.4 added 40 choices: 14 dark, 13 light and 13 animated. Animated themes stop when the operating system asks for reduced motion.

## Termeownal palettes

**Appearance → Termeownal UI → Palette** offers 44 colour schemes, plus **Inherit Active Theme**.

1.3.4 added **Catppuccin Mocha**, **Tokyo Night**, **Rosé Pine**, **Monokai**, **Commodore 64**, **Tuxedo Cat**, **Solarized Light** and **Sakura Latte**.

**Inherit Active Theme** follows the application's theme instead of using its own colours, and is the default. Checkboxes and radio buttons keep their round appearance.

## Low-memory mode

**Settings → System & Device → Memory and performance → Low-memory mode** keeps Neconyan responsive on phones and computers with limited memory. It is saved per browser or device and offers **Auto**, **On** and **Off**.

**Auto** turns on when the browser reports 2 GB of memory or less, or when the Android app reports a low-memory device or 3 GiB of total memory or less. When active, it turns on **No Blur Effect** and keeps 25 recent messages rendered in Roleplay and Conversation instead of larger history windows. Any of those settings you change yourself stays as you set it until you press **Use automatic recommendations**. Changing the Roleplay message limit while a chat is open asks you to reopen the chat to apply the new limit.

## Keep images out of replies

**Settings → Appearance → Avatar & Chat Styles** also holds **Don't send chat images to the model** and **Review chat images**. The switch keeps image files and their saved descriptions out of new automatic replies across the account; pictures stay visible and existing text stays text. The button opens the review panel for the open chat.

[Roleplay](roleplay.md#images-in-replies) explains the per-message choices, [Conversation](conversation.md#review-image-input) has its own panel, and [Something went wrong](../help/troubleshooting.md#image-input-needs-attention) covers repair and recovery.

## Small custom changes

**CSS Snippets** manages named visual rules, with global, theme and chat scopes. CSS is the language that controls the page's appearance. Keep changes small and test them on a phone as well as a desktop.

**Appearance → Custom CSS → Generate CSS with AI** asks a model for a visual change. **Replace** requests a complete updated stylesheet; **Append** requests additions to the existing rules. This uses a model request. The result applies only if the saved CSS hasn't changed while the request runs. Keep a copy of your rules before trying a generated change.

If something becomes unreadable or stops responding after a visual change, disable the relevant snippet or return to a known theme before changing model settings. See [troubleshooting](../help/troubleshooting.md).
