"""Six native, bilingual FOCUS decision-analysis charts.

Every dataset is illustrative. SVG geometry is computed from the data constants.
Public API: get_slides('en' | 'zh' | 'zh-CN'), validate_data().
"""
from html import escape
from math import cos, sin, pi
import json

PAPER = '#ededeb'
INK = '#162720'
GREEN = '#00856c'
DEEP = '#073d32'
SILVER = '#bfcac3'
LEAF = '#a0d4b6'

LINE = {'weeks': [1, 2, 3, 4, 5, 6], 'usual': [11, 10, 10, 9, 9, 8],
        'focused': [10, 9, 8, 6, 5, 4], 'unit': 'median days', 'range': [0, 12]}
AREA = {'weeks': list(range(1, 9)), 'values': [12, 18, 16, 26, 31, 28, 38, 44],
        'unit': 'accepted evidence notes per week', 'range': [0, 50]}
RADAR = {'current': [54, 68, 72, 48, 60], 'pilot': [80, 82, 86, 76, 84],
         'dimensions': ['Clarity', 'Evidence', 'Ownership', 'Speed', 'Review'],
         'unit': 'illustrative rubric points', 'range': [0, 100]}
SANKEY = {'inputs': [40, 35, 25], 'middle': [60, 40], 'outputs': [65, 35],
          'a': [[30, 10], [20, 15], [10, 15]], 'b': [[40, 20], [25, 15]],
          'unit': 'requests', 'total': 100, 'pixels_per_request': 4}
SCATTER = [
    ('Search', '搜索', 1.5, 18), ('Checklist', '清单', 2.8, 32),
    ('Briefing', '简报', 4.0, 25), ('Weekly review', '周评审', 5.2, 42),
    ('Intake', '需求收集', 6.5, 29), ('Handoffs', '交接', 8.0, 38),
    ('Automation', '自动化', 9.5, 46), ('Forecast', '预测', 11.0, 21),
]
HEATMAP = {'values': [[80, 65, 50, 90, 70, 45], [55, 75, 40, 85, 60, 35],
                      [95, 85, 65, 90, 80, 70], [70, 55, 45, 80, 65, 50]],
           'rows': ['Purpose', 'Evidence', 'Owner', 'Next step'],
           'columns': ['A', 'B', 'C', 'D', 'E', 'F'], 'range': [0, 100],
           'unit': 'decision-brief completeness score'}


def tr(lang, en, zh):
    return zh if lang in ('zh', 'zh-CN') else en


def n(value):
    return f'{value:.3f}'.rstrip('0').rstrip('.')


def txt(x, y, value, color=INK, size=28, anchor='start', extra='', style=''):
    return (f'<text class="{style}" x="{n(x)}" y="{n(y)}" fill="{color}" font-size="{size}" '
            f'text-anchor="{anchor}" {extra}>{escape(str(value))}</text>')


def rule(x1, y1, x2, y2, color=INK, width=1.3, extra=''):
    return (f'<line x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" y2="{n(y2)}" '
            f'stroke="{color}" stroke-width="{n(width)}" {extra}/>')


def rect(x, y, w, h, fill, extra=''):
    return (f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" '
            f'fill="{fill}" {extra}/>')


def circle(x, y, r, fill, extra=''):
    return f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" fill="{fill}" {extra}/>'


def poly(points):
    return 'M' + ' L'.join(f'{n(x)} {n(y)}' for x, y in points)


def motion(markup, kind, step):
    """Annotate a data element without changing its final geometry or styling."""
    return markup.replace(' ', f' data-chart-motion="{kind}" data-chart-step="{step}" ', 1)


def graphic(parts, label, description):
    return ('<svg viewBox="0 0 1680 610" xmlns="http://www.w3.org/2000/svg" '
            f'data-information-visual="" role="img" aria-label="{escape(label, quote=True)}">'
            f'<title>{escape(label)}</title><desc>{escape(description)}</desc>' + ''.join(parts) + '</svg>')


