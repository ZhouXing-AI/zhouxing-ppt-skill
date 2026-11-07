THEME={'name': 'GROVE', 'zh': '共生', 'paper': '#F2EFDF', 'ink': '#253A31', 'accent': '#4CA785', 'bright': '#B8D7B8', 'soft': '#DDDCCF', 'second': '#B6A2D3', 'third': '#6385D4', 'body': 'GroveSans', 'cjk': 'GroveCJK', 'display': 'GroveSans', 'cjkd': 'GroveCJK', 'en_weight': 400, 'zh_weight': 400, 'zh_style': 'normal', 'radius': 9, 'titles': [('Give each contribution a place.', '让每一份贡献，都有位置。'), ('Small gatherings grow steadily.', '小小的相聚，慢慢生长。'), ('Listen where support is needed.', '听见，最需要支持的地方。'), ('Count the care that was shared.', '把共享的心意，认真记下。'), ('Make participation easier.', '让参与，变得更容易。'), ('Keep the work in balance.', '让共同的工作，保持平衡。'), ('Leave room to care for the group.', '为照顾彼此，留出时间。'), ('Make it easier to find support.', '让支持，更快抵达。'), ('Grow a shared store of knowledge.', '让共同的经验，逐渐生长。'), ('Look after the whole ecosystem.', '照顾好，社区的每一面。'), ('Help every request find a path.', '让每一份需求，都找到路径。'), ('Choose where to grow next.', '选一处，继续生长。'), ('Notice the gaps in our support.', '看见，共同支持中的空白。'), ('Bring the next gathering closer.', '让下一次相聚，更近一步。'), ('Keep the shared work visible.', '让共同的工作，被看见。'), ('Choose a way to gather.', '选一种方式，相聚。'), ('A season of growing together.', '用一个周期，一起生长。'), ('Find the right kind of support.', '找到，合适的支持方式。'), ('Share our time with care.', '把共同的时间，分配好。'), ('Turn an invitation into participation.', '让一份邀请，变成参与。')], 'cards': [('Welcome', '欢迎', 'Make the first step gentle.', '让第一步轻松一些。'), ('Listen', '倾听', 'Understand what is needed.', '理解真实的需要。'), ('Contribute', '贡献', 'Offer one useful thing.', '分享一份有用的支持。'), ('Sustain', '延续', 'Keep the circle open.', '让联结持续发生。')], 'counts': [16, 24, 36, 48], 'rank': [30, 26, 18, 12], 'ranklabels': [('Getting started', '开始参与'), ('Finding people', '找到同伴'), ('Sharing resources', '资源共享'), ('Keeping momentum', '持续行动')], 'units': ('shared sessions', '共享活动 · 场'), 'evidence': [('Conversations', '交流'), ('Guides', '指南'), ('Shared sessions', '共享活动')], 'groupnames': [('Welcome', '欢迎'), ('Learning', '学习'), ('Contribution', '贡献')], 'radarlabels': [('Welcome', '欢迎'), ('Trust', '信任'), ('Access', '可达'), ('Support', '支持'), ('Continuity', '持续')], 'source': [('Members', '成员'), ('Partners', '伙伴'), ('Hosts', '发起人')], 'middle': [('Connect', '联结'), ('Support', '支持')], 'outputs': [('Resolved', '已回应'), ('Follow up', '持续跟进')], 'scatterlabels': [('Welcome note', '欢迎信'), ('Resource list', '资源单'), ('Open hour', '开放时段'), ('Skill swap', '技能交换'), ('Small circle', '小组交流'), ('Workshop', '工作坊'), ('Mentoring', '结对支持'), ('Gathering', '集体相聚')], 'heatrows': [('Welcome', '欢迎'), ('Resources', '资源'), ('Access', '可达'), ('Follow-up', '跟进')], 'targets': [('Hosts ready', '发起人就绪率'), ('Replies sent', '需求回应率'), ('Resources shared', '资源共享率')], 'stages': [('Invite', '邀请', 'An open first step.', '发出开放的邀请。'), ('Meet', '相聚', 'Listen and connect.', '认真聆听，建立联结。'), ('Grow', '生长', 'Share useful contributions.', '共享有用的贡献。'), ('Continue', '延续', 'Make the next invitation.', '约定下一次相遇。')], 'donutlabels': [('Gathering', '相聚'), ('Preparation', '准备'), ('Follow-up', '跟进')], 'funnellabels': [('Invited', '已邀请'), ('Interested', '有意参与'), ('Registered', '已报名'), ('Joined', '已到场')], 'id': 'grove'}
"""Twenty reproducible bilingual layouts. Data are fictional design examples.
Run get_slides('en'/'zh-CN') and validate_data(); no browser dependencies.
"""
import json, math, re
from html import escape
# THEME is injected into each installed, standalone copy.
KINDS=['four-cards','columns','ranking','pictorial','grouped','stacked','waterfall','line','area','radar','sankey','scatter','heatmap','target','data-table','comparison-table','timeline','branch','donut','funnel']
DATA={
 'pictorial':[40,30,20], 'before':[42,54,62], 'after':[66,74,84],
 'stacked':[[35,25,40],[50,30,20],[65,25,10]],
 'waterfall':[80,30,-20,-25,65], 'line_a':[12,11,10,8,7,6], 'line_b':[10,9,7,6,4,3],
 'area':[8,13,11,18,22,20,28,34], 'radar_a':[50,60,65,55,70], 'radar_b':[80,82,88,76,90],
 'sankey_a':[[30,10],[20,15],[10,15]],'sankey_b':[[40,20],[25,15]],
 'scatter':[[2,35],[4,52],[6,45],[8,68],[10,82],[13,62],[16,90],[18,74]],
 'heatmap':[[80,65,50,90,70,45],[55,75,40,85,60,35],[95,85,65,90,80,70],[70,55,45,80,65,50]],
 'actual':[72,88,94],'target':[80,85,90],
 'table_plan':[24,30,36,42],'table_done':[22,29,33,40],
 'donut':[50,30,20],'funnel':[120,90,60,36]
}

