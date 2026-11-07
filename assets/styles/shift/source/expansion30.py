"""SHIFT: six reusable business layouts (pages 24–29 of the capability sample).
All sample values and wording are retained. Slots are decorative and separate
from information SVGs; native table structures remain editable and accessible.
"""
from html import escape as E
import math,json
THEME="shift"
TYPES=["data-table","option-matrix","timeline","decision-flow","donut","funnel"]
CONFIG={'shift': {'paper': '#e3e3d9',
           'ink': '#1a1302',
           'accent': '#ff661a',
           'muted': '#bcbcbc',
           'soft': '#ffb948',
           'dark': '#1a1302',
           'display': 'ShiftSans,ShiftCJK,sans-serif',
           'body': 'ShiftSans,ShiftCJK,sans-serif',
           'zh': 'ShiftCJK,ShiftSans,sans-serif',
           'weight': '600',
           'zhweight': '900',
           'subject': ['Creative practice', '创意实践'],
           'titles': [['Make the work visible.', '让进展，看得见。'],
                      ['Choose a useful starting point.', '找到合适的起点。'],
                      ['Give each stage its own time.', '每个阶段，都有自己的时间。'],
                      ['A small test decides the next step.', '用一次小试验，决定下一步。'],
                      ['Make room for making.', '把时间，留给动手。'],
                      ['From a spark to a working idea.', '从灵感，到可用的想法。']],
           'sub': [['Four workstreams, one weekly record. Hours are tracked separately from outputs.',
                    '四条工作线，一份周记录。工时与产出分别统计。'],
                   ['Three ways to start. Choose by your available time and intended output.',
                    '三种启动方式，根据可用时间与预期产出来选择。'],
                   ['An eight-week cycle, from first observation to a public release.', '从初次观察到公开发布，安排一个八周的实践周期。'],
                   ['A decision path for a new idea, with an explicit revision route.', '为一个新想法设置明确判断，也为修改留下一条路。'],
                   ['A 40-hour practice week, split into three distinct activities.', '把一周的四十个实践工时，分配给三类不同活动。'],
                   ['One cohort of 100 ideas. Every stage is a subset of the previous stage.',
                    '跟踪同一批一百个想法，每个阶段都是上一阶段的子集。']],
           'rows': [['Observe', '观察'], ['Collect', '收藏'], ['Connect', '连接'], ['Make', '动手']],
           'units': [['notes', '条记录'], ['sources', '份素材'], ['directions', '个方向'], ['prototypes', '个原型']],
           'values': [32, 24, 12, 6],
           'hours': [6, 8, 10, 16],
           'plans': [['A note', '一张笔记'], ['A sketch', '一张草图'], ['A prototype', '一个原型']],
           'time': ['15 min', '60 min', '1 day'],
           'out': [['One observation', '一个观察'], ['Three possibilities', '三种可能'], ['One working test', '一次可用试验']],
           'review': [['Self review', '自行回看'], ['Peer response', '同伴反馈'], ['User feedback', '用户反馈']],
           'phases': [['Observe', '观察'], ['Connect', '连接'], ['Make', '动手'], ['Release', '发布']],
           'shares': [50, 30, 20],
           'sharelabels': [['Making', '动手'], ['Research', '研究'], ['Reflection', '复盘']],
           'funnel': [100, 70, 45, 30],
           'flabels': [['Collected', '收集'], ['Explored', '探索'], ['Tested', '试验'], ['Released', '发布']]}}

def validate_data():
 c=CONFIG['shift']
 assert sum(c['hours'])==40 and sum(c['shares'])==100
 assert len(c['values'])==len(c['rows'])==len(c['units'])==len(c['hours'])==4
 assert c['funnel']==[100,70,45,30]
 assert all(a>=b>0 for a,b in zip(c['funnel'],c['funnel'][1:]))
 assert sum(b-a for a,b in [(0,2),(2,5),(5,7),(7,8)])==8
 assert c['shares']==[50,30,20] and [v*40/100 for v in c['shares']]==[20,12,8]
 return True

