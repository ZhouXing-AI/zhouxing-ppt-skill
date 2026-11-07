"""Six bilingual EDIT charts: manuscripts, review, selection and publication.

All data are illustrative. Geometry is calculated from the constants below;
animation attributes never change the final numbers, coordinates or proportions.
Public API: get_slides('en' | 'zh' | 'zh-CN'), validate_data().
"""
from html import escape
from math import cos, sin, pi
import json

PAPER = '#f2eee7'
BRIGHT = '#fcf8f0'
INK = '#352129'
RED = '#b64032'
BLUSH = '#e8a496'
MUTED = '#d8d1c9'

LINE = {'weeks': [1, 2, 3, 4, 5, 6],
        'copy_edit': [11, 10, 9, 9, 8, 7],
        'proofread': [10, 8, 7, 6, 4, 3],
        'unit': 'median turnaround days', 'range': [0, 12]}
AREA = {'weeks': list(range(1, 9)), 'values': [9, 14, 12, 21, 19, 29, 32, 38],
        'unit': 'accepted short pieces per week', 'range': [0, 40]}
RADAR = {'draft': [52, 72, 64, 58, 46], 'revision': [84, 88, 86, 80, 78],
         'dimensions': ['Structure', 'Accuracy', 'Clarity', 'Voice', 'Rhythm'],
         'unit': 'illustrative editorial rubric points', 'range': [0, 100]}
SANKEY = {'inputs': [50, 30, 20], 'middle': [55, 45], 'outputs': [70, 30],
          'a': [[35, 15], [10, 20], [10, 10]],
          'b': [[40, 15], [30, 15]],
          'unit': 'manuscripts', 'total': 100, 'pixels_per_manuscript': 4}
SCATTER = [
    ('Brief', '短讯', 2, 40), ('Interview', '访谈', 5, 73),
    ('Guide', '指南', 8, 64), ('Profile', '人物', 11, 88),
    ('Explainer', '解读', 14, 57), ('Essay', '随笔', 17, 78),
    ('Report', '专题', 20, 91), ('Review', '评论', 22, 46),
]
HEATMAP = {'values': [[70, 85, 55, 95, 65, 80], [90, 60, 45, 85, 75, 50],
                      [65, 80, 70, 90, 55, 75], [50, 75, 60, 85, 40, 70]],
           'rows': ['Lead', 'Sources', 'Structure', 'Ending'],
           'columns': ['A', 'B', 'C', 'D', 'E', 'F'],
           'range': [0, 100], 'unit': 'editorial readiness rubric points'}


def tr(lang, en, zh):
    return zh if lang in ('zh', 'zh-CN') else en


def n(value):
    return f'{value:.3f}'.rstrip('0').rstrip('.')


def txt(x, y, value, color=INK, size=28, anchor='start', extra='', style=''):
    return (f'<text x="{n(x)}" y="{n(y)}" fill="{color}" font-size="{size}" '
            f'text-anchor="{anchor}" class="{style}" {extra}>{escape(str(value))}</text>')


def rule(x1, y1, x2, y2, color=MUTED, width=1.2, extra=''):
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
    """Annotate one final-state SVG element; do not mutate its geometry."""
    return markup.replace(' ', f' data-chart-motion="{kind}" data-chart-step="{step}" ', 1)


def bracket(x, top, bottom, width=18, color=RED):
    """A static proofreader's bracket, outside quantitative plotting areas."""
    return (f'<path d="M{n(x+width)} {n(top)} H{n(x)} V{n(bottom)} H{n(x+width)}" '
            f'fill="none" stroke="{color}" stroke-width="2"/>')


def graphic(parts, label, description):
    return ('<svg viewBox="0 0 1680 610" xmlns="http://www.w3.org/2000/svg" '
            f'data-information-visual="" role="img" aria-label="{escape(label, quote=True)}">'
            f'<title>{escape(label)}</title><desc>{escape(description)}</desc>' + ''.join(parts) + '</svg>')


