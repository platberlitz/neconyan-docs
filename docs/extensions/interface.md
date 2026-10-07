---
title: Fit the Neconyan interface
guide: nori
quote: "Your extension may be the star of your repository. On somebody's phone, the chat still deserves most of the screen."
---

# Fit the Neconyan interface

Give the chat most of the space. Put occasional settings in the extension settings area. Label your controls and keep frequent actions reachable without cluttering the composer.

## Start in the existing settings host

The starter mounts into **extensions_settings2**, one of the shared extension settings hosts. Use a unique root ID and descriptive heading so your panel can be recognised. Check that the host exists and prevent duplicate panels.

The app can reorganise settings into pages and drawers, changing an element's parent. Prefer existing APIs and inspect actual phone behaviour before depending on the surrounding structure.

## Scope your CSS

Prefix rules with your extension's root class or ID. A global rule for buttons, textareas or a generic class can damage every other tool on the page.

Use Neconyan's colour variables for accent buttons:

```css
#my-extension .my-action {
  min-height: 44px;
  background: var(--neco-ginger);
  border: 1px solid var(--neco-ginger);
  color: var(--neco-on-accent);
}

#my-extension .my-action:hover {
  background: var(--neco-ginger-hover);
}
```

The on-accent variable matters: a pale accent and a dark accent need different label colours. Test both, as well as the default. Avoid hard-coded colours that assume every user has Calico Dark selected.

Keep keyboard focus visible. Use real buttons for actions and labels for inputs. Give icon-only controls an accessible name. A tooltip alone doesn't make a control usable on a phone.

## Design for a phone from the start

Test at **393 × 852** with touch enabled, then at **1280 × 900** on desktop. Let fields shrink within their containers, wrap long labels and avoid fixed widths that exceed the screen.

Use at least 44-pixel targets for important touch controls. Keep the save action visible with the keyboard open. Make a horizontal list deliberately scrollable rather than letting the whole page overflow sideways.

If you add motion, respect the system's reduced-motion preference:

```css
@media (prefers-reduced-motion: no-preference) {
  #my-extension .my-action {
    transition: background-color 120ms ease;
  }
}
```

## Popups and drawer boundaries

Use the app's popup helpers when they fit. A floating element appended directly to the document body can be treated as a click outside the drawer, causing that drawer to close. iPhone-specific rules can also place drawers above floating controls that looked fine in ordinary desktop testing.

Keep your UI inside its intended surface, or integrate with the host's actual overlay policy. Arbitrarily increasing a stacking number doesn't solve outside-click behaviour, focus handling or keyboard dismissal.

Some shell styles override transforms on common button classes. The separate CSS **translate** property can be needed for positioning that must survive those styles. Test the appearance options your extension claims to support.

## Chat HTML is sanitised

Chat messages pass through DOMPurify, which removes unsafe HTML. Neconyan also prefixes most message class names with **custom-**, with exceptions for supported utility classes.

For message HTML containing:

```html
<div class="my-status">Ready</div>
```

the displayed class is normally targeted as:

```css
.mes_text .custom-my-status {
  font-weight: 700;
}
```

Use the plain class in the source HTML that will be sanitised; don't pre-prefix it and accidentally create the wrong selector. This rule concerns chat content, not the ordinary DOM panel created by the starter.

Treat user and model text as text unless it has gone through the appropriate trusted rendering path. Don't bypass sanitisation to make an interactive card work.

## Labels and translation

The context exposes translation helpers and locale registration. Keep user-facing strings separate enough to translate and preserve exact action names throughout your UI. A button should say what happens when pressed, especially if it sends a request or changes saved data.

For the current app-wide rules and tokens, read [DESIGN.md](https://github.com/platberlitz/Neconyan/blob/staging/DESIGN.md). The [testing guide](testing.md) covers the checks to run before sharing your extension.
