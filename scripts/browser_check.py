"""Exercise the built handbook in Chromium, including the Pages path prefix."""
import os
import threading
from pathlib import Path

from playwright.sync_api import expect, sync_playwright
from serve_site import PREFIX, server

ROOT = Path(__file__).resolve().parents[1]
SHOTS = ROOT / 'screenshots'
KEY = 'neconyan-docs:guide-genders:v1'


def contrast(page, selector):
    return page.locator(selector).first.evaluate('''el => {
      const c = getComputedStyle(el);
      const luminance = value => {
        const rgb = value.match(/[\\d.]+/g).slice(0, 3).map(Number).map(n => {
          n /= 255; return n <= .04045 ? n / 12.92 : ((n + .055) / 1.055) ** 2.4;
        });
        return rgb[0] * .2126 + rgb[1] * .7152 + rgb[2] * .0722;
      };
      const a = luminance(c.color), b = luminance(c.backgroundColor);
      return (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
    }''')


def overflow(page):
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'), page.url


def main():
    SHOTS.mkdir(exist_ok=True)
    httpd = server()
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    base = f'http://127.0.0.1:{httpd.server_port}{PREFIX}'
    errors, failures = [], []
    try:
        with sync_playwright() as p:
            executable = os.environ.get('BROWSER_EXECUTABLE')
            browser = p.chromium.launch(headless=True, **({'executable_path': executable} if executable else {}))
            desktop = browser.new_context(viewport={'width': 1280, 'height': 900}, reduced_motion='reduce')
            page = desktop.new_page()
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.on('response', lambda response: failures.append(f'{response.status} {response.url}') if response.status >= 400 else None)
            page.goto(base, wait_until='networkidle')
            expect(page.locator('h1')).to_contain_text('Make yourself at home')
            overflow(page)
            page.screenshot(path=str(SHOTS / 'desktop-home-dark.png'), full_page=True)
            assert contrast(page, '.md-button--primary') >= 4.5
            page.locator('label[title="Switch to light colours"]').click()
            expect(page.locator('body')).to_have_attribute('data-md-color-scheme', 'default')
            assert contrast(page, '.md-button--primary') >= 4.5
            page.screenshot(path=str(SHOTS / 'desktop-home-light.png'), full_page=True)
            page.locator('label[title="Switch to dark colours"]').click()
            page.locator('.guide-settings summary').click()
            pronouns = {'female': 'she/her', 'male': 'he/him', 'neutral': 'they/them'}
            for guide in ('miso', 'taro', 'nori'):
                for gender, label in pronouns.items():
                    page.locator(f'[data-gender-select="{guide}"]').select_option(gender)
                    for portrait in page.locator(f'img[data-guide="{guide}"]').all():
                        expect(portrait).to_have_attribute('src', __import__('re').compile(f'-{gender}\\.(png|webp)$'))
                    expect(page.locator(f'[data-pronouns="{guide}"]').first).to_have_text(label)
                    page.wait_for_function('Array.from(document.querySelectorAll("img[data-guide]")).every(i => i.complete && i.naturalWidth > 0)')
            page.locator('[data-gender-select="miso"]').select_option('male')
            page.locator('[data-gender-select="taro"]').select_option('female')
            page.goto(base + 'start/index.html', wait_until='networkidle')
            expect(page.locator('.guide-note [data-pronouns="miso"]')).to_have_text('he/him')
            page.locator('.guide-settings summary').click()
            expect(page.locator('[data-gender-select="taro"]')).to_have_value('female')
            expect(page.locator('[data-gender-select="nori"]')).to_have_value('neutral')
            page.reload(wait_until='networkidle')
            expect(page.locator('.guide-note img')).to_have_attribute('src', __import__('re').compile('-male.webp$'))
            page.goto(base, wait_until='networkidle')
            shot = page.locator('.screenshot a:visible').first
            shot.focus()
            page.keyboard.press('Enter')
            expect(page.get_by_role('dialog', name='Screenshot viewer')).to_be_visible()
            assert contrast(page, '.screenshot-dialog button') >= 4.5
            page.keyboard.press('Escape')
            expect(page.get_by_role('dialog', name='Screenshot viewer')).not_to_be_visible()
            expect(shot).to_be_focused()
            page.locator('.tabbed-labels label').filter(has_text='phone').click()
            page.locator('.screenshot--phone a:visible').click()
            expect(page.locator('.screenshot-dialog img')).to_have_attribute('src', __import__('re').compile('phone-home.webp$'))
            page.get_by_role('button', name='Close screenshot').click()
            search = page.locator('[data-md-component="search-query"]')
            search.click()
            search.press_sequentially('freeze')
            expect(page.locator('.md-search-result__list')).to_contain_text('freeze', timeout=20000)
            page.keyboard.press('Escape')
            page.goto(base + 'macros/text/', wait_until='networkidle')
            expect(page.locator('#upper')).to_be_visible()
            expect(page.locator('main')).to_contain_text('HELLO')
            page.screenshot(path=str(SHOTS / 'desktop-macros.png'), full_page=False)
            page.goto(base + 'extensions/first-extension/', wait_until='networkidle')
            expect(page.locator('main')).to_contain_text('export function activate')
            assert page.locator('main a[href$="scene-note.zip"]').count() == 1
            # Visit every content page to catch broken images and narrow-screen overflow.
            phone = browser.new_context(viewport={'width': 393, 'height': 852}, is_mobile=True, has_touch=True, device_scale_factor=1, reduced_motion='reduce')
            mobile = phone.new_page()
            mobile.on('pageerror', lambda error: errors.append(str(error)))
            mobile.on('response', lambda response: failures.append(f'{response.status} {response.url}') if response.status >= 400 else None)
            mobile.goto(base, wait_until='networkidle')
            mobile.screenshot(path=str(SHOTS / 'phone-home-dark.png'), full_page=True)
            mobile.locator('.md-header label[for="__drawer"]').click()
            expect(mobile.locator('#__drawer')).to_be_checked()
            expect(mobile.locator('.md-nav--primary')).to_contain_text('Macros')
            mobile.locator('label.md-overlay').click(position={'x': 380, 'y': 400})
            expect(mobile.locator('#__drawer')).not_to_be_checked()
            for path in sorted((ROOT / 'site').rglob('index.html')):
                relative = path.relative_to(ROOT / 'site').as_posix().removesuffix('index.html')
                mobile.goto(base + relative, wait_until='networkidle')
                overflow(mobile)
                assert mobile.evaluate('Array.from(document.querySelectorAll("img[src]")).filter(i => i.loading !== "lazy").every(i => i.complete && i.naturalWidth > 0)'), relative
            mobile.goto(base + 'helpers/notebooks/', wait_until='networkidle')
            mobile.screenshot(path=str(SHOTS / 'phone-notebooks.png'), full_page=False)
            mobile.goto(base + 'macros/pronouns/', wait_until='networkidle')
            mobile.screenshot(path=str(SHOTS / 'phone-pronouns.png'), full_page=False)
            # Corrupt and blocked preference storage must leave usable guide controls.
            page.evaluate('(key) => localStorage.setItem(key, "broken json")', KEY)
            page.goto(base, wait_until='networkidle')
            expect(page.locator('[data-gender-select="miso"]')).to_have_value('neutral')
            blocked = browser.new_context(viewport={'width': 393, 'height': 852})
            blocked.add_init_script('''const get = Storage.prototype.getItem, set = Storage.prototype.setItem;
              Storage.prototype.getItem = function(k) { if (k.startsWith('neconyan-docs:')) throw Error('Blocked'); return get.call(this, k); };
              Storage.prototype.setItem = function(k,v) { if (k.startsWith('neconyan-docs:')) throw Error('Blocked'); return set.call(this, k,v); };''')
            blocked_page = blocked.new_page()
            blocked_page.goto(base, wait_until='networkidle')
            blocked_page.locator('.guide-settings summary').click()
            blocked_page.locator('[data-gender-select="nori"]').select_option('female')
            expect(blocked_page.locator('[role="status"]')).to_contain_text('page')
            offline = browser.new_context(java_script_enabled=False)
            fallback = offline.new_page()
            fallback.goto(base, wait_until='networkidle')
            expect(fallback.locator('h1')).to_be_visible()
            assert fallback.locator('.screenshot a').first.get_attribute('href').endswith('.webp')
            browser.close()
        assert not errors, '\n'.join(errors)
        assert not failures, '\n'.join(failures)
        print('PASS: desktop and phone; every page fits; all nine guide variants; saved choices; search; screenshot keyboard controls; contrast; downloads; storage failures; no-JavaScript reading')
    finally:
        httpd.shutdown()
        httpd.server_close()


if __name__ == '__main__':
    main()
