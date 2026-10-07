# Assets and source material

The application source used for this edition is [Neconyan at 33e9d09](https://github.com/platberlitz/Neconyan/tree/33e9d09), reviewed on 7 October 2026. Existing artwork and screenshots were copied from that source; the handbook doesn’t generate replacement application screens.

## Screenshots

The twelve files under `docs/assets/images/screenshots/` come from `docs/readme/` in Neconyan. They show Home, Roleplay, Conversation, Meower, Story Mode and Notebooks, each on desktop and phone. They contain staged demonstration content with the bundled assistants.

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

Dependencies retain the notices shipped in their packages. The root `LICENSE` covers the handbook’s original code and writing. Bundled Neconyan tools keep their original authors and licences; see the application’s [attribution table](https://github.com/platberlitz/Neconyan/blob/33e9d09/docs/neconyan-native-tools.md).

## Macro reference and extension example

The macro snapshot contains public definitions from Neconyan and its included tools. Editorial notes correct misleading descriptions and keep examples readable. Runtime checks use a separate test account and make no model requests.

The Scene Note starter is part of this handbook. Its source and AGPL-3.0 licence are included together in the download.
