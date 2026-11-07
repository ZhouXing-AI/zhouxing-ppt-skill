"""Six original SHIFT information charts. All numbers are illustrative, not research.

Public API: get_slides('en' | 'zh') -> list[str], validate_data() -> dict.
The SVGs are information content, never decorative artwork slots.
"""
from html import escape
from math import cos, sin, pi

SILVER = '#BCBCBC'
ORANGE = '#FF661A'
INK = '#1A1302'
PAPER = '#E3E3D9'
GOLD = '#FFB948'

LINE = {'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'baseline': [32, 43, 55, 68, 82, 96],
        'new': [30, 39, 58, 77, 101, 124]}
AREA = [80, 104, 96, 138, 166, 154, 204, 230]
RADAR = {'current': [62, 78, 84, 55, 70], 'next': [82, 86, 91, 76, 88]}
SANKEY = {'inputs': [450, 350, 200], 'middle': [650, 350], 'outputs': [600, 400],
          'a': [[350, 100], [200, 150], [100, 100]],
          'b': [[450, 200], [150, 200]]}
SCATTER = [
    ('Docs', '文档', 1.5, 20), ('Intake', '需求收集', 2.5, 48),
    ('Search', '搜索', 3.5, 36), ('Templates', '模板', 4.5, 72),
    ('Review', '评审', 6.0, 58), ('Automation', '自动化', 7.0, 91),
    ('Dashboard', '看板', 8.5, 76), ('Migration', '迁移', 9.2, 42),
]
HEATMAP = [[42, 51, 68, 74, 61, 38], [65, 72, 86, 91, 78, 54],
           [31, 48, 62, 58, 47, 29], [54, 67, 82, 95, 84, 60]]


def tr(lang, en, zh):
    return zh if lang in ('zh', 'zh-CN') else en


def n(value):
    return f'{value:.3f}'.rstrip('0').rstrip('.')


def text(x, y, value, color=INK, size=28, anchor='start', extra='', style=''):
    return (f'<text class="chart-label {style}" x="{n(x)}" y="{n(y)}" '
            f'fill="{color}" font-size="{size}" text-anchor="{anchor}" {extra}>'
            f'{escape(str(value))}</text>')


def line(x1, y1, x2, y2, color, width=1.5, extra=''):
    return (f'<line x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" y2="{n(y2)}" '
            f'stroke="{color}" stroke-width="{width}" {extra}/>')


def rect(x, y, w, h, fill, extra=''):
    return (f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" '
            f'fill="{fill}" {extra}/>')


def circle(x, y, r, fill, extra=''):
    return f'<circle cx="{n(x)}" cy="{n(y)}" r="{r}" fill="{fill}" {extra}/>'


def path(points):
    return 'M' + ' L'.join(f'{n(x)} {n(y)}' for x, y in points)


def motion(markup, kind, step):
    """Annotate a data element without changing its final geometry or styling."""
    return markup.replace(' ', f' data-chart-motion="{kind}" data-chart-step="{step}" ', 1)


def svg(parts, label, cls=''):
    return (f'<svg class="chart-canvas {cls}" data-information-visual="" data-chart-container="" '
            f'viewBox="0 0 1720 620" role="img" aria-label="{escape(label, quote=True)}" '
            f'xmlns="http://www.w3.org/2000/svg"><title>{escape(label)}</title>'
            + ''.join(parts) + '</svg>')


def mini_art(kind,lang):
    choices={'area':('wave','流动曲面','Changing surface'), 'scatter':('prism','转向棱镜','A new perspective')}
    if kind not in choices:return ''
    asset,zh,en=choices[kind];label=tr(lang,en,zh)
    return f'<figure class="sculpture mini-chart-art reveal" data-decoration="true"><div class="artwork-slot" data-artwork-slot="shift-{kind}-accent" data-artwork-id="{asset}" data-artwork-default="{asset}" data-artwork-label="{label}" role="img" aria-label="{label}"></div></figure>'


def section(kind, lang, heading, subtitle, tone, graphic):
    return (f'<section class="slide data-slide chart-slide chart-{kind} {"has-chart-art" if kind in ("area","scatter") else ""}" '
            f'data-tone="{tone}" data-title="{escape(heading, quote=True)}">'
            f'<div class="data-heading"><h2 class="reveal">{heading}</h2></div>'
            f'<p class="data-subtitle reveal">{subtitle}</p>{graphic}{mini_art(kind,lang)}</section>')



