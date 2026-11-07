"""Six FOCUS chart compositions: restrained editorial typography and precise scales.

Values remain identical to the registered FOCUS sample. SVGs are the final static
state, with semantic entrance hooks; no visible production labels are emitted.
"""
from html import escape
import json
PAPER='#ededeb'; INK='#162720'; GREEN='#00856c'; DARK='#073d32'; SILVER='#bfcac3'; PALE='#a0d4b6'


def tr(lang,en,zh):return zh if lang=='zh' else en


def text(x,y,label,size=30,fill=INK,anchor='start',kind='label'):
    attrs=f'x="{x:g}" y="{y:g}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" class="fd-bar-{kind}"'
    if isinstance(label,(tuple,list)):
        value=''.join(f'<tspan x="{x:g}" dy="{0 if i==0 else size*1.4:g}">{escape(str(v))}</tspan>' for i,v in enumerate(label))
    else:value=escape(str(label))
    return f'<text {attrs}>{value}</text>'


def line(x1,y1,x2,y2,color=INK,opacity=.2,width=1.2,dash=None):
    return f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{color}" stroke-opacity="{opacity}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'


def rect(x,y,w,h,fill,stroke=None,extra=''):
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="1.1"' if stroke else '')+f' {extra}/>'


def motion(content,mode,step):return f'<g data-chart-motion="{mode}" data-chart-step="{step}">{content}</g>'


def legend(x,y,color,label,fg=INK,outline=None):
    return rect(x,y-17,20,20,color,outline)+text(x+34,y,label,27,fg)