def get_css():
 return r'''/* SHIFT refinement: scoped to these six original business layouts. */
.slide.x30.xr{background:#e3e3d9;color:#1a1302;--x-ink:#1a1302;--x-paper:#e3e3d9;--x-accent:#ff661a;--x-muted:#bcbcbc;--x-soft:#ffb948;font-synthesis:none}
.slide.x30.xr:before{opacity:.065;background-size:40px 40px}
.slide.x30.xr.x30-silver{background:#bcbcbc}
.slide.x30.xr.x30-orange{background:#ff661a}
.slide.x30.xr.x30-dark{background:#1a1302;color:#e3e3d9;--x-ink:#e3e3d9;--x-paper:#1a1302;--x-accent:#ff661a}
.slide.x30.xr .x30-heading{position:absolute;left:100px;right:100px;top:76px}
.slide.x30.xr .x30-heading h2{position:static;font:600 94px/1.12 ShiftSans,ShiftCJK,sans-serif;margin:0;letter-spacing:-3px;white-space:nowrap}
.slide.x30.xr .x30-heading p{font:400 27px/1.45 ShiftSans,ShiftCJK,sans-serif;margin:24px 0 0;letter-spacing:0;opacity:.84}
html:lang(zh) .slide.x30.xr .x30-heading h2{font-family:ShiftCJK,ShiftSans,sans-serif;font-size:82px;font-weight:900;line-height:1.2;letter-spacing:0;margin:0}
html:lang(zh) .slide.x30.xr .x30-heading p{font-family:ShiftCJK,ShiftSans,sans-serif;font-size:27px;line-height:1.45;letter-spacing:0}
.slide.x30.xr .x30-body{position:absolute;left:100px;top:350px;width:1720px;height:600px}
.slide.x30.xr .x30-body svg{width:100%;height:100%;display:block;overflow:visible}
.slide.x30.xr svg text{font:400 29px ShiftSans,ShiftCJK,sans-serif;letter-spacing:0;fill:var(--x-ink);font-synthesis:none}
.slide.x30.xr svg .xr-mid{font-size:44px;font-weight:600}
.slide.x30.xr svg .xr-number{font-size:46px;font-weight:500;font-variant-numeric:tabular-nums}
.slide.x30.xr svg .xr-small{font-size:25px}
.slide.x30.xr svg .xr-dot{font-family:ShiftDots,monospace;font-weight:900;font-variation-settings:'ROND' 100;letter-spacing:-.045em}
.slide.x30.xr svg .xr-step{font-size:46px}
.slide.x30.xr svg .xr-metric{font-size:194px}
.slide.x30.xr svg .xr-center-total{font-size:188px}
.slide.x30.xr svg .xr-percent{font-size:78px}
.slide.x30.xr [data-chart-motion]{transform-box:view-box}
.slide.x30.xr .x30-art{position:absolute;pointer-events:none}
.slide.x30.xr .x30-art .artwork-slot{width:100%;height:100%}
.slide.x30.xr .x30-art img{display:block;width:100%;height:100%;object-fit:contain}
.slide.x30.xr .x30-art svg{width:100%;height:100%;overflow:visible}
.slide.x30.xr .x30-art-work{left:192px;top:710px;width:230px;height:230px}
.slide.x30.xr .x30-art-time{left:1590px;top:60px;width:220px;height:220px}
.slide.x30.xr .x30-art-release{left:1510px;top:720px;width:230px;height:230px}
/* 24: a semantic total and a true four-column register. */
.slide.x30.xr .xr-work-total{position:absolute;left:0;top:6px;width:440px}
.slide.x30.xr .xr-work-total .xr-total-number{display:block;font:900 260px/.98 ShiftDots,monospace;font-variation-settings:'ROND' 100;letter-spacing:-.08em;color:#1a1302}
.slide.x30.xr .xr-work-total p{font:500 31px/1.4 ShiftSans,ShiftCJK,sans-serif;margin:28px 0 0;letter-spacing:0}
.slide.x30.xr .xr-register-wrap{position:absolute;left:520px;top:4px;width:1200px}
.slide.x30.xr table{border-collapse:collapse;table-layout:fixed;width:100%;color:inherit;font:400 32px/1.35 ShiftSans,ShiftCJK,sans-serif}
.slide.x30.xr table th{font-size:25px;font-weight:500;text-align:left;padding:0 24px 24px;border-bottom:2px solid #1a1302;opacity:1;letter-spacing:0}
.slide.x30.xr table td{height:105px;padding:20px 24px;border-bottom:1px solid #1a130244;vertical-align:middle;letter-spacing:0;text-decoration:none;color:inherit}
.slide.x30.xr table th:first-child,.slide.x30.xr table td:first-child{padding-left:0;width:auto}
.slide.x30.xr .xr-register td:nth-child(2){font:600 49px ShiftSans,ShiftCJK,sans-serif;color:#1a1302}
.slide.x30.xr .xr-register td:last-child,.slide.x30.xr .xr-register th:last-child{text-align:right}
.slide.x30.xr .xr-register td:first-child{font-weight:600}
.slide.x30.xr .xr-register-note{font:400 26px/1.4 ShiftSans,ShiftCJK,sans-serif;margin:26px 0 0;letter-spacing:0}
/* 25: aligned comparison rows; the center header alone is the copper focal point. */
.slide.x30.xr .x30-matrix th{height:160px;padding:0 22px 28px;font:600 43px/1.15 ShiftSans,ShiftCJK,sans-serif;vertical-align:middle;opacity:1;background:none!important;color:#1a1302!important;border-bottom:2px solid #1a1302;text-align:left}
.slide.x30.xr .x30-matrix th:first-child{font:500 25px ShiftSans,ShiftCJK,sans-serif;padding-left:0;width:auto}
.slide.x30.xr .x30-matrix td{height:115px;padding:22px;font:400 31px/1.3 ShiftSans,ShiftCJK,sans-serif;background:none!important;color:#1a1302!important;text-align:left;text-decoration:none}
.slide.x30.xr .x30-matrix td:first-child{font-size:26px;padding-left:0;width:auto}
.slide.x30.xr .x30-matrix th:nth-child(3){border-bottom:6px solid #ff661a}
.slide.x30.xr .xr-plan-head{display:flex;align-items:center;gap:20px}
.slide.x30.xr .xr-plan-coin{flex:0 0 94px;height:94px;border-radius:50%;display:grid;place-items:center;border:2px solid #92938e;background:radial-gradient(ellipse at 30% 20%,#f6f5ec,#bcbcb7 56%,#e3e3d9 76%,#9c9e97);box-shadow:inset 0 0 0 5px #e3e3d977;font:900 45px ShiftDots,monospace;font-variation-settings:'ROND' 100;letter-spacing:-.06em;padding-right:4px}
.slide.x30.xr .x30-matrix th:nth-child(3) .xr-plan-coin{background:#ff661a;border-color:#cc4a0c;box-shadow:inset 0 0 0 5px #ffb94844;color:#1a1302}
.slide.x30.xr .xr-matrix-note{margin-top:26px;font:400 25px/1.4 ShiftSans,ShiftCJK,sans-serif;letter-spacing:0}
/* 26: the small sculpture occupies the heading's reserved right-hand space. */
.slide.x30.xr.x30-timeline .x30-heading{right:360px}
.slide.x30.xr.x30-timeline .x30-heading h2{font-size:90px}
.slide.x30.xr.x30-decision-flow .x30-heading h2{font-size:90px}
.slide.x30.xr .xr-flow-label{font-size:31px;font-weight:500}
html:lang(zh) .slide.x30.xr .xr-plan-head{gap:18px}
html:lang(zh) .slide.x30.xr .x30-matrix th{font-family:ShiftCJK,ShiftSans,sans-serif;font-size:37px}
html:lang(zh) .slide.x30.xr .x30-matrix th:first-child{font-size:25px}
html:lang(zh) .slide.x30.xr .x30-matrix td{font-size:29px}
html:lang(zh) .slide.x30.xr .x30-matrix td:first-child{font-size:26px}
html:lang(zh) .slide.x30.xr.x30-timeline .x30-heading h2,html:lang(zh) .slide.x30.xr.x30-decision-flow .x30-heading h2{font-size:82px}
'''

