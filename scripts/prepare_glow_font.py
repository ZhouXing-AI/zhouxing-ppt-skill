#!/usr/bin/env python3
"""Build a visually unchanged Glow derivative with unique CJK PDF Unicode mappings.
Development-only utility: requires fontTools. Input: official GlowSansSC-Wide-Heavy.otf.
Usage: prepare_glow_font.py INPUT OUTPUT
"""
import sys,copy,collections,json
from fontTools.ttLib import TTFont
f=TTFont(sys.argv[1]);before=f.getBestCmap().copy();top=f['CFF '].cff.topDictIndex[0];cs=top.CharStrings
order=list(f.getGlyphOrder());indices={g:i for i,g in enumerate(order)};groups=collections.defaultdict(list)
for cp,g in before.items():groups[g].append(cp)
nextcid=max(int(g[3:]) for g in order if g.startswith('cid'))+1;changes={}
for old,cps in groups.items():
    if len(cps)<2 or not any(0x2e80<=cp<=0x9fff or 0xf900<=cp<=0xfaff or 0x20000<=cp<=0x3ffff for cp in cps):continue
    for cp in sorted(cps)[1:]:
        name=f'cid{nextcid:05d}';nextcid+=1
        original=cs[old];original.decompile()
        duplicate=copy.copy(original);duplicate.program=list(original.program)
        cs.charStrings[name]=len(cs.charStringsIndex);cs.charStringsIndex.append(duplicate)
        top.charset.append(name);top.FDSelect.gidArray.append(top.FDSelect.gidArray[indices[old]])
        order.append(name)
        for table in ['hmtx','vmtx']:
            if table in f:f[table].metrics[name]=f[table].metrics[old]
        for table in f['cmap'].tables:
            if table.isUnicode() and cp in table.cmap:table.cmap[cp]=name
        changes[cp]={'from':old,'to':name}
f.setGlyphOrder(order);top.CIDCount=nextcid
for rec in f['name'].names:
    if rec.nameID in [1,4,6,16,18,21]:value='ShiftGlowWideHeavy'
    elif rec.nameID==3:value='ShiftGlowWideHeavy:0.91:PDF1'
    else:continue
    rec.string=value.encode(rec.getEncoding())
f['CFF '].cff.fontNames=['ShiftGlowWideHeavy'];top.FullName='ShiftGlowWideHeavy';top.FamilyName='ShiftGlowWideHeavy'
f.flavor=None;f.save(sys.argv[2]);check=TTFont(sys.argv[2]);assert set(check.getBestCmap())==set(before)
print(json.dumps({'cloned_glyphs':len(changes),'codepoints':len(before),'glyphs':len(order)}))
