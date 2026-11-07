#!/usr/bin/env python3
"""Build one offline HTML presentation from a local source project (stdlib only)."""
import argparse,base64,hashlib,json,re
import xml.etree.ElementTree as ET
from html import escape
from html.parser import HTMLParser
from pathlib import Path

class Slides(HTMLParser):
    def __init__(self): super().__init__(); self.titles=[]; self.text=[]; self.stack=[]; self.dot_cjk=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:
            self.stack.append((tag,'dot' in a.get('class','').split()))
        if 'slide' in a.get('class','').split():
            if not a.get('data-title'): raise ValueError('Each slide needs a non-empty data-title for navigation.')
            self.titles.append(a['data-title'])
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0]==tag:
                del self.stack[i:];break
    def handle_data(self,data):
        self.text.append(data)
        if any(dot for _,dot in self.stack):self.dot_cjk.update(c for c in data if is_han(c))

def is_han(c):
    n=ord(c)
    return 0x3400<=n<=0x9fff or 0xf900<=n<=0xfaff or 0x20000<=n<=0x323af

def check_cjk(project,meta,parser,ui):
    if parser.dot_cjk:raise ValueError('Chinese characters cannot use the Latin dot font. Use a Chinese heading class instead: '+''.join(sorted(parser.dot_cjk)))
    text=''.join(parser.text+parser.titles)+meta['title']+meta.get('subtitle','')+json.dumps(ui,ensure_ascii=False)
    needed={ord(c) for c in text if is_han(c)}
    if not needed:return
    covered=set()
    for f in meta['fonts']:
        if f.get('coverage_file'):
            p=(project/f['coverage_file']).resolve()
            if project not in p.parents:raise ValueError('Coverage file must be inside the source project.')
            font=(project/f['file']).resolve()
            if project not in font.parents:raise ValueError('Font file must be inside the source project.')
            coverage=json.loads(p.read_text())
            if coverage.get('font_sha256')!=hashlib.sha256(font.read_bytes()).hexdigest():
                raise ValueError('Font coverage metadata does not match '+f['file']+'. Regenerate it from the final font cmap.')
            for lo,hi in coverage['ranges']:covered.update(range(lo,hi+1))
    missing=needed-covered
    if missing:raise ValueError('Bundled Chinese font lacks these characters; add a licensed font with matching coverage metadata before building: '+''.join(chr(n) for n in sorted(missing)))

def json_script(data):return json.dumps(data,ensure_ascii=False).replace('</','<\\/')

def apply_content_layouts(html):
    """Compile the author's per-slide layout choice; do not infer semantics at playback."""
    class Layouts(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=False)
            self.edits=[]
            self.lines=[0]
            for line in html.splitlines(keepends=True):self.lines.append(self.lines[-1]+len(line))
        def handle_starttag(self,tag,attrs):
            a=dict(attrs)
            if tag!='section' or 'slide' not in a.get('class','').split():return
            layout=a.get('data-content-layout')
            if layout is None:return
            if layout not in {'text','visual'}:raise ValueError('data-content-layout must be text or visual.')
            classes=[c for c in a['class'].split() if c!='text-led']
            if layout=='text':classes.append('text-led')
            raw=self.get_starttag_text()
            updated=re.sub(r'(\s)class\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s>]+)',lambda m:m[1]+'class="'+escape(' '.join(classes),quote=True)+'"',raw,count=1,flags=re.I|re.S)
            line,col=self.getpos();start=self.lines[line-1]+col
            self.edits.append((start,start+len(raw),updated))
    parser=Layouts();parser.feed(html)
    for start,end,replacement in reversed(parser.edits):html=html[:start]+replacement+html[end:]
    return html
def artwork_library(project):
    catalog=project/'graphics/catalog.json'
    if not catalog.exists():return None
    data=json.loads(catalog.read_text());ids=set()
    for asset in data['assets']:
        key=asset['id']
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]*',key) or key in ids:raise ValueError('Invalid or duplicate artwork id: '+key)
        ids.add(key)
        path=(catalog.parent/asset['file']).resolve()
        if catalog.parent.resolve() not in path.parents or path.suffix!='.svg':raise ValueError('Artwork must be an SVG inside graphics/.')
        raw=path.read_bytes();root=ET.fromstring(raw)
        if root.tag.rsplit('}',1)[-1]!='svg':raise ValueError('Artwork is not SVG: '+str(path))
        if b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper():raise ValueError('SVG declarations are not supported.')
        for elem in root.iter():
            if elem.tag.rsplit('}',1)[-1].lower() in {'script','foreignobject','image','iframe'}:raise ValueError('Artwork must be self-contained vector geometry: '+key)
            for attr,value in elem.attrib.items():
                if attr.lower().startswith('on'):raise ValueError('SVG event handlers are not supported.')
                if attr.rsplit('}',1)[-1]=='href' and not value.startswith('#'):raise ValueError('SVG external references are not supported.')
                if re.search(r'(?:https?:|file:|javascript:|@import)',value,re.I):raise ValueError('SVG must not contain external resources.')
        asset['data_url']='data:image/svg+xml;base64,'+base64.b64encode(raw).decode()
    return data