def section(kind, lang, heading, subtitle, unit, values, parts, description, dark=False):
    tone = 'dark' if dark else 'light'
    cls = ' dark-page' if dark else ''
    data = escape(json.dumps(values, ensure_ascii=False, separators=(',', ':')), quote=True)
    emphasized = {
        'line': ('One deadline.', '同一截期。'),
        'area': ('takes shape.', '逐渐成形。'),
        'radar': ('many sides.', '不止改一处。'),
        'sankey': ('a route.', '清晰去向。'),
        'scatter': ('the next story.', '值得写的。'),
        'heatmap': ('need a pass?', '再看？'),
    }
    phrase = emphasized[kind][1 if lang in ('zh', 'zh-CN') else 0]
    heading_markup = escape(heading).replace(escape(phrase), '<em>'+escape(phrase)+'</em>')
    return (f'<section class="slide edit-data edit-analysis ed-{kind}{cls}" data-tone="{tone}" '
            f'data-chart-kind="{kind}" data-chart-values="{data}" data-chart-unit="{escape(unit, quote=True)}" '
            f'data-provenance="illustrative" data-title="{escape(heading, quote=True)}">'
            f'<header class="ed-heading"><h2 class="reveal">{heading_markup}</h2>'
            f'<p class="ed-subtitle reveal">{escape(subtitle)}</p></header>'
            f'<div class="ed-chart" data-chart-container="">{graphic(parts, heading, description)}</div></section>')


def line_slide(lang):
    # A single wide editorial figure. Its two names belong to the actual line ends.
    x = lambda i: 110+i*238
    y = lambda v: 500-v/12*360
    p = [txt(110, 35, tr(lang, 'Turnaround · median days', '周转时间 · 中位天数')),
         rule(110, 70, 1640, 70, RED, 1.2), bracket(10, 112, 500, 25)]
    for value in (0, 3, 6, 9, 12):
        p += [rule(110,y(value),1300,y(value),INK if value==0 else MUTED,1.3 if value==0 else 1),
              txt(81,y(value)+9,value,INK,27,'end')]
    for i in range(6):
        p += [rule(x(i),500,x(i),510,INK,1),txt(x(i),552,tr(lang,f'Week {i+1}',f'第{i+1}周'),INK,28,'middle')]
    for series,(key,color,dash) in enumerate([('copy_edit',INK,'stroke-dasharray="10 7"'),('proofread',RED,'')]):
        points=[(x(i),y(v)) for i,v in enumerate(LINE[key])]
        p.append(motion(f'<path d="{poly(points)}" fill="none" stroke="{color}" stroke-width="4.2" stroke-linejoin="round" {dash}/>','wipe-x' if dash else 'draw',series))
        for px,py in points:
            marker=rect(px-5.5,py-5.5,11,11,PAPER,f'stroke="{color}" stroke-width="2.5"') if key=='copy_edit' else circle(px,py,6.5,PAPER,f'stroke="{color}" stroke-width="2.7"')
            p.append(motion(marker,'pop',2))
        value=LINE[key][-1];yy=y(value)
        p.append(motion(rule(1316,yy,1360,yy,color,1.6,dash),'wipe-x',3))
        name=tr(lang,'Copy edit','文字编辑') if key=='copy_edit' else tr(lang,'Proofread','校对')
        p.append(motion(txt(1382,yy-9,name,color,35,style='ed-chart-display'),'fade',3))
        p.append(motion(txt(1382,yy+38,tr(lang,f'{value} days',f'{value} 天'),color,30),'fade',3))
    return section('line',lang,tr(lang,'Two desks. One deadline.','两道校阅，同一截期。'),
                   tr(lang,'Six weeks of median turnaround, from assignment to a returned manuscript.',
                      '六周内，从分配稿件到交回审稿结果的周转时间中位数。'),
                   tr(lang,'MEDIAN DAYS','单位：天，中位数'),LINE,p,
                   tr(lang,'Weeks 1–6: copy editing takes 11,10,9,9,8,7 median days; proofreading takes 10,8,7,6,4,3. Both series use the same 0–12 day scale. Different review tasks are compared without a causal claim.',
                      '第1至6周，文字编辑为11、10、9、9、8、7天，校对为10、8、7、6、4、3天，均为中位数；共用0至12天标尺。对比两种校阅任务，不作因果推断。'))


