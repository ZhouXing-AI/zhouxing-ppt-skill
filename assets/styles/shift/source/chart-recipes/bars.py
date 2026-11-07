"""Six redesigned SHIFT information charts. Values are illustrative source material.

The finished canvas has no production labels. Native SVG data geometry is the
final state; semantic hooks reveal it without changing any quantitative scale.
"""
from html import escape
import json

INK='#1A1302'; ORANGE='#FF661A'; SILVER='#BCBCBC'; PAPER='#E3E3D9'; GOLD='#FFB948'


def _tr(lang,en,zh): return zh if lang=='zh' else en


def _text(x,y,value,size=30,kind='label',fill=INK,anchor='start',weight=None):
    attrs=f'x="{x:g}" y="{y:g}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" class="bar-{kind}"'
    if weight: attrs+=f' font-weight="{weight}"'
    if isinstance(value,(tuple,list)):
        value=''.join(f'<tspan x="{x:g}" dy="{0 if i==0 else size*1.35:g}">{escape(str(v))}</tspan>' for i,v in enumerate(value))
    else:value=escape(str(value))
    return f'<text {attrs}>{value}</text>'


def _line(x1,y1,x2,y2,stroke=INK,opacity=.2,dash=None,width=1.5):
    extra=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{stroke}" stroke-opacity="{opacity}" stroke-width="{width}"{extra}/>'


def _rect(x,y,w,h,fill,extra=''):
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}" {extra}/>'


def _motion(content,mode,step):
    return f'<g data-chart-motion="{mode}" data-chart-step="{step}">{content}</g>'


def _legend(x,y,color,label,fg=INK,stroke=None):
    return _rect(x,y-18,22,22,color,f'stroke="{stroke}"' if stroke else '')+_text(x+36,y,label,27,fill=fg)


def _materials(key):
    return f'<defs><linearGradient id="{key}-silver" x1="0" y1="0" x2="1" y2=".25"><stop stop-color="#969892"/><stop offset=".18" stop-color="#bcbcb6"/><stop offset=".44" stop-color="#e6e7dd"/><stop offset=".61" stop-color="#b8b9b2"/><stop offset=".82" stop-color="#d8d9d0"/><stop offset="1" stop-color="#a0a29b"/></linearGradient><linearGradient id="{key}-copper" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#a94820"/><stop offset=".17" stop-color="#ff661a"/><stop offset=".43" stop-color="#ff9b58"/><stop offset=".61" stop-color="#ff772b"/><stop offset=".82" stop-color="#d44d16"/><stop offset="1" stop-color="#a43d12"/></linearGradient></defs>'


def _svg(key,lang,title,description,content):
    return f'<svg viewBox="0 0 1720 620" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bar-{key}-{lang}-title bar-{key}-{lang}-desc" data-information-visual="true"><title id="bar-{key}-{lang}-title">{escape(title)}</title><desc id="bar-{key}-{lang}-desc">{escape(description)}</desc>{content}</svg>'


def _mini_art(key,lang):
    choices={'columns':('link','联结双环','Linked loops'), 'ranking':('lens','另一视角','A different lens')}
    if key not in choices:return ''
    asset,zh,en=choices[key];label=zh if lang=='zh' else en
    return f'<figure class="sculpture mini-chart-art reveal" data-decoration="true"><div class="artwork-slot" data-artwork-slot="shift-{key}-accent" data-artwork-id="{asset}" data-artwork-default="{asset}" data-artwork-label="{label}" role="img" aria-label="{label}"></div></figure>'


