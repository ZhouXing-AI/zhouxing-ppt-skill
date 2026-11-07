"""Six reusable business layouts for the three established editorial systems.

Numbers are fictional design examples. Values drive geometry, labels and totals.
Each theme receives a copy with THEME fixed; get_slides(lang) regenerates fragments.
"""
from html import escape as E
import math,json
THEME='focus'
TYPES=['data-table','option-matrix','timeline','decision-flow','donut','funnel']
CONFIG={
'shift':dict(paper='#e3e3d9',ink='#1a1302',accent='#ff661a',muted='#bcbcbc',soft='#ffb948',dark='#1a1302',display='ShiftSans,ShiftCJK,sans-serif',body='ShiftSans,ShiftCJK,sans-serif',zh='ShiftCJK,ShiftSans,sans-serif',weight='600',zhweight='900',subject=['Creative practice','创意实践'],titles=[['Make the work visible.','让进展，看得见。'],['Choose a useful starting point.','找到合适的起点。'],['Give each stage its own time.','每个阶段，都有自己的时间。'],['A small test decides the next step.','用一次小试验，决定下一步。'],['Make room for making.','把时间，留给动手。'],['From a spark to a working idea.','从灵感，到可用的想法。']],sub=[['Four workstreams, one weekly record. Hours are tracked separately from outputs.','四条工作线，一份周记录。工时与产出分别统计。'],['Three ways to start. Choose by your available time and intended output.','三种启动方式，根据可用时间与预期产出来选择。'],['An eight-week cycle, from first observation to a public release.','从初次观察到公开发布，安排一个八周的实践周期。'],['A decision path for a new idea, with an explicit revision route.','为一个新想法设置明确判断，也为修改留下一条路。'],['A 40-hour practice week, split into three distinct activities.','把一周的四十个实践工时，分配给三类不同活动。'],['One cohort of 100 ideas. Every stage is a subset of the previous stage.','跟踪同一批一百个想法，每个阶段都是上一阶段的子集。']],rows=[['Observe','观察'],['Collect','收藏'],['Connect','连接'],['Make','动手']],units=[['notes','条记录'],['sources','份素材'],['directions','个方向'],['prototypes','个原型']],values=[32,24,12,6],hours=[6,8,10,16],plans=[['A note','一张笔记'],['A sketch','一张草图'],['A prototype','一个原型']],time=['15 min','60 min','1 day'],out=[['One observation','一个观察'],['Three possibilities','三种可能'],['One working test','一次可用试验']],review=[['Self review','自行回看'],['Peer response','同伴反馈'],['User feedback','用户反馈']],phases=[['Observe','观察'],['Connect','连接'],['Make','动手'],['Release','发布']],shares=[50,30,20],sharelabels=[['Making','动手'],['Research','研究'],['Reflection','复盘']],funnel=[100,70,45,30],flabels=[['Collected','收集'],['Explored','探索'],['Tested','试验'],['Released','发布']]),
'focus':dict(paper='#ededeb',ink='#162720',accent='#00856c',muted='#bfcac3',soft='#a0d4b6',dark='#073d32',display='MoveSerif,FocusCJK,serif',body='ShiftSans,FocusCJKSans,sans-serif',zh='FocusCJK,MoveSerif,serif',weight='400',zhweight='400',subject=['Decision practice','决策实践'],titles=[['Keep the evidence together.','让依据，放在同一张桌上。'],['Compare the commitments.','比较选择，也比较投入。'],['A decision has a learning horizon.','为决定，安排学习的时间。'],['Let evidence set the next move.','让依据，决定下一步。'],['Attention is a finite resource.','注意力，是有限的资源。'],['Narrow the field with evidence.','用依据，逐步缩小范围。']],sub=[['A weekly decision register. Evidence counts and review hours describe different things.','一份每周决策记录。证据数量与复核工时分别呈现。'],['Three levels of commitment, each with a different cost of learning.','三种投入程度，对应不同的验证成本与决策条件。'],['Eight weeks to ask, test, reflect and make a considered commitment.','用八周提问、试验、复盘，再做出经过考虑的承诺。'],['Move ahead only when the question and the evidence are sufficiently clear.','问题与依据足够清晰时推进，否则先缩小范围。'],['A 40-hour week allocated to understanding, testing and review.','四十个工作小时，分别投入理解、试验与复核。'],['Follow the same 100 questions through review, trial and commitment.','跟踪同一批一百个问题，从复核、试点走向决策。']],rows=[['Research','研究'],['Interviews','访谈'],['Experiments','试验'],['Review','复盘']],units=[['sources','份资料'],['conversations','次访谈'],['trials','次试验'],['decisions','项决定']],values=[28,12,6,4],hours=[12,8,14,6],plans=[['Explore','探索'],['Pilot','试点'],['Commit','投入']],time=['2 hours','2 weeks','8 weeks'],out=[['A sharper question','更清晰的问题'],['A tested assumption','已验证的假设'],['A bounded decision','有边界的决定']],review=[['One reviewer','一位复核者'],['A small team','一个小团队'],['A named owner','一位负责人']],phases=[['Frame','界定'],['Test','试验'],['Learn','复盘'],['Commit','决定']],shares=[45,35,20],sharelabels=[['Understand','理解'],['Experiment','试验'],['Review','复核']],funnel=[100,65,40,25],flabels=[['Questions','问题'],['Reviewed','复核'],['Piloted','试点'],['Committed','决定']]),
'edit':dict(paper='#f2eee7',ink='#352129',accent='#b64032',muted='#d8d1c9',soft='#e8a496',dark='#352129',display='EditSerif,EditCJK,serif',body='ShiftSans,EditCJK,sans-serif',zh='EditCJK,EditSerif,serif',weight='400',zhweight='300',subject=['Editorial practice','编辑实践'],titles=[['A clear view of the issue.','把这一期，梳理清楚。'],['Give each piece the right treatment.','为每一篇，选择合适的编辑。'],['An issue takes shape over time.','一期内容，逐步成形。'],['A good question improves the copy.','一个好问题，推动一次修改。'],['Reserve time for the real edit.','把时间，留给真正的编辑。'],['From submission to publication.','从来稿，到正式刊发。']],sub=[['Four desks, one production record. Article counts are not measures of quality.','四个编辑组，共用一份制作记录。篇数不代表质量。'],['Three editorial passes, matched to the condition of the draft.','根据稿件的实际状态，选择三种不同的编辑工作。'],['An eight-week publication schedule, with a separate check before release.','八周刊发计划，在发布之前为终校留下独立时间。'],['Check the main idea, then the evidence, before approving a piece.','先核对主旨，再核对依据，然后决定是否进入终校。'],['A 40-hour editorial week divided across three kinds of work.','四十个编辑工时，在三类工作之间明确分配。'],['Track the same 100 submissions; each later stage contains fewer pieces.','跟踪同一批一百篇来稿，后续各阶段均为前一阶段的子集。']],rows=[['Features','深度文章'],['Briefs','内容简报'],['Interviews','人物访谈'],['Reviews','评论文章']],units=[['pieces','篇'],['pieces','篇'],['pieces','篇'],['pieces','篇']],values=[8,16,6,10],hours=[14,8,12,6],plans=[['Copy edit','文字编辑'],['Fact check','事实核验'],['Structure edit','结构编辑']],time=['2 hours','4 hours','1 day'],out=[['Clear sentences','清晰的句子'],['Traceable sources','可追溯的来源'],['A coherent argument','连贯的论证']],review=[['Language editor','文字编辑'],['Fact checker','核查编辑'],['Section editor','栏目编辑']],phases=[['Commission','约稿'],['Edit','编辑'],['Check','终校'],['Publish','刊发']],shares=[60,25,15],sharelabels=[['Editing','编辑'],['Verification','核验'],['Production','制作']],funnel=[100,75,50,35],flabels=[['Submitted','来稿'],['Selected','初选'],['Edited','编辑'],['Published','刊发']])}

