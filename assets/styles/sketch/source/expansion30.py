"""Twenty bilingual data compositions. SVG geometry is the final data state.

Run --validate to verify measures, or --lang en/zh-CN --output fragment.html.
THEME is set to its owning style when installed; no external package is required.
"""
from html import escape
from pathlib import Path
import argparse, json, math, textwrap

THEME = 'sketch'
CONFIG = {
 'sketch': dict(paper='#F4F1EC',ink='#212121',accent='#AAF0CE',second='#827F79',third='#D9E6DC',display='SketchSerif',sans='SketchSans',cjk='SketchCJK',cjkdisplay='SketchCJKDisplay',weight=600,cjkweight=900),
 'glow': dict(paper='#FFF1D2',ink='#422532',accent='#F58ACB',second='#FFE63B',third='#D9653B',display='GlowDisplay',sans='GlowSans',cjk='GlowCJK',cjkdisplay='GlowCJKDisplay',weight=400,cjkweight=900),
 'echo': dict(paper='#F0F1ED',ink='#12141F',accent='#A8B9CB',second='#607E9A',third='#D7E1E8',display='EchoDisplay',sans='EchoSans',cjk='EchoCJK',cjkdisplay='EchoCJKDisplay',weight=500,cjkweight=300),
}
COPY = {
 'sketch': {
  'titles': [('A little structure. More ideas.','给想法，一点生长的结构。'),('More drafts reach the table.','让更多草稿，来到桌面。'),('Start with what people notice.','从大家注意到的地方开始。'),('Small notes. A shared collection.','小小纸片，汇成共同收藏。'),('Confidence has many beginnings.','信心，从不同起点生长。'),('Make room for making.','为动手尝试，留出空间。'),('Keep time for another draft.','为下一张草稿，留出时间。'),('Two rhythms of making.','创作，有两种节奏。'),('A practice takes shape.','一种练习，渐渐成形。'),('An idea has more than one side.','一个想法，不止一个侧面。'),('Every note finds a way.','让每张纸片，都有去向。'),('Choose a useful next experiment.','选一个值得尝试的新问题。'),('See what still needs a pass.','看看哪里，还需要再试。'),('Ready is a set of small checks.','准备就绪，来自逐项检查。'),('Keep the detail in view.','把重要细节，放在眼前。'),('Three ways to begin.','从三种方式开始。'),('Give the week a gentle shape.','让这一周，有轻盈的节奏。'),('When a draft meets a question.','当草稿，遇见一个问题。'),('Attention is a shared resource.','注意力，是共同的资源。'),('From a spark to a shared draft.','从一点灵感，到共享草稿。')],
  'stages':[('Notice','观察'),('Collect','收集'),('Try','试验'),('Share','分享')],
  'tasks':[('Look for a useful question.','找到值得追问的问题。'),('Keep a surprising fragment.','留下让人意外的片段。'),('Make one small version.','先做一个小小的版本。'),('Invite a clear response.','邀请一次清楚的反馈。')],
  'series':[('Rough drafts','初步草稿'),('Shared drafts','共享草稿')],
  'units':('Drafts','草稿数'), 'groups':[('Notes','观察笔记'),('Questions','待解问题'),('Fragments','灵感片段')],
  'rank':[('A clearer brief','更清楚的提问'),('More examples','更多具体例子'),('Time to try','动手试验时间'),('A quiet review','安静复看一遍')],
  'dimensions':[('Clarity','清楚'),('Usefulness','有用'),('Novelty','新意'),('Feasibility','可行'),('Care','细致')],
  'plans':[('Solo draft','独自起稿'),('Pair sketch','双人共创'),('Open studio','开放工作室')],
  'target':[('Questions framed','问题已明确'),('Drafts reviewed','草稿已复看'),('Credits recorded','出处已记录')],
  'sources':[('Observation','观察'),('Conversation','交流'),('Archive','旧档')],
  'routes':[('Try now','现在尝试'),('Explore more','继续探索')],
  'results':[('Keep','留下'),('Rework','再做一版')],
 },
 'glow': {
  'titles':[('A good day has four ingredients.','美好一天，有四种成分。'),('More people find their way in.','让更多人，走进现场。'),('What makes a warmer welcome?','怎样的欢迎，让人更自在？'),('Little moments add up.','小小瞬间，慢慢汇成回忆。'),('Comfort grows at its own pace.','自在感，有自己的节奏。'),('Leave time for a little joy.','给一点快乐，留下时间。'),('Save room for the unexpected.','给意外惊喜，留出余量。'),('Arrive once. Come back again.','来过一次，还想再来。'),('A community gathers slowly.','相聚，一点一点发生。'),('A good gathering has many sides.','好的相聚，不止一个侧面。'),('Many doors. One shared table.','从不同入口，来到同一张桌。'),('Choose the next little delight.','选一份值得尝试的小惊喜。'),('Every detail gets its moment.','让每个细节，都被照顾。'),('A warm welcome takes care.','好好欢迎，从逐项准备开始。'),('Keep the day easy to follow.','让当天安排，一目了然。'),('Find your kind of gathering.','找到适合你的相聚方式。'),('Let the day unfold.','让这一天，自然展开。'),('Make the next step feel easy.','让下一步，轻松一点。'),('A shared hour, well spent.','把共同的一小时，用得尽兴。'),('From an invitation to a memory.','从一份邀请，到一段回忆。')],
  'stages':[('Arrive','到场'),('Connect','相聚'),('Play','玩乐'),('Keep','留存')],
  'tasks':[('Make the first minute easy.','让最初一分钟轻松自在。'),('Offer a place at the table.','在桌边，为彼此留个位置。'),('Try something together.','一起，尝试一点新鲜事。'),('Take a small memory home.','带一份小小的记忆回家。')],
  'series':[('New guests','新来朋友'),('Return guests','再次到场')],
  'units':('Guests','到场人数'), 'groups':[('Conversations','交流时刻'),('Games','共同游戏'),('Keepsakes','手作留念')],
  'rank':[('A friendly host','亲切的引导'),('An easy activity','轻松的活动'),('A shared table','一起坐下来'),('Room to pause','停一停的空间')],
  'dimensions':[('Welcome','欢迎'),('Comfort','自在'),('Connection','联结'),('Play','趣味'),('Care','照顾')],
  'plans':[('A small table','小桌相聚'),('An open afternoon','开放午后'),('A lively evening','热闹夜晚')],
  'target':[('Hosts briefed','主持已准备'),('Spaces checked','场地已检查'),('Guests informed','来宾已告知')],
  'sources':[('Friends','朋友邀请'),('Neighbourhood','社区消息'),('Open invitation','公开邀请')],
  'routes':[('Join a table','加入一桌'),('Join a game','加入游戏')],
  'results':[('Stay connected','继续联系'),('Just enjoy today','享受当下')],
 },
 'echo': {
  'titles':[('Four movements. One intention.','四个乐章，同一份心意。'),('A little more space for listening.','为聆听，多留一点空间。'),('Listen for the strongest signal.','听见，最清楚的信号。'),('Fragments form a shared memory.','片段，汇成共同的记忆。'),('Hear the change, one part at a time.','逐项听见，变化的发生。'),('Attention needs a rhythm.','注意力，需要自己的节奏。'),('Leave capacity for a response.','为回应，留下余量。'),('Two voices over time.','让两种声音，随时间展开。'),('Resonance grows through practice.','回响，在练习中慢慢生长。'),('Read the whole listening space.','读懂，聆听空间的各个侧面。'),('Every voice has a path.','让每一种声音，都有去向。'),('Choose where to listen next.','选择，下一个聆听方向。'),('Care becomes visible in detail.','照顾，藏在具体细节里。'),('A space is ready when it listens.','准备好的空间，也会聆听。'),('A quiet record of the essentials.','安静地，记录重要细节。'),('Choose the scale of the room.','选择，适合这次交流的尺度。'),('Compose the time between voices.','安排声音之间的时间。'),('A question can open another path.','一个问题，打开另一条路。'),('Make space for every part.','为每一部分，留出空间。'),('From hearing to carrying it forward.','从听见，到继续传递。')],
  'stages':[('Listen','聆听'),('Tune','调谐'),('Connect','联结'),('Resonate','回响')],
  'tasks':[('Notice what is already here.','注意，已经在这里的声音。'),('Remove a little interference.','移开，一点点多余的干扰。'),('Allow one voice to meet another.','让一种声音，遇见另一种。'),('Leave a trace worth returning to.','留下一点，值得重访的回响。')],
  'series':[('First visits','初次到场'),('Return visits','再次聆听')],
  'units':('Visits','到场次数'), 'groups':[('Voices','声音记录'),('Questions','交流提问'),('Reflections','回望片段')],
  'rank':[('A clear invitation','清楚的邀请'),('A quieter space','安静的空间'),('Time to respond','回应的时间'),('An open ending','开放的结尾')],
  'dimensions':[('Clarity','清晰'),('Presence','在场'),('Ease','松弛'),('Connection','联结'),('Memory','记忆')],
  'plans':[('One conversation','一场对话'),('A listening circle','围坐聆听'),('An open room','开放空间')],
  'target':[('Sound checked','声音已检查'),('Access confirmed','进入路径已确认'),('Notes shared','记录已分享')],
  'sources':[('Invitation','定向邀请'),('Community','社群'),('Discovery','主动发现')],
  'routes':[('Conversation','交谈'),('Quiet listening','安静聆听')],
  'results':[('Carry forward','继续传递'),('Reflect privately','独自回望')],
 },
}