def metal(identifier):
    return (f'<linearGradient id="{identifier}" x1="0" y1="0" x2="1" y2="1">'
            f'<stop stop-color="{PAPER}"/><stop offset=".35" stop-color="{SILVER}"/>'
            f'<stop offset=".64" stop-color="{PAPER}"/><stop offset="1" stop-color="{SILVER}"/></linearGradient>')


def dot_row(x1, x2, y, color, count=26, opacity=.2):
    return ''.join(circle(x1+(x2-x1)*i/(count-1),y,1.7,color,f'opacity="{opacity}"') for i in range(count))


def line_slide(lang):
    x=lambda i:620+i*205;y=lambda v:500-v/140*380
    p=[text(0,40,tr(lang,'New journey · June','新流程 · 6月'),PAPER,30),
       motion(text(0,265,LINE['new'][-1],ORANGE,245,style='chart-dot'),'fade',4),
       text(5,326,tr(lang,'thousand active','千个活跃'),PAPER,34),text(5,370,tr(lang,'workspaces','工作空间'),PAPER,34),
       line(0,422,390,422,PAPER,1.2,'opacity=".32"'),text(5,473,tr(lang,'Baseline','原方案'),PAPER,28),
       motion(text(390,477,LINE['baseline'][-1],PAPER,43,'end'),'fade',4),
       text(5,525,tr(lang,'Same month. Same measure.','同一月份，同一统计口径。'),SILVER,26),
       line(620,34,673,34,PAPER,4,'stroke-dasharray="10 8"'),text(692,44,tr(lang,'Baseline','原方案'),PAPER,28),
       line(1047,34,1100,34,ORANGE,5),text(1119,44,tr(lang,'New journey','新流程'),PAPER,28),
       text(1645,90,tr(lang,'Thousands','千个'),SILVER,25,'end')]
    for v in (0,35,70,105,140):
        p.append(line(620,y(v),1645,y(v),PAPER,1.5,'opacity=".5"') if v==0 else dot_row(620,1645,y(v),PAPER,26,.25))
        p.append(text(590,y(v)+9,v,SILVER,27,'end'))
    for i,label in enumerate(LINE['months']):p.append(text(x(i),554,tr(lang,label,f'{i+1}月'),PAPER,28,'middle'))
    for series,(key,color,dash) in enumerate([('baseline',PAPER,'stroke-dasharray="12 9"'),('new',ORANGE,'')]):
        coords=[(x(i),y(v)) for i,v in enumerate(LINE[key])]
        p.append(motion(f'<path d="{path(coords)}" fill="none" stroke="{color}" stroke-width="5" stroke-linejoin="round" {dash}/>','wipe-x' if dash else 'draw',series))
        p.extend(motion(circle(px,py,6.5,INK,f'stroke="{color}" stroke-width="3.5"'),'pop',2) for px,py in coords)
        p.append(motion(text(1664,y(LINE[key][-1])+10,LINE[key][-1],color,28),'fade',3))
    return section('line',lang,tr(lang,'Momentum, measured.','让增长，看得见。'),tr(lang,'Two journeys, six months. Active workspaces use the same definition.','两种流程，六个月。活跃工作空间采用相同统计口径。'),'dark',svg(p,tr(lang,'Monthly active workspaces in thousands. Zero-to-140 scale; baseline32,43,55,68,82,96; new30,39,58,77,101,124. Large values show June, not cumulative totals.','月度活跃工作空间，单位千个。0至140标尺；原方案32、43、55、68、82、96，新流程30、39、58、77、101、124。大数表示6月而非累计。')))