def section(kind, lang, heading, subtitle, unit, values, parts, description, dark=False):
    accent = {'line': ('less delay.', '少一点等待。'), 'area': ('reusable.', '留给下一次。'), 'radar': ('whole decision.', '看得更完整。'), 'sankey': ('decision path.', '每一步的流向。'), 'scatter': ('test next.', '值得验证的下一步。'), 'heatmap': ('the gaps', '先补齐缺口。')}
    phrase = tr(lang, *accent[kind])
    title_html = escape(heading).replace(escape(phrase), '<em>' + escape(phrase) + '</em>')
    tone = 'dark' if dark else 'light'
    cls = ' dark-page' if dark else ''
    data = escape(json.dumps(values, ensure_ascii=False, separators=(',', ':')), quote=True)
    return (f'<section class="slide focus-data focus-analysis fd-{kind}{cls}" data-tone="{tone}" '
            f'data-chart-kind="{kind}" data-chart-values="{data}" data-chart-unit="{escape(unit, quote=True)}" '
            f'data-provenance="illustrative" data-title="{escape(heading, quote=True)}">'
            f'<header class="fd-heading">'
            f'<h2 class="reveal">{title_html}</h2><p class="fd-subtitle reveal">{escape(subtitle)}</p></header>'
            f'<div class="fd-chart" data-chart-container="">{graphic(parts, heading, description)}</div></section>')



def silver_surface(identifier):
    return (f'<linearGradient id="{identifier}" x1="0" y1="0" x2="1" y2="0">'
            f'<stop stop-color="{SILVER}"/><stop offset=".42" stop-color="{PAPER}"/>'
            f'<stop offset=".65" stop-color="{SILVER}"/><stop offset="1" stop-color="{PAPER}"/></linearGradient>')


def line_slide(lang):
    x=lambda i:100+i*210;y=lambda v:500-v/12*390
    p=[txt(100,35,tr(lang,'Median days to a decision','决策耗时中位数 · 天'),INK,28),
       rule(625,25,672,25,INK,3.5,'stroke-dasharray="9 7"'),txt(690,35,tr(lang,'Usual process','原流程'),INK,27),
       rule(940,25,987,25,GREEN,4),txt(1005,35,tr(lang,'Focused pilot','聚焦试点'),INK,27),
       rule(1275,45,1275,554,SILVER,1.2),txt(1350,87,tr(lang,'Week VI','第6周'),GREEN,42,style='fd-editorial-italic'),
       motion(txt(1350,238,LINE['usual'][-1],INK,132,style='fd-editorial'),'fade',3),
       txt(1450,237,tr(lang,'days','天'),INK,28),txt(1350,292,tr(lang,'Usual process','原流程'),INK,28),
       rule(1350,329,1660,329,SILVER,1.1),
       motion(txt(1350,480,LINE['focused'][-1],GREEN,132,style='fd-editorial'),'fade',3),
       txt(1450,479,tr(lang,'days','天'),INK,28),txt(1350,534,tr(lang,'Focused pilot','聚焦试点'),INK,28)]
    for v in (0,3,6,9,12):
        p += [rule(100,y(v),1150,y(v),INK if v==0 else SILVER,1.3 if v==0 else 1),txt(72,y(v)+9,v,INK,27,'end')]
    for i in range(6):p.append(txt(x(i),552,tr(lang,f'Week {i+1}',f'第{i+1}周'),INK,28,'middle'))
    for series,(key,color,dash) in enumerate([('usual',INK,'stroke-dasharray="10 7"'),('focused',GREEN,'')]):
        points=[(x(i),y(v)) for i,v in enumerate(LINE[key])]
        p.append(motion(f'<path d="{poly(points)}" fill="none" stroke="{color}" stroke-width="4.2" stroke-linejoin="round" {dash}/>','wipe-x' if dash else 'draw',series))
        for px,py in points:
            marker=rect(px-5.5,py-5.5,11,11,PAPER,f'stroke="{color}" stroke-width="2.5"') if key=='usual' else circle(px,py,6.5,PAPER,f'stroke="{color}" stroke-width="3"')
            p.append(motion(marker,'pop',2))
        p.append(motion(txt(1180,y(LINE[key][-1])+11,LINE[key][-1],color,34),'fade',3))
    return section('line', lang, tr(lang, 'Decisions, with less delay.', '让决策，少一点等待。'),
                   tr(lang, 'Two pilot groups; time from an open question to a recorded decision.',
                      '两组试点，比较从提出问题到形成明确决策的时间。'),
                   tr(lang, 'MEDIAN DAYS', '单位：天，中位数'), LINE, p,
                   tr(lang, 'Weeks 1–6. Usual process: 11, 10, 10, 9, 9, 8 days. Focused pilot: 10, 9, 8, 6, 5, 4 days. Both use a 0–12 day scale; lower is faster.',
                      '第1至6周。原流程11、10、10、9、9、8天；聚焦试点10、9、8、6、5、4天。共用0至12天标尺，数值越低耗时越短。'))


