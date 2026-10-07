"""Check documented results and the starter against a disposable Neconyan app.

Run only with a separate test data directory. This intentionally saves example settings.
"""
import argparse
import json
import os
import re
from pathlib import Path

from playwright.sync_api import expect, sync_playwright
from hooks import catalogue, corrections

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--app-url', required=True)
    parser.add_argument('--disposable', action='store_true', required=True)
    args = parser.parse_args()
    cases = []
    registry = {m['name']: m for m in catalogue()}
    for name, note in corrections().items():
        expected = re.match(r'^`([^`]+)`', note.get('result', ''))
        if expected:
            cases.append({'name': name, 'input': note.get('examples', registry[name]['exampleUsage'])[0], 'expected': expected[1]})
    cases += [
        {'name': 'local variable', 'input': '{{setvar::docs_test_location::Library}}{{getvar::docs_test_location}}', 'expected': 'Library'},
        {'name': 'shorthand zero', 'input': '{{.docs_test_score = 0}}{{.docs_test_score ?? 5}}', 'expected': '0'},
        {'name': 'shorthand false fallback', 'input': '{{.docs_test_score = 0}}{{.docs_test_score || 5}}', 'expected': '5'},
        {'name': 'pronoun agreement', 'input': '{{setpronouns::she/her}}{{Sub}} {{pverb::is::are}} ready.', 'expected': 'She is ready.'},
        {'name': 'neutral agreement', 'input': '{{setpronouns::they/them}}{{Sub}} {{pverb::is::are}} ready.', 'expected': 'They are ready.'},
        {'name': 'separate stores', 'input': '{{setvar::docs_test_value::ordinary}}{{setchatvar::docs_test_value::enhanced}}{{getvar::docs_test_value}}/{{getchatvar::docs_test_value}}', 'expected': 'ordinary/enhanced'},
        {'name': 'block spacing', 'input': '{{#trim}}  Keep these edge spaces.  {{/trim}}', 'expected': '  Keep these edge spaces.  '},
    ]
    with sync_playwright() as p:
        executable = os.environ.get('BROWSER_EXECUTABLE')
        browser = p.chromium.launch(headless=True, **({'executable_path': executable} if executable else {}))
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.route('**/*', lambda route: route.continue_() if route.request.url.startswith(args.app_url.rstrip('/') + '/') else route.abort())
        page.goto(args.app_url, wait_until='networkidle', timeout=90000)
        page.wait_for_function('window.SillyTavern?.getContext()?.macros?.registry', timeout=60000)
        page.wait_for_selector('#neconyan_scene_note', state='attached', timeout=60000)
        page.wait_for_function('''() => {
          const ctx = SillyTavern.getContext();
          return ctx.eventSource.autoFireLastArgs.has(ctx.eventTypes.APP_READY);
        }''', timeout=60000)
        if not page.evaluate('SillyTavern.getContext().characters.length'):
            created = page.evaluate('''async () => {
              const response = await fetch('/api/characters/create', {
                method: 'POST', headers: SillyTavern.getContext().getRequestHeaders(),
                body: JSON.stringify({ch_name: 'Documentation test', description: 'Disposable test character.', first_mes: 'Hello.'})
              });
              return response.ok;
            }''')
            assert created, 'Could not create the disposable test character'
            page.reload(wait_until='networkidle')
        page.wait_for_function('SillyTavern.getContext().characters.length > 0')
        page.evaluate('async () => { await SillyTavern.getContext().selectCharacterById(0, {switchMenu: false}); }')
        results = page.evaluate('''async cases => {
          const ctx = SillyTavern.getContext();
          const { power_user } = await import('/scripts/power-user.js');
          power_user.experimental_macro_engine = true;
          await ctx.eventSource.emit(ctx.eventTypes.SETTINGS_UPDATED);
          const { init } = await import('/scripts/extensions/third-party/MacroEnhanced/index.js');
          init();
          const { substituteParams } = await import('/script.js');
          return cases.map(test => ({...test, actual: substituteParams(test.input)}));
        }''', cases)
        failed = [case for case in results if case['actual'] != case['expected']]
        assert not failed, json.dumps(failed, indent=2)
        # Open the actual extension settings panel through the shell if it is hidden.
        page.evaluate('''() => {
          document.querySelector('#extensions_settings2').closest('.drawer-content')?.style.setProperty('display', 'block');
        }''')
        with page.expect_response(lambda response: response.url.endswith('/api/settings/save') and response.request.method == 'POST', timeout=30000) as saved_response:
            state = page.evaluate(r'''async () => {
          const source = [...document.scripts].find(s => /\/scene-note\/index\.js(?:\?|$)/.test(s.src));
          const ext = await import(source.src);
          ext.activate(); ext.activate();
          const count = document.querySelectorAll('#neconyan_scene_note').length;
          const input = document.querySelector('#neconyan_scene_note textarea');
          input.value = '<b>Saved literally</b> & a second line';
          input.dispatchEvent(new Event('input', {bubbles:true}));
          document.querySelector('#neconyan_scene_note button').click();
          return {count, value: SillyTavern.getContext().extensionSettings.neconyan_scene_note.text,
            literal: input.value, unsafeElements: input.querySelectorAll('b').length};
            }''')
        assert saved_response.value.ok, 'The settings save failed'
        assert state['count'] == 1 and state['unsafeElements'] == 0
        assert state['value'] == '<b>Saved literally</b> & a second line'
        # Read the server response directly, independently of browser-side state.
        response = page.request.post(args.app_url.rstrip('/') + '/api/settings/get',
                                     headers=page.evaluate('SillyTavern.getContext().getRequestHeaders()'),
                                     data={'extensionSettings': ['neconyan_scene_note']})
        assert response.ok
        assert response.json()['extension_settings']['neconyan_scene_note']['text'] == state['value']
        page.reload(wait_until='networkidle')
        page.wait_for_selector('#neconyan_scene_note', state='attached', timeout=60000)
        page.wait_for_function('''() => {
          const ctx = SillyTavern.getContext();
          return ctx.eventSource.autoFireLastArgs.has(ctx.eventTypes.APP_READY);
        }''', timeout=60000)
        expect(page.locator('#neconyan_scene_note textarea')).to_have_value('<b>Saved literally</b> & a second line')
        lifecycle = page.evaluate(r'''async () => {
          const source = [...document.scripts].find(s => /\/scene-note\/index\.js(?:\?|$)/.test(s.src));
          const ext = await import(source.src);
          ext.deactivate(); ext.deactivate();
          const removed = !document.querySelector('#neconyan_scene_note');
          ext.activate(); ext.activate();
          return {removed, count: document.querySelectorAll('#neconyan_scene_note').length,
            value: document.querySelector('#neconyan_scene_note textarea').value};
        }''')
        assert lifecycle == {'removed': True, 'count': 1, 'value': '<b>Saved literally</b> & a second line'}
        page.evaluate('''async () => {
          const { disableExtension } = await import('/scripts/extensions.js');
          await disableExtension('third-party/scene-note', false);
        }''')
        expect(page.locator('#neconyan_scene_note')).to_have_count(0)
        page.reload(wait_until='networkidle')
        page.wait_for_function('''() => {
          const ctx = window.SillyTavern?.getContext();
          return ctx?.eventSource.autoFireLastArgs.has(ctx.eventTypes.APP_READY);
        }''', timeout=60000)
        expect(page.locator('#neconyan_scene_note')).to_have_count(0)
        page.evaluate('''async () => {
          const { enableExtension } = await import('/scripts/extensions.js');
          await enableExtension('third-party/scene-note', false);
        }''')
        page.reload(wait_until='networkidle')
        expect(page.locator('#neconyan_scene_note textarea')).to_have_value(state['value'], timeout=60000)
        browser.close()
        print(f'PASS: {len(cases)} documented macro results; starter saves to server, survives reload, preserves literal text, cleans up without duplicates and supports host disable/re-enable')


if __name__ == '__main__':
    main()