def area_slide(lang):
    x=lambda i:105+i*(1535/7);y=lambda v:530-v/240*380;gid='shift-area-foil-'+lang
    p=[f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop stop-color="{ORANGE}" stop-opacity=".86"/><stop offset="1" stop-color="{ORANGE}" stop-opacity=".26"/></linearGradient><pattern id="{gid}-dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="1.7" fill="{INK}" opacity=".2"/></pattern></defs>',
       text(105,36,tr(lang,'Orders · thousands per week','订单量 · 每周千单'),INK,30),text(1282,61,tr(lang,'WEEK 08','第8周'),INK,27),
       motion(text(1640,83,AREA[-1],INK,108,'end',style='chart-dot'),'fade',3),line(1640,107,1640,y(AREA[-1])-15,INK,1.3,'opacity=".55"')]
    for v in (0,60,120,180,240):
        p.append(line(105,y(v),1640,y(v),INK,1.3,f'opacity="{.5 if v==0 else .2}"') if v in (0,120,240) else dot_row(105,1640,y(v),INK,36,.22))
        p.append(text(77,y(v)+9,v,INK,27,'end'))
    coords=[(x(i),y(v)) for i,v in enumerate(AREA)];d=path([(105,530)]+coords+[(1640,530)])+' Z'
    p.append(motion(f'<g><path d="{d}" fill="url(#{gid})"/><path d="{d}" fill="url(#{gid}-dots)"/></g>','wipe-x',0))
    p.append(motion(f'<path d="{path(coords)}" fill="none" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>','draw',1))
    for i in (0,4,7):
        p.append(motion(circle(x(i),y(AREA[i]),7,INK,f'stroke="{PAPER}" stroke-width="2"'),'pop',2))
        if i!=7:p.append(motion(text(x(i),y(AREA[i])-23,AREA[i],INK,34,'middle'),'fade',2))
    for i in range(8):p.append(text(x(i),582,tr(lang,f'W{i+1}',f'第{i+1}周'),INK,28,'middle'))
    return section('area',lang,tr(lang,'Demand, week by week.','需求，一周一周展开。'),tr(lang,'Eight weeks of orders, showing how demand rises and falls.','八周订单，逐周观察需求的起伏。'),'silver',svg(p,tr(lang,'Weekly orders in thousands:80,104,96,138,166,154,204,230. Zero-to-240 axis. No smoothing or cumulative values; texture encodes no additional metric.','每周订单量，单位千单：80、104、96、138、166、154、204、230。零至240标尺，不是累计值，不平滑制造峰谷；材质不编码额外变量。')))

def radar_slide(lang):
    names=[tr(lang,en,zh) for en,zh in [('Speed','速度'),('Clarity','清晰度'),('Reliability','可靠性'),('Reuse','复用性'),('Access','可达性')]]
    cx,cy,radius=430,310,195
    def point(i,v):
        a=-pi/2+i*2*pi/5;return cx+radius*v/100*cos(a),cy+radius*v/100*sin(a)
    gid='shift-radar-silver-'+lang
    p=[f'<defs>{metal(gid)}</defs>',circle(cx,cy,259,f'url(#{gid})',f'stroke="{PAPER}" stroke-width="1.8"'),circle(cx,cy,241,PAPER,f'stroke="{INK}" stroke-width="1.3"'),
       text(1010,66,'0–100',INK,83,style='chart-dot'),text(1014,113,tr(lang,'Same scale. Every axis.','每一轴，同一把标尺。'),INK,29),
       line(1252,163,1300,163,INK,4,'stroke-dasharray="10 7"'),text(1317,173,tr(lang,'Now','当前'),INK,28),
       line(1488,163,1536,163,ORANGE,5),text(1553,173,tr(lang,'Next','改进后'),INK,28)]
    for v in (20,40,60,80,100):
        p.append(f'<path d="{path([point(i,v) for i in range(5)])} Z" fill="none" stroke="{INK}" stroke-width="1.1" opacity=".25"/>')
        p.append(text(cx+10,cy-radius*v/100+8,v,INK,25))
    for i,name in enumerate(names):
        px,py=point(i,100);p.append(line(cx,cy,px,py,INK,1,'opacity=".25"'))
        lx,ly=point(i,147);p.append(text(lx,ly+9,name,INK,29,'middle'))
    for series,(key,color,dash) in enumerate([('current',INK,'stroke-dasharray="11 8"'),('next',ORANGE,'')]):
        coords=[point(i,v) for i,v in enumerate(RADAR[key])]
        p.append(motion(f'<path d="{path(coords)} Z" fill="none" stroke="{color}" stroke-width="4.5" stroke-linejoin="round" {dash}/>','wipe-x' if dash else 'draw',series))
        for px,py in coords:
            marker=rect(px-5.5,py-5.5,11,11,PAPER,f'stroke="{color}" stroke-width="2.8"') if key=='current' else circle(px,py,6,PAPER,f'stroke="{color}" stroke-width="3"')
            p.append(motion(marker,'pop',2))
    for i,name in enumerate(names):
        yy=237+i*75
        p += [line(1010,yy+27,1670,yy+27,INK,1,'opacity=".28"'),motion(text(1010,yy,name,INK,29),'fade',2+i),motion(text(1354,yy,RADAR['current'][i],INK,42,'middle',style='chart-dot'),'fade',2+i),motion(text(1600,yy,RADAR['next'][i],INK,42,'middle',style='chart-dot'),'fade',2+i)]
    return section('radar',lang,tr(lang,'Strength in every direction.','每个方向，都更有力。'),tr(lang,'Five capabilities, compared before and after the improvements.','从当前到改进后，观察五项能力的变化。'),'orange',svg(p,tr(lang,'Current62,78,84,55,70; next82,86,91,76,88. All five axes use0–100, unfilled outlines. The silver disc is a flat backing outside the quantitative scale.','当前62、78、84、55、70；改进后82、86、91、76、88。五轴均为0至100，无填色轮廓；银色盘面是量尺外的平面底座。')))