def tr(lang,en,zh):return zh if lang in ('zh','zh-CN') else en
def pair(lang,v):return tr(lang,*v)
def n(v):return f'{v:.3f}'.rstrip('0').rstrip('.')
def text(x,y,s,size=28,fill=None,anchor='start',cls='',extra=''):
 return f'<text x="{n(x)}" y="{n(y)}" font-size="{size}" fill="{fill or THEME["ink"]}" text-anchor="{anchor}" class="{cls}" {extra}>{escape(str(s))}</text>'
def line(x,y,X,Y,color=None,width=1,extra=''):
 return f'<line x1="{n(x)}" y1="{n(y)}" x2="{n(X)}" y2="{n(Y)}" stroke="{color or THEME["soft"]}" stroke-width="{width}" {extra}/>'
def rect(x,y,w,h,fill,rx=0,extra=''):
 return f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="{rx}" fill="{fill}" {extra}/>'
def circle(x,y,r,fill,extra=''):
 return f'<circle cx="{n(x)}" cy="{n(y)}" r="{r}" fill="{fill}" {extra}/>'
def path(points,fill='none',stroke=None,width=2,close=False,extra=''):
 d='M'+' L'.join(f'{n(x)} {n(y)}' for x,y in points)+(' Z' if close else '')
 return f'<path d="{d}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{width}"' if stroke else '')+f' {extra}/>'
def motion(s,kind='fade',step=0):return s.replace(' ',f' data-chart-motion="{kind}" data-chart-step="{step}" ',1)
def group(s,kind,step):return f'<g data-chart-motion="{kind}" data-chart-step="{step}">{s}</g>'
def tag(lang,i):return pair(lang,THEME['titles'][i])
def label(lang,key,i):return pair(lang,THEME[key][i])
def legend(x,y,color,s,fg):return rect(x,y-19,22,22,color,THEME['radius']/3)+text(x+36,y,s,27,fg)
def symbol(x,y,size,color):
 if THEME['id']=='spark':return path([(x,y),(x+size*.72,y),(x+size,y+size*.28),(x+size,y+size),(x,y+size)],color)
 if THEME['id']=='blend':return rect(x,y,size,size,color,size*.34)
 return f'<path d="M{x} {y+size}Q{x-4} {y-4} {x+size} {y}Q{x+size+4} {y+size+4} {x} {y+size}Z M{x+3} {y+size-3}L{x+size-3} {y+3}" fill="none" stroke="{color}" stroke-width="2.2"/>'
def section(lang,i,parts,subtitle='',values=None,dark=False):
 title=tag(lang,i);kind=KINDS[i];svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1680 610" role="img" aria-label="{escape(title,quote=True)}" data-information-visual=""><title>{escape(title)}</title>'+''.join(parts)+'</svg>'
 return f'<section class="slide expansion30 x30-{kind} {"x30-dark" if dark else ""}" data-tone="{"dark" if dark else "light"}" data-title="{escape(title,quote=True)}" data-chart-kind="{kind}" data-layout-id="{kind}" data-provenance="synthetic-sample" data-chart-values="{escape(json.dumps(values,ensure_ascii=False),quote=True)}"><header class="x30-head"><h2 class="reveal">{escape(title)}</h2><p class="x30-sub reveal">{escape(subtitle)}</p></header><div class="x30-chart" data-chart-container="">{svg}</div></section>'
def axes_y(parts,ticks,maximum,x0,x1,base,height,fg,grid,unit):
 parts.append(text(x0,25,unit,27,fg))
 for v in ticks:
  y=base-v/maximum*height;parts.extend([line(x0,y,x1,y,fg if v==0 else grid,1.2),text(x0-25,y+9,v,27,fg,'end')])

def cards(lang):
 p=[];w=390;gap=40
 for i,c in enumerate(THEME['cards']):
  x=i*(w+gap);y=20+(0 if THEME['id']=='spark' else i%2*35);fill=THEME['accent'] if i==3 else THEME['soft'];fg=THEME['paper'] if i==3 else THEME['ink']
  if THEME['id']=='spark':fill=THEME['bright'] if i==3 else THEME['ink'];fg=THEME['ink'] if i==3 else THEME['paper']
  p.append(group(rect(x,y,w,500,fill,THEME['radius'])+symbol(x+30,y+30,35,fg)+text(x+30,y+210,pair(lang,c[:2]),42,fg,cls='x30-display')+text(x+30,y+306,tr(lang,c[2],c[3]),25,fg)+line(x+30,y+425,x+w-30,y+425,fg,1)+text(x+30,y+473,f'0{i+1}',29,fg),'fade',i))
 return section(lang,0,p,tr(lang,'Four connected roles, each with one clear responsibility.','四个相互连接的环节，各自承担一件清楚的事。'))

