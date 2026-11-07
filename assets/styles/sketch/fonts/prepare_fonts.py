"""Fetch pinned Google Fonts originals and prepare full-coverage SKETCH webfonts."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import quote
import hashlib
import json
import re
import time
import fontTools
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent
ORIGINALS = ROOT / 'originals'
ORIGINALS.mkdir(exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()
def get(url):
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={'User-Agent': 'zhouxing-ppt-font-audit'}), timeout=45) as response:
                return response.read()
        except OSError:
            if attempt == 2: raise
            time.sleep(1 + attempt)

families = {
    'fraunces': ['Fraunces[SOFT,WONK,opsz,wght].ttf', 'OFL.txt', 'METADATA.pb'],
    'poppins': ['Poppins-Regular.ttf', 'Poppins-Medium.ttf', 'OFL.txt', 'METADATA.pb'],
}
pins_file = ROOT / 'source-pins.json'
if pins_file.exists():
    pins = json.loads(pins_file.read_text())
else:
    pins = {family: json.loads(get('https://api.github.com/repos/google/fonts/commits?path=' + quote('ofl/' + family, safe='') + '&per_page=1'))[0]['sha'] for family in families}
    pins_file.write_text(json.dumps(pins, indent=2) + '\n')
jobs = [(family, name) for family, files in families.items() for name in files]
def download(job):
    family, name = job
    url = f'https://raw.githubusercontent.com/google/fonts/{pins[family]}/ofl/{family}/' + quote(name)
    data = get(url)
    folder = ORIGINALS / family
    folder.mkdir(exist_ok=True)
    target = folder / name
    target.write_bytes(data)
    if name == 'OFL.txt':
        assert b'SIL OPEN FONT LICENSE Version 1.1' in data
        (ROOT / (family.title() + '-OFL.txt')).write_bytes(data)
    return {'family': family, 'file': str(target.relative_to(ROOT)), 'source_url': url,
        'commit': pins[family], 'bytes': len(data), 'sha256': sha(data)}
with ThreadPoolExecutor(max_workers=4) as pool:
    originals = list(pool.map(download, jobs))

fraunces_path = ORIGINALS / 'fraunces/Fraunces[SOFT,WONK,opsz,wght].ttf'
variable = TTFont(fraunces_path)
axes = {axis.axisTag: {'min': axis.minValue, 'default': axis.defaultValue, 'max': axis.maxValue} for axis in variable['fvar'].axes}
webfonts = []
for weight in [600, 700]:
    coordinates = {'SOFT': 100, 'WONK': 1, 'opsz': 72, 'wght': weight}
    font = instantiateVariableFont(TTFont(fraunces_path), coordinates, inplace=True)
    font['OS/2'].usWeightClass = weight
    # No Reserved Font Names are declared by this distribution's copyright header.
    # Change style naming to match the instantiated weight; preserve copyright/license.
    style = 'SemiBold' if weight == 600 else 'Bold'
    for record in font['name'].names:
        if record.nameID in [2, 17]:
            record.string = style.encode(record.getEncoding())
        elif record.nameID == 4:
            record.string = ('Fraunces Soft 72 ' + style).encode(record.getEncoding())
        elif record.nameID == 6:
            record.string = ('FrauncesSoft72-' + style).encode(record.getEncoding())
    font.flavor = 'woff2'
    target = ROOT / ('FrauncesSoft72-' + style + '.woff2')
    font.save(target)
    reopened = TTFont(target)
    assert reopened['OS/2'].usWeightClass == weight and 'fvar' not in reopened
    assert set(reopened.getBestCmap()) == set(variable.getBestCmap())
    webfonts.append({'file': target.name, 'css_family': 'SketchSerif', 'weight': weight,
        'style': 'normal', 'source_file': str(fraunces_path.relative_to(ROOT)),
        'variation_coordinates': coordinates, 'unicode_codepoints': len(reopened.getBestCmap()),
        'full_coverage': True, 'subset': False, 'bytes': target.stat().st_size,
        'sha256': sha(target.read_bytes()), 'license': 'Fraunces-OFL.txt'})
for weight, style in [(400, 'Regular'), (500, 'Medium')]:
    source = ORIGINALS / ('poppins/Poppins-' + style + '.ttf')
    font = TTFont(source)
    assert font['OS/2'].usWeightClass == weight
    coverage = set(font.getBestCmap())
    font.flavor = 'woff2'
    target = ROOT / ('Poppins-' + style + '.woff2')
    font.save(target)
    reopened = TTFont(target)
    assert coverage == set(reopened.getBestCmap())
    webfonts.append({'file': target.name, 'css_family': 'SketchSans', 'weight': weight,
        'style': 'normal', 'source_file': str(source.relative_to(ROOT)),
        'unicode_codepoints': len(coverage), 'full_coverage': True, 'subset': False,
        'bytes': target.stat().st_size, 'sha256': sha(target.read_bytes()), 'license': 'Poppins-OFL.txt'})
result = {'prepared_at': datetime.now(timezone.utc).isoformat(), 'official_repository': 'https://github.com/google/fonts',
    'license': 'SIL Open Font License 1.1', 'fonttools_version': fontTools.__version__,
    'source_pins': pins, 'originals': originals, 'fraunces_axes': axes, 'webfonts': webfonts,
    'redistribution': 'Commercial use, embedding, modification and redistribution permitted under OFL 1.1; include copyright and license. Fonts remain OFL, not the project MIT license. Font software may not be sold by itself.',
    'reserved_font_names': 'Neither source OFL copyright header declares a Reserved Font Name.',
    'modifications': 'Fraunces: instantiated full variable font at SOFT=100, WONK=1, opsz=72, wght=600/700; updated instance style names; WOFF2 compression. Poppins: WOFF2 compression only. No glyph subsetting.'}
(ROOT / 'font-manifest.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'pins': pins, 'webfonts': webfonts}, ensure_ascii=False, indent=2))