def area_slide(lang):
    x=lambda i:100+i*210;y=lambda v:510-v/50*380;gid='focus-evidence-wash-'+lang
    p=[f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop stop-color="{LEAF}" stop-opacity=".5"/><stop offset="1" stop-color="{LEAF}" stop-opacity=".06"/></linearGradient></defs>',
       txt(100,35,tr(lang,'Accepted evidence notes / week','每周纳入的证据笔记 · 条'),PAPER,28),
       txt(1570,35,tr(lang,'A growing shared memory','让经验成为共同记忆'),LEAF,36,'end',style='fd-editorial-italic')]
    for v in (0,10,20,30,40,50):
        p += [rule(100,y(v),1570,y(v),PAPER,1.2 if v==0 else 1,f'opacity="{.45 if v==0 else .15}"'),txt(72,y(v)+9,v,PAPER,27,'end')]
    points=[(x(i),y(v)) for i,v in enumerate(AREA['values'])]
    p.append(motion(f'<path d="{poly([(100,510)]+points+[(1570,510)])} Z" fill="url(#{gid})"/>','wipe-x',0))
    p.append(motion(f'<path d="{poly(points)}" fill="none" stroke="{LEAF}" stroke-width="3.8" stroke-linejoin="round"/>','draw',1))
    for i in (0,4,7):
        p.append(motion(circle(x(i),y(AREA['values'][i]),6.5,DEEP,f'stroke="{LEAF}" stroke-width="2.8"'),'pop',2))
        p.append(motion(txt(x(i),y(AREA['values'][i])-24,AREA['values'][i],PAPER,76 if i==7 else 44,'middle',style='fd-editorial'),'fade',2))
    for i in range(8):p.append(txt(x(i),564,tr(lang,f'W{i+1}',f'第{i+1}周'),PAPER,28,'middle'))
    return section('area', lang, tr(lang, 'Evidence, made reusable.', '把证据，留给下一次。'),
                   tr(lang, 'Eight weeks of accepted evidence notes, using the same review criteria.',
                      '八周内纳入知识库的证据笔记，采用相同审核标准。'),
                   tr(lang, 'NOTES PER WEEK', '单位：条／周'), AREA, p,
                   tr(lang, 'Weekly accepted evidence notes: 12, 18, 16, 26, 31, 28, 38, 44. The area starts at zero, on a 0–50 scale. This is not a cumulative series.',
                      '每周纳入的证据笔记为12、18、16、26、31、28、38、44条。面积从零基线展开，纵轴0至50，不是累计序列。'), dark=True)