def validate_data():
    c=CONFIG[THEME]
    assert sum(c['hours'])==40 and sum(c['shares'])==100
    assert len(c['values'])==len(c['rows'])==4
    assert all(a>=b>0 for a,b in zip(c['funnel'],c['funnel'][1:]))
    assert sum(b-a for a,b in [(0,2),(2,5),(5,7),(7,8)])==8
    return True

def get_css():
    c=CONFIG[THEME]
    return f'''/* expansion30: six semantic layouts, scoped away from approved pages */
.slide.x30{{background:{c['paper']};color:{c['ink']};--x-ink:{c['ink']};--x-paper:{c['paper']};--x-accent:{c['accent']};--x-muted:{c['muted']};--x-soft:{c['soft']};font-synthesis:none}}
.slide.x30.x30-dark{{background:{c['dark']};color:{c['paper']};--x-ink:{c['paper']};--x-paper:{c['dark']};--x-accent:{c['soft']}}} 
.slide.x30:before{{opacity:.04}}
.slide.x30 .x30-heading{{position:absolute;left:120px;right:120px;top:78px}}
.slide.x30 .x30-heading h2{{position:static;font: {c['weight']} 101px/1.12 {c['display']};margin:0;letter-spacing:-2px}}
.slide.x30 .x30-heading p{{font:400 28px/1.45 {c['body']};margin:24px 0 0;letter-spacing:0;opacity:.82}}
html:lang(zh) .slide.x30 .x30-heading h2{{font-family:{c['zh']};font-size:80px;font-weight:{c['zhweight']};letter-spacing:0;line-height:1.25}}
html:lang(zh) .slide.x30 .x30-heading p{{font-size:27px;line-height:1.5}}
.slide.x30 .x30-body{{position:absolute;left:120px;top:350px;width:1680px;height:600px}}
.slide.x30 .x30-body svg{{width:100%;height:100%;overflow:visible}}
.slide.x30 svg text{{font:400 28px {c['body']};letter-spacing:0;fill:var(--x-ink)}}
.slide.x30 svg .x30-big{{font: {c['weight']} 104px {c['display']};fill:var(--x-accent)}}
.slide.x30 svg .x30-mid{{font: {c['weight']} 46px {c['display']}}}
.slide.x30 svg .x30-small{{font-size:22px}}
.slide.x30 [data-chart-motion]{{transform-box:view-box}}
.slide.x30 table{{border-collapse:collapse;width:100%;table-layout:fixed;font:400 30px/1.4 {c['body']};color:inherit}}
.slide.x30 th{{font-size:23px;font-weight:400;text-align:left;padding:0 24px 24px;border-bottom:2px solid var(--x-ink);opacity:.8}}
.slide.x30 td{{padding:29px 24px;border-bottom:1px solid color-mix(in srgb,var(--x-ink) 24%,transparent)}}
.slide.x30 th:first-child,.slide.x30 td:first-child{{padding-left:0;width:28%}}
.slide.x30 td:nth-child(2){{color:var(--x-accent);font: {c['weight']} 43px {c['display']}}}
.slide.x30 td:last-child{{text-align:right}}
.slide.x30 th:last-child{{text-align:right}}
.slide.x30 .x30-table-note{{display:flex;justify-content:space-between;align-items:baseline;margin-top:35px;font:400 28px {c['body']}}}
.slide.x30 .x30-table-note b{{font:{c['weight']} 64px {c['display']};color:var(--x-accent)}}
.slide.x30 .x30-option-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;height:100%}}
.slide.x30 .x30-option{{padding:32px 34px;border-top:4px solid var(--x-accent);background:color-mix(in srgb,var(--x-paper) 94%,var(--x-ink));position:relative}}
.slide.x30 .x30-option:nth-child(2){{background:var(--x-accent);color:{c['paper']}}}
.slide.x30 .x30-option h3{{font:{c['weight']} 59px/1.08 {c['display']};margin:0 0 36px;letter-spacing:0}}
.slide.x30 .x30-option dl{{margin:0}}
.slide.x30 .x30-option dt{{font:400 21px {c['body']};opacity:.7;margin:23px 0 10px}}
.slide.x30 .x30-option dd{{font:400 29px/1.4 {c['body']};margin:0}}
.slide.x30 .x30-option .x30-option-index{{position:absolute;right:30px;bottom:22px;font:{c['weight']} 74px {c['display']};opacity:.34}}
html:lang(zh) .slide.x30 .x30-option h3{{font: {c['zhweight']} 47px/1.3 {c['zh']}}}
html:lang(zh) .slide.x30 .x30-option dd{{font-size:27px}}
.slide.x30 .x30-matrix th{{height:110px;font:{c['weight']} 52px/1.2 {c['display']};padding:20px 24px;opacity:1}}
.slide.x30 .x30-matrix th:first-child{{font:400 24px {c['body']};width:22%}}
.slide.x30 .x30-matrix td{{height:135px;font:400 30px/1.4 {c['body']};padding:24px;color:inherit;text-decoration:none;text-align:left}}
.slide.x30 .x30-matrix td:first-child{{font-size:24px;width:22%;padding-left:0}}
.slide.x30 .x30-matrix th:nth-child(3),.slide.x30 .x30-matrix td:nth-child(3){{background:var(--x-accent);color:{c['paper']}}}
.slide.x30 .x30-matrix th:last-child{{text-align:left}}
html:lang(zh) .slide.x30 .x30-matrix th:not(:first-child){{font-family:{c['zh']};font-size:43px;font-weight:{c['zhweight']}}}
html:lang(zh) .slide.x30 .x30-matrix td{{font-size:27px}}
.slide.x30.x30-option-matrix .x30-table-note{{margin-top:26px;font-size:24px}}
'''+('''.slide.x30 .x30-option{border-radius:0 0 120px 0}.slide.x30 .x30-option:nth-child(2){color:#1a1302}.slide.x30 .x30-table-note{border-top:3px dotted #1a130245;padding-top:18px}.slide.x30 svg .x30-big{font-family:ShiftDots,monospace;font-weight:900}''' if THEME=='shift' else '''.slide.x30 .x30-option{border:1px solid #16272020;border-top:4px solid #a0d4b6;box-shadow:0 14px 0 -9px #16272015}.slide.x30 .x30-option:nth-child(2){border-color:#00856c}.slide.x30 .x30-option-index{font-family:MoveItalic,serif}''' if THEME=='focus' else '''.slide.x30 .x30-option{background:#fcf8f0;border-bottom:4px double #b6403240;box-shadow:8px 9px 0 #d8d1c977}.slide.x30 .x30-option:nth-child(2){background:#b64032}.slide.x30 .x30-option-index{font-family:EditItalic,serif}.slide.x30 td:nth-child(2){text-decoration:underline;text-decoration-color:#b6403240;text-underline-offset:9px}''')

