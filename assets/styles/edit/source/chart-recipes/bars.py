"""EDIT's six editorial data compositions, preserving the registered sample data.

Final SVG geometry is always visible. The player only animates semantic groups;
no animation changes a measurement, baseline or paper-slip unit.
"""
from html import escape
import json
PAPER='#f2eee7';LIGHT='#fcf8f0';INK='#352129';RED='#b64032';SOFT='#e8a496';GRAY='#d8d1c9'


def tr(lang,en,zh):return zh if lang=='zh' else en


def text(x,y,value,size=30,fill=INK,anchor='start',kind='label'):
    attrs=f'x="{x:g}" y="{y:g}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" class="edb-{kind}"'
    if isinstance(value,(list,tuple)):
        value=''.join(f'<tspan x="{x:g}" dy="{0 if i==0 else size*1.4:g}">{escape(str(v))}</tspan>' for i,v in enumerate(value))
    else:value=escape(str(value))
    return f'<text {attrs}>{value}</text>'


def line(x1,y1,x2,y2,color=INK,opacity=.2,width=1.2,dash=None):
    extra=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{color}" stroke-opacity="{opacity}" stroke-width="{width}"{extra}/>'


def rect(x,y,w,h,fill,stroke=None):
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="1.2"' if stroke else '')+'/>'


def motion(content,mode,step,value=None):
    data=f' data-value="{value}"' if value is not None else ''
    return f'<g data-chart-motion="{mode}" data-chart-step="{step}"{data}>{content}</g>'


def legend(x,y,color,label,fg=INK,stroke=None):return rect(x,y-18,20,20,color,stroke)+text(x+34,y,label,27,fg)


def svg(key,lang,title,desc,content):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1680 610" role="img" aria-labelledby="edb-{key}-{lang}-title edb-{key}-{lang}-desc" data-information-visual="true"><title id="edb-{key}-{lang}-title">{escape(title)}</title><desc id="edb-{key}-{lang}-desc">{escape(desc)}</desc>{content}</svg>'


def section(key,lang,title,unit,subtitle,chart,data,dark=False):
    emphasis={'columns':('next edition.','准备更充分'),'ranking':('matters.','关键处'),'grouped':('Keep meaning.','留下意思'),'stacked':('more room.','更多篇幅'),'waterfall':('final read.','终校')}
    heading=escape(title)
    if key in emphasis:
        word=emphasis[key][1 if lang=='zh' else 0];heading=heading.replace(escape(word),f'<em>{escape(word)}</em>')
    return f'''<section class="slide edit-data ed-bars ed-{key} {'dark-page' if dark else ''}" data-tone="{'dark' if dark else 'light'}" data-title="{escape(title,quote=True)}" data-chart-kind="{key}" data-chart-unit="{escape(unit,quote=True)}" data-provenance="illustrative" data-chart-values='{json.dumps(data,ensure_ascii=False,separators=(',',':'))}'>
  <header class="ed-heading"><h2 class="reveal">{heading}</h2><p class="ed-subtitle reveal">{escape(subtitle)}</p></header>
  <div class="ed-chart" data-chart-container="true">{chart}</div>
</section>'''