def area_slide(lang):
    # A typographic weekly figure and one open ink-page plot; no generic chart card.
    x=lambda i:620+i*140
    y=lambda v:505-v/40*365
    gid='edit-weekly-ink-'+lang
    p=[f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop stop-color="{BLUSH}" stop-opacity=".65"/><stop offset="1" stop-color="{BLUSH}" stop-opacity=".08"/></linearGradient></defs>',
       txt(8,43,tr(lang,'In the eighth week','第八周'),BLUSH,39,style='ed-chart-italic'),
       motion(txt(-5,290,AREA['values'][-1],PAPER,250,style='ed-chart-display'),'fade',2),
       txt(9,350,tr(lang,'accepted short pieces','篇短稿，确认采用'),PAPER,30),
       rule(0,408,445,408,BLUSH,1.2),
       txt(9,463,tr(lang,'Counted week by week.','按周记录，逐期成形。'),BLUSH,38,style='ed-chart-italic'),
       txt(620,43,tr(lang,'Accepted pieces / week','每周采用短稿 · 篇'),PAPER,28)]
    for value in (0,10,20,30,40):
        p += [rule(620,y(value),1600,y(value),PAPER,1.2 if value==0 else 1,f'opacity="{.42 if value==0 else .16}"'),
              txt(592,y(value)+9,value,PAPER,27,'end')]
    points=[(x(i),y(v)) for i,v in enumerate(AREA['values'])]
    p += [motion(f'<path d="{poly([(620,505)]+points+[(1600,505)])} Z" fill="url(#{gid})"/>','wipe-x',0),
          motion(f'<path d="{poly(points)}" fill="none" stroke="{BLUSH}" stroke-width="4.2" stroke-linejoin="round"/>','draw',1)]
    for i in (0,3,7):
        p += [motion(circle(x(i),y(AREA['values'][i]),6.5,INK,f'stroke="{BLUSH}" stroke-width="2.8"'),'pop',2),
              motion(txt(x(i),y(AREA['values'][i])-22,AREA['values'][i],PAPER,37,'middle'),'fade',2)]
    for i in range(8):p.append(txt(x(i),559,tr(lang,f'W{i+1}',f'第{i+1}周'),PAPER,27,'middle'))
    return section('area',lang,tr(lang,'An issue takes shape.','让每一期，逐渐成形。'),
                   tr(lang,'Short pieces accepted each week, under one unchanged editorial standard.',
                      '采用相同编辑标准，记录每周确认采用的短稿数量。'),
                   tr(lang,'ACCEPTED PIECES PER WEEK','单位：篇／周'),AREA,p,
                   tr(lang,'Weekly accepted short pieces:9,14,12,21,19,29,32,38. The area is plotted from the zero baseline on a 0–40 scale. These are separate weekly counts, not a cumulative series.',
                      '每周采用的短稿为9、14、12、21、19、29、32、38篇；面积从零基线展开，纵轴0至40。这里是每周数量，不是累计数量。'),dark=True)