def radar_slide(lang):
    names=[tr(lang,en,zh) for en,zh in zip(RADAR['dimensions'],['清晰度','证据','责任归属','速度','复盘'])]
    cx,cy,radius=395,300,195
    def point(i,v):
        a=-pi/2+i*2*pi/5;return cx+radius*v/100*cos(a),cy+radius*v/100*sin(a)
    p=[txt(900,49,tr(lang,'Current to possible.','从当前，到可能。'),GREEN,45,style='fd-editorial-italic'),
       rule(900,83,1660,83,INK,1.2),txt(1230,131,tr(lang,'Current','当前'),INK,26,'middle'),
       txt(1430,131,tr(lang,'Pilot','试点'),GREEN,26,'middle'),txt(1620,131,tr(lang,'Δ points','变化／分'),INK,26,'middle')]
    for v in (20,40,60,80,100):
        p.append(f'<path d="{poly([point(i,v) for i in range(5)])} Z" fill="none" stroke="{SILVER}" stroke-width="1.2"/>')
        p.append(txt(cx+12,cy-radius*v/100+8,v,INK,25))
    p.append(txt(cx+12,cy+22,0,INK,25))
    for i,name in enumerate(names):
        px,py=point(i,100);p.append(rule(cx,cy,px,py,SILVER,1.1))
        px,py=point(i,137);p.append(txt(px,py+10,name,INK,29,'middle'))
    for series,(key,color,dash) in enumerate([('current',INK,'stroke-dasharray="9 7"'),('pilot',GREEN,'')]):
        points=[point(i,v) for i,v in enumerate(RADAR[key])]
        p.append(motion(f'<path d="{poly(points)} Z" fill="none" stroke="{color}" stroke-width="4.1" stroke-linejoin="round" {dash}/>','wipe-x' if dash else 'draw',series))
        for px,py in points:
            marker=rect(px-5,py-5,10,10,PAPER,f'stroke="{color}" stroke-width="2.5"') if key=='current' else circle(px,py,6,PAPER,f'stroke="{color}" stroke-width="2.8"')
            p.append(motion(marker,'pop',2))
    for i,name in enumerate(names):
        yy=210+i*80;delta=RADAR['pilot'][i]-RADAR['current'][i]
        p += [motion(txt(900,yy,name,INK,30),'fade',2+i),motion(txt(1230,yy,RADAR['current'][i],INK,49,'middle',style='fd-editorial'),'fade',2+i),motion(txt(1430,yy,RADAR['pilot'][i],GREEN,49,'middle',style='fd-editorial'),'fade',2+i),motion(txt(1620,yy,f'+{delta}',GREEN,27,'middle'),'fade',2+i),rule(900,yy+27,1660,yy+27,SILVER,1)]
    return section('radar',lang,tr(lang,'Assess the whole decision.','把判断，看得更完整。'),
                   tr(lang,'Each dimension uses the same 0–100 scale and definition.',
                      '各维度采用同一0—100分量表与统一定义。'),
                   tr(lang,'RUBRIC POINTS · 0–100','量表评分：0—100分'),RADAR,p,
                   tr(lang,'Five equally scaled axes: clarity, evidence, ownership, speed, review. Current 54,68,72,48,60; pilot 80,82,86,76,84. The table shows exact values; both outlines are unfilled.',
                      '清晰度、证据、责任归属、速度、复盘五轴均为0至100。当前54、68、72、48、60；试点80、82、86、76、84。两个无填色轮廓不遮挡，右表保留全部数值。'))


def sankey_positions():
    out=[]
    for totals in (SANKEY['inputs'],SANKEY['middle'],SANKEY['outputs']):
        gap=(480-sum(totals)*SANKEY['pixels_per_request'])/(len(totals)-1)
        yy=70;group=[]
        for v in totals:
            h=v*SANKEY['pixels_per_request'];group.append((yy,h));yy+=h+gap
        out.append(group)
    return out