def get_slides(lang='en'):
    validate_data();c=CONFIG[THEME];z=lang.startswith('zh');i=int(z)
    tr=lambda x:E(x[i]);data=[]
    def tx(x,y,t,cls='',anchor='start',extra=''):
        return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}" {extra}>{E(str(t))}</text>'
    def svg(body,label):return f'<svg viewBox="0 0 1680 600" role="img" aria-label="{E(label)}" data-information-visual>{body}</svg>'
    def motion(b,mode='fade',step=0):return f'<g data-chart-motion="{mode}" data-chart-step="{step}">{b}</g>'
    def section(n,body,dark=False,values=None):
        tone='dark' if dark else 'light'
        return f'<section class="slide x30 x30-{TYPES[n]} {"x30-dark" if dark else ""}" data-tone="{tone}" data-title="{tr(c["titles"][n])}" data-layout-id="{TYPES[n]}" data-chart-values=\'{json.dumps(values or {},ensure_ascii=False)}\'><header class="x30-heading reveal"><h2>{tr(c["titles"][n])}</h2><p>{tr(c["sub"][n])}</p></header><div class="x30-body" data-chart-container>{body}</div></section>'
    # 24: table, genuinely tabular content rather than dashboard cards.
    heads=[['Workstream','工作线'],['Output','产出'],['Unit','单位'],['Time / hours','工时 / 小时']]
    b='<table aria-label="'+tr(c['subject'])+'"><thead><tr>'+''.join('<th scope="col">'+tr(h)+'</th>' for h in heads)+'</tr></thead><tbody>'
    for j in range(4):
        b+=f'<tr data-chart-motion="fade" data-chart-step="{j}"><td data-edit>{tr(c["rows"][j])}</td><td>{c["values"][j]}</td><td data-edit>{tr(c["units"][j])}</td><td>{c["hours"][j]}</td></tr>'
    b+='</tbody></table><div class="x30-table-note"><span data-edit>'+('不同产出，不合并计数。' if z else 'Different outputs. No combined count.')+'</span><span>'+('总投入 ' if z else 'Total time ')+'<b>40</b> '+('小时' if z else 'hours')+'</span></div>'
    data.append(section(0,b,values={'outputs':c['values'],'hours':c['hours']}))
    # 25: genuine cross-tab comparison, distinct from the four-card layout.
    b='<table class="x30-matrix"><thead><tr><th scope="col">'+('比较维度' if z else 'Consideration')+'</th>'+''.join('<th scope="col" data-edit>'+tr(p)+'</th>' for p in c['plans'])+'</tr></thead><tbody>'
    times=[[v,['十五分钟','一小时','一天'][j] if THEME=='shift' else ['两小时','两周','八周'][j] if THEME=='focus' else ['两小时','四小时','一天'][j]] for j,v in enumerate(c['time'])]
    for j,(label,values) in enumerate([(['Time needed','所需时间'],times),(['Intended output','预期产出'],c['out']),(['Review by','反馈方式'],c['review'])]):
        b+=f'<tr data-chart-motion="fade" data-chart-step="{j}"><td data-edit>'+tr(label)+'</td>'+''.join('<td data-edit>'+tr(v)+'</td>' for v in values)+'</tr>'
    b+='</tbody></table><div class="x30-table-note"><span data-edit>'+('选择投入程度，不给方案排高低。' if z else 'Choose the commitment, not a universal winner.')+'</span></div>'
    if THEME=='shift':b=b.replace('class="x30-matrix"','class="x30-matrix" style="--x-paper:#e3e3d9"')
    data.append(section(1,b))
    # 26: timed stages; eight columns, four precisely located durations.
    b='';x0=420;step=150;starts=[0,2,5,7];ends=[2,5,7,8]
    for w in range(9):
        x=x0+w*step;b+=f'<line x1="{x}" y1="70" x2="{x}" y2="500" stroke="currentColor" opacity=".13"/>'
        if w<8:b+=tx(x+step/2,35,('第'+str(w+1)+'周') if z else 'W'+str(w+1),'x30-small','middle')
    for j,(a,e) in enumerate(zip(starts,ends)):
        y=95+j*105;b+=tx(0,y+40,c['phases'][j][i],'x30-mid')
        fill=c['accent'] if j%2==0 else c['muted'];fg=c['paper'] if THEME!='shift' and j%2==0 else c['ink']
        label=(str(e-a)+'周') if z else str(e-a)+(' week' if e-a==1 else ' weeks')
        b+=motion(f'<rect x="{x0+a*step}" y="{y}" width="{(e-a)*step}" height="66" rx="{33 if THEME=="shift" else 0}" fill="{fill}"/>'+tx(x0+(a+e)*step/2,y+42,label,'','middle',f'style="fill:{fg}"'),'grow-x',j)
    b+=tx(0,570,('每个阶段结束，再进入下一阶段。' if z else 'Finish one stage before moving to the next.'),'x30-small')
    data.append(section(2,svg(b,c['titles'][2][i]),values={'start_weeks':starts,'end_weeks':ends,'total_weeks':8}))
    # 27: branch logic; start -> first gate -> second gate -> release, two revision exits.
    labels=([['New idea','新想法'],['Question clear?','问题清楚吗？'],['Test useful?','试验有效吗？'],['Make it real','继续制作'],['Narrow the question','缩小问题'],['Try a smaller test','缩小试验']] if THEME=='shift' else [['A proposal','一个提案'],['Scope clear?','范围清楚吗？'],['Evidence enough?','依据充分吗？'],['Commit','做出决定'],['Reframe the scope','重新界定'],['Gather evidence','补充依据']] if THEME=='focus' else [['A draft','一份稿件'],['Main idea clear?','主旨清晰吗？'],['Sources verified?','来源可核实吗？'],['Final review','进入终校'],['Revise the argument','修改论证'],['Verify the sources','核实来源']])
    b='<defs><marker id="'+THEME+'-flow-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 1L9 5L0 9" fill="none" stroke="currentColor" stroke-width="1.5"/></marker></defs>'
    for j,(a,e) in enumerate([(250,400),(690,840),(1130,1320)]):b+=f'<path d="M{a} 165H{e-14}" stroke="currentColor" fill="none" stroke-width="2" marker-end="url(#{THEME}-flow-arrow)" data-chart-motion="draw" data-chart-step="{j}"/>'
    for j,x in enumerate([545,985]):
        b+=f'<path d="M{x} 270V385" stroke="currentColor" fill="none" stroke-width="2" marker-end="url(#{THEME}-flow-arrow)" data-chart-motion="draw" data-chart-step="{j+2}"/>'
        b+=tx(x+22,335,'否' if z else 'No','x30-small')
    for x in [760,1210]:b+=tx(x,135,'是' if z else 'Yes','x30-small','middle')
    for j,(x,w) in enumerate([(0,250),(400,290),(840,290),(1320,330)]):
        if j in [1,2]:shape=f'<path d="M{x+w/2} 60L{x+w} 165L{x+w/2} 270L{x} 165Z" fill="none" stroke="currentColor" stroke-width="2"/>'
        else:shape=f'<rect x="{x}" y="105" width="{w}" height="120" rx="{60 if THEME=="shift" else 0}" fill="{c["soft"] if j==3 else c["paper"]}"/>'
        fg=c['ink'] if j in [0,3] else c['paper'];b+=motion(shape+tx(x+w/2,175,labels[j][i],'','middle',f'style="fill:{fg}"'),'fade',j)
    for j,x in enumerate([395,835]):
        b+=motion(f'<rect x="{x}" y="405" width="300" height="104" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="7 6"/>'+tx(x+150,466,labels[j+4][i],'','middle'),'fade',j+4)
    b+=tx(0,582,('完成修改后，重新检查对应条件。' if z else 'After revising, return to the corresponding check.'),'x30-small')
    data.append(section(3,svg(b,c['titles'][3][i]),True))
    # 28: donut, lengths encode percentages. Total 40 h, labels include both % and hours.
    b='';cx,cy,r=330,285,210;offset=0
    for j,v in enumerate(c['shares']):
        # Closed annular sectors retain exact proportions in DOM-to-image PDF
        # snapshots; dashed circles can produce a seam at the wraparound.
        a0=2*math.pi*offset/100-math.pi/2;a1=2*math.pi*(offset+v)/100-math.pi/2
        def point(radius,angle):return f'{cx+radius*math.cos(angle):.6f} {cy+radius*math.sin(angle):.6f}'
        outer,inner=r+37,r-37;large=int(v>50)
        d=f'M {point(outer,a0)} A {outer} {outer} 0 {large} 1 {point(outer,a1)} L {point(inner,a1)} A {inner} {inner} 0 {large} 0 {point(inner,a0)} Z'
        b+=f'<path d="{d}" fill="{[c["accent"],c["ink"],c["muted"]][j]}" data-chart-motion="fade" data-chart-step="{j}"/>';offset+=v
    b+=tx(cx,cy+16,'40','x30-big','middle')+tx(cx,cy+68,'小时 / 周' if z else 'hours / week','x30-small','middle')
    for j,v in enumerate(c['shares']):
        y=92+j*170;b+=f'<line x1="780" y1="{y-28}" x2="1660" y2="{y-28}" stroke="currentColor" opacity=".25"/><rect x="780" y="{y+6}" width="18" height="18" fill="{[c["accent"],c["ink"],c["muted"]][j]}"/>'
        b+=tx(830,y+26,c['sharelabels'][j][i],'x30-mid')+tx(1395,y+35,str(v)+'%','x30-mid','end')+tx(1660,y+30,f'{v*40/100:g} '+('小时' if z else 'hours'),'','end')
    data.append(section(4,svg(b,c['titles'][4][i]),values={'shares':c['shares'],'total_hours':40}))
    # 29: funnel uses constant-height bars, never trapezoid area as a quantity.
    b='';maxv=c['funnel'][0]
    for j,v in enumerate(c['funnel']):
        w=900*v/maxv;x=460+(900-w)/2;y=32+j*138
        b+=tx(0,y+57,c['flabels'][j][i],'x30-mid')
        b+=motion(f'<rect x="{x}" y="{y}" width="{w}" height="86" rx="{43 if THEME=="shift" else 0}" fill="{c["accent"] if j==3 else c["muted"]}"/>'+tx(910,y+57,v,'x30-mid','middle',f'style="fill:{c["paper"] if j==3 and THEME!="shift" else c["ink"]}"'),'grow-x',j)
        rate=v/maxv*100;b+=tx(1660,y+57,f'{rate:g}%','x30-mid','end')
        if j<3:b+=f'<path d="M910 {y+98}v19m-7-7 7 7 7-7" fill="none" stroke="currentColor" opacity=".6"/>'
    b+=tx(1660,590,'占起始批次的比例' if z else 'Share of the initial cohort','x30-small','end')
    data.append(section(5,svg(b,c['titles'][5][i]),values={'counts':c['funnel'],'denominator':maxv}))
    return data

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--lang',default='en');p.add_argument('--css',action='store_true');args=p.parse_args()
    print(get_css() if args.css else '\n\n'.join(get_slides(args.lang)))
