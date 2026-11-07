#!/usr/bin/env python3
"""Render the selected working deck's reusable extension layouts, without replacing its slides."""
import argparse,importlib.util,json,sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--project',required=True,type=Path)
    p.add_argument('--lang',choices=['en','zh','zh-CN'])
    p.add_argument('--output',required=True,type=Path)
    a=p.parse_args();project=a.project.expanduser().resolve();out=a.output.expanduser().resolve()
    if out.exists():p.error('Output already exists; choose a new fragment file.')
    recipe=project/'source/expansion30.py'
    if not recipe.is_file():p.error('Working deck has no source/expansion30.py recipe.')
    meta=json.loads((project/'deck.json').read_text());lang=a.lang or meta.get('lang','en')
    sys.dont_write_bytecode=True
    spec=importlib.util.spec_from_file_location('layout_extensions',recipe);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    module.validate_data();sections=module.get_slides(lang)
    if not sections or not all(isinstance(s,str) and '<section' in s for s in sections):p.error('Recipe must return non-empty slide sections.')
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text('\n\n'.join(sections)+'\n')
    print(json.dumps({'output':str(out),'sections':len(sections),'language':lang,'complete_deck':False},ensure_ascii=False))

if __name__=='__main__':main()
