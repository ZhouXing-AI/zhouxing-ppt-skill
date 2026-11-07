"""Prepare the approved full Chinese font pair without changing English entries."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib, json, time, http.client
from fontTools.ttLib import TTFont
from fontTools.ttLib import woff2
import fontTools

ROOT = Path(__file__).resolve().parent
ORIG = ROOT / 'originals-cjk'
ORIG.mkdir(exist_ok=True)
sha = lambda data: hashlib.sha256(data).hexdigest()
prior_manifest = json.loads((ROOT/'font-manifest-cjk.json').read_text()) if (ROOT/'font-manifest-cjk.json').exists() else {}
known_originals = {Path(item['file']).name:item['sha256'] for item in prior_manifest.get('originals',[])}
def get(url):
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={'User-Agent':'zhouxing-font-audit'}), timeout=90) as response:
                return response.read()
        except (OSError, http.client.HTTPException):
            if attempt == 2: raise
            time.sleep(attempt + 1)
pins = {'swei_spring':'365dde98b93b82fa809acb91587b63b0fbde1c0a',
    'wenkai_gb_tag':'v1.530'}
if (ROOT/'cjk-source-pins.json').exists():
    pins = json.loads((ROOT/'cjk-source-pins.json').read_text())
else:
    pins['wenkai_gb_commit'] = json.loads(get('https://api.github.com/repos/lxgw/LxgwWenKaiGB/commits/v1.530'))['sha']
(ROOT/'cjk-source-pins.json').write_text(json.dumps(pins, indent=2)+'\n')
swei_base = 'https://raw.githubusercontent.com/max32002/swei-spring/'+pins['swei_spring']+'/'
wenkai_base = 'https://raw.githubusercontent.com/lxgw/LxgwWenKaiGB/'+pins['wenkai_gb_commit']+'/'
jobs = [
 ('SweiSpringSugarCJKsc-Black.ttf', swei_base+quote('CJK SC/SweiSpringSugarCJKsc-Black.ttf'), None),
 ('SweiSpringSugarCJKsc-Black.woff2', swei_base+quote('WebFont/CJK SC/SweiSpringSugarCJKsc-Black.woff2'), None),
 ('SweiSpring-OFL.txt', swei_base+'SIL_Open_Font_License_1.1.txt', None),
 ('SweiSpring-README.md', swei_base+'README.md', None),
 ('LXGWWenKaiGB-Regular.ttf', 'https://github.com/lxgw/LxgwWenkaiGB/releases/download/v1.530/LXGWWenKaiGB-Regular.ttf', '5561d48097d92e5ab99fe7b1459d381bbcdff533bfc479207b089c6860c3990e'),
 ('LXGWWenKaiGB-OFL.txt', wenkai_base+'OFL.txt', None),
]
def fetch(job):
    name, url, expected = job
    data = (ORIG/name).read_bytes() if (ORIG/name).exists() else get(url)
    if expected: assert sha(data) == expected, 'Official release digest mismatch: '+name
    if name in known_originals: assert sha(data) == known_originals[name], 'Pinned original SHA mismatch: '+name
    (ORIG/name).write_bytes(data)
    print('Downloaded',name,len(data),flush=True)
    return {'file':'originals-cjk/'+name, 'source_url':url, 'bytes':len(data), 'sha256':sha(data), 'official_release_sha256':expected}
with ThreadPoolExecutor(max_workers=4) as pool:
    originals=list(pool.map(fetch,jobs))

def coverage(font_path, alias, family):
    font = TTFont(font_path)
    points = sorted(font.getBestCmap())
    ranges=[]
    for point in points:
        if ranges and point==ranges[-1][1]+1: ranges[-1][1]=point
        else: ranges.append([point,point])
    data={'font_sha256':sha(font_path.read_bytes()),'family':family,'css_family':alias,'codepoints':len(points),'ranges':ranges}
    target=ROOT/(alias+'-coverage.json')
    target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    return data, sha(target.read_bytes())

display = ROOT/'SketchCJKDisplay.woff2'
display.write_bytes((ORIG/'SweiSpringSugarCJKsc-Black.woff2').read_bytes())
display_font=TTFont(display)
display_ttf=TTFont(ORIG/'SweiSpringSugarCJKsc-Black.ttf')
assert display_font['OS/2'].usWeightClass==900
assert set(display_font.getBestCmap())==set(display_ttf.getBestCmap())

body_ttf=ORIG/'LXGWWenKaiGB-Regular.ttf'
body_font=TTFont(body_ttf,recalcTimestamp=False)
assert body_font['OS/2'].usWeightClass==400
body_points=set(body_font.getBestCmap())
# The converted font receives a non-reserved family name; original TTF is retained.
rename={1:'Sketch CJK',2:'Regular',3:'zhouxing-ppt-skill:SketchCJK-Regular:1.530',
    4:'Sketch CJK Regular',6:'SketchCJK-Regular',16:'Sketch CJK',17:'Regular',18:'Sketch CJK Regular',21:'Sketch CJK',22:'Regular'}
for record in body_font['name'].names:
    if record.nameID in rename:
        record.string=rename[record.nameID].encode(record.getEncoding())
body=ROOT/'SketchCJK.woff2'
body_font.flavor='woff2'
body_font.flavorData=woff2.WOFF2FlavorData(transformedTables=set())
# Preserve SFNT tables without the expensive optional glyf preprocessing.
# Quality 9 remains lossless; it favors a bounded build over a marginal size gain.
original_compress=woff2.brotli.compress
def compress_for_web(data, **kwargs):
    kwargs['quality']=9
    return original_compress(data, **kwargs)
woff2.brotli.compress=compress_for_web
print('Compressing full WenKai GB, no glyf transforms, Brotli quality 9',flush=True)
body_font.save(body)
print('Compressed body',body.stat().st_size,flush=True)
assert set(TTFont(body).getBestCmap())==body_points
fonts=[]
for alias,path,family,weight,license_name,upstream in [
    ('SketchCJKDisplay',display,'Swei Spring Sugar CJK SC',900,'SweiSpring-OFL.txt','SweiSpringSugarCJKsc-Black.woff2'),
    ('SketchCJK',body,'Sketch CJK / based on LXGW WenKai GB',400,'LXGWWenKaiGB-OFL.txt','LXGWWenKaiGB-Regular.ttf')]:
    license_bytes=(ORIG/license_name).read_bytes()
    assert b'SIL OPEN FONT LICENSE Version 1.1' in license_bytes
    (ROOT/license_name).write_bytes(license_bytes)
    cov, cov_hash=coverage(path,alias,family)
    fonts.append({'family':alias,'file':'fonts/'+path.name,'weight':str(weight),'style':'normal',
        'coverage_file':'fonts/'+alias+'-coverage.json', 'sha256':sha(path.read_bytes()),
        'bytes':path.stat().st_size,'codepoints':cov['codepoints'],'coverage_sha256':cov_hash,
        'license_file':'fonts/'+license_name,'license_sha256':sha(license_bytes),
        'upstream_filename':upstream,'full_coverage':True,'subset':False})
(ROOT/'fonts-array-cjk.json').write_text(json.dumps([{k:f[k] for k in ['family','file','weight','style','coverage_file']} for f in fonts],ensure_ascii=False,indent=2)+'\n')
manifest={'prepared_at':datetime.now(timezone.utc).isoformat(),'license_spdx':'OFL-1.1',
    'official_sources':['https://github.com/max32002/swei-spring','https://github.com/lxgw/LxgwWenKaiGB'],
    'source_pins':pins,'originals':originals,'fonts':fonts,'fonttools_version':fontTools.__version__,
    'original_files_scope':'Preparation workspace cache only; originals-cjk is excluded from the distributable Skill. Restore original bytes from these pinned source URLs and verify the listed SHA-256 values.',
    'compression':{'transformed_tables':[],'brotli_quality':9,'lossless':True},
    'no_text_subsetting':True,'english_font_entries_modified':False,
    'modifications':{'SketchCJKDisplay':'Official complete WOFF2 original bytes copied unchanged; CSS alias only.',
        'SketchCJK':'Full official TTF converted to WOFF2; only font primary family/style names renamed to Sketch CJK to avoid reserved LXGW names. Glyphs, outlines, metrics and cmap retained.'}}
(ROOT/'font-manifest-cjk.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'fonts':fonts,'total_bytes':sum(f['bytes'] for f in fonts)},ensure_ascii=False,indent=2))