def columns(lang):
 p=[];vals=THEME['counts'];base=510;h=390
 # BLEND is a full-width chart; SPARK and GROVE pair a typographic measure with a plot.
 full=THEME['id']=='blend';x0=100 if full else 650;x1=1600
 axes_y(p,[0,15,30,45,60],60,x0,x1,base,h,THEME['ink'],THEME['soft'],pair(lang,THEME['units']))
 if not full:p += [motion(text(0,226,vals[-1],200,THEME['accent'],cls='x30-display'),'fade',2),text(6,315,tr(lang,'in the latest cycle','最新一轮的成果'),30),line(0,360,475,360,THEME['accent'],1.4),text(6,424,tr(lang,'Each cycle is counted separately.','每轮单独计数，非累计。'),26)]
 step=(x1-x0)/4
 for i,v in enumerate(vals):
  x=x0+step*(i+.5);top=base-v/60*h;w=min(150,step*.42)
  p += [motion(rect(x-w/2,top,w,base-top,THEME['accent'] if i==3 else THEME['second'],min(THEME['radius'],8)),'grow-y',i),motion(text(x,top-22,v,39,THEME['ink'],'middle',cls='x30-display'),'fade',i+1),text(x,565,tr(lang,f'Cycle {i+1}',f'第{i+1}轮'),27,anchor='middle')]
 return section(lang,1,p,tr(lang,'Four cycles, measured with the same completion criteria.','四轮实践，采用同一套完成标准。'),{'values':vals,'axis':[0,60],'cumulative':False})

def ranking(lang):
 dark=THEME['id']=='spark';fg=THEME['paper'] if dark else THEME['ink'];col=THEME['bright'] if dark else THEME['accent'];p=[];start=430;scale=28
 for v in (0,10,20,30,40):p += [line(start+v*scale,55,start+v*scale,490,THEME['soft'],1,'opacity=".35"'),text(start+v*scale,562,v,27,fg,'middle')]
 for i,v in enumerate(THEME['rank']):
  y=66+i*120;p += [text(0,y+38,label(lang,'ranklabels',i),30,fg),motion(rect(start,y,v*scale,48,col if i==0 else THEME['second'],THEME['radius']),'grow-x',i),motion(text(start+v*scale+20,y+37,v,34,fg),'fade',i+1)]
 p.append(text(1550,609,tr(lang,'Mentions in review · count','评审中提及次数 · 次'),26,fg,'end'))
 return section(lang,2,p,tr(lang,'Rank the questions by how often they appeared in the review.','按评审中的提及次数，安排下一步的关注顺序。'),{'values':THEME['rank'],'axis':[0,40],'unit':'mentions'},dark)

