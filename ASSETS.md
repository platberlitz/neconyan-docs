# Assets and source material

The bundled artwork was copied from [Neconyan at 6e0269d0](https://github.com/platberlitz/Neconyan/tree/6e0269d0), reviewed on 21 October 2026. Screenshot sources and capture dates are recorded separately below.

## Screenshots

I captured these screenshots on 18 November 2026 from [Neconyan at 6b6a8696](https://github.com/platberlitz/Neconyan/tree/6b6a8696), a 1.5.6 staging build with the Catline cat pile for Extensions. Home, Roleplay, Catelier, Simple Mode, Conversation, Meower, Story Mode, Notebooks, Scratchpad, Agents, Proofreader and Device sync each have a desktop and phone image. There's also a phone shot of the open workspace menu, where the new icon is visible. The app README and this handbook use identical copies.

The captures use disposable demonstration data: Calico Dark with its default accent, bundled assistants and staged chats, posts, notes, a character dossier and a Scratchpad discussion. I set Background Visibility to 0% for opaque reading panels; the wallpaper still shows behind Home and the chat, as it should at every setting. The default colours and visibility setting were checked before every capture. No personal account data was used. The Proofreader example runs the real Agent workflow with one intercepted provider request returning a fixed sample response; its edit, Undo and Redo were checked again at both widths. It isn't a live model demonstration. No external model requests were made.

The two Notebooks images, `desktop-notes.webp` and `phone-notes.webp`, are the exception. They were retaken on 18 November 2026 for the decluttered phone layout and copied unchanged from the app README's `docs/readme/` folder, where they were added in [commit 4979d561](https://github.com/platberlitz/Neconyan/commit/4979d561). I didn't capture them for this handbook. The desktop image is 1280×900 and the phone image 393×852 pixels, so the phone image is smaller than the others.

The guides are reviewed against Neconyan 1.5.6 at `d3f33f5d`, the latest published release. Version 1.5.6 replaces Background Visibility with **Settings → Appearance → Panels**, which came after these captures, so panel transparency can look slightly different in the app.

I used Playwright with Chromium at 1280×900 for desktop with a pixel ratio of 1, and 393×852 with touch emulation for phone at a pixel ratio of 1.5. The saved images are 1280×900 and 590×1278 pixels. These are browser viewport captures, not physical-phone or Safari verification. I converted them to WebP at quality 80, method 6, without resizing or compositing interface elements.

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
