# Assets and source material

The bundled artwork was copied from [Neconyan at 6e0269d0](https://github.com/platberlitz/Neconyan/tree/6e0269d0), reviewed on 21 October 2026. Screenshot sources and capture dates are recorded separately below.

## Screenshots

The fifteen files under `docs/assets/images/screenshots/` were recaptured on 30 October 2026 from the running application with disposable demonstration data. They replace the 1.3.0 captures and the 1.3.7 Simple Mode capture. Home, Roleplay, Conversation, Meower, Story Mode, Notebooks and Scratchpad each have a desktop and phone image; `desktop-simple.webp` shows the shorter Simple Mode sidebar and composer.

The captures use [Neconyan at a4f53894](https://github.com/platberlitz/Neconyan/tree/a4f53894). Its application interface matches the [1.4.0 release at 5f9229c4](https://github.com/platberlitz/Neconyan/tree/5f9229c4); the later commit only changes the next staging version, its test expectations and the handover record. The captures show the Calico Dark theme, bundled assistants and staged chats, posts, notes and a Scratchpad discussion. No personal account data was used, and capture made no model requests.

Playwright captured Chromium at 1280×900 for desktop and 393×852 with touch emulation for phone, at a pixel ratio of 1. These are browser viewport captures, not physical-phone or Safari verification. The screenshots were converted to WebP at quality 90 without resizing or compositing interface elements.

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