def _section(key,lang,tone,title,subtitle,chart,data):
    # A short English final word carries the established dot typography; chart
    # labels and values always remain in the highly readable sans family.
    heading=escape(title)
    if lang=='en':
        leading,word=title.rsplit(' ',1)
        heading=escape(leading)+' <span class="bar-title-dot">'+escape(word)+'</span>'
    return f'<section class="slide data-slide bar-slide bar-{key} bar-{lang} {tone} {"has-chart-art" if key in ("columns","ranking") else ""}" data-title="{escape(title,quote=True)}" data-tone="{tone}" data-nav-tone="{("dark" if tone=="dark" else "warm" if tone=="orange" else "silver")}" data-chart-kind="{key}" data-chart-values=\'{json.dumps(data,ensure_ascii=False,separators=(",",":"))}\'><header class="data-heading"><h2 class="reveal">{heading}</h2><p class="data-subtitle bar-subtitle reveal">{escape(subtitle)}</p></header><div class="bar-chart" data-chart-container="true">{chart}</div>{_mini_art(key,lang)}</section>'


def _columns(lang):
    values=[18,26,35,48];quarters=['Q1','Q2','Q3','Q4']
    title=_tr(lang,'Release, then repeat.','小步发布，持续累积。')
    subtitle=_tr(lang,'A product team ships more small releases each quarter.','一支产品团队，每个季度都发布更多小版本。')
    base,scale=490,6.5
    p=[_materials('bar-columns'),_text(0,22,_tr(lang,'Releases','发布次数'),27),
       _text(1695,22,_tr(lang,'18 → 48 across four quarters','四个季度，18 → 48'),29,anchor='end')]
    for tick in [0,15,30,45,60]:
        y=base-tick*scale
        p+=[_line(105,y,1700,y,opacity=.5 if tick==0 else .22,dash=None if tick==0 else '2 14',width=2 if tick==0 else 1.2),_text(76,y+10,tick,28,'number',anchor='end')]
    for i,(x,quarter,value) in enumerate(zip([325,745,1165,1585],quarters,values)):
        top=base-value*scale;hot=i==3;material='copper' if hot else 'silver'
        cap='#ffb06a' if hot else '#d9dcd3';edge='#a33b12' if hot else '#777b74'
        faces=''.join([f'<ellipse cx="{x}" cy="{base}" rx="85" ry="9" fill="{edge}"/>',
          _rect(x-85,top,170,base-top,f'url(#bar-columns-{material})'),
          f'<ellipse cx="{x}" cy="{top:g}" rx="85" ry="9" fill="{cap}" stroke="{edge}" stroke-width="1.4"/>',
          _line(x-74,top+4,x-74,base-4,PAPER,.45,width=2),
          _line(x+72,top+4,x+72,base-4,INK,.14,width=1)])
        p+=[f'<g data-series="releases" data-value="{value}" data-zero="{base}" data-top="{top}" data-scale="{scale}">',
            _motion(faces,'grow-y',i),_motion(_text(x,top-29,value,48,'number',ORANGE if hot else INK,'middle',600),'fade',i+1),
            _text(x,548,quarter,32,'number',anchor='middle'),'</g>']
    p += [_text(105,615,'+30',60,'dot',ORANGE),_text(285,605,_tr(lang,'more releases from Q1 to Q4','从第一季到第四季，新增 30 次发布'),29),
          _text(1700,605,_tr(lang,'A steadier rhythm. A smaller batch.','频率更稳定，每次更轻量。'),27,anchor='end')]
    desc=_tr(lang,'Quarterly releases Q1 18, Q2 26, Q3 35, Q4 48; Q4 minus Q1 is 30. Axis zero to 60. The centerlines of all short top and bottom ellipses use the same quantitative scale. Silver marks the first three quarters, copper highlights Q4.','季度发布次数18、26、35、48；第四季较第一季增加30次。纵轴0至60，所有柱体短椭圆的顶底中心使用相同数值标尺。前三季为银色，第四季以铜橙突出。')
    return _section('columns',lang,'silver',title,subtitle,_svg('columns',lang,title,desc,''.join(p)),{'unit':'releases','quarters':quarters,'values':values,'axis_max':60})


