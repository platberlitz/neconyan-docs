# Neconyan handbook

The official Neconyan documentation, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

I want you to get a reply before you need to understand every setting. The guides start with that, then cover the four chat modes, writing tools and helpers. The macro reference and extension tutorials hold the detail you can come back to later.

Miso, Taro and Nori explain things in their own voices. You can choose each guide’s male, female or neutral appearance independently. Their dialogue is written documentation; reading it doesn’t call a model.

The site includes 52 pages, a reference for 201 registered macros, twelve real demonstration screenshots and a downloadable extension starter. The practical guides were reviewed for Neconyan 1.2.1 against source `f467dbf` on 8 October 2026. The macro catalogue and extension examples retain their reviewed 7 October snapshots.

## Preview locally

Use Python 3.12. From this repository:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-test.txt
.venv/bin/mkdocs serve
```

Open the address printed by MkDocs. It rebuilds when you change a page.

To check the project address layout used by GitHub Pages:

```bash
.venv/bin/mkdocs build --strict
.venv/bin/python scripts/serve_site.py --port 4599
```

```text
http://127.0.0.1:4599/neconyan-docs/
```

## Edit a guide

Edit the Markdown files in `docs/`. Each guide has a title, a guide name and a short quote at the top. Use `miso` for getting started, `taro` for settings and troubleshooting, or `nori` for writing and characters.

Keep the first useful action near the top and explain how the reader can tell it worked. Mention prerequisites before the step that needs them. Use short steps when the order matters. Put optional detail below the basic task.

Use British spelling and single quotes in prose. Preserve the spelling of real controls and all code. Apply the Neconyan Proofreader agent’s editing rules as a final pass, keeping the meaning and each guide’s personality. The source rules are in the app’s bundled `proofreader.json` template.

Avoid repeated 'same X' phrasing and three-item lists written for rhythm. Keep an item when it helps the reader, including factual sets and exact options.

Use demonstration data for screenshots. Desktop captures are 1280×900 and phone captures are 393×852. Keep verification captures in `screenshots/`; that directory is ignored. Images published in the handbook belong in `docs/assets/images/screenshots/`.

## Update the macro reference

The reference is built from a reviewed snapshot, so adding a macro won’t silently leave it out of the handbook.

- `data/macro-registry.json` holds the captured definitions and aliases.
- `data/macro-notes.yml` holds reviewed explanations and checked examples.
- `scripts/hooks.py` groups the entries and adds them to the reference pages during the build.

Capture a new snapshot from a **disposable Neconyan instance**, with the bundled tools enabled. This enables newer macro support in that browser session. The snapshot contains macro definitions only.

```bash
.venv/bin/playwright install chromium
.venv/bin/python scripts/capture_macros.py \
  --app-url http://127.0.0.1:4487 \
  --disposable \
  --output data/macro-registry.json
```

Review the differences against the application source. Update the notes, category mapping, documented count, check script and version date together. Keep identifiers and examples exact. A third-party extension or custom macro can change the installed list, so the reader’s in-app Reference remains useful.

## Check the site

```bash
.venv/bin/mkdocs build --strict
.venv/bin/python scripts/check_site.py
.venv/bin/playwright install chromium
.venv/bin/python scripts/browser_check.py
```

The static check covers local links, anchors, assets, macro coverage and the starter archive. The browser check covers every content page at phone width, desktop reading, search, guide choices, screenshot zoom, contrast and storage failures. It saves screenshots in the ignored directory.

If Chromium is already installed somewhere else, set `BROWSER_EXECUTABLE` to its full path.

The optional app check needs a separately running Neconyan instance with disposable data. Install the Scene Note example in that test account’s extensions directory before running it. The check creates a test character when needed, changes test variables and saves extension settings. It makes no model requests.

```bash
.venv/bin/python scripts/check_app_examples.py \
  --app-url http://127.0.0.1:4487 \
  --disposable
```

## Publish with GitHub Pages

The configured destination is:

```text
https://platberlitz.github.io/neconyan-docs/
```

1. Run the checks above and push the reviewed source to `main` in `platberlitz/neconyan-docs`.
2. Wait for the documentation workflow's build, browser checks and deployment to finish.
3. Open the address above and check the changed guides.

GitHub Pages is configured to publish through GitHub Actions. The documentation workflow can also be run manually.

The workflow checks pull requests without publishing them. It builds the starter ZIP from the example’s source files, so the download matches the tutorial. Generated output stays out of Git.

If the account or repository name changes, update the configured address and the project-prefix checks before deploying.

## Credits and licences

The handbook and its original source use AGPL-3.0. The extension starter includes its own copy of the licence. Font notices ship beside the fonts. See [ASSETS.md](ASSETS.md) for artwork, screenshot and dependency provenance.
