#!/usr/bin/env python3
"""Render FOCUS's fourteen bilingual chart/layout recipes into a new HTML fragment."""
import argparse
import importlib.util
import json
import sys
from pathlib import Path


def render(project, lang):
    """Use the work copy's own data recipes; do not rewrite or rebuild the deck."""
    metadata = json.loads((project / 'deck.json').read_text(encoding='utf-8'))
    if metadata.get('style') != 'focus':
        raise ValueError('This renderer requires a FOCUS working copy.')
    sys.dont_write_bytecode = True
    recipe_dir = project / 'source' / 'chart-recipes'
    modules = {}
    for name in ('extras', 'bars', 'analysis_charts'):
        source = recipe_dir / (name + '.py')
        if not source.is_file():
            raise ValueError('Missing FOCUS recipe: ' + str(source))
        spec = importlib.util.spec_from_file_location('focus_recipe_' + name, source)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.validate_data()
        modules[name] = module
    locale = 'zh' if lang == 'zh-CN' else 'en'
    extras = modules['extras'].get_slides(locale)
    bars = modules['bars'].get_slides(locale)
    analysis = modules['analysis_charts'].get_slides(locale)
    if (len(extras), len(bars), len(analysis)) != (2, 6, 6):
        raise ValueError('Expected two extras, six bar charts and six analysis charts.')
    # Sample order: card + six bars + six analysis charts + target progress.
    slides = [extras[0], *bars, *analysis, extras[1]]
    if len(slides) != 14 or any(not s.lstrip().startswith('<section') for s in slides):
        raise ValueError('The FOCUS recipes must return fourteen complete sections.')
    return '\n\n'.join(slides) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True, help='FOCUS working-copy directory')
    parser.add_argument('--lang', choices=['en', 'zh-CN'], required=True)
    parser.add_argument('--output', required=True, help='New HTML fragment; refuses overwrite')
    args = parser.parse_args()
    output = Path(args.output).resolve()
    if output.exists():
        parser.error('Output already exists; choose a new file so existing work is preserved.')
    try:
        html = render(Path(args.project).resolve(), args.lang)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open('x', encoding='utf-8') as handle:
            handle.write(html)
    except (ValueError, OSError, AssertionError) as error:
        parser.error(str(error))
    print(str(output))


if __name__ == '__main__':
    main()
