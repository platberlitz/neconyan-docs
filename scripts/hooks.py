"""Build downloads and the reviewed, complete macro reference."""
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

import yaml

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    'characters': {'names', 'character'},
    'chat': {'chat', 'state'},
    'prompts': {'prompts'},
    'dates': {'time', 'enhanced-date'},
    'basics': {'utility', 'random'},
    'variables': {'variable', 'enhanced-chatvar'},
    'conditions': {'enhanced-logic', 'enhanced-compat'},
    'text': {'enhanced-text'},
    'lists': {'enhanced-list'},
    'maths': {'enhanced-math'},
    'saved-values': {'enhanced-state'},
    'lorebooks': {'enhanced-lorebook'},
    'pronouns': {'enhanced-pronoun'},
    'special': {'legacy'},
}


def catalogue():
    return json.loads((ROOT / 'data/macro-registry.json').read_text())['registry']


def corrections():
    return yaml.safe_load((ROOT / 'data/macro-notes.yml').read_text())


def plain(text):
    """Format inline macro references without interpreting their brackets."""
    parts = re.split(r'(`[^`]*`|{{.*?}})', text)
    for index, part in enumerate(parts):
        if part.startswith('`'):
            continue
        if part.startswith('{{'):
            parts[index] = f'`{part}`'
            continue
        parts[index] = (part.replace('Capitalizes', 'Capitalises')
                        .replace('Capitalize', 'Capitalise')
                        .replace('capitalize', 'capitalise')
                        .replace('"', "'").replace('\u2014', '; ').replace('\u2013', '-'))
    return ''.join(parts)


def render_macro(macro, notes):
    name = macro['name']
    note = notes.get(name, {})
    anchor = 'comment' if name == '//' else name.lower().replace('_', '-')
    lines = [f'## {name} {{#{anchor}}}', '',
             plain(note.get('description', macro['description'])), '']
    examples = note.get('examples', macro['exampleUsage']) or ['{{' + name + '}}']
    lines += ['```text', examples[0], '```', '']
    if note.get('result'):
        lines += [f"**Result:** {note['result']}", '']
    if note.get('note'):
        lines += [plain(note['note']), '']
    args = macro['unnamedArgDefs']
    aliases = macro['aliases']
    if args or aliases or len(examples) > 1 or macro['list'] is not None:
        details = []
        for arg in args:
            default = arg['defaultValue']
            optional = 'Optional. ' if arg['optional'] else ''
            default_text = ''
            if default is not None and str(default) != 'null':
                default_text = ' Default: empty text.' if default == '' else f' Default: `{default}`.'
            description = note.get('arguments', {}).get(arg['name'], arg['description'])
            details.append(f"- **{arg['name']}**: {optional}{plain(description)}{default_text}")
        if macro['list'] is not None:
            details.append('- **More values**: add each extra item after `::`. See the example for its format.')
        if aliases:
            details.append('- **Other accepted names**: ' + ', '.join(f"`{a['alias']}`" for a in aliases) + '.')
        if len(examples) > 1:
            details += ['', 'More examples:', '', '```text', *examples[1:3], '```']
        detail_lines = '\n'.join(details).splitlines()
        lines += ['??? info "Arguments and other names"', '', *['    ' + line if line else '' for line in detail_lines], '']
    return '\n'.join(lines)


def on_page_markdown(markdown, page, config, files):
    match = re.search(r'<!-- macro-reference: ([a-z-]+) -->', markdown)
    if not match:
        return markdown
    group = match.group(1)
    macros = sorted((m for m in catalogue() if m['category'] in GROUPS[group]), key=lambda m: m['name'].lower())
    notes = corrections()
    rendered = '\n'.join(render_macro(m, notes) for m in macros)
    return markdown.replace(match.group(0), rendered)


def on_pre_build(config):
    macros = catalogue()
    covered = set().union(*GROUPS.values())
    missing = {m['category'] for m in macros} - covered
    if missing:
        raise ValueError(f'Macro categories without documentation: {missing}')
    unknown = set(corrections()) - {m['name'] for m in macros}
    if unknown:
        raise ValueError(f'Macro notes with unknown names: {unknown}')
    example = ROOT / 'docs/assets/downloads/scene-note'
    archive = example.with_suffix('.zip')
    with ZipFile(archive, 'w') as output:
        for path in sorted(example.iterdir()):
            if path.is_file():
                entry = ZipInfo(f'scene-note/{path.name}', (2026, 10, 7, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = 0o644 << 16
                output.writestr(entry, path.read_bytes())