COLUMNS=[18,26,32,44]; RANKING=[42,34,26,18]; PICTORIAL=[24,20,16]
BEFORE=[42,56,70]; AFTER=[58,72,84]
STACKED=[[20,45,35],[30,40,30],[40,35,25]]
LINE_A=[12,18,22,30,35,42]; LINE_B=[8,12,17,21,26,32]
AREA=[12,15,14,24,29,32,38,46]
RADAR_A=[56,68,52,74,60]; RADAR_B=[82,78,76,86,80]
SANKEY_A=[[35,15],[15,15],[10,10]]; SANKEY_B=[[45,15],[25,15]]
SCATTER=[(3,30),(5,56),(8,42),(10,76),(12,62),(15,88),(18,70),(21,82)]
HEAT=[[70,85,55,95,65,80],[90,60,45,85,75,50],[65,80,70,90,55,75],[50,75,60,85,40,70]]
TARGETS=[(72,80),(88,85),(94,95)]; SHARES=[40,35,25]; FUNNEL=[200,150,120,90]
KINDS=['four-cards','columns','ranking','pictorial','grouped','stacked','waterfall','line','area','radar','sankey','scatter','heatmap','target','data-table','comparison','timeline','branch','donut','funnel']

def fmt(n): return f'{n:g}'
def tr(lang,en,zh): return zh if lang.startswith('zh') else en
def get_slides(lang='en'):
 lang='zh-CN' if lang.startswith('zh') else 'en'
 c=CONFIG[THEME];copy=COPY[THEME];z=lang.startswith('zh');t=lambda p:p[1 if z else 0]
 slides=[]
 for index,kind in enumerate(KINDS):
  dark=(index in {2,6,8,12,18}) if THEME!='echo' else index not in {0,3,7,10,14,17}
  bg=c['ink'] if dark else c['paper']; fg=c['paper'] if dark else c['ink']
  if THEME=='glow' and not dark and index in {0,4,9,15,19}: bg=c['second'] if index%2==0 else c['accent']
  if THEME=='sketch' and not dark and index in {4,9,15,19}:bg=c['accent']
  accent=c['accent'] if dark or THEME!='echo' else '#293E53'
  colors=[accent,c['second'],c['third']]
  if THEME=='sketch' and not dark:colors=[c['ink'],c['second'],c['accent']]
  colors=[c['ink'] if color==bg else color for color in colors]
  if THEME=='glow' and kind in {'line','radar'} and not dark:colors=[c['ink'],c['third'],c['second']]
  stroke=fg;title=t(copy['titles'][index]);p=[];data={};sub=''
  def text(x,y,value,size=30,color=None,anchor='start',display=False,extra=''):
   cls='x30-display' if display else 'x30-label'
   return f'<text x="{fmt(x)}" y="{fmt(y)}" font-size="{size}" fill="{color or fg}" text-anchor="{anchor}" class="{cls}" {extra}>{escape(str(value))}</text>'
  def rule(x,y,x2,y2,opacity=.22,color=None,dash=None):
   return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color or fg}" stroke-width="1.5" opacity="{opacity}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
  def rect(x,y,w,h,fill=None,outline=False,rx=0):
   return f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" rx="{rx}" fill="{fill or accent}"'+(f' stroke="{fg}" stroke-width="{2 if THEME=="glow" else 1.5}"' if outline else '')+'/>'
  def circle(x,y,r,fill,outline=False):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"'+(f' stroke="{fg}" stroke-width="1.5"' if outline else '')+'/>'
  def motion(value,mode='fade',step=0):return f'<g data-chart-motion="{mode}" data-chart-step="{step}">{value}</g>'
  def labelpair(x,y,a,b):return text(x,y,a,30)+text(x,y+49,b,51,display=True)
  def scalegrid(left,top,width,height,maxval,ticks,unit):
   out=[text(left,top-26,unit,26)]
   for v in ticks:
    y=top+height*(1-v/maxval);out += [rule(left,y,left+width,y,.42 if v==0 else .14),text(left-20,y+10,v,26,anchor='end')]
   return out
  def legend(x,y,label,color):return rect(x,y-20,20,20,color)+text(x+32,y,label,26)
  def note(x,y,n,head,body,w=380,h=520):
   fill=c['paper'];ink=c['ink'];edge=rect(x+7,y+7,w,h,c['ink']) if THEME!='echo' else ''
   shape=rect(x,y,w,h,fill,True,12 if THEME=='glow' else 1)
   if THEME=='sketch':shape+=rule(x+24,y+22,x+w-24,y+22,.6,c['ink'])
   if THEME=='echo':shape=rect(x,y,w,h,'none',True,4)
   ncolor=ink if THEME!='echo' else fg
   lines=textwrap.wrap(body,11 if z else 23)
   if z:
    for j in range(1,len(lines)):
     while lines[j] and lines[j][0] in '。，、；：！？':lines[j-1]+=lines[j][0];lines[j]=lines[j][1:]
    lines=[line for line in lines if line]
   return edge+shape+text(x+28,y+105,n,78,ncolor,display=True)+text(x+28,y+215,head,43,ncolor,display=True)+''.join(text(x+28,y+310+j*44,line,27,ncolor) for j,line in enumerate(lines))
  if kind=='four-cards':
   sub=tr(lang,'A separate intention for each part of the process.','每一个环节，都有自己的用意。')
   for i,(stage,task) in enumerate(zip(copy['stages'],copy['tasks'])):
    x=i*425;body=t(task);p.append(motion(note(x,20,str(i+1).zfill(2),t(stage),body), 'fade',i))
   data={'stages':[t(x) for x in copy['stages']]}
  elif kind=='columns':
   sub=tr(lang,'Four independent sessions. Each value counts only that session.','四场独立记录，每个数值只属于当场。');data={'values':COLUMNS,'axis':[0,50],'cumulative':False}
   p+=scalegrid(90,70,1510,430,50,[0,10,20,30,40,50],t(copy['units']))
   for i,v in enumerate(COLUMNS):
    x=235+i*385;h=v*8.6;p += [motion(rect(x,500-h,180,h,colors[i%3],THEME=='sketch',10 if THEME=='glow' else 0),'grow-y',i),motion(text(x+90,480-h,v,60,anchor='middle',display=True),'fade',i+1),text(x+90,555,tr(lang,f'Session {i+1}',f'第{i+1}场'),29,anchor='middle')]
  elif kind=='ranking':
   sub=tr(lang,'120 responses, each assigned to one main preference.','120份反馈，每份只归入一个主要偏好。');data={'values':RANKING,'sum':120,'axis':[0,50]}
   for v in [0,10,20,30,40,50]:p +=[rule(400+v*22,45,400+v*22,500,.13),text(400+v*22,555,v,26,anchor='middle')]
   p.append(text(400,38,tr(lang,'Responses','反馈份数'),26))
   for i,v in enumerate(RANKING):
    y=85+i*115;p +=[text(0,y+33,t(copy['rank'][i]),32),motion(rect(400,y,22*v,48,colors[i%3],False,24 if THEME=='glow' else 0),'grow-x',i),text(424+22*v,y+36,v,42,display=True)]
  elif kind=='pictorial':
   sub=tr(lang,'Every mark stands for four moments, never for quality.','每枚标记代表四份记录，不表示质量。');data={'values':PICTORIAL,'per_symbol':4,'symbols':15,'total':60}
   p +=[text(8,238,60,220,display=True),text(8,310,tr(lang,'records kept','份记录被留下'),34),rule(0,357,350,357),text(8,412,tr(lang,'One mark = four records','每枚标记 = 四份记录'),26)]
   for row,v in enumerate(PICTORIAL):
    y=35+row*170;p.append(text(460,y+20,t(copy['groups'][row]),31))
    for i in range(v//4):
     x=480+i*145
     if THEME=='sketch':shape=rect(x,y+48,68,88,c['paper'],True)+rule(x+13,y+74,x+53,y+74,.6)+rule(x+13,y+93,x+49,y+93,.4)
     elif THEME=='glow':shape=circle(x+35,y+90,41,colors[row],True)+text(x+35,y+102,'4',32,c['ink'],'middle')
     else:shape=f'<path d="M{x+34} {y+43}Q{x+80} {y+97} {x+34} {y+137}Q{x-12} {y+97} {x+34} {y+43}Z" fill="{colors[row]}" stroke="{fg}" stroke-width="1.4"/>'
     p.append(motion(shape,'pop',row*3+i))
    p.append(text(1590,y+110,v,60,anchor='end',display=True))
  elif kind=='grouped':
   sub=tr(lang,'The same three groups, on a shared 0–100 confidence scale.','同样三组参与者，共用0至100分的信心量表。');data={'before':BEFORE,'after':AFTER,'axis':[0,100],'causality':False}
   p +=[legend(20,30,tr(lang,'Before','开始前'),colors[1]),legend(290,30,tr(lang,'After','结束后'),colors[0])]
   for i,(a,b) in enumerate(zip(BEFORE,AFTER)):
    left=i*570+64;p.append(text(left+210,90,tr(lang,f'Group {i+1}',f'第{i+1}组'),37,anchor='middle',display=True))
    for v in [0,50,100]:y=490-v*3.2;p +=[rule(left,y,left+420,y,.22),text(left-13,y+9,v,24,anchor='end')]
    for j,v in enumerate([a,b]):
     x=left+80+j*170;p +=[motion(rect(x,490-v*3.2,100,v*3.2,colors[1-j],THEME=='sketch',8 if THEME=='glow' else 0),'grow-y',i*2+j),text(x+50,469-v*3.2,v,43,anchor='middle',display=True)]
   p.append(text(1660,580,tr(lang,'Confidence score / 100','信心评分／100分'),26,anchor='end'))
  elif kind=='stacked':
   sub=tr(lang,'Three 60-minute sessions, each divided by its own total time.','三场各60分钟的活动，分别按自身总时长计算占比。');data={'values':STACKED,'totals':[100]*3,'duration_minutes':60}
   labels=[tr(lang,'Listen','聆听'),tr(lang,'Make together','共同参与'),tr(lang,'Reflect','回望')]
   for j in range(3):p.append(legend(330+j*390,40,labels[j],colors[j]))
   for row,vals in enumerate(STACKED):
    y=95+row*140;x=280;p.append(text(0,y+49,tr(lang,f'Round {row+1}',f'第{row+1}轮'),40,display=True))
    for j,v in enumerate(vals):
     w=v*13;p +=[motion(rect(x,y,w,72,colors[j],True,0),'wipe-x',row),text(x+w/2,y+49,f'{v}%',34,c['paper'] if colors[j]==c['ink'] else c['ink'],'middle')];x+=w
   for v in [0,25,50,75,100]:p.append(text(280+v*13,565,f'{v}%',26,anchor='middle'))
  elif kind=='waterfall':
   sub=tr(lang,'100 + 20 − 30 − 15 = 75 staff-hours still available.','100 + 20 − 30 − 15 = 75人时，仍可用于后续。');data={'initial':100,'changes':[20,-30,-15],'remaining':75,'axis':[0,140]}
   spans=[(0,100),(100,120),(120,90),(90,75),(0,75)];values=[100,20,-30,-15,75];labs=[('Planned','原有'),('Added','追加'),('Prepare','准备'),('Support','支持'),('Available','剩余')]
   p+=scalegrid(95,60,1515,440,140,[0,35,70,105,140],tr(lang,'Staff-hours','人时'))
   for i,((a,b),v) in enumerate(zip(spans,values)):
    x=190+i*300;y=500-max(a,b)*440/140;h=abs(b-a)*440/140;p +=[motion(rect(x,y,140,h,colors[i%3]),'grow-y',i),text(x+70,y-22,('+' if i==1 else '')+str(v),45,anchor='middle',display=True),text(x+70,555,t(labs[i]),29,anchor='middle')]
    if i<4:p.append(rule(x+140,500-b*440/140,x+300,500-b*440/140,.5,dash='6 7'))
  elif kind=='line':
   sub=tr(lang,'Weekly counts follow two different paths; neither line is cumulative.','每周分别计数，两条线都不是累计值。');data={'series':[LINE_A,LINE_B],'axis':[0,50]}
   p+=scalegrid(95,55,1300,445,50,[0,10,20,30,40,50],t(copy['units']))
   for j,vs in enumerate([LINE_A,LINE_B]):
    pts=[(95+i*260,500-v*8.9) for i,v in enumerate(vs)];path='M'+' L'.join(f'{x},{y}' for x,y in pts);col=colors[j];dash=' stroke-dasharray="9 7"' if j else ''
    p.append(f'<path d="{path}" fill="none" stroke="{col}" stroke-width="4"{dash} data-chart-motion="{"wipe-x" if j else "draw"}" data-chart-step="{j}"/>')
    for i,(x,y) in enumerate(pts):p.append(motion(circle(x,y,7,col,True),'pop',i))
    p.append(text(1430,pts[-1][1]+8,t(copy['series'][j])+(': ' if not z else '：')+str(vs[-1]),26))
   for i in range(6):p.append(text(95+i*260,555,tr(lang,f'W{i+1}',f'第{i+1}周'),28,anchor='middle'))
  elif kind=='area':
   sub=tr(lang,'A count of contributions received in each week, not a running total.','每周收到的贡献分别记录，不计算累计总量。');data={'values':AREA,'axis':[0,50],'cumulative':False}
   p +=[text(0,75,tr(lang,'In week eight','第八周'),30),text(0,285,46,220,display=True),text(8,355,tr(lang,'contributions','份贡献'),35),rule(0,400,380,400,.4),text(8,465,tr(lang,'A practice worth returning to.','一种值得重访的练习。'),27)]
   p+=scalegrid(560,55,1060,445,50,[0,10,20,30,40,50],tr(lang,'Contributions / week','每周贡献份数'))
   pts=[(560+i*1060/7,500-v*8.9) for i,v in enumerate(AREA)];d='M'+' L'.join(f'{x},{y}' for x,y in pts)
   p.append(motion(f'<path d="{d}L1620,500H560Z" fill="{accent}" fill-opacity=".28"/>','wipe-x'))
   p.append(f'<path d="{d}" fill="none" stroke="{accent}" stroke-width="4" data-chart-motion="draw" data-chart-step="1"/>')
   for i,(x,y) in enumerate(pts):p +=[text(x,555,str(i+1),26,anchor='middle'),motion(circle(x,y,5,accent),'pop',i)]
  elif kind=='radar':
   sub=tr(lang,'Five separate scores, read with the table rather than by polygon area.','五项独立评分，结合数值表阅读，不按面积求总分。');data={'before':RADAR_A,'after':RADAR_B,'axis':[0,100]}
   p +=[text(0,35,tr(lang,'Dimension','维度'),27),text(480,35,tr(lang,'First','初次'),27,anchor='middle'),text(680,35,tr(lang,'Later','后次'),27,anchor='middle'),rule(430,56,530,56,.9,colors[0],'8 6'),rule(630,56,730,56,.9,colors[1])]
   for i,(a,b) in enumerate(zip(RADAR_A,RADAR_B)):
    y=115+i*94;p +=[rule(0,y+29,780,y+29),text(0,y,t(copy['dimensions'][i]),35),text(480,y,a,46,anchor='middle',display=True),text(680,y,b,46,anchor='middle',display=True)]
   cx,cy,r=1230,300,205
   def coords(vs):return [(cx+math.cos(-math.pi/2+i*math.tau/5)*r*v/100,cy+math.sin(-math.pi/2+i*math.tau/5)*r*v/100) for i,v in enumerate(vs)]
   for v in [25,50,75,100]:p.append(f'<polygon points="'+ ' '.join(f'{x},{y}' for x,y in coords([v]*5))+f'" fill="none" stroke="{fg}" opacity=".2"/>')
   for i,(x,y) in enumerate(coords([100]*5)):
    p.append(rule(cx,cy,x,y,.2));lx=cx+(x-cx)*1.24;ly=cy+(y-cy)*1.24;p.append(text(lx,ly+8,t(copy['dimensions'][i]),28,anchor='middle'))
   for j,vs in enumerate([RADAR_A,RADAR_B]):
    pts=coords(vs);d='M'+' L'.join(f'{x},{y}' for x,y in pts)+'Z';p.append(f'<path d="{d}" fill="none" stroke="{colors[j]}" stroke-width="3"'+(' stroke-dasharray="8 7"' if j==0 else '')+f' data-chart-motion="{"wipe-x" if j==0 else "draw"}" data-chart-step="{j}"/>')
   p.append(text(cx,592,tr(lang,'Score / 100','评分／100分'),25,anchor='middle'))
  elif kind=='sankey':
   sub=tr(lang,'100 contributions, each taking one main route. Every flow is counted.','100份贡献，各走一条主要路径，每条流向都保留数量。');data={'layers':[[50,30,20],[60,40],[70,30]],'matrices':[SANKEY_A,SANKEY_B],'pixels_per_unit':4}
   xs=[0,705,1410];width=250;ys=[[75,300,445],[70,360],[70,390]];vs=data['layers'];labels=[copy['sources'],copy['routes'],copy['results']]
   for layer,matrix in enumerate([SANKEY_A,SANKEY_B]):
    src=[0]*len(matrix);dst=[0]*len(matrix[0])
    for i,row in enumerate(matrix):
     for j,v in enumerate(row):
      x1=xs[layer]+width;x2=xs[layer+1];y1=ys[layer][i]+src[i]*4;y2=ys[layer+1][j]+dst[j]*4;h=v*4;mid=(x1+x2)/2
      d=f'M{x1},{y1}C{mid},{y1} {mid},{y2} {x2},{y2}V{y2+h}C{mid},{y2+h} {mid},{y1+h} {x1},{y1+h}Z'
      p.append(motion(f'<path d="{d}" fill="{colors[i%3]}" opacity=".5"/>','wipe-x',layer*3+i));p.append(text(mid,(y1+y2+h)/2+9,v,25,extra=f'stroke="{bg}" stroke-width="7" paint-order="stroke"'));src[i]+=v;dst[j]+=v
   for layer in range(3):
    for i,v in enumerate(vs[layer]):
     y=ys[layer][i];p.append(motion(rect(xs[layer],y,width,v*4,c['paper'] if THEME!='echo' else '#293E53',True),'fade',layer*2))
     col=c['ink'] if THEME!='echo' else c['paper'];lines=textwrap.wrap(t(labels[layer][i]),7 if z else 13)
     first=y+v*2+8-(len(lines)-1)*13
     p +=[text(xs[layer]+16,first+j*26,line,22,col) for j,line in enumerate(lines)]
     p.append(text(xs[layer]+232,y+v*2+13,v,37,col,'end',True))
   p.append(text(1660,600,tr(lang,'Contributions / count','贡献份数'),24,anchor='end'))
  elif kind=='scatter':
   sub=tr(lang,'Estimated effort and a 0–100 usefulness score for eight possibilities.','八个备选方向：预计投入小时数，与0至100分的有用性评分。');data={'points':SCATTER,'x_axis':[0,24],'y_axis':[0,100]}
   p+=scalegrid(120,55,1450,440,100,[0,25,50,75,100],tr(lang,'Usefulness / 100','有用性／100分'))
   for i,(x,v) in enumerate(SCATTER):
    px=120+x/24*1450;py=495-v*4.4;p +=[motion(circle(px,py,9,colors[i%3],True),'pop',i),text(px+17,py-18,chr(65+i),29)]
   for v in [0,4,8,12,16,20,24]:p.append(text(120+v/24*1450,548,v,26,anchor='middle'))
   p.append(text(1570,600,tr(lang,'Estimated effort / hours','预计投入／小时'),26,anchor='end'))
  elif kind=='heatmap':
   sub=tr(lang,'Four checks across six versions. Every score stays visible.','六个版本、四项检查，每格保留准确数值。');data={'scores':HEAT,'axis':[0,100],'bands':[[0,49],[50,74],[75,100]]}
   for col in range(6):
    x=305+col*217;p +=[rect(x,5,194,495,c['paper'],THEME!='echo',9 if THEME=='glow' else 0),text(x+97,55,tr(lang,f'Version {col+1}',f'版本{col+1}'),27,c['ink'],'middle')]
   for row in range(4):
    y=85+row*98;p.append(text(260,y+54,t(copy['stages'][row]),33,anchor='end'))
    for col in range(6):
     v=HEAT[row][col];color=[c['paper'],c['second'],accent][0 if v<50 else 1 if v<75 else 2];x=316+col*217
     p +=[motion(rect(x,y,172,82,color,True),'fade',row),text(x+86,y+55,v,41,c['ink'],'middle',True)]
   for j,(label,color) in enumerate(zip(['0–49','50–74','75–100'],[c['paper'],c['second'],accent])):p.append(legend(450+j*350,580,label,color))
  elif kind=='target':
   sub=tr(lang,'A separate threshold for each check; averages cannot replace one.','每项都有独立门槛，平均值不能代替单项检查。');data={'actual_target':TARGETS,'difference_pp':[a-b for a,b in TARGETS],'axis':[0,100]}
   for i,(v,g) in enumerate(TARGETS):
    x=i*570;p +=[text(x,55,t(copy['target'][i]),34),text(x,220,str(v),160,display=True),text(x+250,215,'%',70,display=True),rule(x,280,x+500,280,.3)]
    p +=[f'<g opacity=".16">{rect(x,345,500,24,fg)}</g>',motion(rect(x,345,5*v,24,colors[i]),'grow-x',i),rule(x+5*g,326,x+5*g,390,.9),text(x+500,427,tr(lang,f'Target {g}%',f'目标 {g}%'),28,anchor='end')]
    delta=v-g;message=tr(lang,f'{delta:+d} percentage points',f'{"高于" if delta>=0 else "低于"}目标 {abs(delta)} 个百分点');p.append(text(x,510,message,28))
  elif kind=='data-table':
   sub=tr(lang,'Task counts: planned, completed and still open. Every row reconciles.','任务数：计划、已完成、待完成，每行都能核对。');data={'unit':'tasks','planned':[30,24,18,28],'done':[24,21,15,20],'open':[6,3,3,8],'totals':[100,80,20]}
   xs=[24,790,1110,1450];heads=[tr(lang,'Workstream','工作项'),tr(lang,'Planned','计划'),tr(lang,'Complete','已完成'),tr(lang,'Open','待完成')]
   for j,h in enumerate(heads):p.append(text(xs[j],55,h,31,anchor='start' if j==0 else 'middle'))
   p.append(rule(0,86,1660,86,.65))
   for i in range(5):
    y=160+i*91;vals=[data[k][i] for k in ['planned','done','open']] if i<4 else data['totals'];lab=t(copy['stages'][i]) if i<4 else tr(lang,'Total','总计')
    if i==4:p.append(rect(0,y-57,1660,84,c['paper'] if dark else (c['accent'] if THEME!='echo' else '#D7E1E8'),False,6))
    col=c['ink'] if i==4 else fg;p.append(text(24,y,lab,35,col,display=True))
    for j,v in enumerate(vals):p.append(text(xs[j+1],y,v,46,col,'middle',True))
    if i<4:p.append(rule(0,y+25,1660,y+25))
  elif kind=='comparison':
   sub=tr(lang,'Compare formats on practical constraints, not on an invented overall score.','比较具体条件，不为不同方案拼出虚构的综合分。');data={'capacity':[8,20,40],'duration_minutes':[60,90,120],'hosts':[1,2,4]}
   xcols=[615,1035,1455];rows=[tr(lang,'People','人数'),tr(lang,'Minutes','分钟'),tr(lang,'Hosts','主持人数')]
   p.append(rect(0,0,1660,108,c['paper'] if dark else (c['accent'] if THEME!='echo' else '#D7E1E8')))
   p.append(text(24,69,tr(lang,'Format','方案'),31,c['ink']))
   for j,x in enumerate(xcols):p.append(text(x,69,t(copy['plans'][j]),34,c['ink'],'middle',True))
   for i,label in enumerate(rows):
    y=205+i*130;p +=[text(24,y,label,34),rule(0,y+42,1660,y+42,.28)]
    for j,x in enumerate(xcols):p.append(text(x,y,data[['capacity','duration_minutes','hosts'][i]][j],67,anchor='middle',display=True))
   for x in [400,825,1245]:p.append(rule(x,0,x,507,.22))
  elif kind=='timeline':
   sub=tr(lang,'Four stages, one clear hand-off at each boundary.','四个阶段，每次交接都有明确的结果。')
   durations=[1,2,2,1] if THEME=='sketch' else ([10,20,20,10] if THEME=='glow' else [15,20,15,10]);unit=tr(lang,'days','天') if THEME=='sketch' else tr(lang,'minutes','分钟');data={'stages':4,'durations':durations,'unit':unit,'total_duration':sum(durations)}
   p.append(rule(80,265,1580,265,.65))
   outputs={'sketch':[('A shared question','共同的问题'),('A rough version','粗略的版本'),('A useful response','有用的回应'),('A next step','下一步行动')],'glow':[('A warm hello','亲切的问候'),('A new connection','新的联结'),('A shared delight','共同的快乐'),('A small memory','小小的回忆')],'echo':[('A quiet arrival','安静地到场'),('A clear signal','清楚的信号'),('A shared response','共同的回应'),('A lasting thought','留下的想法')]}[THEME]
   for i in range(4):
    duration=str(durations[i])+(' ' if not z else '')+(('day' if durations[i]==1 else 'days') if THEME=='sketch' and not z else unit)
    x=80+i*500;p.append(motion(circle(x,265,22,colors[i%3],True),'pop',i));p +=[text(x,85,t(copy['stages'][i]),49,anchor='middle' if i else 'start',display=True),text(x,160,duration,30,anchor='middle' if i else 'start')]
    lx=max(0,x-160);p +=[text(lx,390,t(outputs[i]),32),text(lx,465,tr(lang,f'Step {i+1}',f'第{i+1}阶段'),26)]
  elif kind=='branch':
   sub=tr(lang,'A decision route, not a quantitative flow. Follow the labels.','这是判断路径，不是流量图，请沿文字阅读。');data={'nodes':6,'quantitative':False,'branches':['yes','no']}
   def box(x,y,w,h,label,fill=None):return rect(x,y,w,h,fill or c['paper'],True,18 if THEME=='glow' else 2)+text(x+w/2,y+h/2+13,label,31,c['paper'] if fill=='#293E53' else c['ink'],'middle')
   start=tr(lang,'Bring one question','带来一个问题');dec=tr(lang,'Clear enough to try?','足够清楚，可以试试？')
   marker=f'x30-{THEME}-{lang}-arrow';p.append(f'<defs><marker id="{marker}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M1 1L9 5L1 9" fill="none" stroke="{fg}" stroke-width="1.2"/></marker></defs>')
   def arrow(line):return line.replace('/>',f' marker-end="url(#{marker})"/>')
   p +=[box(0,210,360,125,start),box(590,210,500,125,dec),arrow(rule(360,272,590,272,.8)),arrow(rule(1090,272,1280,130,.8)),arrow(rule(1090,272,1280,445,.8))]
   p +=[text(1155,168,tr(lang,'Yes','是'),27),text(1155,403,tr(lang,'Not yet','还没'),27),box(1280,62,370,130,tr(lang,'Try a small version','做一个小版本'),accent),box(1280,390,370,130,tr(lang,'Ask one more question','再问一个问题'))]
   p +=[rule(1465,520,1465,575,.6),rule(1465,575,840,575,.6),arrow(rule(840,575,840,335,.6)),text(1090,564,tr(lang,'Return with a clearer brief','带着更清楚的提问回来'),26,anchor='middle')]
  elif kind=='donut':
   sub=tr(lang,'One 60-minute session, divided into three parts that sum to 100%.','一场60分钟的活动，三部分合计100%。');data={'shares':SHARES,'minutes':[24,21,15],'total':60}
   cx,cy,r=380,290,210;circ=math.tau*r;offset=0
   p.append(circle(cx,cy,r,'none'))
   for j,v in enumerate(SHARES):
    p.append(motion(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{colors[j]}" stroke-width="76" stroke-dasharray="{circ*v/100} {circ*(1-v/100)}" stroke-dashoffset="{-circ*offset/100}" transform="rotate(-90 {cx} {cy})"/>','fade',j));offset+=v
   p +=[text(cx,cy+12,'60',132,anchor='middle',display=True),text(cx,cy+72,tr(lang,'minutes together','分钟，在一起'),29,anchor='middle')]
   labs=[('Listen','聆听'),('Participate','参与'),('Reflect','回望')]
   for i,v in enumerate(SHARES):
    y=80+i*170;p +=[rect(880,y-10,24,24,colors[i]),text(930,y+15,t(labs[i]),38),text(1640,y+20,f'{v}%',65,anchor='end',display=True),text(930,y+71,tr(lang,f'{data["minutes"][i]} minutes',f'{data["minutes"][i]}分钟'),27),rule(880,y+112,1650,y+112)]
  elif kind=='funnel':
   sub=tr(lang,'One cohort at four stages. Width encodes the count at each stage.','同一批对象的四个阶段，每一行宽度准确对应数量。');data={'stages':FUNNEL,'retained_percent':45,'stage_rates':[75,80,75]}
   labels=[('Captured','捕捉灵感'),('Framed','明确问题'),('Tried','动手尝试'),('Shared','分享草稿')] if THEME=='sketch' else [('Invited','收到邀请'),('Responded','作出回应'),('Participated','实际参与'),('Continued','继续同行')]
   for i,v in enumerate(FUNNEL):
    y=10+i*138;w=v*4.8;x=480+(960-w)/2;p +=[text(0,y+62,t(labels[i]),39),motion(rect(x,y,w,92,colors[i%3],True,46 if THEME=='glow' else 0),'grow-x',i),text(x+w+35,y+64,v,54,display=True)]
   p.append(text(1660,587,tr(lang,'90 / 200 = 45% of the original cohort','90 / 200 = 最初对象的45%'),29,anchor='end'))
  body=''.join(p)
  title_attr=escape(title,quote=True);metadata=escape(json.dumps(data,ensure_ascii=False,separators=(',',':')),quote=True)
  slides.append(f'<section class="slide x30 x30-{THEME} chart-{kind} {"x30-dark" if dark else ""}" data-layout-id="{THEME}-{kind}" data-title="{title_attr}" data-tone="{"dark" if dark else "light"}" data-chart-kind="{kind}" data-chart-values="{metadata}" style="--x30-bg:{bg};--x30-fg:{fg};--x30-accent:{accent}"><header class="x30-heading"><h2 class="reveal">{escape(title)}</h2><p class="reveal">{escape(sub)}</p></header><div class="x30-content" data-chart-container><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1680 610" role="img" aria-label="{title_attr}" data-information-visual><title>{escape(title)}</title>{body}</svg></div></section>')
 return slides

def get_css():
 c=CONFIG[THEME]
 return f'''/* EXPANSION30 START — {THEME.upper()} data compositions only. */
.slide.x30{{background:var(--x30-bg);color:var(--x30-fg);font-synthesis:none}}
.slide.x30 .x30-heading{{position:absolute;left:120px;right:120px;top:80px}}
.slide.x30 .x30-heading h2{{position:static;font-family:{c['display']},serif;font-weight:{c['weight']};font-size:92px;line-height:1.12;letter-spacing:-2px;margin:0;color:var(--x30-fg)}}
.slide.x30 .x30-heading p{{font:400 27px/1.5 {c['sans']},sans-serif;letter-spacing:0;margin:24px 0 0;color:var(--x30-fg);opacity:.78}}
.slide.x30 .x30-content{{position:absolute;left:120px;top:350px;width:1680px;height:610px}}
.slide.x30 .x30-content>svg{{display:block;width:100%;height:100%;overflow:visible}}
.slide.x30 svg .x30-label{{font-family:{c['sans']},sans-serif;font-weight:400;letter-spacing:0}}
.slide.x30 svg .x30-display{{font-family:{c['display']},serif;font-weight:{c['weight']};letter-spacing:-1px}}
.slide.x30 [data-chart-motion]{{transform-box:view-box}}
html:lang(zh) .slide.x30 .x30-heading h2{{font-family:{c['cjkdisplay']},serif;font-size:74px;font-weight:{c['cjkweight']};line-height:1.25;letter-spacing:0;font-style:normal}}
html:lang(zh) .slide.x30 .x30-heading p{{font-family:{c['cjk']},sans-serif;font-size:26px;letter-spacing:0}}
html:lang(zh) .slide.x30 svg .x30-label{{font-family:{c['cjk']},{c['sans']},sans-serif;font-weight:400;letter-spacing:0}}
html:lang(zh) .slide.x30 svg .x30-display{{font-family:{c['display']},{c['cjk']},serif;font-weight:{c['weight']};letter-spacing:0}}
/* EXPANSION30 END */
'''

def validate_data():
 assert sum(COLUMNS)==sum(RANKING)==120
 assert sum(PICTORIAL)==60 and all(v%4==0 for v in PICTORIAL)
 assert all(sum(row)==100 for row in STACKED)
 assert 100+20-30-15==75
 assert all(0<=v<=50 for v in LINE_A+LINE_B+AREA)
 assert all(0<=v<=100 for v in RADAR_A+RADAR_B)
 assert [sum(r) for r in SANKEY_A]==[50,30,20]
 assert [sum(r[j] for r in SANKEY_A) for j in range(2)]==[60,40]
 assert [sum(r) for r in SANKEY_B]==[60,40]
 assert [sum(r[j] for r in SANKEY_B) for j in range(2)]==[70,30]
 assert all(0<=x<=24 and 0<=y<=100 for x,y in SCATTER)
 assert len(HEAT)==4 and all(len(r)==6 for r in HEAT) and all(0<=v<=100 for r in HEAT for v in r)
 assert [a-b for a,b in TARGETS]==[-8,3,-1]
 assert sum([30,24,18,28])==100 and sum([24,21,15,20])==80
 assert sum(SHARES)==100 and [v*.6 for v in SHARES]==[24,21,15]
 assert FUNNEL[-1]/FUNNEL[0]*100==45
 assert [FUNNEL[i+1]/FUNNEL[i]*100 for i in range(3)]==[75,80,75]
 for lang in ['en','zh-CN']:
  pages=get_slides(lang);assert len(pages)==20
  assert all('data-information-visual' in p for p in pages)
 return {'passed':True,'theme':THEME,'new_pages_per_language':20,'chart_kinds':KINDS,'sankey_total':100,'sankey_flow_count':10,'provenance':'Original illustrative local data; replace with user data before factual use.'}

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--lang',choices=['en','zh-CN'],default='en');parser.add_argument('--output',type=Path);parser.add_argument('--validate',action='store_true');args=parser.parse_args()
 result=validate_data()
 if args.output:
  if args.output.exists():raise SystemExit('Refusing to overwrite an existing fragment.')
  args.output.write_text('\n'.join(get_slides(args.lang)))
 print(json.dumps(result,ensure_ascii=False,indent=2))