def columns(lang):
    values=[24,30,36,42]
    labels=tr(lang,['Issue 01','Issue 02','Issue 03','Issue 04'],['第 01 期','第 02 期','第 03 期','第 04 期'])
    title=tr(lang,'Ready for the next edition.','下一期，准备更充分。')
    base,scale=510,8
    parts=[text(110,20,tr(lang,'Articles cleared for publication','终校通过的待刊文章 · 篇'),27),
           text(1640,20,tr(lang,'Each issue counted separately','每期独立统计，非累计'),27,RED,'end')]
    for tick in [0,10,20,30,40,50]:
        y=base-tick*scale
        parts += [line(110,y,1640,y,opacity=.4 if tick==0 else .12),text(83,y+9,tick,27,anchor='end',kind='number')]
    for i,(x,label,value) in enumerate(zip([320,710,1100,1490],labels,values)):
        top,w,depth,lift=base-value*scale,166,7,5
        front=RED if i==3 else LIGHT;edge='#8d312b' if i==3 else GRAY;cap=SOFT if i==3 else '#e8e2d9'
        faces=''.join([f'<path d="M{x+w/2:g} {top:g}l{depth} {-lift}V{base-lift:g}l{-depth} {lift}Z" fill="{edge}" stroke="{INK}" stroke-opacity=".18"/>',
                       rect(x-w/2,top,w,base-top,front,RED if i==3 else '#c2b8b1'),
                       f'<path d="M{x-w/2:g} {top:g}l{depth} {-lift}h{w}l{-depth} {lift}Z" fill="{cap}" stroke="{INK}" stroke-opacity=".18"/>',
                       line(x-w/2+12,top+13,x+w/2-12,top+13,LIGHT if i==3 else RED,.6,1.4),
                       line(x-w/2+12,top+20,x+w/2-12,top+20,LIGHT if i==3 else INK,.18,1)])
        parts += [f'<g data-front-value="{value}" data-front-baseline="{base}" data-front-top="{top}" data-front-scale="{scale}">',motion(faces,'grow-y',i,value),
                  motion(text(x+3,top-28,value,58,RED if i==3 else INK,'middle','serif'),'fade',i+1),text(x+3,566,label,33,anchor='middle',kind='serif'),'</g>']
    desc=tr(lang,'Articles cleared at the final proof deadline in four separate issues: 24, 30, 36, 42. Counts are independent, not cumulative. Every front face shares a zero baseline and eight pixels per article on a zero-to-50 axis. Seven-pixel paper edges are decorative.','四期在终校截止时通过的待刊文章分别为24、30、36、42篇。各期独立计数，非累计。柱体正面共用零基线，每篇8像素，纵轴0至50篇。7像素浅纸边仅表示材质。')
    return section('columns',lang,title,tr(lang,'ARTICLES CLEARED · COUNT','终校通过的待刊文章 · 篇'),tr(lang,'Four independent issues, counted at the final proof deadline.','四期各自统计，均以终校截止时通过的篇数为准。'),svg('columns',lang,title,desc,''.join(parts)),{'unit':'articles','labels':labels,'values':values,'cumulative':False,'axis_min':0,'axis_max':50,'baseline':base,'scale':scale})


def ranking(lang):
    labels=tr(lang,['Ambiguity','Repetition','Structure','Tone','Typos'],['含义模糊','内容重复','结构问题','语气不当','文字错漏']);values=[36,28,22,14,10]
    title=tr(lang,'Edit where it matters.','把校改，用在关键处。')
    start,scale=410,26
    parts=[]
    for tick in [0,10,20,30,40]:
        x=start+tick*scale
        parts += [line(x,40,x,505,PAPER,.13),text(x,550,tick,27,PAPER,'middle','number')]
    for i,(label,value) in enumerate(zip(labels,values)):
        y=55+i*96;color=SOFT if i<2 else GRAY
        parts += [text(0,y+34,label,43,PAPER,kind='serif'),motion(rect(start,y,value*scale,40,color),'grow-x',i,value),
                  motion(text(start+value*scale+20,y+34,value,38,PAPER,kind='number'),'fade',i+1),line(0,y+67,1640,y+67,PAPER,.17)]
    bracket=f'<path d="M1625 49h15v148h-15" fill="none" stroke="{SOFT}" stroke-width="1.5"/>'
    parts += [motion(bracket,'draw',1),text(0,603,tr(lang,'110 proof marks · One primary category per mark','共 110 处批注 · 每处只归入一个主要类别'),26,PAPER),
              text(1640,603,tr(lang,'64 concern ambiguity or repetition.','其中 64 处，指向模糊或重复。'),30,SOFT,'end','serif')]
    desc=tr(lang,'Primary categories of 110 proof marks: ambiguity 36, repetition 28, structure 22, tone 14, typos 10. The first two categories account for 64 marks. Five bars use the same zero-to-40 axis. Every mark belongs to exactly one primary category.','110处校样批注分为含义模糊36、内容重复28、结构问题22、语气不当14、文字错漏10处。前两项合计64处。五条共用0至40量尺，每处只归入一个主要类别。')
    return section('ranking',lang,title,tr(lang,'PROOF MARKS · COUNT','校样批注 · 处'),tr(lang,'Rank the primary reasons for a mark, then choose the first editing pass.','按批注的主要原因排序，确定第一轮校改的重点。'),svg('ranking',lang,title,desc,''.join(parts)),{'unit':'proof marks','labels':labels,'values':values,'total':110,'top_two':64,'axis_min':0,'axis_max':40},True)


