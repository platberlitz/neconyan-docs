"""Capture public macro definitions from a disposable Neconyan installation."""
import argparse
import json
import os
from pathlib import Path

from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--app-url', required=True)
    parser.add_argument('--disposable', action='store_true', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    with sync_playwright() as playwright:
        executable = os.environ.get('BROWSER_EXECUTABLE')
        browser = playwright.chromium.launch(headless=True, **({'executable_path': executable} if executable else {}))
        try:
            page = browser.new_page()
            origin = args.app_url.rstrip('/') + '/'
            page.route('**/*', lambda route: route.continue_() if route.request.url.startswith(origin) else route.abort())
            page.goto(origin, wait_until='networkidle', timeout=90000)
            page.wait_for_function('window.SillyTavern?.getContext()?.macros?.registry', timeout=60000)
            await_ready = '''() => new Promise(resolve => {
              const ctx = SillyTavern.getContext();
              const ready = () => { ctx.eventSource.removeListener(ctx.eventTypes.APP_READY, ready); resolve(); };
              ctx.eventSource.on(ctx.eventTypes.APP_READY, ready);
            })'''
            page.evaluate(await_ready)
            snapshot = page.evaluate('''async () => {
              const ctx = SillyTavern.getContext();
              const { power_user } = await import('/scripts/power-user.js');
              power_user.experimental_macro_engine = true;
              await ctx.eventSource.emit(ctx.eventTypes.SETTINGS_UPDATED);
              const { init } = await import('/scripts/extensions/third-party/MacroEnhanced/index.js');
              init();
              const { getMacroCatalog } = await import('/scripts/extensions/third-party/MacroEnhanced/src/catalog.js');
              return {registry: ctx.macros.registry.getAllMacros({excludeAliases: true}), enhanced: getMacroCatalog()};
            }''')
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(snapshot, indent=2) + '\n')
            print(f"Captured {len(snapshot['registry'])} primary macros and {len(snapshot['enhanced'])} Macro Enhanced definitions")
        finally:
            browser.close()


if __name__ == '__main__':
    main()