def radar_slide(lang):
    # A ruled proof table and its open diagram share one page, without a boxed sidebar.
    names=[tr(lang,en,zh) for en,zh in zip(RADAR['dimensions'],['结构','准确','清晰','语气','节奏'])]
    cx,cy,radius=1230,315,188
    def point(i,v):
        a=-pi/2+i*2*pi/5
        return cx+radius*v/100*cos(a),cy+radius*v/100*sin(a)
    p=[txt(35,38,tr(lang,'Read the revision, dimension by dimension.','逐项读懂，这一次修订。'),RED,42,style='ed-chart-italic'),
       rule(35,77,740,77,INK,1.2),
       rule(405,118,441,118,INK,3.5,'stroke-dasharray="9 6"'),txt(456,127,tr(lang,'Draft','初稿'),INK,27),
       rule(600,118,636,118,RED,3.5),txt(650,127,tr(lang,'Revision','修订稿'),INK,27),
       bracket(0,168,559,18),txt(1230,603,tr(lang,'Editorial points · 0–100','编辑评分 · 0—100分'),INK,28,'middle')]
    for i,name in enumerate(names):
        yy=210+i*77
        p += [motion(txt(35,yy,name,INK,32),'fade',2+i),
              motion(txt(471,yy,RADAR['draft'][i],INK,49,'middle',style='ed-chart-display'),'fade',2+i),
              motion(txt(665,yy,RADAR['revision'][i],RED,49,'middle',style='ed-chart-display'),'fade',2+i),
              rule(35,yy+25,740,yy+25,MUTED,1)]
    for v in (20,40,60,80,100):
        p += [f'<path d="{poly([point(i,v) for i in range(5)])} Z" fill="none" stroke="{MUTED}" stroke-width="1.2"/>',
              txt(cx+12,cy-radius*v/100+8,v,INK,25)]
    p.append(txt(cx+12,cy+23,0,INK,25))
    for i,name in enumerate(names):
        px,py=point(i,100);p.append(rule(cx,cy,px,py,MUTED,1.2))
        px,py=point(i,139);p.append(txt(px,py+9,name,INK,29,'middle'))
    for series,(key,color,dash) in enumerate([('draft',INK,'stroke-dasharray="10 7"'),('revision',RED,'')]):
        points=[point(i,v) for i,v in enumerate(RADAR[key])]
        p.append(motion(f'<path d="{poly(points)} Z" fill="none" stroke="{color}" stroke-width="4.1" stroke-linejoin="round" {dash}/>','wipe-x' if dash else 'draw',series))
        for px,py in points:
            marker=rect(px-5,py-5,10,10,PAPER,f'stroke="{color}" stroke-width="2.5"') if key=='draft' else circle(px,py,6,PAPER,f'stroke="{color}" stroke-width="2.7"')
            p.append(motion(marker,'pop',2))
    return section('radar',lang,tr(lang,'A revision has many sides.','好修订，不止改一处。'),
                   tr(lang,'Draft and revision, assessed on five 0–100 point scales with the same definitions.',
                      '对初稿与修订稿逐项评估；五个维度均采用0—100分与同一定义。'),
                   tr(lang,'EDITORIAL POINTS · 0–100','编辑评分：0—100分'),RADAR,p,
                   tr(lang,'Structure,accuracy,clarity,voice,rhythm each use 0–100. Draft52,72,64,58,46; revision84,88,86,80,78. Both outlines are unfilled and the ledger preserves all exact scores. Polygon area is not used as an overall quality score.',
                      '结构、准确、清晰、语气、节奏均采用0至100分。初稿52、72、64、58、46，修订稿84、88、86、80、78。轮廓不填色，左表保留准确数值；不以多边形面积判断整体质量。'))


def sankey_positions():
    positions=[]
    for totals in (SANKEY['inputs'],SANKEY['middle'],SANKEY['outputs']):
        gap=(480-sum(totals)*SANKEY['pixels_per_manuscript'])/(len(totals)-1)
        yy=65;group=[]
        for v in totals:
            h=v*SANKEY['pixels_per_manuscript'];group.append((yy,h));yy+=h+gap
        positions.append(group)
    return positions