def sankey_slide(lang):
    gid="focus-review-silver-"+lang
    p=[f"<defs>{silver_surface(gid)}</defs>"];positions=sankey_positions();xs=[95,760,1350];widths=[190,200,200];colors=[GREEN,SILVER,LEAF]
    labels=[]
    for stage,matrix in enumerate((SANKEY['a'],SANKEY['b'])):
        src=[0]*len(matrix);dst=[0]*len(matrix[0])
        for i,row in enumerate(matrix):
            for j,value in enumerate(row):
                sy=positions[stage][i][0]+src[i];ty=positions[stage+1][j][0]+dst[j];h=value*4
                x1=xs[stage]+widths[stage];x2=xs[stage+1];dx=(x2-x1)*.45
                path=(f'M{n(x1)} {n(sy)} C{n(x1+dx)} {n(sy)} {n(x2-dx)} {n(ty)} {n(x2)} {n(ty)} '
                      f'L{n(x2)} {n(ty+h)} C{n(x2-dx)} {n(ty+h)} {n(x1+dx)} {n(sy+h)} {n(x1)} {n(sy+h)} Z')
                color=colors[i] if stage==0 else [GREEN,LEAF][j]
                p.append(motion(f'<path data-flow-stage="{stage+1}" data-flow-source="{i}" data-flow-target="{j}" data-flow-value="{value}" d="{path}" fill="{color}" fill-opacity=".38"/>', 'wipe-x', 1+stage*2))
                # t=.18 stays near the distinct source ends, keeping all ten values apart.
                t=.18;u=1-t;lx=u**3*x1+3*u*u*t*(x1+dx)+3*u*t*t*(x2-dx)+t**3*x2
                blend=3*t*t-2*t*t*t;ly=(1-blend)*(sy+h/2)+blend*(ty+h/2)
                labels.append(motion(txt(lx,ly+9,value,INK,28,'middle',f'data-flow-label="{stage+1}-{i}-{j}" stroke="{PAPER}" stroke-width="6" paint-order="stroke" stroke-linejoin="round"'), 'fade', 2+stage*2))
                src[i]+=h;dst[j]+=h
    names=[[tr(lang,'Research','研究'),tr(lang,'Customers','客户'),tr(lang,'Operations','运营')],
           [tr(lang,'Investigate','调研'),tr(lang,'Test','试验')],
           [tr(lang,'Commit','推进'),tr(lang,'Hold','暂缓')]]
    for g,totals in enumerate((SANKEY['inputs'],SANKEY['middle'],SANKEY['outputs'])):
        p.append(txt(xs[g]+widths[g]/2,29,tr(lang,['Source','Review route','Decision'][g],['问题来源','评估路径','决策结果'][g]),INK,28,'middle'))
        for i,v in enumerate(totals):
            yy,h=positions[g][i];fill=PAPER if g==0 else f'url(#{gid})' if g==1 else [DEEP,LEAF][i];fg=PAPER if g==2 and i==0 else INK
            p += [motion(rect(xs[g],yy,widths[g],h,fill,f'stroke="{GREEN}" stroke-width="1.2"'), 'fade', g*2),motion(txt(xs[g]+widths[g]/2,yy+h/2-16,names[g][i],fg,25,'middle'), 'fade', g*2),
                  motion(txt(xs[g]+widths[g]/2,yy+h/2+32,v,fg,55,'middle',style='fd-editorial'), 'fade', g*2)]
    p+=labels
    return section('sankey',lang,tr(lang,'Follow the decision path.','看清，每一步的流向。'),
                   tr(lang,'One hundred requests, from their source through review to a recorded decision.',
                      '同一批100项需求，从问题来源，经评估路径，走向明确决定。'),
                   tr(lang,'REQUESTS · TOTAL 100','单位：项 · 总量100'),SANKEY,p,
                   tr(lang,'Sources research40, customers35, operations25; investigation60 and testing40; commit65 and hold35. First-stage flows30,10,20,15,10,15. Second-stage flows40,20,25,15. All ten ribbons are labelled. Every node balances its incoming and outgoing requests.',
                      '来源为研究40、客户35、运营25；调研60、试验40；推进65、暂缓35。第一层六条流量30、10、20、15、10、15；第二层四条40、20、25、15。全部十条标值，每节点流入流出守恒。'))