def pictorial(lang):
 p=[];vals=DATA['pictorial']
 for i,v in enumerate(vals):
  x=i*580
  if i:p.append(line(x-40,0,x-40,550,THEME['soft']))
  p += [text(x,55,label(lang,'evidence',i),34),motion(text(x,225,v,132,THEME['accent'],cls='x30-display'),'fade',i),text(x+175,216,tr(lang,'records','份记录'),27)]
  for j in range(v//5):p.append(group(symbol(x+(j%4)*112,285+(j//4)*100,58,THEME['accent']),'pop',i+j))
 p += [line(0,560,1680,560,THEME['ink']),text(0,608,tr(lang,'One symbol = 5 records','每个图形 = 5份记录'),27),text(1680,608,tr(lang,'90 records in three collections','三类来源，共90份记录'),28,THEME['accent'],'end')]
 return section(lang,3,p,tr(lang,'Every equal-sized symbol stands for the same number of documented items.','每个等大图形，都代表相同数量的归档记录。'),{'values':vals,'per_symbol':5})

def grouped(lang):
 p=[legend(425,23,THEME['second'],tr(lang,'Before','调整前'),THEME['ink']),legend(700,23,THEME['accent'],tr(lang,'After','调整后'),THEME['ink'])];start=425;scale=11.4
 for v in (0,25,50,75,100):p += [line(start+v*scale,65,start+v*scale,505,THEME['soft']),text(start+v*scale,570,f'{v}%',27,anchor='middle')]
 for i,(a,b) in enumerate(zip(DATA['before'],DATA['after'])):
  y=85+i*160;p.append(text(0,y+50,label(lang,'groupnames',i),35,cls='x30-display'))
  for j,(v,c) in enumerate([(a,THEME['second']),(b,THEME['accent'])]):p += [motion(rect(start,y+j*48,v*scale,32,c,min(THEME['radius'],10)),'grow-x',i*2+j),motion(text(start+v*scale+18,y+j*48+25,f'{v}%',29),'fade',i*2+j+1)]
 p.append(text(1660,608,tr(lang,'Share completing the agreed task · %','完成约定任务的比例 · %'),26,anchor='end'))
 return section(lang,4,p,tr(lang,'Compare the same three task categories before and after the change.','在相同的三类任务中，对比调整前后的完成比例。'),{'before':DATA['before'],'after':DATA['after'],'axis':[0,100]})

def stacked(lang):
 p=[];labels=[tr(lang,'Ready','已就绪'),tr(lang,'In progress','进行中'),tr(lang,'Open','待解决')];colors=[THEME['accent'],THEME['second'],THEME['soft']]
 for j in range(3):p.append(legend(260+j*470,25,colors[j],labels[j],THEME['ink']))
 if THEME['id']=='spark':
  for v in (0,25,50,75,100):p += [line(130,505-v*3.8,1600,505-v*3.8,THEME['soft']),text(102,514-v*3.8,f'{v}%',26,anchor='end')]
  for i,vals in enumerate(DATA['stacked']):
   cx=410+i*490;y=505;chunk=[]
   for j,v in enumerate(vals):hh=v*3.8;y-=hh;chunk += [rect(cx-130,y,260,hh,colors[j]),text(cx,y+hh/2+10,f'{v}%',30,THEME['paper'] if j==0 else THEME['ink'],'middle')]
   p += [group(''.join(chunk),'grow-y',i),text(cx,560,tr(lang,f'Review {i+1}',f'第{i+1}次评审'),27,anchor='middle')]
 else:
  for i,vals in enumerate(DATA['stacked']):
   y=100+i*150;x=290;chunk=[];p.append(text(250,y+45,tr(lang,f'Review {i+1}',f'第{i+1}次评审'),28,anchor='end'))
   for j,v in enumerate(vals):w=v*12.8;chunk += [rect(x,y,w,75,colors[j]),text(x+w/2,y+48,f'{v}%',30,THEME['paper'] if j==0 else THEME['ink'],'middle')];x+=w
   p.append(group(''.join(chunk),'wipe-x',i))
  for v in (0,25,50,75,100):p.append(text(290+v*12.8,565,f'{v}%',27,anchor='middle'))
 return section(lang,5,p,tr(lang,'Each review accounts for the full set of work; every composition totals 100%.','每次评审，都完整呈现当时的工作集合；各组均为100%。'),{'values':DATA['stacked'],'unit':'percent'})

def waterfall(lang):
 p=[];base=510;scale=3.2;xs=[220,530,840,1150,1460];spans=[(0,80),(80,110),(110,90),(90,65),(0,65)];labels=[tr(lang,'Opening','期初'),tr(lang,'Added','新增'),tr(lang,'Delivery','执行'),tr(lang,'Review','评审'),tr(lang,'Available','可用')]
 axes_y(p,[0,30,60,90,120],120,100,1650,base,384,THEME['ink'],THEME['soft'],tr(lang,'Shared working time · hours','可分配工作时间 · 小时'))
 for i,(x,(a,b),v) in enumerate(zip(xs,spans,DATA['waterfall'])):
  y=base-max(a,b)*scale;c=THEME['accent'] if i in(0,4) else THEME['bright'] if v>0 else THEME['second']
  p += [motion(rect(x-75,y,150,abs(a-b)*scale,c,min(THEME['radius'],8)),'grow-y',i),motion(text(x,y-21,('+' if i==1 else '')+str(v),39,THEME['ink'],'middle',cls='x30-display'),'fade',i+1),text(x,566,labels[i],28,anchor='middle')]
  if i<4:p.append(motion(line(x+75,base-b*scale,xs[i+1]-75,base-b*scale,THEME['ink'],1.3,'stroke-dasharray="7 6"'),'wipe-x',i+1))
 return section(lang,6,p,tr(lang,'80 + 30 − 20 − 25 = 65 hours available for the next round.','80 + 30 − 20 − 25 = 65小时，为下一轮保留余量。'),{'values':DATA['waterfall'],'axis':[0,120],'unit':'hours'})

def trend(lang,area=False):
 idx=8 if area else 7;dark=area and THEME['id']!='grove';fg=THEME['paper'] if dark else THEME['ink'];accent=THEME['bright'] if dark else THEME['accent'];p=[]
 maxv=40 if area else 15;vals=DATA['area'] if area else DATA['line_a'];count=len(vals);base=510;height=380;x0=100;x1=1530
 axes_y(p,list(range(0,41,10)) if area else [0,3,6,9,12,15],maxv,x0,x1,base,height,fg,THEME['soft'],tr(lang,'Accepted contributions / week','每周采用贡献 · 份') if area else tr(lang,'Turnaround · median days','周转时间 · 中位天数'))
 if not area:p += [legend(700,25,THEME['second'],tr(lang,'Track A','路径A'),fg),legend(1000,25,accent,tr(lang,'Track B','路径B'),fg)]
 for j,key in enumerate(['area'] if area else ['line_a','line_b']):
  values=DATA[key];points=[(x0+i*(x1-x0)/(count-1),base-v/maxv*height) for i,v in enumerate(values)];c=accent if area or j==1 else THEME['second']
  if area:p.append(motion(path([(x0,base)]+points+[(x1,base)],c,close=True,extra='fill-opacity=".25"'),'wipe-x',0))
  p.append(motion(path(points,stroke=c,width=4,extra='stroke-dasharray="10 7"' if not area and j==0 else ''),'wipe-x' if not area and j==0 else 'draw',j))
  for i,(x,y) in enumerate(points):
   p.append(motion(circle(x,y,6,THEME['ink'] if dark else THEME['paper'],f'stroke="{c}" stroke-width="2.8"'),'pop',2))
   if i in (0,count-1):p.append(motion(text(x,y-22,values[i],34,fg,'middle'),'fade',3))
 for i in range(count):p.append(text(x0+i*(x1-x0)/(count-1),565,tr(lang,f'W{i+1}',f'第{i+1}周'),27,fg,'middle'))
 return section(lang,idx,p,tr(lang,'Weekly counts, under the same acceptance criteria; these are not cumulative.','每周数量使用同一采用标准，分别计数而非累计。') if area else tr(lang,'Two work streams, measured on the same six-week schedule.','在相同的六周周期内，记录两条工作路径。'),{'values':DATA['area'],'axis':[0,40],'cumulative':False} if area else {'a':DATA['line_a'],'b':DATA['line_b'],'axis':[0,15]},dark)

def radar(lang):
 p=[];cx=430;cy=315;r=188
 def pt(i,v):a=-math.pi/2+i*2*math.pi/5;return cx+r*v/100*math.cos(a),cy+r*v/100*math.sin(a)
 for v in [20,40,60,80,100]:p += [path([pt(i,v) for i in range(5)],stroke=THEME['soft'],width=1,close=True),text(cx+12,cy-r*v/100+9,v,25)]
 p.append(text(cx+12,cy+25,0,25))
 for i in range(5):
  x,y=pt(i,100);p.append(line(cx,cy,x,y,THEME['soft']));x,y=pt(i,139);p.append(text(x,y+10,label(lang,'radarlabels',i),28,anchor='middle'))
 for j,key in enumerate(['radar_a','radar_b']):
  c=THEME['second'] if j==0 else THEME['accent'];points=[pt(i,v) for i,v in enumerate(DATA[key])]
  p.append(motion(path(points,stroke=c,width=4,close=True,extra='stroke-dasharray="9 6"' if j==0 else ''),'wipe-x' if j==0 else 'draw',j))
  for x,y in points:p.append(motion(circle(x,y,6,THEME['paper'],f'stroke="{c}" stroke-width="2.5"'),'pop',2))
 p += [text(940,45,tr(lang,'One scale. Five checks.','同一标尺，五项检查。'),36,THEME['accent'],cls='x30-display'),line(940,80,1660,80,THEME['ink']),text(1320,128,tr(lang,'Current','当前'),26,anchor='middle'),text(1575,128,tr(lang,'Next','下一版'),26,anchor='middle')]
 for i in range(5):
  y=210+i*78;p += [text(940,y,label(lang,'radarlabels',i),28),motion(text(1320,y,DATA['radar_a'][i],42,anchor='middle',cls='x30-display'),'fade',2+i),motion(text(1575,y,DATA['radar_b'][i],42,THEME['accent'],'middle',cls='x30-display'),'fade',2+i),line(940,y+26,1660,y+26,THEME['soft'])]
 return section(lang,9,p,tr(lang,'Five dimensions use the same 0–100 rubric; exact scores stay beside the outlines.','五个维度统一采用0—100分量表，准确分数与轮廓并列。'),{'current':DATA['radar_a'],'next':DATA['radar_b'],'axis':[0,100]})

def sankey(lang):
 totals=[[40,35,25],[60,40],[65,35]];positions=[]
 for vs in totals:
  gap=(480-400)/(len(vs)-1);y=65;g=[]
  for v in vs:g.append((y,v*4));y+=v*4+gap
  positions.append(g)
 xs=[25,725,1395];widths=[250,250,260];p=[];labels=[];colors=[THEME['accent'],THEME['second'],THEME['third']]
 for stage,matrix in enumerate([DATA['sankey_a'],DATA['sankey_b']]):
  src=[0]*len(matrix);dst=[0]*len(matrix[0])
  for i,row in enumerate(matrix):
   for j,v in enumerate(row):
    sy=positions[stage][i][0]+src[i];ty=positions[stage+1][j][0]+dst[j];h=v*4;x1=xs[stage]+widths[stage];x2=xs[stage+1];dx=(x2-x1)*.45
    d=f'M{x1} {sy}C{x1+dx} {sy} {x2-dx} {ty} {x2} {ty}L{x2} {ty+h}C{x2-dx} {ty+h} {x1+dx} {sy+h} {x1} {sy+h}Z'
    c=colors[i] if stage==0 else colors[j];p.append(motion(f'<path d="{d}" fill="{c}" fill-opacity=".38" data-flow-stage="{stage+1}" data-flow-value="{v}"/>','wipe-x',stage*2+1))
    t=.2;u=1-t;lx=u**3*x1+3*u*u*t*(x1+dx)+3*u*t*t*(x2-dx)+t**3*x2;blend=3*t*t-2*t*t*t;ly=(1-blend)*(sy+h/2)+blend*(ty+h/2)
    labels.append(motion(text(lx,ly+9,v,28,anchor='middle',extra=f'stroke="{THEME["paper"]}" stroke-width="6" paint-order="stroke"'),'fade',stage*2+2));src[i]+=h;dst[j]+=h
 for g,vs in enumerate(totals):
  p.append(text(xs[g],25,tr(lang,['Source','Primary route','Outcome'][g],['来源','主要路径','结果'][g]),27))
  for i,v in enumerate(vs):
   y,h=positions[g][i];fill=THEME['paper'] if g<2 else THEME['accent'];fg=THEME['ink'] if g<2 else THEME['paper']
   p += [motion(rect(xs[g],y,widths[g],h,fill,THEME['radius'],f'stroke="{THEME["accent"]}" stroke-width="1.5"'),'fade',g*2),motion(text(xs[g]+18,y+h/2+9,label(lang,['source','middle','outputs'][g],i),25,fg),'fade',g*2),motion(text(xs[g]+widths[g]-17,y+h/2+15,v,43,fg,'end',cls='x30-display'),'fade',g*2)]
 p += labels
 return section(lang,10,p,tr(lang,'The same 100 requests; each follows one primary route and all flows are counted.','同一批100项需求，每项归入一条主要路径；所有流量均计数。'),{'inputs':totals[0],'middle':totals[1],'outputs':totals[2],'a':DATA['sankey_a'],'b':DATA['sankey_b'],'scale':4})

def scatter(lang):
 p=[];base=505;x0=100;x1=1570;scale=(x1-x0)/20
 axes_y(p,[0,25,50,75,100],100,x0,x1,base,370,THEME['ink'],THEME['soft'],tr(lang,'Usefulness rating · points','预期实用度评分 · 分'))
 for v in [0,5,10,15,20]:p += [line(x0+v*scale,505,x0+v*scale,515,THEME['ink']),text(x0+v*scale,560,v,28,anchor='middle')]
 for i,(hours,score) in enumerate(DATA['scatter']):
  x=x0+hours*scale;y=base-score*3.7;left=hours>15;p += [motion(circle(x,y,10,THEME['accent'],f'data-point-id="{i}" stroke="{THEME["paper"]}" stroke-width="2"'),'pop',i),motion(text(x+(-18 if left else 18),y+(38 if THEME['id']=='grove' and i==2 else -19),label(lang,'scatterlabels',i),27,anchor='end' if left else 'start'),'fade',i+1)]
 p.append(text(1570,608,tr(lang,'Estimated effort · hours','预计投入 · 小时'),27,anchor='end'))
 return section(lang,11,p,tr(lang,'Compare eight proposed activities by estimated effort and a shared 0–100 rating.','八个待验证的提案，比较预计投入与统一的0—100分评价。'),{'points':DATA['scatter'],'x':[0,20],'y':[0,100],'same_size':True})

def heatmap(lang):
 dark=THEME['id']=='blend';fg=THEME['paper'] if dark else THEME['ink'];p=[]
 for j in range(6):p.append(text(360+j*220,35,tr(lang,f'Team {chr(65+j)}',f'{chr(65+j)}组'),28,fg,'middle'))
 p.append(line(0,63,1660,63,fg,1.1))
 for i,row in enumerate(DATA['heatmap']):
  y=88+i*108;p.append(text(0,y+56,label(lang,'heatrows',i),30,fg,cls='x30-display'))
  for j,v in enumerate(row):
   fill=THEME['paper'] if v<50 else THEME['second'] if v<75 else THEME['accent'];ink=THEME['paper'] if v>=75 else THEME['ink']
   p += [motion(rect(260+j*220,y,200,87,fill,THEME['radius']/2,f'stroke="{THEME["soft"]}" stroke-width="1" data-heat-value="{v}"'),'fade',i),motion(text(360+j*220,y+59,v,39,ink,'middle',cls='x30-display'),'fade',i)]
 p.append(text(0,587,tr(lang,'Readiness / 100','就绪度／100分'),29,fg))
 for i,(s,c) in enumerate([('0–49',THEME['paper']),('50–74',THEME['second']),('75–100',THEME['accent'])]):p += [rect(850+i*265,555,30,30,c,0,f'stroke="{THEME["soft"]}"'),text(895+i*265,582,s,26,fg)]
 return section(lang,12,p,tr(lang,'Six teams, four checks, one shared rubric. Every cell keeps its exact score.','六组、四项检查，使用同一量表；每格保留准确分数。'),{'values':DATA['heatmap'],'bands':[[0,49],[50,74],[75,100]]},dark)

def target(lang):
 dark=THEME['id']!='grove';fg=THEME['paper'] if dark else THEME['ink'];col=THEME['bright'] if dark else THEME['accent'];p=[]
 for i,(a,b) in enumerate(zip(DATA['actual'],DATA['target'])):
  x=i*580;w=480;delta=a-b
  if i:p.append(line(x-45,0,x-45,580,THEME['soft'],1,'opacity=".4"'))
  p += [text(x,40,label(lang,'targets',i),29,fg),motion(text(x,235,f'{a}%',126,col,cls='x30-display'),'fade',i),rect(x,330,w,20,THEME['soft'],0,'opacity=".25"'),motion(rect(x,330,w*a/100,20,col),'grow-x',i),motion(line(x+w*b/100,312,x+w*b/100,370,fg,3),'fade',i+1),text(x+w*b/100,290,tr(lang,f'Target {b}%',f'目标{b}%'),25,fg,'middle')]
  for tick in [0,50,100]:p.append(text(x+w*tick/100,422,f'{tick}%',26,fg,'middle'))
  p += [line(x,472,x+w,472,THEME['soft'],1,'opacity=".4"'),text(x,536,tr(lang,f'{abs(delta)} points '+('above target' if delta>=0 else 'to target'),f'高于目标{delta}个百分点' if delta>=0 else f'距目标还差{-delta}个百分点'),27,col)]
 return section(lang,13,p,tr(lang,'Show progress and target on the same scale, including work already beyond the target.','进展与目标使用同一标尺，也保留已经超出目标的部分。'),{'actual':DATA['actual'],'targets':DATA['target'],'axis':[0,100]},dark)

def data_table(lang):
 p=[];cols=[0,700,1025,1340,1680];headers=[tr(lang,'Workstream','工作方向'),tr(lang,'Planned','计划'),tr(lang,'Delivered','完成'),tr(lang,'Remaining','待完成')]
 p.append(rect(0,0,1680,87,THEME['accent'],THEME['radius']))
 for j,h in enumerate(headers):p.append(text(cols[j]+28,54,h,29,THEME['paper']))
 for i,(plan,done) in enumerate(zip(DATA['table_plan'],DATA['table_done'])):
  y=88+i*108
  if i%2==0:p.append(rect(0,y,1680,108,THEME['soft'],0,'fill-opacity=".4"'))
  name=tr(lang,THEME['cards'][i][0],THEME['cards'][i][1]);p.append(text(28,y+67,name,32))
  for j,v in enumerate([plan,done,plan-done]):p.append(motion(text(cols[j+1]+28,y+67,v,36,THEME['accent'] if j==2 else THEME['ink'],cls='x30-display'),'fade',i))
  p.append(line(0,y+108,1680,y+108,THEME['soft']))
 p += [text(0,595,tr(lang,'Agreed items · count','约定事项 · 项'),27),text(1680,595,tr(lang,'132 planned · 124 delivered · 8 remaining','计划132项 · 完成124项 · 待完成8项'),27,THEME['accent'],'end')]
 return section(lang,14,p,tr(lang,'A shared ledger gives each workstream a plan, a result and a visible remainder.','用一份共同台账，记录各方向的计划、完成与剩余事项。'),{'planned':DATA['table_plan'],'delivered':DATA['table_done'],'remaining':[2,1,3,2],'unit':'items'})

def compare(lang):
 p=[];xs=[0,450,860,1270];widths=[420,380,380,410];headers=[tr(lang,'Decision criterion','选择条件'),tr(lang,'Quick session','短时交流'),tr(lang,'Working session','共同实践'),tr(lang,'Extended programme','持续计划')]
 for j in range(4):
  if j:p.append(rect(xs[j],0,widths[j],535,THEME['soft'] if j!=2 else THEME['bright'],THEME['radius']))
  p.append(text(xs[j]+20,55,headers[j],26))
 rows=[(tr(lang,'Time together','共同时间'),['30 min','2 h','4 weeks'],['30分钟','2小时','4周']), (tr(lang,'Primary outcome','主要成果'),['A clear question','A tested draft','A repeatable practice'],['明确问题','验证草案','形成持续实践']), (tr(lang,'Preparation','准备程度'),['Light','Moderate','Substantial'],['较少','适中','较多']), (tr(lang,'Best when','适用情况'),['You need alignment','You need evidence','You need continuity'],['需要达成共识','需要获得证据','需要长期延续'])]
 for i,(label,en,zh) in enumerate(rows):
  y=140+i*108;p.append(text(20,y,label,29));p.append(line(0,y+34,1680,y+34,THEME['paper'],1))
  for j in range(3):p.append(motion(text(xs[j+1]+20,y,tr(lang,en[j],zh[j]),26),'fade',i))
 return section(lang,15,p,tr(lang,'Choose the format by the work it needs to support, rather than by size alone.','按需要推进的工作选择形式，而不只比较规模大小。'),{'formats':['30 minutes','2 hours','4 weeks'],'qualitative':True})

def timeline(lang):
 p=[];ys=[235,235,235,235];xs=[210,630,1050,1470]
 p.append(line(210,235,1470,235,THEME['accent'],3))
 for i,(x,c) in enumerate(zip(xs,THEME['stages'])):
  p += [motion(symbol(x-20,215,40,THEME['accent']),'pop',i),text(x,171,tr(lang,f'Week {i+1}',f'第{i+1}周'),28,anchor='middle'),motion(text(x,335,tr(lang,c[0],c[1]),40,THEME['accent'],'middle',cls='x30-display'),'fade',i),text(x,404,tr(lang,c[2],c[3]),26,anchor='middle')]
 return section(lang,16,p,tr(lang,'A four-week sequence, with a concrete outcome at the end of each stage.','一个四周周期，每个阶段都形成明确的成果。'),{'stages':4,'duration_weeks':4})

def branch(lang):
 p=[];fg=THEME['ink'];ac=THEME['accent'];soft=THEME['soft'];rx=THEME['radius'];
 p += [path([(390,275),(610,275)],stroke=ac,width=2.5),path([(935,275),(1110,275),(1110,125),(1260,125)],stroke=ac,width=2.5),path([(935,275),(1110,275),(1110,425),(1260,425)],stroke=ac,width=2.5)]
 nodes=[(0,215,390,120,tr(lang,'Define the need','明确需要')),(610,185,325,180,tr(lang,'Enough evidence?','证据是否充分？')),(1260,65,400,120,tr(lang,'Proceed with a small step','以小步行动推进')),(1260,365,400,120,tr(lang,'Run one focused test','先做一次聚焦验证'))]
 for i,(x,y,w,h,s) in enumerate(nodes):p += [motion(rect(x,y,w,h,soft if i!=2 else THEME['bright'],rx,f'stroke="{ac}" stroke-width="1.5"'),'fade',i),motion(text(x+w/2,y+h/2+11,s,28,fg,'middle'),'fade',i)]
 p += [text(1145,105,tr(lang,'Yes','是'),25,ac),text(1145,405,tr(lang,'Not yet','还没有'),25,ac),path([(1460,485),(1460,557),(770,557),(770,365)],stroke=ac,width=2,extra='stroke-dasharray="8 6"'),text(1140,605,tr(lang,'Return with evidence','带着证据，重新判断'),27,ac,'middle')]
 # Arrowheads encode direction, including the feedback return.
 for x,y,kind in [(605,275,'r'),(1255,125,'r'),(1255,425,'r'),(770,369,'u')]:p.append(path([(x-9,y-6),(x,y),(x-9,y+6)] if kind=='r' else [(x-6,y+9),(x,y),(x+6,y+9)],stroke=ac,width=2.5))
 return section(lang,17,p,tr(lang,'One decision point, two clear actions and a route back to review.','一个判断点，两条明确行动路径，并保留返回评估的回路。'),{'decision_branches':2,'feedback':True})

def donut(lang):
 p=[];cx=420;cy=305;r=205;stroke=72;length=2*math.pi*r;offset=0;colors=[THEME['accent'],THEME['second'],THEME['third']]
 for i,v in enumerate(DATA['donut']):
  # No SVG transform: circumference begins at 3 o'clock and preserves exact angles.
  p.append(motion(circle(cx,cy,r,'none',f'stroke="{colors[i]}" stroke-width="{stroke}" stroke-dasharray="{n(length*v/100)} {n(length*(100-v)/100)}" stroke-dashoffset="{n(-offset)}"'),'fade',i));offset+=length*v/100
 p += [text(cx,cy+8,'100%',81,THEME['ink'],'middle',cls='x30-display'),text(cx,cy+65,tr(lang,'shared time','共同时间'),28,anchor='middle')]
 for i,v in enumerate(DATA['donut']):
  y=95+i*175;p += [symbol(920,y,30,colors[i]),text(978,y+26,label(lang,'donutlabels',i),32),motion(text(1660,y+51,f'{v}%',76,THEME['accent'],'end',cls='x30-display'),'fade',i),line(920,y+105,1660,y+105,THEME['soft'])]
 return section(lang,18,p,tr(lang,'Allocate the same time budget across three kinds of work; the shares total 100%.','将同一份时间预算，分配给三类工作；比例合计100%。'),{'values':DATA['donut'],'unit':'percent'})

def funnel(lang):
 p=[];maxv=DATA['funnel'][0];center=620;maxw=1060
 # Equal-height, flat horizontal bands make width the only quantitative encoding.
 for i,v in enumerate(DATA['funnel']):
  y=25+i*135;w=maxw*v/maxv;fill=THEME['accent'] if i==3 else THEME['second'] if i==1 else THEME['bright'];fg=THEME['paper'] if i==3 else THEME['ink']
  p += [motion(rect(center-w/2,y,w,88,fill,THEME['radius']),'grow-x',i),motion(text(center,y+57,v,43,fg,'middle',cls='x30-display'),'fade',i+1),text(1270,y+40,label(lang,'funnellabels',i),31),text(1270,y+81,f'{v/maxv*100:g}%',26,THEME['accent'])]
 return section(lang,19,p,tr(lang,'Follow one cohort through four stages; percentages use the original 120 as the denominator.','同一批对象经过四个阶段，所有百分比均以最初120个为分母。'),{'values':DATA['funnel'],'width_scale':maxw/maxv,'percent':[100,75,50,30]})

def get_slides(lang='en'):
 if lang not in ('en','zh','zh-CN'):raise ValueError('Unsupported locale')
 return [cards(lang),columns(lang),ranking(lang),pictorial(lang),grouped(lang),stacked(lang),waterfall(lang),trend(lang),trend(lang,True),radar(lang),sankey(lang),scatter(lang),heatmap(lang),target(lang),data_table(lang),compare(lang),timeline(lang),branch(lang),donut(lang),funnel(lang)]

def validate_data():
 assert len(THEME['titles'])==20 and len(get_slides('en'))==20
 assert all(0<=v<=60 for v in THEME['counts'])
 assert all(0<=v<=40 for v in THEME['rank'])
 assert sum(DATA['pictorial'])==90 and all(v%5==0 for v in DATA['pictorial'])
 assert all(sum(row)==100 for row in DATA['stacked'])
 assert sum(DATA['waterfall'][:-1])==DATA['waterfall'][-1]==65
 assert len(DATA['line_a'])==len(DATA['line_b'])==6 and max(DATA['line_a']+DATA['line_b'])<=15
 assert len(DATA['area'])==8 and max(DATA['area'])<=40
 assert len(DATA['radar_a'])==len(DATA['radar_b'])==5 and max(DATA['radar_a']+DATA['radar_b'])<=100
 a,b=DATA['sankey_a'],DATA['sankey_b'];assert [sum(r) for r in a]==[40,35,25]
 assert [sum(r[j] for r in a) for j in range(2)]==[60,40]==[sum(r) for r in b]
 assert [sum(r[j] for r in b) for j in range(2)]==[65,35]
 assert len(DATA['scatter'])==8 and all(0<=x<=20 and 0<=y<=100 for x,y in DATA['scatter'])
 assert len(DATA['heatmap'])==4 and all(len(r)==6 and all(0<=v<=100 for v in r) for r in DATA['heatmap'])
 assert all(0<=v<=100 for v in DATA['actual']+DATA['target'])
 assert sum(DATA['table_plan'])==132 and sum(DATA['table_done'])==124
 assert sum(DATA['donut'])==100
 assert DATA['funnel']==sorted(DATA['funnel'],reverse=True)
 return {'pass':True,'theme':THEME['id'],'new_pages':20,'languages':['en','zh-CN'],'data_origin':'synthetic-sample','sankey_total':100,'flows':10,'heat_cells':24,'scatter_points':8,'donut_total':100,'funnel_denominator':120}

if __name__=='__main__':
 import argparse
 from pathlib import Path
 p=argparse.ArgumentParser();p.add_argument('--lang',default='en',choices=['en','zh','zh-CN']);p.add_argument('--output',type=Path);a=p.parse_args();validate_data()
 if a.output:
  if a.output.exists():raise SystemExit('Output already exists; choose a new file.')
  a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text('\n'.join(get_slides(a.lang)))
 else:print(json.dumps(validate_data(),ensure_ascii=False,indent=2))