def fill_artwork_slots(html,library):
    if not library:return html
    assets={a['id']:a for a in library['assets']}
    def fill(match):
        start=match.group(1);key=re.search(r'data-artwork-id="([^"]+)"',start)
        if not key or key[1] not in assets:raise ValueError('An artwork slot refers to a missing asset.')
        a=assets[key[1]]
        return start+'<img src="'+a['data_url']+'" alt="'+escape(a['name_en'],quote=True)+'" draggable="false"></div>'
    return re.sub(r'(<div\b[^>]*data-artwork-slot="[^"]+"[^>]*>)\s*</div>',fill,html)

def build(project,output=None):
    project=Path(project).resolve();src=project/'source';meta=json.loads((project/'deck.json').read_text());html=(src/'slides.html').read_text()
    meta.pop('presentation_mode',None)
    html=apply_content_layouts(html)
    library=artwork_library(project);html=fill_artwork_slots(html,library)
    for art in sorted((project/'graphics').glob('*.svg')):
        if '__'+art.stem+'__' in html:html=html.replace('__'+art.stem+'__',art.read_text())
    unresolved=re.findall(r'__[A-Za-z][A-Za-z0-9_-]*__',html)
    if unresolved:raise ValueError('Missing graphics: '+', '.join(sorted(set(unresolved))))
    parser=Slides();parser.feed(html)
    if not parser.titles:raise ValueError('The source contains no slides.')
    ui=json.loads((src/'ui.json').read_text()) if (src/'ui.json').exists() else {}
    check_cjk(project,meta,parser,ui)
    fonts=[]
    for f in meta['fonts']:
        p=(project/f['file']).resolve()
        if project not in p.parents:raise ValueError('Font file must be inside the source project.')
        fmt='woff2' if p.suffix=='.woff2' else 'opentype' if p.suffix=='.otf' else 'truetype';mime='font/woff2' if fmt=='woff2' else 'font/otf' if fmt=='opentype' else 'font/ttf'
        unicode_rule=';unicode-range:'+f['unicode_range'] if f.get('unicode_range') else ''
        font_style=f.get('style','normal')
        if font_style not in {'normal','italic'}:raise ValueError('Font style must be normal or italic: '+f['family'])
        fonts.append('@font-face{font-family:'+json.dumps(f['family'])+';font-weight:'+f['weight']+';font-style:'+font_style+';font-display:block;src:url(data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()+') format("'+fmt+'")'+unicode_rule+'}')
    notices={p.name:p.read_text() for p in sorted((project/'fonts').glob('*.txt'))}
    notices.update({p.name:p.read_text() for p in sorted((project/'source').glob('*LICENSE.txt'))})
    title=meta['title']+(' · '+meta['subtitle'] if meta.get('subtitle') else '')
    css=(src/'viewport-base.css').read_text()+'\n'+''.join(fonts)+'\n'+(src/'style.css').read_text()
    if (src/'locale-zh.css').exists():css+='\n'+(src/'locale-zh.css').read_text()
    if (src/'artwork.css').exists():css+='\n'+(src/'artwork.css').read_text()
    for extra_css in ['text-layouts.css','player-controls.css','cursor.css']:
        if (src/extra_css).exists():css+='\n'+(src/extra_css).read_text()
    artwork_data='<script id="artwork-library" type="application/json">'+json_script(library)+'</script>' if library else ''
    artwork_html=(src/'artwork.html').read_text() if (src/'artwork.html').exists() else ''
    artwork_js='<script>'+(src/'artwork.js').read_text().replace('</script','<\\/script')+'</script>' if (src/'artwork.js').exists() else ''
    cursor_data='';cursor_js=''
    if (src/'cursor.js').exists():
        cursor_config=json.loads((src/'cursor.json').read_text())
        cursor_config['svg']=(src/'cursor.svg').read_text()
        cursor_data='<script id="cursor-art" type="application/json">'+json_script(cursor_config)+'</script>'
        cursor_js='<script>'+(src/'cursor.js').read_text().replace('</script','<\\/script')+'</script>'
    chart_js='<script>'+(src/'chart-motion.js').read_text().replace('</script','<\\/script')+'</script>' if (src/'chart-motion.js').exists() else ''
    pdf_scripts=''.join('<script>'+re.sub(r'//# sourceMappingURL=.*', '', (src/name).read_text()).replace('</script', '<\\/script')+'</script>' for name in ['html-to-image.js','pdf-lib.js','pdf-export.js'])
    result='<!doctype html><html lang="'+escape(meta.get('lang','en'),quote=True)+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+'</title><style>'+css+'</style><script id="font-licenses" type="application/json">'+json_script(notices)+'</script><script id="deck-meta" type="application/json">'+json_script(meta)+'</script><script id="deck-ui" type="application/json">'+json_script(ui)+'</script>'+artwork_data+cursor_data+'</head><body><main id="stage" aria-label="'+escape(meta['title'],quote=True)+'">'+html+(src/'navigation.html').read_text()+'</main>'+(src/'controls.html').read_text()+artwork_html+pdf_scripts+cursor_js+chart_js+'<script>'+(src/'player.js').read_text()+'</script>'+artwork_js+'</body></html>'
    out=Path(output).resolve() if output else project/'index.html';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(result)
    return {'output':str(out),'slides':len(parser.titles),'titles':parser.titles,'bytes':out.stat().st_size}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--project',required=True);p.add_argument('--output');a=p.parse_args()
    try:print(json.dumps(build(a.project,a.output),ensure_ascii=False,indent=2))
    except (ValueError,OSError,KeyError,ET.ParseError) as e:p.exit(1,str(e)+'\n')