def _ranking(lang):
    labels=_tr(lang,['Access','Setup','Billing','Import','Other'],['账户权限','初始配置','账单问题','数据导入','其他']);values=[42,34,27,19,13]
    title=_tr(lang,'Remove friction first.','先解决最大的阻力。')
    subtitle=_tr(lang,'One month, 135 support requests. Access accounts for 42 — about 31%.','一个月，135 件新用户工单；权限问题有 42 件，约占 31%。')
    start,scale=410,24.0
    p=[_text(start,20,_tr(lang,'Support requests','工单数量'),27,fill=PAPER),
       _text(1710,20,_tr(lang,'Start with access','先从权限问题下手'),27,fill=ORANGE,anchor='end')]
    for tick in [0,10,20,30,40,50]:
        x=start+tick*scale
        p += [_line(x,47,x,525,PAPER,.12,dash='2 13',width=1.2),_text(x,585,tick,28,'number',PAPER,'middle')]
    for i,(label,value) in enumerate(zip(labels,values)):
        y=57+i*96
        color=ORANGE if i==0 else SILVER
        p += [_text(0,y+43,f'{i+1:02}',42,'dot',ORANGE if i==0 else PAPER),
              _text(110,y+39,label,36,fill=PAPER),
              _motion(_rect(start,y,value*scale,54,color),'grow-x',i),
              _motion(_text(start+value*scale+23,y+42,value,44,'number',color,weight=600),'fade',i+1),
              _line(0,y+81,1715,y+81,PAPER,.2,width=1)]
    desc=_tr(lang,'Onboarding tickets: access42, setup34, billing27, import19, other13; total135. Access is31.1 percent, rounded to31. The common horizontal axis runs from zero to50 requests.','新用户工单：权限42、配置34、账单27、导入19、其他13，总计135。权限占31.1%，约为31%。各条共用0至50件的水平标尺。')
    return _section('ranking',lang,'dark',title,subtitle,_svg('ranking',lang,title,desc,''.join(p)),{'unit':'tickets','labels':labels,'values':values,'total':135,'axis_max':50})


