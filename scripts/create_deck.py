#!/usr/bin/env python3
"""Copy a confirmed style and build an offline deck; infer locale from the supplied brief."""
import argparse,json,shutil
from pathlib import Path
from build_deck import build,is_han
SKILL=Path(__file__).resolve().parents[1]

def infer_language(text):
    # Explicit output-language intent is resolved by the caller using --lang.
    # Mixed Chinese/English briefs use the Chinese composition; Latin-only uses English.
    if not text.strip() or any(is_han(c) for c in text):return 'zh-CN'
    return 'en'

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',required=True);p.add_argument('--style',default='shift');p.add_argument('--title')
    p.add_argument('--lang',choices=['auto','zh-CN','en'],default='auto',help='Explicit locale overrides brief detection.')
    group=p.add_mutually_exclusive_group();group.add_argument('--prompt',help='User creative brief for language detection; not slide generation.');group.add_argument('--prompt-file',type=Path)
    a=p.parse_args()
    text=a.prompt or ''
    if a.prompt_file:
        try:text=a.prompt_file.expanduser().read_text(encoding='utf-8')
        except OSError as e:p.error(str(e))
    lang=infer_language(text or a.title or '') if a.lang=='auto' else a.lang
    styles=json.loads((SKILL/'styles.json').read_text())['styles']
    if a.style not in [s['id'] for s in styles]:p.error('Unknown style. Available: '+', '.join(s['id'] for s in styles))
    source=SKILL/'assets/styles'/a.style;out=Path(a.out).expanduser().resolve();locale=source/'locales'/lang
    if lang!='en' and not locale.exists():p.error('This style does not contain a template for '+lang)
    if out.exists() and (not out.is_dir() or any(out.iterdir())):p.error('Output must be a new or empty directory. Existing work is never overwritten.')
    out.mkdir(parents=True,exist_ok=True)
    for directory in ['source','fonts','graphics']:
        if (source/directory).exists():shutil.copytree(source/directory,out/directory,dirs_exist_ok=True)
    meta=json.loads((source/'deck.json').read_text())
    if locale.exists():
        meta.update(json.loads((locale/'deck.json').read_text()))
        shutil.copyfile(locale/'slides.html',out/'source/slides.html')
        if (locale/'ui.json').exists():
            shutil.copyfile(locale/'ui.json',out/'source/ui.json')
    meta['lang']=lang
    if a.title:meta['title']=a.title;meta['subtitle']='';meta['download_name']='presentation.html'
    (out/'deck.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
    print(json.dumps({'language':lang,**build(out)},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
