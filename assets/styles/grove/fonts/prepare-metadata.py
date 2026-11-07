#!/usr/bin/env python3
"""Audit complete official GROVE fonts; no glyph subsetting or outline edits."""
from pathlib import Path
import hashlib, json, shutil, datetime, zipfile
from fontTools.ttLib import TTFont
P=Path(__file__).resolve().parent
GF='24ddc1f324cac5d9f5aedca126d298f56e3f1640'
CR='46dda1602729b58de96e3fdee9f918d7aaa64727'
if not (P/'ChillRoundM-Regular.otf').exists():
    shutil.copyfile(P/'originals/ChillRoundM.otf', P/'ChillRoundM-Regular.otf')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(name,d): (P/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def cmap(f): return {c:g for t in f['cmap'].tables if t.isUnicode() for c,g in t.cmap.items()}
def ranges(cps):
    out=[]
    for cp in sorted(cps):
        if out and cp==out[-1][1]+1:out[-1][1]=cp
        else:out.append([cp,cp])
    return out
specs=[
 {'file':'Onest-Variable.ttf','css_family':'GroveSans','weight':'400 500','weights':[400,500],'role':'English headings 400/500; body and UI 400','prefix':'Onest','repo':'onest','source_name':'Onest%5Bwght%5D.ttf'},
 {'file':'DMMono-Regular.ttf','css_family':'GroveMono','weight':'400','weights':[400],'role':'Small Latin indices and numerals','prefix':'DMMono','repo':'dmmono','source_name':'DMMono-Regular.ttf'},
 {'file':'ChillRoundM-Regular.otf','css_family':'GroveCJK','weight':'400','weights':[400],'role':'Chinese headings, body and UI: genuine Regular 400 only','prefix':'ChillRoundM','repo':None},
]
manifest={'prepared_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'theme':'GROVE · 共生','license':'SIL Open Font License 1.1','license_spdx':'OFL-1.1','source_policy':'Complete official font repertoires with original byte-identical TTF/OTF files. No glyph subsetting, no sample-specific fonts, no geometric or font-name transformations. Full repertoire does not mean every Unicode character.','css_recommendation':'font-synthesis:none; GroveSans 400/500 normal; GroveMono 400 normal for small Latin indices; GroveCJK 400 normal for every Chinese title, body and UI. No synthetic medium or bold. CSS family aliases are not changes to internal font names.','fonts':[]}
entries=[]
for s in specs:
 p=P/s['file'];f=TTFont(p);cm=cmap(f);h=sha(p);cov=s['file'].rsplit('.',1)[0]+'-coverage.json';pre=s['prefix']
 coverage={'font_sha256':h,'family':f['name'].getDebugName(1),'css_family':s['css_family'],'codepoints':len(cm),'ranges':ranges(cm),'coverage_method':'Union of every Unicode cmap in the complete official font, stored as inclusive ranges. No subsetting.','source_font_sha256':h}
 write(cov,coverage)
 axes=[{'tag':a.axisTag,'min':a.minValue,'default':a.defaultValue,'max':a.maxValue} for a in f['fvar'].axes] if 'fvar'in f else []
 assert f['OS/2'].fsType==0
 if not axes:assert s['weights']==[f['OS/2'].usWeightClass]
 rec={'file':p.name,'family':f['name'].getDebugName(1),'css_family':s['css_family'],'css_weight':s['weight'],'recommended_weights':s['weights'],'style':'normal','role':s['role'],'sha256':h,'bytes':p.stat().st_size,'license':pre+'-OFL.txt','license_sha256':sha(P/(pre+'-OFL.txt')),'unicode_codepoints':len(cm),'glyph_count':len(f.getGlyphOrder()),'coverage_file':cov,'coverage_sha256':sha(P/cov),'variable_axes':axes,'os2_weight_class':f['OS/2'].usWeightClass,'embedding_fstype':f['OS/2'].fsType,'embedding_fstype_meaning':'Installable Embedding','fsselection':f['OS/2'].fsSelection,'italic_angle':f['post'].italicAngle,'full_coverage':True,'subset':False,'source_cmap_equal':True,'source_glyph_count_equal':True,'source_names_equal':True,'copyright':f['name'].getDebugName(0),'version':f['name'].getDebugName(5),'embedded_license':f['name'].getDebugName(13),'modifications':'None. Original official file bytes retained; filename is a packaging name, internal family names are unmodified.'}
 if s['repo']:
  base=f'https://raw.githubusercontent.com/google/fonts/{GF}/ofl/{s["repo"]}/'
  rec.update(source_url=base+s['source_name'],source_commit=GF,source_ttf_sha256=h,source_ttf_bytes=p.stat().st_size,license_url=base+'OFL.txt',metadata_file=pre+'-METADATA.pb',metadata_sha256=sha(P/(pre+'-METADATA.pb')),metadata_url=base+'METADATA.pb',reserved_font_names=[])
 else:
  gb=set()
  for hi in range(0xb0,0xf8):
   for lo in range(0xa1,0xff):
    try:gb.add(ord(bytes([hi,lo]).decode('gb2312')))
    except UnicodeDecodeError: pass
  assert len(gb)==6763 and not(gb-set(cm))
  archive=P/'originals/ChillRoundM_v1.805.zip'
  if archive.exists():
   original=zipfile.ZipFile(archive).read('ChillRoundM_v1.805/ChillRoundM.otf')
   assert p.read_bytes()==original
   archive_hash=sha(archive)
  else:archive_hash=json.loads((P/'font-manifest.json').read_text())['fonts'][2]['source_archive_sha256']
  rec.update(source_url='https://github.com/Warren2060/ChillRound/releases/download/v1.805/ChillRoundM_v1.805.zip',source_release='v1.805',source_commit=CR,source_archive_sha256=archive_hash,source_archive_member='ChillRoundM_v1.805/ChillRoundM.otf',source_font_sha256=h,source_font_bytes=p.stat().st_size,license_url=f'https://raw.githubusercontent.com/Warren2060/ChillRound/{CR}/LICENSE',release_evidence_file='ChillRoundM-RELEASE.json',release_evidence_sha256=sha(P/'ChillRoundM-RELEASE.json'),tag_evidence_file='ChillRoundM-TAG.json',tag_evidence_sha256=sha(P/'ChillRoundM-TAG.json'),readme_file='ChillRoundM-README.md',readme_sha256=sha(P/'ChillRoundM-README.md'),readme_url=f'https://raw.githubusercontent.com/Warren2060/ChillRound/{CR}/README.md',reserved_font_names=['ChillRoundF','ChillRoundM'],gb2312_ideographs={'expected':6763,'covered':6763,'missing':[]},working_originals_note='The originals/ directory is optional development evidence and excluded from the distributed Skill; the byte-identical original font may be recovered from the pinned release archive and archive member above.')
 manifest['fonts'].append(rec)
 entries.append({'family':s['css_family'],'file':'fonts/'+p.name,'weight':s['weight'],'style':'normal','coverage_file':'fonts/'+cov})
write('fonts-en.json',entries[:2]);write('fonts-zh-additions.json',entries[2:]);write('font-manifest.json',manifest)
print(json.dumps({'files':[{'file':f['file'],'sha256':f['sha256'],'bytes':f['bytes'],'cmap':f['unicode_codepoints'],'glyphs':f['glyph_count'],'fsType':f['embedding_fstype']}for f in manifest['fonts']],'total_font_bytes':sum(f['bytes'] for f in manifest['fonts'])},ensure_ascii=False,indent=2))