def svg(key,lang,title,desc,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1680 610" role="img" aria-labelledby="focus-{key}-{lang}-title focus-{key}-{lang}-desc" data-information-visual="true"><title id="focus-{key}-{lang}-title">{escape(title)}</title><desc id="focus-{key}-{lang}-desc">{escape(desc)}</desc>{body}</svg>'


def section(key,lang,title,unit,subtitle,chart,data,dark=False):
    emphases={'columns':('built over time.','积累'),'grouped':('Clearer decisions.','判断更一致'),'stacked':('uncertainty','不确定'),'waterfall':('the unknown.','未知')}
    heading=escape(title)
    if key in emphases:
        word=emphases[key][1 if lang=='zh' else 0]
        heading=heading.replace(escape(word),'<em>'+escape(word)+'</em>')
    return f'<section class="slide focus-data fd-bars fd-{key} {("dark-page" if dark else "")}" data-tone="{("dark" if dark else "light")}" data-title="{escape(title,quote=True)}" data-chart-kind="{key}" data-chart-unit="{escape(unit,quote=True)}" data-provenance="illustrative" data-chart-values=\'{json.dumps(data,ensure_ascii=False,separators=(",",":"))}\'><header class="fd-heading"><h2 class="reveal">{heading}</h2><p class="fd-subtitle reveal">{escape(subtitle)}</p></header><div class="fd-chart" data-chart-container="true">{chart}</div></section>'


def columns(lang):
    title=tr(lang,'Evidence, built over time.','证据，在观察中积累。')
    values=[24,38,52,68];labels=tr(lang,['Week 1','Week 2','Week 3','Week 4'],['第 1 周','第 2 周','第 3 周','第 4 周'])
    base,scale=500,5.35
    defs='<defs><linearGradient id="fd-black-silver" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#21382e"/><stop offset=".22" stop-color="#52695d"/><stop offset=".48" stop-color="#ccd8cf"/><stop offset=".61" stop-color="#7d9284"/><stop offset=".82" stop-color="#364e41"/><stop offset="1" stop-color="#142b21"/></linearGradient><linearGradient id="fd-emerald" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#063d31"/><stop offset=".23" stop-color="#00856c"/><stop offset=".5" stop-color="#78c4a7"/><stop offset=".64" stop-color="#2b9a7b"/><stop offset="1" stop-color="#07513f"/></linearGradient></defs>'
    parts=[defs,motion(text(0,192,'68',214,GREEN,kind='serif'),'fade',2),
           text(7,251,tr(lang,'verified records by Week 4','第 4 周末，累计核实记录'),29),
           line(0,307,480,307,GREEN,.35),
           motion(text(0,435,'+44',105,INK,kind='serif'),'fade',3),
           text(7,487,tr(lang,'added after Week 1','第 1 周末之后的新增记录'),28),
           text(7,568,tr(lang,'24 → 68, counted cumulatively.','24 → 68，均为累计快照。'),27),
           text(725,20,tr(lang,'Cumulative verified observations','累计核实记录 · 条'),27)]
    for tick in [0,20,40,60,80]:
        y=base-tick*scale
        parts += [line(730,y,1660,y,opacity=.45 if tick==0 else .15),text(703,y+9,tick,27,anchor='end',kind='number')]
    for i,(x,label,value) in enumerate(zip([845,1085,1325,1565],labels,values)):
        top=base-value*scale;w=96;depth=8;lift=6;green=i==3
        faces=''.join([f'<path d="M{x+w/2:g} {top:g}l{depth} {-lift}V{base-lift:g}l{-depth} {lift}Z" fill="{DARK if green else INK}"/>',
                      rect(x-w/2,top,w,base-top,'url(#fd-emerald)' if green else 'url(#fd-black-silver)'),
                      f'<path d="M{x-w/2:g} {top:g}l{depth} {-lift}h{w}l{-depth} {lift}Z" fill="{PALE if green else SILVER}" stroke="#537364" stroke-width=".8"/>',
                      line(x-w/2+2,top+2,x-w/2+2,base-2,PAPER,.5,1),
                      line(x+w/2-3,top+2,x+w/2-3,base-2,INK,.35,1)])
        parts += [f'<g data-series="observations" data-value="{value}" data-front-baseline="{base}" data-front-top="{top:g}">',motion(faces,'grow-y',i),motion(text(x+3,top-27,value,43,GREEN if green else INK,'middle','number'),'fade',i+1),text(x+3,552,label,28,anchor='middle'),'</g>']
    desc=tr(lang,'Cumulative verified observations at week-end:24,38,52,68. These are snapshots, not weekly additions. Forty-four records were added after Week1 through Week4. The front faces share a zero baseline and5.35 pixels per record; shallow metal edges are decorative.','四个周末累计核实记录为24、38、52、68条，是累计快照而非每周新增。第1周末至第4周末新增44条。柱体正面共同从零起算，每条记录5.35像素；浅金属边沿仅作材质表达。')
    data={'unit':'observations','labels':labels,'values':values,'cumulative':True,'measurement':'week-end snapshot','comparison':'end of Week 1 to end of Week 4','axis_min':0,'axis_max':80,'gain':44,'scale':scale,'baseline':base}
    return section('columns',lang,title,tr(lang,'CUMULATIVE VERIFIED OBSERVATIONS','累计已核实记录'),tr(lang,'Cumulative verified records at each week-end, counted on the same basis.','四个周末的累计核实记录（条），采用同一统计口径。'),svg('columns',lang,title,desc,''.join(parts)),data)


def ranking(lang):
    title=tr(lang,'Start with the largest gap.','先看最大的信息缺口。')
    labels=tr(lang,['User needs','Cost','Delivery','Risk'],['用户需求','成本约束','交付安排','潜在风险']);values=[36,24,18,12]
    start,scale=90,37.5
    parts=[]
    for tick in [0,10,20,30,40]:
        x=start+tick*scale
        parts += [line(x,54,x,498,PAPER,.12),text(x,571,tick,28,PAPER,'middle','number')]
    for i,(label,value) in enumerate(zip(labels,values)):
        y=68+i*126;color=PALE if i==0 else SILVER
        parts += [text(start,y-22,label,44,PAPER,kind='serif'),
                  motion(text(start+value*scale,y-22,value,39,color,'end','number'),'fade',i+1),
                  motion(rect(start,y,value*scale,34,color),'grow-x',i),
                  line(start,y+34,1590,y+34,PAPER,.18,1)]
    parts += [text(90,610,tr(lang,'Mentions in decision review','决策评审提及次数'),26,PAPER),
              text(1590,610,tr(lang,'36 of 90 mentions concern user needs — 40%.','90 次提及中的 36 次，指向用户需求：40%。'),26,PALE,'end')]
    desc=tr(lang,'Information gaps in decision reviews: user needs36,cost24,delivery18,risk12;90 total mentions. User needs are exactly40%. Four thin horizontal bars share a0–40 scale and one zero origin.','决策评审信息缺口：用户需求36、成本24、交付18、风险12次，共90次。用户需求恰占40%。四条水平细条共用0至40量尺及同一零起点。')
    return section('ranking',lang,title,tr(lang,'MENTIONS IN REVIEW','评审提及次数'),tr(lang,'Rank unanswered questions before deciding where to investigate.','按决策评审中的提及次数排列信息缺口，明确研究重点。'),svg('ranking',lang,title,desc,''.join(parts)),{'unit':'mentions','labels':labels,'values':values,'total':90,'highlight_share':40,'axis_min':0,'axis_max':40},True)


def pictorial(lang):
    title=tr(lang,'Count the evidence.','让证据，可以计数。')
    labels=tr(lang,['Interviews','Tests','Field notes'],['访谈记录','试验记录','现场笔记']);values=[50,35,25];unit=5
    parts=[line(0,6,1680,6,INK,.45)]
    for col,(origin,label,value) in enumerate(zip([0,575,1150],labels,values)):
        if col:parts.append(line(origin-30,6,origin-30,535,INK,.22))
        parts += [text(origin+3,62,label,45,kind='serif'),motion(text(origin,211,value,142,GREEN,kind='serif'),'fade',col+1),
                  text(origin+163,202,tr(lang,'records','份记录'),28)]
        for i in range(value//unit):
            x=origin+8+(i%5)*96;y=286+(i//5)*117
            glyph=''.join([f'<path d="M{x} {y}h32l16 16v59h-48Z" fill="{PAPER}" stroke="{GREEN}" stroke-width="1.7"/>',
                           f'<path d="M{x+32} {y}v16h16" fill="none" stroke="{GREEN}" stroke-width="1.5"/>',
                           line(x+10,y+35,x+36,y+35,GREEN,.7,1.2),line(x+10,y+47,x+31,y+47,GREEN,.5,1.2)])
            parts.append(f'<g data-unit="{unit}" data-row="{col}" data-chart-motion="pop" data-chart-step="{col+i}">{glyph}</g>')
    parts += [line(0,555,1680,555,INK,.45),text(0,597,tr(lang,'Each document = 5 records','每枚文档 = 5 份记录'),27),text(1680,597,tr(lang,'110 records. Three source types.','110 份记录，来自三类来源。'),33,GREEN,'end','serif')]
    desc=tr(lang,'Interviews50,tests35,field notes25 records. Each equal-sized document represents five records:10,7,5 documents,22 in all,110 records total. A record is an archived evidence item, not a unique participant.','访谈50份、试验35份、现场笔记25份。每个等大的文档表示5份记录，三组分别10、7、5个图形，合计22个与110份记录。记录是一份归档证据，并不等同于独立参与者。')
    return section('pictorial',lang,title,tr(lang,'RESEARCH RECORDS','研究记录数量'),tr(lang,'One document represents five records. A record is an evidence item, not a participant.','每枚文档代表 5 份归档证据；记录数并不等同于参与者人数。'),svg('pictorial',lang,title,desc,''.join(parts)),{'unit':'records','labels':labels,'values':values,'per_unit':unit,'total':110,'data_units':22})


def grouped(lang):
    title=tr(lang,'Better briefs. Clearer decisions.','边界更清楚，判断更一致。')
    labels=tr(lang,['Strategy','Delivery','Discovery'],['战略讨论','交付评审','探索研究']);before,after=[48,56,60],[72,76,84]
    start,scale=425,11.7
    parts=[legend(start,20,SILVER,tr(lang,'Before','调整前')),legend(720,20,GREEN,tr(lang,'After','调整后')),
           text(1660,20,tr(lang,'Next-action clarity · %','下一步行动清晰度 · %'),26,anchor='end')]
    for tick in [0,25,50,75,100]:
        x=start+tick*scale
        parts += [line(x,54,x,505,opacity=.14),text(x,567,f'{tick}%',28,anchor='middle',kind='number')]
    for group,(label,a,b) in enumerate(zip(labels,before,after)):
        y=84+group*165
        parts += [text(0,y+48,label,43,kind='serif')]
        for series,(value,color) in enumerate([(a,SILVER),(b,GREEN)]):
            yy=y+series*44
            parts += [motion(rect(start,yy,value*scale,29,color),'grow-x',group*2+series),motion(text(start+value*scale+17,yy+25,f'{value}%',32,GREEN if series else INK,kind='number'),'fade',group*2+series+1)]
        parts.append(line(0,y+108,1660,y+108,opacity=.22))
    parts.append(text(0,610,tr(lang,'Strategy reviews: 48% → 72%, a gain of 24 percentage points.','战略讨论：48% → 72%，提升 24 个百分点。'),28,GREEN,kind='serif'))
    desc=tr(lang,'Reviewers able to name the next action, before/after:strategy48/72%,delivery56/76%,discovery60/84%. Every horizontal pair uses a common0–100% axis. Strategy increases24 percentage points.','能够说明下一步行动的评审者，调整前后分别为：战略48%/72%，交付56%/76%，探索60%/84%。三个横向成对图共用0至100%量尺，战略讨论提高24个百分点。')
    return section('grouped',lang,title,tr(lang,'NEXT-ACTION CLARITY · %','下一步行动清晰度 · %'),tr(lang,'The share of reviewers who can name the next action, before and after clearer briefs.','任务边界调整前后，能够明确说出下一步行动的评审者比例。'),svg('grouped',lang,title,desc,''.join(parts)),{'unit':'percent','labels':labels,'before':before,'after':after,'highlight_index':0,'highlight_gain':24,'axis_min':0,'axis_max':100})


def stacked(lang):
    title=tr(lang,'Make uncertainty visible.','把不确定，摆在眼前。')
    labels=tr(lang,['Early','Midpoint','Decision'],['初步观察','中期研究','决策之前']);series=tr(lang,['Verified','Assumptions','Open questions'],['已核实','暂定假设','开放问题'])
    values=[[35,25,40],[50,30,20],[65,25,10]]
    parts=[legend(175,20,GREEN,series[0]),legend(670,20,SILVER,series[1]),legend(1165,20,PALE,series[2])]
    base,scale=500,4
    for tick in [0,25,50,75,100]:
        y=base-tick*scale
        parts += [line(175,y,1535,y,opacity=.35 if tick==0 else .14),text(145,y+10,f'{tick}%',27,anchor='end',kind='number')]
    for col,(center,label,vals) in enumerate(zip([425,885,1345],labels,values)):
        y=base
        parts.append(f'<g data-chart-motion="grow-y" data-chart-step="{col}">')
        for i,(value,color) in enumerate(zip(vals,[GREEN,SILVER,PALE])):
            h=value*scale;y-=h
            parts += [rect(center-132,y,264,h,color),text(center,y+h/2+11,f'{value}%',32,PAPER if i==0 else INK,'middle','number')]
        parts += ['</g>',text(center,556,label,36,anchor='middle',kind='serif')]
    parts.append(text(840,609,tr(lang,'Open questions: 40% at the start, 10% before the decision.','开放问题的占比，从最初的 40% 降至决策前的 10%。'),27,anchor='middle'))
    desc=tr(lang,'Evidence status at early,midpoint,decision stages. From bottom to top,verified/assumptions/open questions:35/25/40%,50/30/20%,65/25/10%. Each column is exactly100%,with a shared0–100% vertical axis.','初步、中期、决策前的证据状态，按底部至顶部的已核实/暂定假设/开放问题排序：35/25/40%、50/30/20%、65/25/10%。每根柱均为100%，共用0至100%纵轴。')
    return section('stacked',lang,title,tr(lang,'SHARE OF EVIDENCE · %','证据状态占比 · %'),tr(lang,'As research progresses, a larger share of the evidence becomes verified.','从初步观察到决策，已核实信息的占比逐步增加。'),svg('stacked',lang,title,desc,''.join(parts)),{'unit':'percent','labels':labels,'series':series,'values':values,'axis_min':0,'axis_max':100})


def waterfall(lang):
    title=tr(lang,'Keep room for the unknown.','给未知，留一份余量。')
    labels=tr(lang,['Opening','Added','Fieldwork','Prototypes','Available'],['期初预算','追加投入','实地研究','原型验证','可用余额']);values=[80,30,-25,-20,65]
    parts=[legend(105,18,PAPER,tr(lang,'Balance','预算余额'),PAPER),legend(430,18,PALE,tr(lang,'Added budget','追加预算'),PAPER),legend(840,18,SILVER,tr(lang,'Spend','研究支出'),PAPER),
           text(1650,18,tr(lang,'Net change −15','净变化 −15'),28,PALE,'end','number')]
    base,scale,w=510,3.4,160;centers=[240,550,860,1170,1480]
    for tick in [0,30,60,90,120]:
        y=base-tick*scale
        parts += [line(105,y,1650,y,PAPER,.3 if tick==0 else .13),text(79,y+10,tick,28,PAPER,'end','number')]
    spans=[(0,80),(80,110),(110,85),(85,65),(0,65)]
    for i,(x,label,value,(start,end)) in enumerate(zip(centers,labels,values,spans)):
        top=base-max(start,end)*scale;h=abs(end-start)*scale
        color=PAPER if i in [0,4] else PALE if value>0 else SILVER
        parts += [motion(rect(x-w/2,top,w,h,color),'grow-y',i),motion(text(x,top-23,f'+{value}' if i==1 else value,42,PALE if i==1 else PAPER,'middle','number'),'fade',i+1),text(x,565,label,29,PAPER,'middle')]
        if i<4:parts.append(motion(line(x+w/2,base-end*scale,centers[i+1]-w/2,base-end*scale,PAPER,.6,1.3,'7 6'),'wipe-x',i+1))
    parts.append(text(105,608,tr(lang,'USD thousands · A measured reserve for the next decision.','单位：千美元 · 为下一次判断，保留可用余量。'),27,SILVER))
    desc=tr(lang,'Research budget in USD thousands: opening80, added30, fieldwork−25, prototypes−20, available65. Cumulative80→110→85→65. Net change−15. Floating bars and connectors share one zero-based0–120 scale.','研究预算，单位千美元：期初80，追加30，实地研究−25，原型验证−20，可用65。累计余额80→110→85→65，净变化−15。浮动柱与连接线共用0至120的零基线量尺。')
    return section('waterfall',lang,title,tr(lang,'RESEARCH BUDGET · USD THOUSANDS','研究预算 · 千美元'),tr(lang,'Research budget (USD thousands): 80 + 30 − 25 − 20 = 65 available.','研究预算（千美元）：80 + 30 − 25 − 20 = 65，保留给下一次判断。'),svg('waterfall',lang,title,desc,''.join(parts)),{'unit':'USD thousands','labels':labels,'values':values,'cumulative':[80,110,85,65,65],'net_change':-15,'axis_min':0,'axis_max':120},True)


def get_slides(lang):
    """Return six self-contained FOCUS sections; accepts en, zh, and zh-CN."""
    lang='zh' if lang in ('zh','zh-CN') else 'en'
    return [fn(lang) for fn in (columns,ranking,pictorial,grouped,stacked,waterfall)]


def validate_data():
    """Recheck current recipes, output SVG structure, scales and narrative claims."""
    import re
    import math
    import xml.etree.ElementTree as ET
    def require(test,why):
        if not test:raise ValueError('FOCUS bar recipes: '+why)
    def close(a,b):return math.isclose(a,b,rel_tol=1e-9,abs_tol=1e-9)
    report={'passed':True,'languages':{}};baseline=None
    for lang in ('en','zh'):
        slides=get_slides(lang);require(len(slides)==6,lang+': six sections required')
        data=[]
        for i,slide in enumerate(slides):
            match=re.search(r"data-chart-values='([^']+)'",slide)
            require(match is not None,f'{lang}/{i}: missing metadata')
            data.append(json.loads(match.group(1)))
            root=ET.fromstring(re.search(r'<svg\b.*?</svg>',slide,re.S).group(0))
            require(root.attrib['viewBox']=='0 0 1680 610',f'{lang}/{i}: wrong coordinate system')
            require('data-information-visual' in root.attrib and 'artwork-slot' not in slide,f'{lang}/{i}: chart/artwork contract')
            ids={e.attrib['id'] for e in root.iter() if 'id' in e.attrib}
            for ref in re.findall(r'url\(#([^)]*)\)',slide):require(ref in ids,f'{lang}/{i}: unresolved local gradient')
            for e in root.iter():
                require(e.tag.rsplit('}',1)[-1] not in {'image','script','foreignObject'},f'{lang}/{i}: external or nonvector content')
        a,b,c,d,e,f=data
        require(len(a['labels'])==len(a['values'])==4,'column category mismatch')
        require(a['axis_min']==0 and all(0<=v<=a['axis_max'] for v in a['values']),'column axis bounds')
        require(close(a['values'][-1]-a['values'][0],a['gain']) and a['gain']==44,'+44 claim')
        front=re.findall(r'data-value="([0-9.]+)" data-front-baseline="([0-9.]+)" data-front-top="([0-9.]+)"',slides[0])
        require(len(front)==4,'front-face geometry metadata')
        require(all(close((float(base)-float(top))/a['scale'],float(v)) for v,base,top in front),'front-face heights do not match zero-baseline values')
        require(len(b['labels'])==len(b['values'])==4 and b['values']==sorted(b['values'],reverse=True),'ranking structure')
        require(b['axis_min']==0 and all(0<=v<=b['axis_max'] for v in b['values']),'ranking axis bounds')
        require(close(sum(b['values']),b['total']) and b['total']>0,'ranking total')
        require(close(b['values'][0]/b['total']*100,b['highlight_share']) and b['highlight_share']==40,'40% share claim')
        units=re.findall(r'data-unit="([0-9.]+)"',slides[2])
        require(len(c['labels'])==len(c['values'])==3 and all(v>=0 and v%c['per_unit']==0 for v in c['values']),'pictorial units')
        require(c['per_unit']==5 and len(units)==c['data_units']==22 and all(float(v)==5 for v in units),'document units and legend')
        require(close(sum(c['values']),c['total']) and close(len(units)*5,c['total']) and c['total']==110,'110 records claim')
        require(len(d['labels'])==len(d['before'])==len(d['after'])==3,'grouped series lengths')
        require(d['axis_min']==0 and d['axis_max']==100 and all(0<=v<=100 for v in d['before']+d['after']),'grouped percentage axis')
        j=d['highlight_index'];require(close(d['after'][j]-d['before'][j],d['highlight_gain']) and d['highlight_gain']==24,'+24 percentage-point claim')
        require(len(e['labels'])==len(e['values'])==3 and len(e['series'])==3,'stacked series lengths')
        require(e['axis_min']==0 and e['axis_max']==100 and all(len(row)==3 and all(0<=v<=100 for v in row) and close(sum(row),100) for row in e['values']),'100% stacked totals')
        v=f['values'];require(len(v)==len(f['labels'])==5,'waterfall categories')
        require(v[0]>=0 and v[1]>=0 and all(x<=0 for x in v[2:-1]),'waterfall inflow/outflow signs')
        run=v[0];balances=[run]
        for change in v[1:-1]:run+=change;balances.append(run)
        balances.append(v[-1])
        require(close(run,v[-1]) and balances==f['cumulative'],'waterfall cumulative balances')
        require(f['axis_min']==0 and all(0<=x<=f['axis_max'] for x in balances),'waterfall axis bounds')
        require(close(v[-1]-v[0],f['net_change']) and f['net_change']==-15,'net change -15 claim')
        numbers=[{k:v for k,v in item.items() if k not in ('labels','series')} for item in data]
        if baseline is None:baseline=numbers
        else:require(numbers==baseline,'Chinese and English data differ')
        report['languages'][lang]={'sections':6,'charts':6,'pictorial_units':22,'numeric_claims':'PASS','zero_baselines':'PASS','svg_structure':'PASS'}
    return report