def _pictorial(lang):
    values=[60,45,30,25];labels=_tr(lang,['Team A','Team B','Team C','Team D'],['团队 A','团队 B','团队 C','团队 D'])
    title=_tr(lang,'Give every idea a place.','让每一个提案，都被看见。')
    subtitle=_tr(lang,'Monthly proposals from four teams. Each metal disc represents five proposals.','四支团队的月度提案。每枚金属圆片代表 5 个提案。')
    p=[_materials('bar-pictorial'),_line(860,0,860,550,INK,.3,width=1.5)]
    for i,(label,value) in enumerate(zip(labels,values)):
        ox=0 if i%2==0 else 920;oy=0 if i<2 else 292
        p += [_text(ox+8,oy+36,label,36),_text(ox+794,oy+42,value,51,'number',anchor='end',weight=600),_line(ox,oy+60,ox+800,oy+60,INK,.4)]
        for j in range(value//5):
            x=ox+48+(j%6)*133;y=oy+123+(j//6)*87
            disc=f'<circle cx="{x}" cy="{y}" r="31" fill="url(#bar-pictorial-silver)" stroke="#676b64" stroke-width="1.8"/><circle cx="{x}" cy="{y}" r="26" fill="none" stroke="#f3f3e8" stroke-opacity=".55" stroke-width="1.1"/>'
            p.append(f'<g data-unit="5" data-chart-motion="pop" data-chart-step="{i+j}">{disc}</g>')
    p += [_line(0,563,1720,563,INK,.4),f'<circle cx="18" cy="602" r="12" fill="url(#bar-pictorial-silver)" stroke="#676b64"/>',
          _text(45,613,_tr(lang,'= 5 proposals','= 5 个提案'),27),
          _text(1720,613,_tr(lang,'32 discs · 160 proposals','32 枚圆片 · 160 个提案'),32,'number',anchor='end')]
    desc=_tr(lang,'Teams A/B/C/D submitted60/45/30/25 proposals. Each equal-sized filled disc equals five proposals. Twelve, nine, six, five data discs give32 total, representing160 proposals. The separate small legend disc is excluded.','团队A/B/C/D提案分别为60/45/30/25。每枚等大圆片代表5个提案，四组分别12、9、6、5枚，合计32枚与160个提案。底部小图例圆片不计入数据。')
    return _section('pictorial',lang,'orange',title,subtitle,_svg('pictorial',lang,title,desc,''.join(p)),{'unit':'proposals','labels':labels,'values':values,'per_dot':5,'total':160})


def _grouped(lang):
    labels=_tr(lang,['Campaign','Website','Product'],['营销活动','网站项目','产品设计']);before=[50,60,70];after=[70,80,90]
    title=_tr(lang,'A clearer brief. A better start.','清晰任务，让交付更稳。')
    subtitle=_tr(lang,'First-pass approval rises by 20 percentage points across all three project types.','三个项目类型的一次通过率，在明确任务后均提升 20 个百分点。')
    p=[_legend(0,17,PAPER,_tr(lang,'Before','调整前'),stroke=INK),_legend(265,17,ORANGE,_tr(lang,'After','调整后')),
       _text(1715,17,_tr(lang,'First-pass approval · %','一次通过率 · %'),27,anchor='end')]
    base,scale=500,3.6
    for group,(origin,label,a,b) in enumerate(zip([0,590,1180],labels,before,after)):
        p.append(_text(origin+290,91,label,37,anchor='middle'))
        for tick in [0,50,100]:
            y=base-tick*scale
            p += [_line(origin+85,y,origin+535,y,opacity=.38 if tick==0 else .2,dash=None if tick==0 else '2 11'),_text(origin+66,y+10,f'{tick}%',26,'number',anchor='end')]
        for series,(x,value,color) in enumerate([(origin+145,a,PAPER),(origin+345,b,ORANGE)]):
            top=base-value*scale
            bar=_rect(x,top,125,base-top,color,f'stroke="{INK}" stroke-width="1.4"' if series==0 else '')
            p += [_motion(bar,'grow-y',group*2+series),_motion(_text(x+62.5,top-20,value,43,'number',anchor='middle',weight=600),'fade',group*2+series+1),
                  _text(x+62.5,550,_tr(lang,'Before' if series==0 else 'After','调整前' if series==0 else '调整后'),27,anchor='middle')]
        if group<2:p.append(_line(origin+565,64,origin+565,574,INK,.23))
    p += [_line(0,590,1720,590,INK,.35),_text(0,618,'+20',64,'dot',ORANGE),_text(240,613,_tr(lang,'percentage points, in every project type.','个百分点，每一种项目都同样提升。'),28),_text(1720,613,_tr(lang,'A shared 0–100% scale.','统一使用 0–100% 量尺。'),25,anchor='end')]
    desc=_tr(lang,'First-pass approval before and after: Campaign50/70%, Website60/80%, Product70/90%. Each pair uses the same0–100% scale and zero baseline. All three increase by20 percentage points.','一次通过率：营销50%至70%，网站60%至80%，产品70%至90%。三个小图均用同一0至100%标尺与零基线，均提升20个百分点。')
    return _section('grouped',lang,'silver',title,subtitle,_svg('grouped',lang,title,desc,''.join(p)),{'unit':'percent','labels':labels,'before':before,'after':after,'axis_max':100})


def _stacked(lang):
    labels=_tr(lang,['Sprint 1','Sprint 2','Sprint 3'],['迭代 1','迭代 2','迭代 3'])
    series=_tr(lang,['Build','Research','Operations'],['核心开发','用户研究','日常运营']);rows=[[40,35,25],[50,30,20],[60,25,15]]
    title=_tr(lang,'More time reaches the core.','让更多时间回到核心。')
    subtitle=_tr(lang,'Build time rises from 40% to 60%; each sprint accounts for 100% of team capacity.','核心开发工时占比从 40% 升至 60%；每次迭代均完整呈现团队工时。')
    start,width=255,1450
    p=[]
    p += [_materials('bar-stacked'),_legend(start,19,ORANGE,series[0],PAPER),_legend(750,19,GOLD,series[1],PAPER),_legend(1240,19,SILVER,series[2],PAPER)]
    for tick in [0,25,50,75,100]:
        x=start+width*tick/100
        p += [_line(x,66,x,526,PAPER,.15,dash='2 13',width=1),_text(x,578,f'{tick}%',28,'number',PAPER,'middle')]
    for row,(label,values) in enumerate(zip(labels,rows)):
        y=85+row*165
        p += [_text(0,y+43,f'0{row+1}',38,'dot',ORANGE),_text(0,y+86,label,30,fill=PAPER),f'<g data-chart-motion="wipe-x" data-chart-step="{row}">']
        x=start
        for k,(value,color) in enumerate(zip(values,[ORANGE,GOLD,'url(#bar-stacked-silver)'])):
            w=width*value/100
            p += [_rect(x,y,w,105,color),_text(x+w/2,y+69,f'{value}%',46,'number',INK,'middle',600)]
            x+=w
        p.append('</g>')
        if row<2:
            end1=start+width*values[0]/100;end2=start+width*rows[row+1][0]/100
            p.append(_motion(_line(end1,y+105,end2,y+165,ORANGE,.8,width=2),'draw',row+1))
    p.append(_text(255,620,_tr(lang,'Three priorities. One fixed pool of time.','三类工作，分配同一份有限时间。'),26,fill=SILVER))
    desc=_tr(lang,'Build/research/operations shares are40/35/25%,50/30/20%,60/25/15% across three sprints. Each row totals100%. Connector lines follow only the build-share boundary, from40 to50 to60%. All segment widths use the same scale.','三次迭代的核心开发/用户研究/运营占比为40/35/25%、50/30/20%、60/25/15%，每行100%。细连接线仅跟随开发占比边界40→50→60，全部条段采用相同长度标尺。')
    return _section('stacked',lang,'dark',title,subtitle,_svg('stacked',lang,title,desc,''.join(p)),{'unit':'percent','labels':labels,'series':series,'values':rows,'axis_max':100})


def _waterfall(lang):
    labels=_tr(lang,['Opening','Collections','Payroll','Operations','Closing'],['期初现金','客户回款','人员支出','运营支出','期末现金']);values=[120,90,-55,-25,130]
    title=_tr(lang,'What stays after the work?','经营收支，最终留下多少？')
    subtitle=_tr(lang,'Quarterly cash bridge · USD thousands · 120 + 90 − 55 − 25 = 130','季度现金收支桥 · 单位：千美元 · 120 + 90 − 55 − 25 = 130')
    p=[_legend(105,18,INK,_tr(lang,'Cash balance','现金余额')),_legend(465,18,ORANGE,_tr(lang,'Cash in','现金流入')),
       _legend(775,18,PAPER,_tr(lang,'Cash out','现金流出'),stroke=INK),_text(1700,18,_tr(lang,'Net change +10','净增加 +10'),30,'number',ORANGE,'end',600)]
    base,scale,w=500,1.7,205;centers=[245,565,885,1205,1525]
    for tick in [0,60,120,180,240]:
        y=base-tick*scale
        p += [_line(105,y,1700,y,opacity=.5 if tick==0 else .18,dash=None if tick==0 else '2 14',width=2 if tick==0 else 1.2),_text(80,y+10,tick,28,'number',anchor='end')]
    spans=[(0,120),(120,210),(210,155),(155,130),(0,130)]
    for i,(x,label,value,(start,end)) in enumerate(zip(centers,labels,values,spans)):
        top,height=base-max(start,end)*scale,abs(end-start)*scale
        color=INK if i in (0,4) else ORANGE if value>0 else PAPER
        bar=_rect(x-w/2,top,w,height,color,f'stroke="{INK}" stroke-width="1.6"' if color==PAPER else '')
        p += [_motion(bar,'grow-y',i),_motion(_text(x,top-24,f'+{value}' if i==1 else value,47,'number',ORANGE if i==1 else INK,'middle',600),'fade',i+1),_text(x,556,label,30,anchor='middle')]
        if i<4:p.append(_motion(_line(x+w/2,base-end*scale,centers[i+1]-w/2,base-end*scale,opacity=.7,dash='7 7',width=2),'wipe-x',i+1))
    p += [_line(105,590,1700,590,INK,.3),_text(105,620,_tr(lang,'A bridge from opening cash to closing cash.','从期初出发，一笔一笔走到期末。'),27),_text(1700,620,'120 → 130',35,'number',anchor='end')]
    desc=_tr(lang,'Cash in USD thousands: opening120, collections+90, payroll−55, operations−25, closing130. Cumulative balances120,210,155,130. Peak210, net increase10. All bars use the same zero-based0–240 scale; floating bars start and end at exact balances.','现金单位千美元：期初120、回款+90、人员−55、运营−25、期末130。累计余额120、210、155、130，峰值210，净增10。所有柱形使用同一0至240标尺，浮动条两端对应准确的累计余额。')
    return _section('waterfall',lang,'silver',title,subtitle,_svg('waterfall',lang,title,desc,''.join(p)),{'unit':'USD thousands','labels':labels,'values':values,'cumulative':[120,210,155,130,130],'axis_max':240})


def get_slides(lang):
    """Return the six data pages; en, zh, and zh-CN are supported."""
    lang='zh' if lang in ('zh','zh-CN') else 'en'
    return [fn(lang) for fn in (_columns,_ranking,_pictorial,_grouped,_stacked,_waterfall)]


def validate_data():
    """Validate current bilingual recipe output; raise ValueError on a broken claim.

    Checks the metadata generated by the same builders, along with dot counts,
    axis ranges, chart structure, and the numerical claims in these examples.
    This function is intentionally separate from rendering and changes no HTML.
    """
    import math
    import re
    import xml.etree.ElementTree as ET

    def require(condition, message):
        if not condition:
            raise ValueError('SHIFT bar recipes: ' + message)

    def close(a, b):
        return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)

    report = {'passed': True, 'languages': {}}
    reference_numbers = None
    for lang in ('en', 'zh'):
        slides = get_slides(lang)
        require(len(slides) == 6, f'{lang}: expected six chart sections')
        data = []
        for index, slide in enumerate(slides, 1):
            match = re.search(r"data-chart-values='([^']+)'", slide)
            require(match is not None, f'{lang}/{index}: missing chart metadata')
            data.append(json.loads(match.group(1)))
            svg = re.search(r'<svg\b.*?</svg>', slide, re.S)
            require(svg is not None, f'{lang}/{index}: missing inline SVG')
            root = ET.fromstring(svg.group(0))
            require(root.attrib.get('viewBox') == '0 0 1720 620', f'{lang}/{index}: unexpected chart coordinate system')
            require('data-information-visual' in root.attrib, f'{lang}/{index}: chart must be information-bearing')
            require('artwork-slot' not in svg.group(0), f'{lang}/{index}: information SVG cannot contain a replaceable artwork slot')

        columns, ranking, pictorial, grouped, stacked, waterfall = data
        require(len(columns['quarters']) == len(columns['values']) == 4, f'{lang}: column categories do not match values')
        require(all(0 <= v <= columns['axis_max'] for v in columns['values']), f'{lang}: a column exceeds its zero-based axis')
        require(close(columns['values'][-1] - columns['values'][0], 30), f'{lang}: the +30 releases claim is no longer true')

        require(len(ranking['labels']) == len(ranking['values']) == 5, f'{lang}: ranking categories do not match values')
        require(ranking['values'] == sorted(ranking['values'], reverse=True), f'{lang}: ranking is not descending')
        require(all(0 <= v <= ranking['axis_max'] for v in ranking['values']), f'{lang}: ranking exceeds its zero-based axis')
        require(close(sum(ranking['values']), ranking['total']), f'{lang}: support-ticket total is incorrect')
        require(ranking['total'] > 0 and round(100 * ranking['values'][0] / ranking['total']) == 31, f'{lang}: the rounded 31% access share is no longer true')

        require(len(pictorial['labels']) == len(pictorial['values']) == 4, f'{lang}: pictorial categories do not match values')
        require(pictorial['per_dot'] == 5, f'{lang}: the dot legend states five proposals')
        require(all(v >= 0 and v % pictorial['per_dot'] == 0 for v in pictorial['values']), f'{lang}: pictorial values must use complete five-proposal units')
        dots = re.findall(r'data-unit="([0-9.]+)"', slides[2])
        require(all(float(v) == pictorial['per_dot'] for v in dots), f'{lang}: a dot has a different unit')
        require(close(sum(pictorial['values']), pictorial['total']) and close(len(dots) * pictorial['per_dot'], pictorial['total']), f'{lang}: pictorial data dots and total do not agree')
        require(len(dots) == 32, f'{lang}: the 32-dot summary is no longer true')

        require(len(grouped['labels']) == len(grouped['before']) == len(grouped['after']) == 3, f'{lang}: grouped categories do not match values')
        require(grouped['axis_max'] == 100 and all(0 <= v <= 100 for v in grouped['before'] + grouped['after']), f'{lang}: approval rates need a zero-to-100-percent axis')
        require(all(close(b - a, 20) for a, b in zip(grouped['before'], grouped['after'])), f'{lang}: the shared +20 percentage-point improvement is no longer true')

        require(len(stacked['labels']) == len(stacked['values']) == 3 and len(stacked['series']) == 3, f'{lang}: stacked categories do not match values')
        require(stacked['axis_max'] == 100 and all(len(row) == 3 and all(0 <= v <= 100 for v in row) and close(sum(row), 100) for row in stacked['values']), f'{lang}: each stacked bar must total 100 percent')
        require(close(stacked['values'][0][0], 40) and close(stacked['values'][-1][0], 60), f'{lang}: the build-time 40%-to-60% statement is no longer true')

        v = waterfall['values']
        require(len(waterfall['labels']) == len(v) == 5, f'{lang}: waterfall categories do not match values')
        require(v[0] >= 0 and v[1] >= 0 and all(x <= 0 for x in v[2:-1]), f'{lang}: waterfall signs disagree with its inflow/outflow labels')
        running = v[0]
        cumulative = [running]
        for change in v[1:-1]:
            running += change
            cumulative.append(running)
        cumulative.append(v[-1])
        require(close(running, v[-1]), f'{lang}: cash bridge does not reach closing cash')
        require(all(close(a, b) for a, b in zip(cumulative, waterfall['cumulative'])) and len(cumulative) == len(waterfall['cumulative']), f'{lang}: cumulative cash balances are inconsistent')
        require(all(0 <= amount <= waterfall['axis_max'] for amount in cumulative), f'{lang}: cash balance exceeds its axis')
        require(close(v[-1] - v[0], 10), f'{lang}: the +10 net-change claim is no longer true')

        numbers = [{k: value for k, value in item.items() if k not in ('labels', 'series')} for item in data]
        if reference_numbers is None:
            reference_numbers = numbers
        else:
            require(numbers == reference_numbers, 'English and Chinese quantitative data differ')
        report['languages'][lang] = {'sections': 6, 'svg_charts': 6, 'pictorial_data_dots': len(dots), 'numerical_claims': 'PASS', 'axes': 'PASS'}
    return report

