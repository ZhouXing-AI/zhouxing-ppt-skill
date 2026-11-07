#!/usr/bin/env python3
"""Render SHIFT's fourteen bilingual data/layout recipes without overwriting a deck."""
import argparse,importlib.util,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--project',required=True);p.add_argument('--lang',choices=['en','zh-CN'],required=True);p.add_argument('--output',required=True);a=p.parse_args()
project=Path(a.project).resolve();recipes=project/'source/chart-recipes';modules={}
for name in ['extras','bars','analysis_charts']:
 spec=importlib.util.spec_from_file_location(name,recipes/(name+'.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);modules[name]=m
 if hasattr(m,'validate_data'):m.validate_data()
lang='zh' if a.lang=='zh-CN' else 'en';extra=modules['extras'].get_slides(lang);slides=[extra[0]]+modules['bars'].get_slides(lang)+modules['analysis_charts'].get_slides(lang)+[extra[1]];assert len(slides)==14
out=Path(a.output).resolve()
if out.exists():p.error('Output already exists; choose a new file so existing work is preserved.')
out.parent.mkdir(parents=True,exist_ok=True);out.write_text('\n\n'.join(slides)+'\n');print(str(out))