def scatter_slide(lang):
    x=lambda v:100+v/12*1440;y=lambda v:500-v/50*380
    p=[txt(100,34,tr(lang,'Hours saved / week','预计每周节省时间 · 小时'),INK,28),txt(1540,34,tr(lang,'Where effort can matter.','让投入，用在值得之处。'),GREEN,36,'end',style='fd-editorial-italic')]
    for v in (0,10,20,30,40,50):
        p += [rule(100,y(v),1540,y(v),INK if v==0 else SILVER,1.3 if v==0 else 1),txt(73,y(v)+9,v,INK,27,'end')]
    for v in (0,2,4,6,8,10,12):p += [rule(x(v),500,x(v),510,INK,1.2),txt(x(v),549,v,INK,28,'middle')]
    p.append(txt(1540,601,tr(lang,'Estimated effort · person-days','预计投入 · 人日'),INK,28,'end'))
    for i,(en,zh,effort,impact) in enumerate(SCATTER):
        px,py=x(effort),y(impact)
        marker=circle(px,py,10.5,GREEN,f'data-point-id="{i}" stroke="{PAPER}" stroke-width="2.5"')
        p.append(motion(marker,'pop',i))
        tx,anchor=(px-18,'end') if effort>=9 else (px+18,'start')
        p.append(motion(txt(tx,py-18,tr(lang,en,zh),INK,28,anchor),'fade',i+1))
    # Numerical annotation is tied to the same plotted point, not a new prediction.
    px,py=x(9.5),y(46)
    p += [rule(px,py+15,px,py+75,GREEN,1.2),motion(txt(px,py+113,tr(lang,'46 h/week · 9.5 person-days','46小时/周 · 9.5人日'),GREEN,30,'middle',style='fd-editorial'),'fade',7)]
    return section('scatter',lang,tr(lang,'Choose what to test next.','选出，值得验证的下一步。'),
                   tr(lang,'Compare eight proposals by effort and potential weekly time saved.',
                      '把八个提案放在同一张坐标上，比较预计投入与每周节省时间。'),
                   tr(lang,'EFFORT & WEEKLY HOURS SAVED','投入与每周节省时间'),
                   {'points':[{'name_en':a,'name_zh':b,'effort_person_days':x,'hours_saved_per_week':y} for a,b,x,y in SCATTER],
                    'x_range':[0,12],'y_range':[0,50]},p,
                   tr(lang,'Eight labelled proposals. X is estimated effort in person-days from0–12; y is estimated hours saved each week from0–50. No causal relationship is claimed.',
                      '八个具名提案。横轴预计投入0至12人日，纵轴预计每周节省0至50小时，不作因果推断。'))


def heatmap_slide(lang):
    rows=[tr(lang,en,zh) for en,zh in zip(HEATMAP['rows'],['目标','证据','负责人','下一步'])]
    p=[rule(0,59,1645,59,INK,1.3)]
    for i,col in enumerate(HEATMAP['columns']):p.append(txt(360+i*222,34,tr(lang,f'Team {col}',f'{col}组'),INK,28,'middle'))
    for i,values in enumerate(HEATMAP['values']):
        yy=84+i*110;p.append(txt(0,yy+58,rows[i],INK,43,style='fd-editorial'))
        for j,v in enumerate(values):
            fill=PAPER if v<50 else SILVER if v<75 else DEEP;fg=PAPER if v>=75 else INK
            p += [motion(rect(260+j*222,yy,200,91,fill,f'stroke="{SILVER}" stroke-width="1" data-heat-row="{i}" data-heat-column="{j}" data-heat-value="{v}"'),'fade',i),motion(txt(360+j*222,yy+62,v,fg,51,'middle',style='fd-editorial'),'fade',i)]
    p.append(txt(0,581,tr(lang,'Completeness / 100','完整度／100分'),GREEN,36,style='fd-editorial-italic'))
    for i,(label,fill) in enumerate([('0–49',PAPER),('50–74',SILVER),('75–100',DEEP)]):
        xx=795+i*265;p += [rect(xx,549,32,32,fill,f'stroke="{SILVER}" stroke-width="1"'),txt(xx+47,578,label,INK,27)]
    return section('heatmap',lang,tr(lang,'Find the gaps before committing.','做决定前，先补齐缺口。'),
                   tr(lang,'Purpose, evidence, ownership and next steps across six teams.',
                      '六个团队，依次检查目标、证据、负责人和下一步。'),
                   tr(lang,'COMPLETENESS SCORE · 0–100','完整度评分：0—100分'),HEATMAP,p,
                   tr(lang,'A4 by6 matrix of illustrative decision-brief completeness scores. Rows purpose,evidence,owner,next step; teamsA–F. Bands0–49,50–74,75–100. Higher means a more complete brief, not a better decision outcome.',
                      '4行6列决策简报完整度示例评分，行是目标、证据、负责人、下一步，列是A至F组。分段0至49、50至74、75至100。高分代表简报更完整，不代表决策结果更好。'))