def pictorial(lang):
    title=tr(lang,'Every piece earns its place.','每一篇，都有自己的位置。')
    labels=tr(lang,['Essays','Briefings','Interviews'],['深度文章','内容简报','访谈整理']);values,unit=[32,24,20],4
    parts=[motion(text(0,216,'76',236,RED,kind='serif'),'fade',3),text(4,282,tr(lang,'pieces in one collection','篇内容，组成同一份选集'),29),
           line(4,327,340,327,RED,.65,1.5),text(4,380,tr(lang,['Each proof slip','stands for four pieces.'],['每枚校样','代表 4 篇内容。']),29),
           text(4,521,tr(lang,['The symbols count pieces,','not length or quality.'],['图形只计篇数，','不表示篇幅或质量。']),25),line(390,24,390,567,INK,.22)]
    for row,(label,value) in enumerate(zip(labels,values)):
        y=53+row*172
        parts += [text(435,y+21,label,37,kind='serif')]
        for i in range(value//unit):
            x=760+i*83;color=LIGHT
            slip=''.join([rect(x,y-14,52,78,color,'#c8bbb4'),line(x+6,y-2,x+46,y-2,RED,.9,1.5),
                          line(x+11,y+15,x+40,y+15,INK,.34),line(x+11,y+27,x+36,y+27,INK,.25),
                          f'<path d="M{x+13} {y+44}l7 7 16-19" fill="none" stroke="{RED}" stroke-width="2"/>'])
            parts.append(f'<g data-unit="{unit}" data-row="{row}" data-chart-motion="pop" data-chart-step="{row+i}">{slip}</g>')
        parts += [motion(text(1640,y+40,value,49,RED,'end','serif'),'fade',row+7),line(435,y+109,1640,y+109,INK,.2)]
    desc=tr(lang,'The selected collection contains 32 essays, 24 briefings and 20 interviews: 76 pieces. Every equal-sized proof slip represents four pieces; rows contain eight, six and five slips, 19 in total. Symbols measure count, not length or quality.','选集含深度文章32篇、内容简报24篇、访谈整理20篇，共76篇。每枚等大校样代表4篇，三行分别8、6、5枚，共19枚；图形不编码篇幅或质量。')
    return section('pictorial',lang,title,tr(lang,'SELECTED CONTENT · PIECES','已选内容 · 篇'),tr(lang,'Different formats belong in the same reading collection.','不同体裁，组成同一份选集。'),svg('pictorial',lang,title,desc,''.join(parts)),{'unit':'pieces','labels':labels,'values':values,'per_unit':unit,'data_units':19,'total':76})


def grouped(lang):
    title=tr(lang,'Cut words. Keep meaning.','删去冗词，留下意思。')
    labels=tr(lang,['Welcome','About','Help'],['欢迎页','介绍页','帮助页']);before,after=[240,320,400],[180,240,280]
    base,scale=485,.72
    parts=[legend(0,20,GRAY,tr(lang,'Before editing','编辑前')),legend(335,20,RED,tr(lang,'After editing','编辑后')),
           text(1680,20,tr(lang,'Passage length · English words','段落篇幅 · 英文单词数'),27,anchor='end')]
    for group,(origin,label,a,b) in enumerate(zip([0,585,1170],labels,before,after)):
        parts += [rect(origin,50,510,460,LIGHT),text(origin+276,100,label,44,anchor='middle',kind='serif')]
        for tick in [0,250,500]:
            y=base-tick*scale
            parts += [line(origin+65,y,origin+485,y,opacity=.38 if tick==0 else .14),text(origin+51,y+9,tick,25,anchor='end',kind='number')]
        for series,(x,value,color) in enumerate([(origin+158,a,GRAY),(origin+328,b,RED)]):
            top=base-value*scale
            parts += [motion(rect(x,top,100,base-top,color),'grow-y',group*2+series,value),motion(text(x+50,top-19,value,38,RED if series else INK,'middle','number'),'fade',group*2+series+1)]
    parts += [line(0,545,1680,545,RED,.55),motion(text(840,599,tr(lang,'960 → 700 words. 260 removed.','960 → 700 词，合计减少 260 词。'),42,RED,'middle','serif'),'fade',6)]
    desc=tr(lang,'The same three English passages before and after editing: welcome 240 to 180 words, about 320 to 240, help 400 to 280. Three paper panels share a zero-to-500 axis and 0.72 pixels per word. Total 960 to 700: 260 words removed. This measures length, not comprehension.','同样三段英文编辑前后的单词数：欢迎页240至180，介绍页320至240，帮助页400至280。三张校样共用0至500词量尺，每词0.72像素。总量960至700，减少260词；本图不直接测量理解效果。')
    return section('grouped',lang,title,tr(lang,'PASSAGE LENGTH · ENGLISH WORDS','段落篇幅 · 英文单词数'),tr(lang,'Compare the same three passages. This measures length, not comprehension.','对照同样三段英文的修改前后，仅测量篇幅，不直接测量理解效果。'),svg('grouped',lang,title,desc,''.join(parts)),{'unit':'English words','labels':labels,'before':before,'after':after,'total_before':960,'total_after':700,'words_removed':260,'axis_min':0,'axis_max':500})


def stacked(lang):
    title=tr(lang,'Give the point more room.','给重点，更多篇幅。')
    labels=tr(lang,['Draft 1','Draft 2','Draft 3'],['初稿','二稿','三稿']);series=tr(lang,['Main point','Support','Background'],['主旨表达','论据支撑','背景铺垫']);values=[[30,40,30],[40,40,20],[50,35,15]]
    start,width=330,1250;colors=[RED,SOFT,GRAY]
    parts=[legend(330,20,RED,series[0]),legend(785,20,SOFT,series[1]),legend(1190,20,GRAY,series[2])]
    for tick in [0,25,50,75,100]:
        x=start+width*tick/100
        parts += [line(x,64,x,464,opacity=.14),text(x,563,f'{tick}%',27,anchor='middle',kind='number')]
    for row,(label,vals) in enumerate(zip(labels,values)):
        y=83+row*151
        parts += [text(0,y+45,label,45,kind='serif'),f'<g data-chart-motion="wipe-x" data-chart-step="{row}">']
        x=start
        for i,(value,color) in enumerate(zip(vals,colors)):
            w=width*value/100
            parts += [rect(x,y,w,65,color),text(x+w/2,y+44,f'{value}%',37,LIGHT if i==0 else INK,'middle','number')];x+=w
        parts.append('</g>')
    bracket=f'<path d="M330 473v12h625v-12" fill="none" stroke="{RED}" stroke-width="1.5"/>'
    parts += [motion(bracket,'draw',3),motion(text(642.5,523,tr(lang,'Main point: 30% → 50% (+20 pp)','主旨占比：30% → 50%（+20 个百分点）'),27,RED,'middle'),'fade',3),
              text(start,609,tr(lang,'Each draft uses its own word count; every row totals 100%.','各稿以自身字数为分母，每行合计 100%；总字数不必相同。'),25)]
    desc=tr(lang,'Words by primary function: main point/support/background in Drafts 1,2,3 are 30/40/30, 40/40/20 and 50/35/15 percent. Main-point share rises by 20 percentage points. Every row totals 100% of its own draft, not an equal absolute word count.','三稿按文字主要功能划分，主旨／论据／背景分别为30/40/30、40/40/20、50/35/15%。主旨提高20个百分点。每行合计当稿字数的100%，不代表总字数相同。')
    return section('stacked',lang,title,tr(lang,'WORDS BY PRIMARY FUNCTION · %','按主要功能划分的字数占比 · %'),tr(lang,'The main point gains space as background becomes more selective.','主旨表达的占比提高，背景铺垫变得更有取舍。'),svg('stacked',lang,title,desc,''.join(parts)),{'unit':'percent of draft words','labels':labels,'series':series,'values':values,'axis_min':0,'axis_max':100,'main_point_gain_pp':20,'separate_denominators':True})


def waterfall(lang):
    title=tr(lang,'Leave time for the final read.','为终校，留出时间。')
    labels=tr(lang,['In hand','Added','Fact-check','Rewrite','Still open'],['原有工时','追加工时','事实核查','改写用时','剩余工时']);values=[52,16,-18,-12,38]
    spans=[(0,52),(52,68),(68,50),(50,38),(0,38)];base,scale,bar_width=510,5.3,150;centers=[225,545,865,1185,1505]
    parts=[legend(105,15,PAPER,tr(lang,'Available','可用工时'),PAPER),legend(445,15,SOFT,tr(lang,'Added','追加'),PAPER),legend(735,15,GRAY,tr(lang,'Used','已用'),PAPER),
           text(1640,15,tr(lang,'Staff-hours','单位：人时'),27,PAPER,'end')]
    for tick in [0,20,40,60,80]:
        y=base-tick*scale
        parts += [line(105,y,1645,y,PAPER,.4 if tick==0 else .14),text(80,y+10,tick,28,PAPER,'end','number')]
    for i,(x,label,value,(start,end)) in enumerate(zip(centers,labels,values,spans)):
        top,height=base-max(start,end)*scale,abs(end-start)*scale;color=PAPER if i in (0,4) else SOFT if value>0 else GRAY
        parts += [motion(rect(x-bar_width/2,top,bar_width,height,color),'grow-y',i,value),motion(text(x,top-23,f'+{value}' if i==1 else value,45,SOFT if i==1 else PAPER,'middle','number'),'fade',i+1),text(x,566,label,30,PAPER,'middle')]
        if i<4:parts.append(motion(line(x+bar_width/2,base-end*scale,centers[i+1]-bar_width/2,base-end*scale,SOFT,.75,1.5,'7 6'),'wipe-x',i+1))
    parts += [text(105,609,tr(lang,'Still open = capacity not yet assigned','剩余工时 = 尚未分配的产能'),26,PAPER),text(1640,609,tr(lang,'Net change −14 staff-hours','净变化 −14 人时'),27,SOFT,'end')]
    desc=tr(lang,'Weekly editing capacity in staff-hours: 52 initially available, 16 added, 18 used for fact-checking and 12 used for rewriting; 38 remain unassigned. Cumulative capacity 52 to 68 to 50 to 38, net change minus 14. All bars and connectors use a zero-to-80 axis.','本周编辑工时池：原有52人时，追加16人时，事实核查用去18人时，改写用去12人时，剩余38人时尚未分配。累计52至68至50至38，净变化−14人时。所有柱体与连接线共用0至80量尺。')
    return section('waterfall',lang,title,tr(lang,'WEEKLY EDIT CAPACITY · STAFF-HOURS','每周编辑产能 · 人时'),tr(lang,'52 + 16 − 18 − 12 = 38 staff-hours still available for the next pass.','52 + 16 − 18 − 12 = 38 人时，仍可留给下一轮校阅。'),svg('waterfall',lang,title,desc,''.join(parts)),{'unit':'staff-hours','labels':labels,'values':values,'cumulative':[52,68,50,38,38],'net_change':-14,'axis_min':0,'axis_max':80},True)


def get_slides(lang):
    """Return six editorial data sections, in English or Chinese."""
    lang='zh' if lang in ('zh','zh-CN') else 'en'
    return [fn(lang) for fn in (columns,ranking,pictorial,grouped,stacked,waterfall)]


def validate_data():
    """Validate the actual generated quantities, geometry, semantics, and hooks."""
    import math
    import re
    import xml.etree.ElementTree as ET

    def require(test, why):
        if not test:
            raise ValueError('EDIT bars: ' + why)

    def close(a, b):
        return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)

    report, reference = {'passed': True, 'languages': {}}, None
    for lang in ('en', 'zh'):
        slides = get_slides(lang)
        require(len(slides) == 6, 'expected six sections')
        data, total_hooks = [], 0
        for i, s in enumerate(slides):
            data.append(json.loads(re.search(r"data-chart-values='([^']+)'", s).group(1)))
            root = ET.fromstring(re.search(r'<svg\b.*?</svg>', s, re.S).group(0))
            require(root.attrib.get('viewBox') == '0 0 1680 610', 'wrong chart coordinates')
            require('data-information-visual' in root.attrib and 'data-chart-container' in s, 'missing information-chart contract')
            require('artwork-slot' not in s, 'a data chart cannot be replaceable artwork')
            hooks = [e for e in root.iter() if 'data-chart-motion' in e.attrib]
            require(bool(hooks), f'{i}: no semantic motion hooks')
            total_hooks += len(hooks)
            require(all(e.attrib['data-chart-motion'] in {'grow-y', 'grow-x', 'wipe-x', 'draw', 'pop', 'fade'} and int(e.attrib['data-chart-step']) >= 0 for e in hooks), f'{i}: bad motion hook')
            require(all(e.tag.rsplit('}', 1)[-1] not in {'image', 'script', 'foreignObject'} for e in root.iter()), 'SVG must be self-contained vector content')
            require(all(float(e.attrib['font-size']) >= 25 for e in root.iter() if 'font-size' in e.attrib), 'chart type below 25px')
        a, b, c, d, e, f = data
        require(a['values'] == [24, 30, 36, 42] and not a['cumulative'], 'separate issue counts')
        require(a['axis_min'] == 0 and all(0 <= v <= a['axis_max'] for v in a['values']), 'column axis')
        faces = re.findall(r'data-front-value="([0-9.]+)" data-front-baseline="([0-9.]+)" data-front-top="([0-9.]+)" data-front-scale="([0-9.]+)"', slides[0])
        require(len(faces) == 4 and all(close((float(base)-float(top))/float(scale), float(value)) for value, base, top, scale in faces), 'paper-stack front heights')
        require(b['values'] == sorted(b['values'], reverse=True) and sum(b['values']) == b['total'] == 110, 'proof ranking and total')
        require(sum(b['values'][:2]) == b['top_two'] == 64, '64 proof marks claim')
        require(b['axis_min'] == 0 and max(b['values']) <= b['axis_max'], 'ranking scale')
        symbols = re.findall(r'data-unit="(\d+)"', slides[2])
        require(len(symbols) == c['data_units'] == 19 and all(int(n) == c['per_unit'] == 4 for n in symbols), 'proof-slip unit')
        require(sum(c['values']) == c['total'] == len(symbols) * c['per_unit'] == 76 and all(v % c['per_unit'] == 0 for v in c['values']), 'proof-slip totals')
        require(sum(d['before']) == d['total_before'] == 960 and sum(d['after']) == d['total_after'] == 700, 'word-count totals')
        require(d['total_before'] - d['total_after'] == d['words_removed'] == 260, '260-word reduction')
        require(d['axis_min'] == 0 and all(0 <= v <= d['axis_max'] for v in d['before'] + d['after']), 'word-count axis')
        require(all(sum(row) == 100 and len(row) == len(e['series']) for row in e['values']) and e['separate_denominators'], 'composition denominators')
        require(e['values'][-1][0] - e['values'][0][0] == e['main_point_gain_pp'] == 20, 'main-point share gain')
        require(e['axis_min'] == 0 and e['axis_max'] == 100, 'stacked axis')
        v = f['values']; running = v[0]; balances = [running]
        for change in v[1:-1]:
            running += change
            balances.append(running)
        balances.append(v[-1])
        require(running == v[-1] == 38 and balances == f['cumulative'], 'staff-hour conservation')
        require(v[1] > 0 and all(n < 0 for n in v[2:-1]), 'capacity inflow and usage signs')
        require(v[-1] - v[0] == f['net_change'] == -14, 'capacity net change')
        require(f['axis_min'] == 0 and all(0 <= n <= f['axis_max'] for n in balances), 'capacity axis')
        quantities = [{k: v for k, v in item.items() if k not in {'labels', 'series'}} for item in data]
        if reference is None:
            reference = quantities
        else:
            require(quantities == reference, 'bilingual quantitative mismatch')
        report['languages'][lang] = {'sections': 6, 'svg_charts': 6, 'data_symbols': 19, 'motion_hooks': total_hooks, 'numeric_claims': 'PASS', 'geometry': 'PASS', 'axes_and_units': 'PASS'}
    return report