def sankey_slide(lang):
    p = []
    gid="shift-flow-silver-"+lang
    p.append(f"<defs>{metal(gid)}</defs>")
    scale = .45
    groups = [SANKEY['inputs'], SANKEY['middle'], SANKEY['outputs']]
    xs = [95, 785, 1435]
    widths = [180, 190, 180]
    positions = []
    for totals in groups:
        gap = (510-sum(totals)*scale)/(len(totals)-1)
        yy = 60
        current = []
        for v in totals:
            current.append((yy, v*scale)); yy += v*scale+gap
        positions.append(current)
    colors = [ORANGE, PAPER, GOLD]
    def ribbon(x1, x2, y1, y2, h, color):
        dx=(x2-x1)*.45
        d=(f'M{n(x1)} {n(y1)} C{n(x1+dx)} {n(y1)} {n(x2-dx)} {n(y2)} {n(x2)} {n(y2)} '
           f'L{n(x2)} {n(y2+h)} C{n(x2-dx)} {n(y2+h)} {n(x1+dx)} {n(y1+h)} {n(x1)} {n(y1+h)} Z')
        return f'<path d="{d}" fill="{color}" opacity=".64"/>'
    flow_labels=[]
    for stage, matrix in enumerate([SANKEY['a'], SANKEY['b']]):
        src_offset=[0]*len(matrix); dst_offset=[0]*len(matrix[0])
        for i,row in enumerate(matrix):
            for j,value in enumerate(row):
                sy=positions[stage][i][0]+src_offset[i]
                ty=positions[stage+1][j][0]+dst_offset[j]
                h=value*scale
                color=colors[i] if stage==0 else [ORANGE,GOLD][j]
                x1,x2=xs[stage]+widths[stage],xs[stage+1]
                flow=ribbon(x1,x2,sy,ty,h,color).replace('<path ',f'<path data-flow-stage="{stage+1}" data-flow-source="{i}" data-flow-target="{j}" data-flow-value="{value}" ',1)
                p.append(motion(flow, 'wipe-x', 1+stage*2))
                # Label within the nearly-horizontal source end of each ribbon.
                # t=.12 cubic Bézier position; width scaling is identical at both ends.
                t=.12; u=1-t; dx=(x2-x1)*.45
                lx=u**3*x1+3*u*u*t*(x1+dx)+3*u*t*t*(x2-dx)+t**3*x2
                ly=(1-(3*t*t-2*t*t*t))*(sy+h/2)+(3*t*t-2*t*t*t)*(ty+h/2)
                flow_labels.append(motion(text(lx,ly+10,value,PAPER if color==ORANGE else INK,31,'middle',
                                        'style="font-weight:600"'), 'fade', 2+stage*2))
                src_offset[i]+=h;dst_offset[j]+=h
    labels = [[tr(lang,'Organic','自然流量'),tr(lang,'Paid','广告流量'),tr(lang,'Partners','合作来源')],
              [tr(lang,'Product','产品路径'),tr(lang,'Service','服务路径')],
              [tr(lang,'Activated','已激活'),tr(lang,'Pending','待激活')]]
    for g,totals in enumerate(groups):
        p.append(text(xs[g]+widths[g]/2,27,tr(lang,['Source','Journey','Outcome'][g],['来源','路径','结果'][g]),PAPER,28,'middle'))
        for i,v in enumerate(totals):
            yy,h=positions[g][i];fill=colors[i] if g==0 else f'url(#{gid})' if g==1 else [ORANGE,GOLD][i]
            p += [motion(rect(xs[g],yy,widths[g],h,fill), 'fade', g*2),
                  motion(text(xs[g]+widths[g]/2,yy+h/2-19,labels[g][i],INK,27,'middle'), 'fade', g*2),
                  motion(text(xs[g]+widths[g]/2,yy+h/2+34,v,INK,49,'middle',style='chart-dot'), 'fade', g*2)]
    p += flow_labels
    p.append(text(95,614,tr(lang,"1,000 people at every stage","每一层均为1,000人"),SILVER,27))
    return section('sankey', lang, tr(lang, 'From reach to activation.', '从触达，到真正激活。'),
                   tr(lang, 'One cohort, taking different routes toward activation.',
                      '同一批访客，沿不同路径走向激活。'), 'dark',
                   svg(p, tr(lang,'Sankey flow: 450 organic, 350 paid, 200 partners; 650 product and 350 service; 600 activated and 400 pending. Each ribbon is labelled with its count.',
                             '桑基图：自然450、广告350、合作200；产品650、服务350；已激活600、待激活400。每条流带标注人数。')))