def validate_data():
    assert len(LINE['weeks'])==len(LINE['usual'])==len(LINE['focused'])==6
    assert all(0<=v<=12 for k in ('usual','focused') for v in LINE[k])
    assert len(AREA['weeks'])==len(AREA['values'])==8 and all(0<=v<=50 for v in AREA['values'])
    assert len(RADAR['dimensions'])==5
    assert all(len(RADAR[k])==5 and all(0<=v<=100 for v in RADAR[k]) for k in ('current','pilot'))
    a,b=SANKEY['a'],SANKEY['b']
    assert [sum(r)for r in a]==SANKEY['inputs']
    assert [sum(r[j]for r in a)for j in range(2)]==SANKEY['middle']
    assert [sum(r)for r in b]==SANKEY['middle']
    assert [sum(r[j]for r in b)for j in range(2)]==SANKEY['outputs']
    assert sum(SANKEY['inputs'])==sum(SANKEY['middle'])==sum(SANKEY['outputs'])==100
    assert all(v>0 for matrix in (a,b)for row in matrix for v in row)
    assert sum(len(row)for matrix in (a,b)for row in matrix)==10
    assert min(v*4 for matrix in (a,b)for row in matrix for v in row)>=40
    assert all(70<=y and y+h<=550 for group in sankey_positions()for y,h in group)
    assert len(SCATTER)==8 and all(0<=x<=12 and 0<=y<=50 for _,_,x,y in SCATTER)
    assert len(set(a for a,_,_,_ in SCATTER))==8
    assert len(HEATMAP['values'])==4 and all(len(r)==6 and all(0<=v<=100 for v in r)for r in HEATMAP['values'])
    return {'status':'PASS','line':{'series':2,'points_each':6,'unit':'median days','axis':[0,12]},
            'area':{'points':8,'unit':'notes/week','axis':[0,50],'zero_baseline':True,'cumulative':False},
            'radar':{'series':2,'dimensions':5,'axis_each':[0,100],'unfilled':True},
            'sankey':{'layers':[3,2,2],'total_each':100,'flow_labels':10,'node_conservation':True,'pixels_per_request':4,'minimum_ribbon_height':40},
            'scatter':{'points':8,'x_unit':'person-days','y_unit':'hours saved/week','causal_claim':False},
            'heatmap':{'rows':4,'columns':6,'exact_values':24,'score_range':[0,100],'bands':[[0,49],[50,74],[75,100]]}}


def get_slides(lang='en'):
    if lang not in ('en','zh','zh-CN'):
        raise ValueError('lang must be en, zh or zh-CN')
    validate_data()
    return [f(lang)for f in (line_slide,area_slide,radar_slide,sankey_slide,scatter_slide,heatmap_slide)]


if __name__=='__main__':
    print(json.dumps(validate_data(),ensure_ascii=False,indent=2))