def sankey_slide(lang):
    positions=sankey_positions();xs=[30,730,1390];widths=[260,250,260]
    p=[];labels=[];scale=SANKEY['pixels_per_manuscript'];colors=[RED,INK,BLUSH]
    for stage,matrix in enumerate((SANKEY['a'],SANKEY['b'])):
        src=[0]*len(matrix);dst=[0]*len(matrix[0])
        for i,row in enumerate(matrix):
            for j,v in enumerate(row):
                sy=positions[stage][i][0]+src[i];ty=positions[stage+1][j][0]+dst[j];h=v*scale
                x1=xs[stage]+widths[stage];x2=xs[stage+1];dx=(x2-x1)*.45
                path=(f'M{n(x1)} {n(sy)} C{n(x1+dx)} {n(sy)} {n(x2-dx)} {n(ty)} {n(x2)} {n(ty)} '
                      f'L{n(x2)} {n(ty+h)} C{n(x2-dx)} {n(ty+h)} {n(x1+dx)} {n(sy+h)} {n(x1)} {n(sy+h)} Z')
                color=colors[i] if stage==0 else [RED,INK][j]
                p.append(motion(f'<path data-flow-stage="{stage+1}" data-flow-source="{i}" data-flow-target="{j}" data-flow-value="{v}" d="{path}" fill="{color}" fill-opacity=".29"/>','wipe-x',1+stage*2))
                t=.20;u=1-t;lx=u**3*x1+3*u*u*t*(x1+dx)+3*u*t*t*(x2-dx)+t**3*x2
                blend=3*t*t-2*t*t*t;ly=(1-blend)*(sy+h/2)+blend*(ty+h/2)
                labels.append(motion(txt(lx,ly+9,v,INK,28,'middle',f'data-flow-label="{stage+1}-{i}-{j}" stroke="{PAPER}" stroke-width="6" paint-order="stroke" stroke-linejoin="round"'),'fade',2+stage*2))
                src[i]+=h;dst[j]+=h
    names=[[tr(lang,'Open call','征稿'),tr(lang,'Archive','存稿'),tr(lang,'Commission','约稿')],
           [tr(lang,'Copy edit','文字编辑'),tr(lang,'Fact check','事实核查')],
           [tr(lang,'Publish','采用'),tr(lang,'Rework','退修')]]
    for g,totals in enumerate((SANKEY['inputs'],SANKEY['middle'],SANKEY['outputs'])):
        p.append(txt(xs[g],27,tr(lang,['Manuscript source','Primary review','Outcome'][g],['稿件来源','主要校阅路径','处理结果'][g]),INK,28))
        for i,v in enumerate(totals):
            yy,h=positions[g][i];fill=BRIGHT if g<2 else [RED,INK][i];fg=PAPER if g==2 else INK
            p += [motion(rect(xs[g],yy,widths[g],h,fill,f'stroke="{RED if g<2 else fill}" stroke-width="1.3"'),'fade',g*2),
                  motion(txt(xs[g]+20,yy+h/2+9,names[g][i],fg,26),'fade',g*2),
                  motion(txt(xs[g]+widths[g]-19,yy+h/2+14,v,fg,46,'end',style='ed-chart-display'),'fade',g*2)]
    p+=labels
    p += [rule(30,580,1650,580,RED,1.2),txt(30,610,tr(lang,'100 manuscripts · one primary review route for each','100篇稿件 · 每篇归入一条主要校阅路径'),INK,27)]
    return section('sankey',lang,tr(lang,'Every manuscript has a route.','让每一篇稿，有清晰去向。'),
                   tr(lang,'From manuscript source, through its primary review, to a publishing decision.',
                      '从稿件来源，经主要校阅路径，走向采用或退修的决定。'),
                   tr(lang,'MANUSCRIPTS · TOTAL 100','单位：篇 · 总量100'),SANKEY,p,
                   tr(lang,'Sources:open call50,archive30,commission20. Primary review:copy edit55,fact check45. Outcomes:publish70,rework30. First-layer flows35,15,10,20,10,10; second-layer40,15,30,15. All ten flows are labelled; all nodes and layers conserve the total100.',
                      '征稿50、存稿30、约稿20篇；主要路径为文字编辑55、事实核查45篇；采用70、退修30篇。第一层流量35、15、10、20、10、10，第二层40、15、30、15。十条均标值，所有节点与层均守恒。'))


