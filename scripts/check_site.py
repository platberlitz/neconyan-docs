"""Check local links, reference coverage and the downloadable example."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from zipfile import ZipFile

from hooks import GROUPS, catalogue

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
BASE = 'https://platberlitz.github.io/neconyan-docs/'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.issues = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.issues.append(f"Duplicate id: {attrs['id']}")
            self.ids.add(attrs['id'])
        for attribute in ('href', 'src', 'poster'):
            if attrs.get(attribute):
                self.links.append((tag, attrs[attribute]))
        if tag == 'img' and 'alt' not in attrs:
            self.issues.append('Image has no alternative text attribute')


def main():
    pages = {p: Page(p.read_text()) for p in SITE.rglob('*.html')}
    assert pages, 'Build the site first'
    errors = []
    for path, page in pages.items():
        errors += [f'{path.relative_to(SITE)}: {issue}' for issue in page.issues]
        relative = path.relative_to(SITE).as_posix()
        source_url = urljoin(BASE, relative.removesuffix('index.html'))
        for tag, value in page.links:
            target = urlsplit(urljoin(source_url, value))
            if target.scheme not in ('http', 'https') or target.netloc != urlsplit(BASE).netloc:
                continue
            prefix = urlsplit(BASE).path
            if not target.path.startswith(prefix):
                errors.append(f'{relative}: link escapes project URL: {value}')
                continue
            destination = SITE / unquote(target.path[len(prefix):])
            if destination.is_dir():
                destination /= 'index.html'
            if not destination.exists():
                errors.append(f'{relative}: missing file: {value}')
            elif tag == 'a' and target.fragment and destination in pages:
                fragment = unquote(target.fragment)
                if fragment not in pages[destination].ids:
                    errors.append(f'{relative}: missing anchor: {value}')
    for css in SITE.rglob('*.css'):
        for value in re.findall(r'url\([\'"]?([^\)\'\"]+)', css.read_text()):
            if value.startswith(('data:', 'http:', 'https:', '#', '/')):
                continue
            if not (css.parent / unquote(urlsplit(value).path)).exists():
                errors.append(f'{css.relative_to(SITE)}: missing CSS asset: {value}')
    macros = catalogue()
    assert len(macros) == 201, 'Review the catalogue count when updating it'
    for macro in macros:
        groups = [group for group, categories in GROUPS.items() if macro['category'] in categories]
        assert len(groups) == 1, macro['name']
        path = SITE / f'macros/{groups[0]}/index.html'
        anchor = 'comment' if macro['name'] == '//' else macro['name'].lower().replace('_', '-')
        assert anchor in pages[path].ids, f"Missing macro: {macro['name']}"
        for alias in macro['aliases']:
            assert alias['alias'] in path.read_text(), f"Missing alias: {alias['alias']}"
    search = json.loads((SITE / 'search/search_index.json').read_text())
    assert any('freeze' in entry['text'] for entry in search['docs']), 'Reference missing from search'
    example = ROOT / 'docs/assets/downloads/scene-note'
    with ZipFile(SITE / 'assets/downloads/scene-note.zip') as archive:
        for path in example.iterdir():
            assert archive.read(f'scene-note/{path.name}') == path.read_bytes(), path.name
        assert 'scene-note/LICENSE' in archive.namelist()
    for path in (ROOT / 'docs').rglob('*.md'):
        assert '\u2014' not in path.read_text(), f'Em dash in {path}'
    for path in pages:
        assert '<!-- macro-reference:' not in path.read_text(), f'Unexpanded reference in {path}'
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} HTML pages, local links and assets, all 201 macros and aliases, search, starter archive')


if __name__ == '__main__':
    main()