def scatter_slide(lang):
    x=lambda v:105+v/10*1490;y=lambda v:500-v/100*385
    peak=max(SCATTER,key=lambda item:item[3]);px,py=x(peak[2]),y(peak[3])
    p=[text(105,34,tr(lang,'Hours saved / week','每周节省小时'),INK,30),circle(1050,24,8,ORANGE),text(1070,34,tr(lang,'≤ 4.5 person-days','≤ 4.5人日'),INK,27),circle(1415,24,8,INK),text(1435,34,'> 4.5',INK,27)]
    for v in (0,25,50,75,100):
        p.append(line(105,y(v),1595,y(v),INK,1.5,'opacity=".5"') if v==0 else dot_row(105,1595,y(v),INK,36,.28))
        p.append(text(78,y(v)+9,v,INK,27,'end'))
    for v in (0,2,4,6,8,10):p += [line(x(v),500,x(v),510,INK,1.3),text(x(v),553,v,INK,28,'middle')]
    p += [line(px,py,px,500,INK,1.3,'stroke-dasharray="4 7" opacity=".35"'),line(105,py,px,py,INK,1.3,'stroke-dasharray="4 7" opacity=".35"'),text(1595,612,tr(lang,'Effort · person-days','投入 · 人日'),INK,28,'end')]
    for i,(en,zh,effort,impact) in enumerate(SCATTER):
        color=ORANGE if effort<=4.5 else INK;cx,cy=x(effort),y(impact)
        p.append(motion(circle(cx,cy,18,color,f'data-point-id="{i}" stroke="{PAPER}" stroke-width="3"'),'pop',i))
        tx,anchor=(cx-22,'end') if effort>8 else (cx+22,'start')
        p.append(motion(text(tx,cy-26,tr(lang,en,zh),color if en=='Templates' else INK,35 if en in ('Templates','Automation') else 29,anchor,extra='font-weight="600"' if en in ('Templates','Automation') else ''),'fade',i+1))
        if impact==peak[3]:p.append(motion(text(cx-24,cy+45,f'{impact} h',INK,32,'end'),'fade',i+1))
    return section('scatter',lang,tr(lang,'Choose the useful next move.','选出，值得做的下一步。'),tr(lang,'Eight proposals, compared by estimated effort and weekly time saved.','八个提案，比较预计投入与每周节省时间。'),'silver',svg(p,tr(lang,'Eight equal-radius points; x0–10 person-days, y0–100 hours saved per week. Orange points take at most4.5 person-days. Guides mark Automation:7 person-days,91 hours. Estimates are not causal proof.','八点半径一致，横轴0至10人日，纵轴每周节省0至100小时。铜橙点投入不超过4.5人日。辅助线标记自动化7人日、91小时；不作因果推断。')))