def scatter_slide(lang):
    x=lambda v:110+v/24*1440
    y=lambda v:500-v/100*365
    p=[txt(110,35,tr(lang,'Editorial relevance · points','选题相关度 · 分'),INK,28),
       rule(110,70,1550,70,RED,1.2),
       f'<path d="M70 115H40V165 M1590 525h30v-50" fill="none" stroke="{RED}" stroke-width="1.5"/>']
    for v in (0,25,50,75,100):
        p += [rule(110,y(v),1550,y(v),INK if v==0 else MUTED,1.3 if v==0 else 1),txt(82,y(v)+9,v,INK,27,'end')]
    for v in (0,4,8,12,16,20,24):
        p += [rule(x(v),500,x(v),510,INK,1),txt(x(v),551,v,INK,28,'middle')]
    for i,(en,zh,hours,score) in enumerate(SCATTER):
        px,py=x(hours),y(score);tx,anchor=(px-18,'end') if hours>=20 else (px+18,'start')
        p += [motion(circle(px,py,10,BRIGHT,f'data-point-id="{i}" stroke="{RED}" stroke-width="3.3"'),'pop',i),
              motion(txt(tx,py-18,tr(lang,en,zh),INK,29,anchor),'fade',i+1)]
    p.append(txt(1550,607,tr(lang,'Estimated reporting effort · hours','预计采写投入 · 小时'),INK,28,'end'))
    return section('scatter',lang,tr(lang,'Choose the next story.','选出下一篇，值得写的。'),
                   tr(lang,'Eight story ideas, compared by estimated reporting time and editorial relevance.',
                      '从预计采写时间与选题相关度，比较八个待验证的想法。'),
                   tr(lang,'HOURS & RELEVANCE POINTS','采写小时与相关度评分'),
                   {'points':[{'name_en':en,'name_zh':zh,'reporting_hours':hours,'relevance_points':score} for en,zh,hours,score in SCATTER],
                    'x_range':[0,24],'y_range':[0,100]},p,
                   tr(lang,'Eight labelled story ideas. The x-axis is estimated reporting hours0–24; the y-axis is editorial relevance points0–100. Relevance is an illustrative rubric score, not readership or actual impact. Point size is constant; no causal relationship is claimed.',
                      '八个具名选题。横轴为预计采写0至24小时，纵轴为选题相关度0至100分。相关度是示例量表评分，不是阅读量或实际影响；点大小一致，不作因果推断。'))


def heatmap_slide(lang):
    # Six narrow proof strips: their equal-width cells still form a strict 4×6 matrix.
    rows=[tr(lang,en,zh) for en,zh in zip(HEATMAP['rows'],['导语','信源','结构','收尾'])]
    p=[]
    for j,col in enumerate(HEATMAP['columns']):
        xx=260+j*230
        p += [rect(xx,0,198,508,BRIGHT),rule(xx+16,63,xx+182,63,RED,1.2),
              txt(xx+99,44,tr(lang,f'Piece {col}',f'稿件{col}'),INK,30,'middle',style='ed-chart-display')]
    for i,vals in enumerate(HEATMAP['values']):
        yy=84+i*101;p.append(txt(220,yy+56,rows[i],PAPER,33,'end',style='ed-chart-display'))
        for j,v in enumerate(vals):
            xx=260+j*230;fill=BRIGHT if v<50 else BLUSH if v<75 else RED;fg=PAPER if v>=75 else INK
            p += [motion(rect(xx+14,yy,170,84,fill,f'stroke="{MUTED if v<50 else fill}" stroke-width="1" data-heat-row="{i}" data-heat-column="{j}" data-heat-value="{v}"'),'fade',i),
                  motion(txt(xx+99,yy+57,v,fg,47,'middle',style='ed-chart-display'),'fade',i)]
    p += [txt(8,583,tr(lang,'Readiness / 100','就绪度／100分'),PAPER,37,style='ed-chart-italic')]
    for i,(label,fill) in enumerate([('0–49',BRIGHT),('50–74',BLUSH),('75–100',RED)]):
        xx=840+i*270;p += [rect(xx,551,32,32,fill),txt(xx+48,580,label,PAPER,27)]
    return section('heatmap',lang,tr(lang,'Which pages need a pass?','哪一篇，还需要再看？'),
                   tr(lang,'Six pieces, checked against four readiness criteria. Each score remains visible.',
                      '六篇稿件，按导语、信源、结构与收尾，逐项检查就绪程度。'),
                   tr(lang,'READINESS POINTS · 0–100','就绪度评分：0—100分'),HEATMAP,p,
                   tr(lang,'A4×6 matrix:lead,sources,structure,ending across piecesA–F. Each cell uses the same editorial readiness rubric0–100; bands0–49,50–74,75–100. Higher scores indicate readiness against these checks, not predicted audience response.',
                      '四行六列矩阵：导语、信源、结构、收尾，对应A至F稿件；统一使用0至100分就绪度量表，色阶0至49、50至74、75至100。高分表示更符合这些检查标准，不预测读者反馈。'),dark=True)


