# Assets and source material

The bundled artwork was copied from [Neconyan at 6e0269d0](https://github.com/platberlitz/Neconyan/tree/6e0269d0), reviewed on 21 October 2026. Screenshot sources and capture dates are recorded separately below.

## Screenshots

All twenty-two screenshots were recaptured on 9 November 2026 from the running [Neconyan 1.5.3 candidate at efdf32f6](https://github.com/platberlitz/Neconyan/tree/efdf32f6), after the filled Send paw and solid Stop square were added. Home, Roleplay, Catelier, Simple Mode, Conversation, Meower, Story Mode, Notebooks, Scratchpad, Agents and Proofreader each have a desktop and phone image.

The captures use disposable demonstration data: Calico Dark with a purple accent, bundled assistants and staged chats, posts, notes, a character dossier and a Scratchpad discussion. No personal account data was used. The Proofreader example runs the real Agent workflow with one intercepted provider request returning a fixed sample response; its edit, Undo and Redo were checked again at both widths. It isn't a live model demonstration. No external model requests were made.

These replace the eighteen images previously captured on 30 October, 5 November and 8 November, and add the four Agents and Proofreader images.

Playwright captured Chromium at 1280×900 for desktop with a pixel ratio of 1, and 393×852 with touch emulation for phone at a pixel ratio of 1.5. These are browser viewport captures, not physical-phone or Safari verification. The screenshots were converted to WebP at quality 80 without resizing or compositing interface elements.

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
