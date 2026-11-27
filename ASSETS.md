# Assets and source material

The bundled artwork was copied from [Neconyan at 6e0269d0](https://github.com/platberlitz/Neconyan/tree/6e0269d0), reviewed on 21 October 2026. Screenshot sources and capture dates are recorded separately below.

## Screenshots

I captured these screenshots on 27 November 2026 from the `chore/release-1.6.0` branch of Neconyan. Its app code matched [Neconyan at 73555b9c](https://github.com/platberlitz/Neconyan/tree/73555b9c888a11d32519b179e56c860b89ec6cff), the 1.6.0 staging candidate, when I took the first set. Later that day I retook the Simple Mode chat and Author's Note, Agents, Device sync, Scratchpad and desktop Meower images from the same branch after it gained a Conversation save fix, which doesn't change how any of these screens look. The retakes show controls that the first set had cut off or covered. Home, Roleplay, Catelier, Conversation, Meower, Story Mode, Notebooks, Scratchpad, Agents, Proofreader, Device sync and three Simple Mode views each have a desktop and phone image. There's also a phone shot of the open workspace menu. The app README uses identical copies, plus three Simple Mode images the handbook doesn't show (`desktop-simple-ask.webp`, `phone-simple-ask.webp` and `phone-simple-menu.webp`).

The captures use a disposable data root with demonstration data only: Calico Dark with its default accent and the default accent profiles, **Panel opacity** at 100%, the bundled Miso, Taro and Nori cards, and staged chats, posts, notes, a character dossier and a Scratchpad round table. No personal account data was used. The Simple Mode chat and Author's Note images are connected to a small local test service with a model called 'demo', so the composer shows its usual send button; the other views have no model connected, so their composer shows **Connect**. The Proofreader example runs the real Agent workflow against a small local test service that returns a fixed sample response through a connection profile called 'Demonstration response'. I switched that Agent off again before the other captures. No external model requests were made.

I used Playwright with Chromium at 1280×900 for desktop with a pixel ratio of 1, and 393×852 with touch emulation for phone at a pixel ratio of 1.5, with reduced motion on. The saved images are 1280×900 and 590×1278 pixels. These are browser viewport captures, not physical-phone or Safari verification. I converted them to WebP at quality 80, method 6, without resizing or compositing interface elements.

## Assistant artwork

The nine portraits under `docs/assets/images/icons/` come from `public/img/neconyan/assistant-icons/`.

The nine illustrations under `docs/assets/images/guides/` come from `public/img/neconyan/tour/`:

- Miso: `tour-07-miso-home`, in male, female and neutral variants.
- Taro: `tour-05-taro-agents`, in male, female and neutral variants.
- Nori: `tour-04-nori-lorebooks`, in male, female and neutral variants.

The logo comes from `public/img/neconyan/cat-head.webp`. The favicon comes from `public/img/neconyan-icon-192.png`. Character identities and personalities follow Neconyan’s assistant design document. These original bundled assets are distributed with the application’s AGPL-3.0 licence.

## Fonts

The fonts are served by the site itself:

- **Nunito**, by Vernon Adams, Cyreal and Jacques Le Bailly. Source: Neconyan’s `public/webfonts/Nunito/`. Licence: `docs/assets/fonts/Nunito-OFL.txt`.
- **Fredoka One**, by Milena Brandão. Source: Neconyan’s `public/webfonts/FredokaOne/`. Licence: `docs/assets/fonts/FredokaOne-OFL.txt`.

Both use the SIL Open Font Licence. The copied notices are authoritative for copyright and reserved names.

## Site dependencies

- [Material for MkDocs](https://github.com/squidfunk/mkdocs-material), by Martin Donath, uses the MIT licence.
- [MkDocs](https://github.com/mkdocs/mkdocs) uses the BSD licence.
- [PyMdown Extensions](https://github.com/facelessuser/pymdown-extensions), by Isaac Muse, uses the MIT licence.
- [Playwright](https://github.com/microsoft/playwright) is used for verification under Apache-2.0.

Dependencies retain the notices shipped in their packages. The root `LICENSE` covers the handbook’s original code and writing. Bundled Neconyan tools keep their original authors and licences; see the application’s [attribution table](https://github.com/platberlitz/Neconyan/blob/6e0269d0/docs/neconyan-native-tools.md).

## Macro reference and extension example

The macro snapshot contains public definitions from Neconyan and its included tools. Editorial notes correct misleading descriptions and keep examples readable. Runtime checks use a separate test account and make no model requests.

The Scene Note starter is part of this handbook. Its source and AGPL-3.0 licence are included together in the download.