def get_slides(lang='en'):
 validate_data();c=CONFIG['shift'];z=lang.startswith('zh');i=int(z);data=[]
 tr=lambda pair:E(pair[i])
 def tx(x,y,t,cls='',anchor='start',extra=''):
  return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}" {extra}>{E(str(t))}</text>'
 def svg(body,label):return f'<svg viewBox="0 0 1720 600" role="img" aria-label="{E(label)}" data-information-visual="true">{body}</svg>'
 def motion(body,mode='fade',step=0):return f'<g data-chart-motion="{mode}" data-chart-step="{step}">{body}</g>'
 def artwork(key,asset,position,label):
  return f'<div class="x30-art x30-art-{position} sculpture reveal" data-decoration><div class="artwork-slot" data-artwork-slot="{key}" data-artwork-id="{asset}" data-artwork-default="{asset}" data-artwork-label="{E(label)}" data-decoration></div></div>'
 def section(n,body,tone='silver',values=None,art=''):
  return f'<section class="slide x30 xr x30-{TYPES[n]} x30-{tone}" data-tone="{("silver" if tone=="paper" else tone)}" data-title="{tr(c["titles"][n])}" data-layout-id="{TYPES[n]}" data-chart-values=\'{json.dumps(values or {},ensure_ascii=False)}\'><header class="x30-heading"><h2 class="reveal">{tr(c["titles"][n])}</h2><p class="reveal">{tr(c["sub"][n])}</p></header><div class="x30-body" data-chart-container="true">{body}</div>{art}</section>'
 # 24: the total is time, not a sum of heterogeneous outputs.
 b='<aside class="xr-work-total" data-chart-motion="fade"><span class="xr-total-number">40</span><p>'+('总投入 · 小时' if z else 'Total time · hours')+'</p></aside><div class="xr-register-wrap"><table class="xr-register" aria-label="'+tr(c['subject'])+'"><colgroup><col style="width:31%"><col style="width:18%"><col style="width:28%"><col style="width:23%"></colgroup><thead><tr>'
 heads=[['Workstream','工作线'],['Output','产出'],['Unit','单位'],['Time / hours','工时 / 小时']]
 b+=''.join('<th scope="col">'+tr(h)+'</th>' for h in heads)+'</tr></thead><tbody>'
 for j in range(4):
  b+=f'<tr data-chart-motion="fade" data-chart-step="{j}"><td data-edit>{tr(c["rows"][j])}</td><td>{c["values"][j]}</td><td data-edit>{tr(c["units"][j])}</td><td>{c["hours"][j]}</td></tr>'
 b+='</tbody></table><p class="xr-register-note" data-edit>'+('不同产出，不合并计数。' if z else 'Different outputs. No combined count.')+'</p></div>'
 data.append(section(0,b,'silver',{'outputs':c['values'],'hours':c['hours']},artwork('work-register','stack','work','思考叠层' if z else 'Layers of thought')))
 # 25: real comparison table; the coins establish three headings, not three cards.
 b='<table class="x30-matrix"><colgroup><col style="width:22%"><col style="width:26%"><col style="width:26%"><col style="width:26%"></colgroup><thead><tr><th scope="col">'+('比较维度' if z else 'Consideration')+'</th>'
 for j,p in enumerate(c['plans']):
  b+='<th scope="col"><div class="xr-plan-head"><span class="xr-plan-coin" aria-hidden="true">0'+str(j+1)+'</span><span data-edit>'+tr(p)+'</span></div></th>'
 b+='</tr></thead><tbody>'
 times=[[v,['十五分钟','一小时','一天'][j]] for j,v in enumerate(c['time'])]
 for j,(label,values) in enumerate([(['Time needed','所需时间'],times),(['Intended output','预期产出'],c['out']),(['Review by','反馈方式'],c['review'])]):
  b+=f'<tr data-chart-motion="fade" data-chart-step="{j}"><td data-edit>'+tr(label)+'</td>'+''.join('<td data-edit>'+tr(v)+'</td>' for v in values)+'</tr>'
 b+='</tbody></table><p class="xr-matrix-note" data-edit>'+('选择投入程度，不给方案排高低。' if z else 'Choose the commitment, not a universal winner.')+'</p>'
 data.append(section(1,b,'paper'))
 # 26: eight equal calendar columns and flat bars with exact durations.
 b='';x0=440;step=150;starts=[0,2,5,7];ends=[2,5,7,8]
 for w in range(9):
  x=x0+w*step;b+=f'<line x1="{x}" y1="62" x2="{x}" y2="518" stroke="#1a1302" opacity=".16"/>'
  if w<8:b+=tx(x+step/2,34,('第'+str(w+1)+'周') if z else 'W'+str(w+1),'xr-small','middle')
 for j,(a,e) in enumerate(zip(starts,ends)):
  y=94+j*112
  b+=f'<line x1="0" y1="{y-24}" x2="1690" y2="{y-24}" stroke="#1a1302" stroke-opacity=".30"/>'
  b+=tx(0,y+40,'0'+str(j+1),'xr-dot xr-step')+tx(88,y+40,c['phases'][j][i],'xr-mid')
  fill=c['ink'] if j%2==0 else c['paper'];fg=c['paper'] if j%2==0 else c['ink']
  label=str(e-a)+('周' if z else (' week' if e-a==1 else ' weeks'))
  b+=motion(f'<rect x="{x0+a*step}" y="{y}" width="{(e-a)*step}" height="54" fill="{fill}"/>'+tx(x0+(a+e)*step/2,y+37,label,'','middle',f'style="fill:{fg}"'),'grow-x',j)
 b+='<line x1="0" y1="518" x2="1690" y2="518" stroke="#1a1302" stroke-opacity=".30"/>'
 b+=tx(0,576,'每个阶段结束，再进入下一阶段。' if z else 'Finish one stage before moving to the next.','xr-small')
 data.append(section(2,svg(b,c['titles'][2][i]),'orange',{'start_weeks':starts,'end_weeks':ends,'total_weeks':8},artwork('time-stages','cascade','time','递进曲面' if z else 'Stepping surfaces')))
 # 27: two explicit checks, two correction loops; start/end are theme roundels.
 b='''<defs><linearGradient id="shift-x30-roundel" x1="0" y1="0" x2="1" y2=".6"><stop stop-color="#797c75"/><stop offset=".28" stop-color="#e3e3d9"/><stop offset=".62" stop-color="#bcbcbc"/><stop offset="1" stop-color="#f1f0e7"/></linearGradient><marker id="shift-x30-flow-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 1L9 5L0 9" fill="none" stroke="#e3e3d9" stroke-width="1.5"/></marker></defs>'''
 for j,(a,e) in enumerate([(200,386),(700,866),(1180,1414)]):
  b+=f'<path d="M{a} 180H{e}" stroke="#e3e3d9" fill="none" stroke-width="2.5" marker-end="url(#shift-x30-flow-arrow)" data-chart-motion="draw" data-chart-step="{j}"/>'
 for j,x in enumerate([550,1030]):
  b+=f'<path d="M{x} 290V384" stroke="#e3e3d9" fill="none" stroke-width="2.5" marker-end="url(#shift-x30-flow-arrow)" data-chart-motion="draw" data-chart-step="{j+2}"/>'
  b+=tx(x+22,340,'否' if z else 'No','xr-small')
 for x in [785,1295]:b+=tx(x,152,'是' if z else 'Yes','xr-small','middle')
 b+=motion('<circle cx="110" cy="180" r="90" fill="url(#shift-x30-roundel)" stroke="#bcbcbc" stroke-width="2"/><circle cx="110" cy="180" r="81" fill="none" stroke="#1a1302" stroke-opacity=".18"/>'+tx(110,190,'新想法' if z else 'New idea','xr-flow-label','middle','style="fill:#1a1302"'),'fade',0)
 gates=[(['Question','clear?'],['问题','清楚吗？']),(['Test','useful?'],['试验','有效吗？'])]
 for j,x in enumerate([550,1030]):
  lines=gates[j][i]
  body=f'<path d="M{x} 70L{x+150} 180L{x} 290L{x-150} 180Z" fill="#e3e3d9" fill-opacity=".045" stroke="#e3e3d9" stroke-width="2.5"/>'
  body+=tx(x,167,lines[0],'xr-flow-label','middle')+tx(x,208,lines[1],'xr-flow-label','middle')
  b+=motion(body,'fade',j+1)
 b+=motion('<circle cx="1550" cy="180" r="122" fill="#ff661a"/><circle cx="1550" cy="180" r="112" fill="none" stroke="#1a1302" stroke-opacity=".30" stroke-width="1.5"/>'+tx(1550,169,'继续' if z else 'Make it','xr-flow-label','middle','style="fill:#1a1302"')+tx(1550,212,'制作' if z else 'real','xr-flow-label','middle','style="fill:#1a1302"'),'fade',3)
 for j,x in enumerate([400,880]):
  label=(['缩小问题','缩小试验'] if z else ['Narrow the question','Try a smaller test'])[j]
  b+=motion(f'<rect x="{x}" y="398" width="300" height="80" fill="#bcbcbc" fill-opacity=".12" stroke="#e3e3d9" stroke-width="1.5"/>'+tx(x+150,447,label,'xr-small','middle'),'fade',j+4)
  b+=f'<path d="M{x} 438H{x-85}V180H{x-14}" fill="none" stroke="#e3e3d9" stroke-opacity=".65" stroke-width="2" marker-end="url(#shift-x30-flow-arrow)" data-chart-motion="draw" data-chart-step="{j+5}"/>'
 b+=tx(0,581,'完成修改后，重新检查对应条件。' if z else 'After revising, return to the corresponding check.','xr-small')
 data.append(section(3,svg(b,c['titles'][3][i]),'dark'))
 # 28: closed annular sectors. Exact proportions and the PDF seam fix are preserved.
 b='';cx,cy,r=320,280,220;offset=0
 for j,v in enumerate(c['shares']):
  a0=2*math.pi*offset/100-math.pi/2;a1=2*math.pi*(offset+v)/100-math.pi/2
  def point(radius,angle):return f'{cx+radius*math.cos(angle):.6f} {cy+radius*math.sin(angle):.6f}'
  outer,inner=r+40,r-40;large=int(v>50)
  d=f'M {point(outer,a0)} A {outer} {outer} 0 {large} 1 {point(outer,a1)} L {point(inner,a1)} A {inner} {inner} 0 {large} 0 {point(inner,a0)} Z'
  b+=f'<path d="{d}" fill="{[c["accent"],c["ink"],c["paper"]][j]}" data-chart-motion="fade" data-chart-step="{j}"/>';offset+=v
 b+=tx(cx-6,cy+42,'40','xr-dot xr-center-total','middle')+tx(cx,cy+110,'小时 / 周' if z else 'hours / week','xr-small','middle')
 for j,v in enumerate(c['shares']):
  y=94+j*172;b+=f'<line x1="730" y1="{y-34}" x2="1710" y2="{y-34}" stroke="#1a1302" opacity=".30"/><circle cx="745" cy="{y+4}" r="10" fill="{[c["accent"],c["ink"],c["paper"]][j]}"/>'
  b+=tx(790,y+20,c['sharelabels'][j][i],'xr-mid')+tx(1410,y+26,str(v)+'%','xr-number','end')+tx(1710,y+22,f'{v*40/100:g} '+('小时' if z else 'hours'),'','end')
 b+='<line x1="730" y1="576" x2="1710" y2="576" stroke="#1a1302" opacity=".30"/>'
 data.append(section(4,svg(b,c['titles'][4][i]),'silver',{'shares':c['shares'],'total_hours':40}))
 # 29: all four exact-width bars + rates; the terminal 30% is the visual emphasis.
 b='''<defs><linearGradient id="shift-x30-funnel-silver" x1="0" y1="0" x2="1" y2=".13"><stop stop-color="#91958d"/><stop offset=".20" stop-color="#d2d3cb"/><stop offset=".44" stop-color="#f0efe4"/><stop offset=".76" stop-color="#b4b6af"/><stop offset="1" stop-color="#9d9f97"/></linearGradient><linearGradient id="shift-x30-funnel-copper" x1="0" y1="0" x2="1" y2=".12"><stop stop-color="#b84b1c"/><stop offset=".32" stop-color="#ff661a"/><stop offset=".53" stop-color="#ffb27b"/><stop offset="1" stop-color="#d75419"/></linearGradient></defs>'''
 maxv=c['funnel'][0];center=710;scale=8
 for j,v in enumerate(c['funnel']):
  w=scale*v;x=center-w/2;y=34+j*132
  b+=tx(0,y+48,c['flabels'][j][i],'xr-mid')
  fill='url(#shift-x30-funnel-copper)' if j==3 else 'url(#shift-x30-funnel-silver)'
  bar=f'<rect x="{x}" y="{y}" width="{w}" height="72" fill="{fill}" stroke="#1a1302" stroke-opacity=".25" stroke-width="1"/><path d="M{x+1} {y+1}H{x+w-1}" stroke="#fffbed" stroke-opacity=".65"/>'
  b+=motion(bar+tx(center,y+49,v,'xr-number','middle'),'grow-x',j)
  b+=tx(1260,y+48,f'{v/maxv*100:g}%','xr-number','end')
  if j<3:b+=f'<path d="M{center} {y+88}v23m-7-7 7 7 7-7" fill="none" stroke="#1a1302" opacity=".55"/>'
 b+='<line x1="1315" y1="0" x2="1315" y2="574" stroke="#1a1302" stroke-opacity=".26"/>'
 b+=tx(1360,184,'30','xr-dot xr-metric')+tx(1594,184,'%','xr-percent')
 if z:b+=tx(1365,286,'占起始批次的比例','xr-small')
 else:b+=tx(1365,280,'Share of the','xr-small')+tx(1365,316,'initial cohort','xr-small')
 data.append(section(5,svg(b,c['titles'][5][i]),'paper',{'counts':c['funnel'],'denominator':maxv},artwork('released-ideas','bloom','release','萌发形态' if z else 'Emerging form')))
 return data

if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--lang',choices=['en','zh','zh-CN'],default='en');p.add_argument('--css',action='store_true');a=p.parse_args()
 print(get_css() if a.css else '\n\n'.join(get_slides(a.lang)))