def heatmap_slide(lang):
    columns=[tr(lang,en,zh) for en,zh in zip(['Mon','Tue','Wed','Thu','Fri','Sat'],['周一','周二','周三','周四','周五','周六'])]
    rows=[tr(lang,en,zh) for en,zh in zip(['Web','Mobile','Email','Support'],['网页','移动端','邮件','客服'])]
    peak=max((v,r,c) for r,row in enumerate(HEATMAP) for c,v in enumerate(row));gid='shift-heat-silver-'+lang
    p=[f'<defs>{metal(gid)}</defs>',line(1320,46,1320,554,INK,1.4,'opacity=".35"'),text(1380,112,tr(lang,'PEAK CAPACITY USED','最高使用率'),INK,25),motion(text(1380,283,f'{peak[0]}%',INK,132,style='chart-dot'),'fade',4),text(1382,349,rows[peak[1]],INK,34),text(1382,395,columns[peak[2]],INK,29),line(1380,443,1690,443,INK,1.2,'opacity=".3"'),text(1382,492,tr(lang,'Used ÷ planned','已用 ÷ 计划'),INK,27)]
    for i,label in enumerate(columns):p.append(text(301.5+i*175,38,label,INK,28,'middle'))
    for row,values in enumerate(HEATMAP):
        yy=82+row*112;p.append(text(185,yy+60,rows[row],INK,30,'end'))
        for col,v in enumerate(values):
            fill=PAPER if v<50 else f'url(#{gid})' if v<75 else INK;color=PAPER if v>=75 else INK
            p += [motion(rect(220+col*175,yy,163,96,fill,f'rx="3" data-heat-row="{row}" data-heat-column="{col}" data-heat-value="{v}"'),'fade',row),motion(text(301.5+col*175,yy+62,f'{v}%',color,39,'middle',style='chart-dot'),'fade',row)]
    for i,(label,fill) in enumerate([('0–49%',PAPER),('50–74%',f'url(#{gid})'),('75–100%',INK)]):
        xx=220+i*350;p += [rect(xx,559,31,31,fill,'rx="2"'),text(xx+47,586,label,INK,27)]
    return section('heatmap',lang,tr(lang,'Find the pressure points.','找到，最忙的时刻。'),tr(lang,'Capacity used as a share of planned capacity, across four channels and six days.','四个渠道、六天安排，对比已使用产能占计划产能的比例。'),'orange',svg(p,tr(lang,'Four by six exact percentages. Equal-size cells; bands0–49,50–74,75–100 percent. Peak95 percent is Support/Thursday. Middle-band metallic tint is fixed and encodes no second variable.','四行六列准确百分比；格子同大小，色阶0至49、50至74、75至100%。最高值客服周四95%；中段银色材质固定，不编码其他变量。')))

def validate_data():
    assert len(LINE['months'])==len(LINE['baseline'])==len(LINE['new'])==6
    assert all(0<=v<=140 for key in ('baseline','new') for v in LINE[key])
    assert len(AREA)==8 and all(0<=v<=240 for v in AREA)
    assert all(len(s)==5 and all(0<=v<=100 for v in s) for s in RADAR.values())
    a,b=SANKEY['a'],SANKEY['b']
    assert [sum(r) for r in a]==SANKEY['inputs']
    assert [sum(r[j] for r in a) for j in range(2)]==SANKEY['middle']
    assert [sum(r) for r in b]==SANKEY['middle']
    assert [sum(r[j] for r in b) for j in range(2)]==SANKEY['outputs']
    assert sum(SANKEY['inputs'])==sum(SANKEY['middle'])==sum(SANKEY['outputs'])==1000
    assert all(v>0 for matrix in (a,b) for row in matrix for v in row)
    assert len(SCATTER)==8 and all(0<=x<=10 and 0<=y<=100 for _,_,x,y in SCATTER)
    assert len(HEATMAP)==4 and all(len(r)==6 and all(0<=v<=100 for v in r) for r in HEATMAP)
    return {'line': '2 × 6 points; zero to 140', 'area': '8 points; zero to 240',
            'radar': '2 × 5; shared 0–100 scale', 'sankey': '3 → 2 → 2; 1,000 conserved; scale .45 px/person',
            'scatter': '8 labelled proposals', 'heatmap': '4 × 6; exact percentages', 'status': 'PASS'}


def get_slides(lang='en'):
    if lang not in ('en','zh','zh-CN'):
        raise ValueError("lang must be en, zh or zh-CN")
    validate_data()
    return [fn(lang) for fn in (line_slide,area_slide,radar_slide,sankey_slide,scatter_slide,heatmap_slide)]


if __name__=='__main__':
    import json
    print(json.dumps(validate_data(),ensure_ascii=False,indent=2))