def validate_data():
    assert len(LINE['weeks'])==len(LINE['copy_edit'])==len(LINE['proofread'])==6
    assert all(0<=value<=12 for key in ('copy_edit','proofread') for value in LINE[key])
    assert len(AREA['weeks'])==len(AREA['values'])==8 and all(0<=value<=40 for value in AREA['values'])
    assert len(RADAR['dimensions'])==5
    assert all(len(RADAR[key])==5 and all(0<=value<=100 for value in RADAR[key]) for key in ('draft','revision'))
    a,b=SANKEY['a'],SANKEY['b']
    assert [sum(row) for row in a]==SANKEY['inputs']
    assert [sum(row[j] for row in a) for j in range(2)]==SANKEY['middle']
    assert [sum(row) for row in b]==SANKEY['middle']
    assert [sum(row[j] for row in b) for j in range(2)]==SANKEY['outputs']
    assert sum(SANKEY['inputs'])==sum(SANKEY['middle'])==sum(SANKEY['outputs'])==SANKEY['total']==100
    flows=[value for matrix in (a,b) for row in matrix for value in row]
    assert len(flows)==10 and min(flows)>0
    assert min(flows)*SANKEY['pixels_per_manuscript']>=40
    assert all(65<=yy and yy+h<=545 for group in sankey_positions() for yy,h in group)
    assert len(SCATTER)==8 and len({en for en,_,_,_ in SCATTER})==8
    assert all(0<=hours<=24 and 0<=score<=100 for _,_,hours,score in SCATTER)
    assert len(HEATMAP['values'])==4 and len(HEATMAP['columns'])==6
    assert all(len(row)==6 and all(0<=value<=100 for value in row) for row in HEATMAP['values'])
    return {'status':'PASS',
            'line':{'series':2,'points_each':6,'unit':'median turnaround days','axis':[0,12]},
            'area':{'points':8,'unit':'accepted pieces/week','axis':[0,40],'zero_baseline':True,'cumulative':False},
            'radar':{'series':2,'dimensions':5,'axis_each':[0,100],'unfilled':True},
            'sankey':{'layers':[3,2,2],'total_each':100,'flow_labels':10,'node_conservation':True,'pixels_per_manuscript':4,'minimum_ribbon_height':40},
            'scatter':{'points':8,'x_unit':'estimated reporting hours','x_range':[0,24],'y_unit':'editorial relevance points','y_range':[0,100],'causal_claim':False},
            'heatmap':{'rows':4,'columns':6,'exact_values':24,'score_range':[0,100],'bands':[[0,49],[50,74],[75,100]]}}


def get_slides(lang='en'):
    if lang not in ('en','zh','zh-CN'):
        raise ValueError('lang must be en, zh or zh-CN')
    validate_data()
    return [make(lang) for make in (line_slide,area_slide,radar_slide,sankey_slide,scatter_slide,heatmap_slide)]


if __name__=='__main__':
    print(json.dumps(validate_data(),ensure_ascii=False,indent=2))
