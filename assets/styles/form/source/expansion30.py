"""Twenty bilingual, regenerable information layouts. Data are authored examples.
Run validate_data() after editing values. get_slides(lang) renders final SVG geometry;
metadata describes the data, not a browser-side chart engine.
"""
from html import escape
from math import sin,cos,pi
import json
CONFIG = {'name': 'FORM', 'zh': '成形', 'bg': '#dcdbd5', 'ink': '#0755bb', 'accent': '#0755bb', 'soft': '#91acd0', 'muted': '#c7c8c4', 'paper': '#ecece6', 'dark': '#0755bb', 'light': '#ecece6', 'dark_accent': '#ecece6', 'dark_soft': '#99bae5', 'display': 'FormDisplay', 'cjkdisplay': 'FormCJK', 'body': 'ShiftSans', 'cjk': 'FormCJK', 'weight': 400, 'title_size': 94, 'zh_size': 84, 'cards': [('Observe', '观察', 'Notice what changes.', '看见真实的变化。'), ('Frame', '界定', 'Set one clear boundary.', '划清一条边界。'), ('Shape', '塑形', 'Make the idea testable.', '让想法可以试验。'), ('Review', '检验', 'Keep what holds up.', '留下经得起检验的。')], 'columns': [18, 26, 34, 42], 'column_max': 50, 'column_unit': ('Reviewed studies', '已评审方案 · 个'), 'ranking': [32, 26, 20, 12], 'rank_labels': [('Navigation', '导览'), ('Hierarchy', '层级'), ('Spacing', '间距'), ('Feedback', '反馈')], 'rank_max': 40, 'rank_unit': ('Observed friction points', '观察到的问题 · 处'), 'pictorial': [24, 18, 12], 'per_unit': 3, 'pict_labels': [('Sketches', '草图'), ('Models', '模型'), ('Tests', '试验')], 'group_before': [52, 64, 68], 'group_after': [76, 82, 88], 'group_labels': [('Finding', '查找'), ('Choosing', '选择'), ('Completing', '完成')], 'stacks': [[30, 45, 25], [45, 35, 20], [55, 30, 15]], 'stack_labels': [('Concept', '概念稿'), ('Prototype', '原型稿'), ('Refinement', '精修稿')], 'stack_series': [('Core form', '主体'), ('Detail', '细节'), ('Context', '背景')], 'waterfall': [80, 24, -28, -20, 56], 'water_max': 120, 'water_labels': [('Opening', '期初'), ('Added', '追加'), ('Making', '制作'), ('Testing', '试验'), ('Available', '可用')], 'line_a': [10, 9, 9, 7, 6, 5], 'line_b': [9, 8, 6, 5, 4, 3], 'line_labels': [('Initial route', '原路径'), ('Revised route', '修订路径')], 'area': [8, 12, 10, 18, 22, 20, 28, 32], 'area_max': 40, 'area_unit': ('Prototypes tested per week', '每周测试原型 · 个'), 'radar_a': [52, 64, 58, 70, 60], 'radar_b': [82, 84, 80, 88, 86], 'radar_labels': [('Clarity', '清楚'), ('Use', '可用'), ('Balance', '平衡'), ('Structure', '结构'), ('Recall', '记忆')], 'source_labels': [('Observation', '观察'), ('Workshop', '共创'), ('Research', '研究')], 'mid_labels': [('Study', '研究'), ('Test', '试验')], 'out_labels': [('Advance', '推进'), ('Hold', '暂缓')], 'scatter_labels': [('Arc', '拱'), ('Fold', '折'), ('Loop', '环'), ('Plane', '面'), ('Ridge', '脊'), ('Frame', '框')], 'targets': [78, 92, 68], 'goals': [85, 90, 80], 'target_labels': [('Study review', '方案复核'), ('Prototype test', '原型测试'), ('Detail check', '细节检查')], 'table_labels': [('Arc', '拱'), ('Fold', '折'), ('Loop', '环'), ('Plane', '面')], 'compare_labels': [('Quick study', '快速研究'), ('Focused test', '聚焦试验'), ('Full pilot', '完整试点')], 'time_labels': [('Observe', '观察'), ('Frame', '界定'), ('Make', '制作'), ('Review', '复核')], 'branch_labels': [('New idea', '新的想法'), ('Testable?', '可测试？'), ('Build a model', '制作模型'), ('Reframe', '重新界定'), ('Review evidence', '复核证据')], 'donut_labels': [('Making', '制作'), ('Testing', '试验'), ('Review', '复核')], 'funnel_labels': [('Ideas', '想法'), ('Framed', '已界定'), ('Tested', '已测试'), ('Selected', '已选定')], 'copy': [('A shape needs four decisions.', '成形，需要四次判断。', 'Move from noticing to a form that can be reviewed.', '从观察出发，让形态接受检验。'), ('More studies reach review.', '让更多方案进入评审。', 'Independent batches, counted at the same review checkpoint.', '各批独立统计，均在相同评审节点计数。'), ('Start where the friction is.', '从阻力最大的地方开始。', 'Count each finding once under its primary issue.', '每处问题只计入一个主要类别。'), ('Ideas leave visible traces.', '让想法留下可见的痕迹。', 'Different kinds of work, counted with equal units.', '用等大的单位，记录不同类型的工作。'), ('A clearer form works better.', '让形态更清楚，也更好用。', 'Task completion before and after refinement, on the same 0–100% scale.', '精修前后的任务完成率，采用同一百分比量尺。'), ('Give the core more space.', '给主体更多空间。', 'Each version is measured against its own total.', '每个版本，都以自身总量为分母。'), ('Keep capacity for the next test.', '为下一次试验留下余量。', 'One design-work pool, measured in staff-hours.', '同一设计工时池，单位为人时。'), ('A shorter route to a decision.', '让决策路径更短。', 'Median review days across six rounds; lower is faster.', '六轮评审的中位天数，数值越低，用时越短。'), ('Testing becomes a practice.', '让试验成为持续实践。', 'Weekly output, not a cumulative series.', '记录每周产出，并非累计数量。'), ('Quality has several dimensions.', '从不同维度，检验质量。', 'Keep the five scales equal and the exact scores visible.', '五个维度使用相同量尺，并保留精确分数。'), ('Follow an idea through review.', '看清想法如何通过评审。', 'The same 100 proposals, from source to outcome.', '同一批一百项提案，从来源追踪到结果。'), ('Choose the next useful test.', '选择下一项有用的试验。', 'Estimated effort and usefulness support a discussion, not a guarantee.', '以预计投入和价值评分辅助讨论，而非保证结果。'), ('Make the missing detail visible.', '让缺失的细节被看见。', 'Six concepts, four checks, one consistent 0–100 rubric.', '六个概念、四项检查，共用百分制量表。'), ('Read progress beside the goal.', '把进展，放在目标旁边。', 'Every review has its own threshold.', '每项复核，都有自己的门槛。'), ('Keep the evidence legible.', '让每份证据清楚可读。', 'Trials, successful tasks and completion rates stay together.', '试验次数、成功次数与完成率放在一起阅读。'), ('Choose a test with purpose.', '有目的地选择试验。', 'Time, effort and coverage describe different trade-offs.', '从周期、投入与覆盖率理解不同取舍。'), ('Make room for each phase.', '给每个阶段留出空间。', 'Four sequential phases; widths represent working days.', '四个连续阶段，宽度准确表示工作日。'), ('Turn a question into a test.', '把问题变成可执行的试验。', 'A decision branch clarifies the next step.', '用明确分支，决定下一步行动。'), ('Balance the work, deliberately.', '有意识地平衡工作投入。', 'Allocation shares belong to one complete work budget.', '各项占比，属于同一个完整工作预算。'), ('Select with a clear denominator.', '让筛选有清楚的分母。', 'One cohort moves through four nested stages.', '同一批候选，依次通过四个筛选阶段。')], 'scatter': [(2, 45), (4, 72), (6, 64), (8, 86), (10, 60), (12, 78)], 'heatmap': [[72, 85, 58, 92, 64, 80], [88, 62, 45, 85, 76, 54], [65, 78, 72, 90, 56, 74], [52, 76, 60, 86, 42, 70]], 'table_trials': [20, 25, 20, 25], 'table_success': [16, 20, 18, 23], 'compare_days': [2, 5, 10], 'compare_hours': [4, 12, 24], 'compare_coverage': [40, 70, 90], 'timeline': [3, 5, 4, 2], 'donut': [40, 35, 25], 'funnel': [100, 72, 48, 24], 'sankey_a': [[30, 10], [20, 15], [10, 15]], 'sankey_b': [[40, 20], [25, 15]]}
KINDS=['four-cards','columns','ranking','pictorial','grouped','stacked','waterfall','line','area','radar','sankey','scatter','heatmap','target','data-table','comparison','timeline','branch','donut','funnel']

def pair(v,z):return v[1 if z else 0]
def f(v):return f'{v:.3f}'.rstrip('0').rstrip('.')
def txt(x,y,value,size=28,color=None,anchor='start',display=False):
 return f'<text x="{f(x)}" y="{f(y)}" font-size="{size}" fill="{color or C.fg}" text-anchor="{anchor}" class="x30-{("display" if display else "label")}">{escape(str(value))}</text>'
def rect(x,y,w,h,fill,stroke=None,extra=''):
 return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="1.2"' if stroke else '')+f' {extra}/>'
def line(x1,y1,x2,y2,color=None,opacity=.22,width=1.2,dash=None):
 return f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{color or C.fg}" stroke-opacity="{opacity}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def path(d,fill='none',stroke=None,width=2,extra=''):
 return f'<path d="{d}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{width}"' if stroke else '')+f' {extra}/>'
def circle(x,y,r,fill,stroke=None):
 return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="2"' if stroke else '')+'/>'
def motion(markup,kind='fade',step=0):return f'<g data-chart-motion="{kind}" data-chart-step="{step}">{markup}</g>'
def legend(x,y,color,label):return rect(x,y-18,20,20,color)+txt(x+34,y,label,26)
def points(ps):return 'M'+' L'.join(f'{f(x)} {f(y)}' for x,y in ps)

class Canvas:
 def __init__(self,i,z):
  self.i=i;self.z=z;self.kind=KINDS[i];self.p=[];self.data={};self.unit='';self.dark=i in [2,6,8,13,18] if CONFIG['name']!='AXIS' else i in [0,2,5,7,10,12,14,16,18]
  self.bg=CONFIG['dark'] if self.dark else CONFIG['bg'];self.fg=CONFIG['light'] if self.dark else CONFIG['ink'];self.a=CONFIG['dark_accent'] if self.dark else CONFIG['accent'];self.b=CONFIG['dark_soft'] if self.dark else CONFIG['soft'];self.c=CONFIG['muted'];self.paper=CONFIG['paper'];self.labels=lambda key:[pair(x,z) for x in CONFIG[key]]
  if CONFIG['name']=='INDEX' and self.dark:self.bg={2:'#1e4bd7',6:'#191919',8:'#0c7866',13:'#581e70',18:'#191919'}[i]
 def t(self,en,zh):return zh if self.z else en
 def add(self,*items):self.p.extend(items)
 def yaxis(self,x1,x2,base,maximum,height,ticks):
  for v in ticks:
   y=base-v/maximum*height;self.add(line(x1,y,x2,y,opacity=.45 if v==0 else .18),txt(x1-24,y+9,v,27,anchor='end'))
 def finish(self):
  row=CONFIG['copy'][self.i];title=row[1 if self.z else 0];sub=row[3 if self.z else 2]
  if self.i==3:sub+=self.t(f' One symbol = {CONFIG["per_unit"]} items.',f' 每个图形代表 {CONFIG["per_unit"]} 项。')
  if self.i==10:unit=self.t('items','项')
  else:unit=self.unit
  data=escape(json.dumps(self.data,ensure_ascii=False,separators=(',',':')),quote=True)
  return f'<section class="slide x30 x30-{CONFIG["name"].lower()} x30-{self.kind}{(" x30-dark" if self.dark else "")}" data-tone="{("dark" if self.dark else "light")}" data-title="{escape(title,quote=True)}" data-layout="{self.kind}" data-layout-id="{self.kind}" data-chart-kind="{self.kind}" data-chart-unit="{escape(unit,quote=True)}" data-provenance="illustrative" data-chart-values="{data}" style="--xbg:{self.bg};--xfg:{self.fg};--xa:{self.a};--xb:{self.b}"><header class="x30-heading"><h2 class="reveal">{escape(title)}</h2><p class="reveal">{escape(sub)}</p></header><div class="x30-body" data-chart-container><svg viewBox="0 0 1680 610" xmlns="http://www.w3.org/2000/svg" data-information-visual="true" role="img" aria-label="{escape(title,quote=True)}"><title>{escape(title)}</title><desc>{escape(json.dumps(self.data,ensure_ascii=False))}</desc>{"".join(self.p)}</svg></div></section>'


def make(i,z):
 global C
 C=Canvas(i,z);c=C;t=c.t;cfg=CONFIG
 if i==0:
  for j,(en,zh,eb,zb) in enumerate(cfg['cards']):
   x=j*430;fill=c.a if j==3 else c.paper;fg=c.bg if j==3 else cfg['ink']
   card=rect(x,10,390,540,fill,cfg['muted'])
   if cfg['name']=='INDEX':card=path(f'M{x} 42V10h160l30 32h200v508H{x}Z',fill)+circle(x+35,90,7,c.bg)
   if cfg['name']=='FORM':card+=line(x+6,15,x+384,15,'#ffffff',.7,3)+line(x+384,15,x+384,545,cfg['ink'],.12,3)
   card+=txt(x+30,128,['I','II','III','IV'][j],80,fg,display=True)+txt(x+30,258,zh if z else en,42,fg,display=True)
   words=(zb if z else eb);lines=[words] if len(words)<26 else words.split(' ',3)[:3]+[' '.join(words.split(' ')[3:])]
   # Keep four meaningful short statements, never a decorative production label.
   if not z:
    chunks={'Notice what changes.':['Notice what changes.'],'Set one clear boundary.':['Set one clear boundary.'],'Make the idea testable.':['Make the idea testable.'],'Keep what holds up.':['Keep what holds up.']}
    words=eb;tokens=words.split();lines=[];cur=''
    for w in tokens:
     if len(cur+' '+w)>22:lines.append(cur);cur=w
     else:cur=(cur+' '+w).strip()
    if cur:lines.append(cur)
   else:lines=[words]
   for k,v in enumerate(lines):card+=txt(x+30,352+k*42,v,26,fg)
   card+=line(x+30,480,x+360,480,fg,.35)
   c.add(motion(card,'fade',j))
  c.data={'steps':[b if z else a for a,b,_,_ in cfg['cards']]}
 elif i==1:
  vals=cfg['columns'];maximum=cfg['column_max'];c.yaxis(100,1640,505,maximum,390,list(range(0,maximum+1,maximum//5)))
  c.add(txt(100,25,pair(cfg['column_unit'],z),27))
  for j,v in enumerate(vals):
   x=220+j*390;h=v/maximum*390;y=505-h;col=rect(x,y,145,h,c.a if j==3 else c.b)
   if cfg['name']=='FORM':col+=line(x+2,y+2,x+142,y+2,'#ffffff',.7,2)+line(x+142,y+2,x+142,503,cfg['ink'],.15,3)
   if cfg['name']=='AXIS':col+=line(x+18,y+3,x+18,502,c.paper,.45)+line(x+24,y+3,x+24,502,c.paper,.25)
   c.add(motion(col,'grow-y',j),motion(txt(x+72.5,y-24,v,44,c.a if j==3 else c.fg,'middle',True),'fade',j+1),txt(x+72.5,562,t(f'Batch {j+1}',f'第 {j+1} 批'),29,anchor='middle'))
  c.data={'values':vals,'axis':[0,maximum],'cumulative':False};c.unit=pair(cfg['column_unit'],z)
 elif i==2:
  vals=cfg['ranking'];maximum=cfg['rank_max'];start=425;width=1130
  c.add(txt(start,22,pair(cfg['rank_unit'],z),27))
  for v in [0,maximum/2,maximum]:c.add(line(start+v/maximum*width,45,start+v/maximum*width,500,opacity=.15),txt(start+v/maximum*width,560,f(v),27,anchor='middle'))
  for j,(v,label) in enumerate(zip(vals,c.labels('rank_labels'))):
   y=75+j*113;c.add(txt(0,y+34,label,36,display=True),motion(rect(start,y,v/maximum*width,44,c.a if j==0 else c.b),'grow-x',j),motion(txt(start+v/maximum*width+20,y+34,v,37),'fade',j+1),line(0,y+77,1640,y+77,opacity=.18))
  c.add(txt(0,609,t(f'{sum(vals)} findings in total',f'合计 {sum(vals)} 处问题'),27));c.data={'values':vals,'labels':c.labels('rank_labels'),'total':sum(vals),'axis':[0,maximum]};c.unit=pair(cfg['rank_unit'],z)
 elif i==3:
  vals=cfg['pictorial'];unit=cfg['per_unit']
  for j,(v,label) in enumerate(zip(vals,c.labels('pict_labels'))):
   y=70+j*170;c.add(txt(0,y+35,label,38,display=True))
   for k in range(v//unit):
    x=480+k*94;shape=rect(x,y-15,49,65,c.a)
    if cfg['name']=='FORM':shape=circle(x+25,y+18,27,c.a)+circle(x+25,y+18,16,c.bg)
    elif cfg['name']=='INDEX':shape=path(f'M{x} {y-10}v-10h20l10 10h23v65h-53Z',c.a)+line(x+8,y+15,x+43,y+15,c.bg,.7)
    else:shape=rect(x,y,56,42,c.a)+line(x+8,y+12,x+48,y+12,c.bg,.55)+line(x+8,y+20,x+48,y+20,c.bg,.3)
    c.add(f'<g data-unit="{unit}" data-chart-motion="pop" data-chart-step="{j+k}">{shape}</g>')
   c.add(motion(txt(1630,y+40,v,54,c.a,'end',True),'fade',j+5),line(0,y+108,1640,y+108))
  c.add(txt(0,609,t(f'{sum(vals)} items across three types',f'三类工作，共 {sum(vals)} 项'),28));c.data={'values':vals,'labels':c.labels('pict_labels'),'per_unit':unit,'total':sum(vals),'symbol_count':sum(vals)//unit};c.unit='items'
 elif i==4:
  aa,bb=cfg['group_before'],cfg['group_after'];c.add(legend(100,20,c.b,t('Before','调整前')),legend(440,20,c.a,t('After','调整后')),txt(1640,20,t('Task success · %','任务成功率 · %'),27,anchor='end'));c.yaxis(100,1640,500,100,360,[0,25,50,75,100])
  for j,(a,b,label) in enumerate(zip(aa,bb,c.labels('group_labels'))):
   center=360+j*520
   for k,(x,v,col) in enumerate([(center-100,a,c.b),(center+20,b,c.a)]):c.add(motion(rect(x,500-v*3.6,90,v*3.6,col),'grow-y',2*j+k),motion(txt(x+45,500-v*3.6-21,f'{v}%',35,col if k else c.fg,'middle'),'fade',j+k+1))
   c.add(txt(center+10,565,label,32,anchor='middle',display=True))
  c.data={'before':aa,'after':bb,'labels':c.labels('group_labels'),'axis':[0,100]};c.unit='percent'
 elif i==5:
  vals=cfg['stacks'];colors=[c.a,c.b,c.c];start=300;width=1300
  for j,label in enumerate(c.labels('stack_series')):c.add(legend(start+j*435,20,colors[j],label))
  for v in [0,25,50,75,100]:c.add(line(start+width*v/100,55,start+width*v/100,485,opacity=.12),txt(start+width*v/100,558,f'{v}%',27,anchor='middle'))
  for j,(vs,label) in enumerate(zip(vals,c.labels('stack_labels'))):
   y=83+j*155;x=start;block='';c.add(txt(0,y+47,label,34,display=True))
   for k,(v,col) in enumerate(zip(vs,colors)):
    w=width*v/100;block+=rect(x,y,w,78,col)+txt(x+w/2,y+51,f'{v}%',35,c.bg if k==0 else cfg['ink'],'middle');x+=w
   c.add(motion(block,'wipe-x',j))
  c.add(txt(start,609,t('Each row totals 100% of its own snapshot.','每行均为当时总量的百分之百，不代表各期总量相同。'),25));c.data={'values':vals,'labels':c.labels('stack_labels'),'series':c.labels('stack_series'),'axis':[0,100],'separate_denominators':True};c.unit='percent'
 elif i==6:
  vals=cfg['waterfall'];maximum=cfg['water_max'];base=510;scale=400/maximum;centers=[230,550,870,1190,1510];levels=[vals[0]]
  for v in vals[1:-1]:levels.append(levels[-1]+v)
  spans=[(0,vals[0])]+list(zip(levels[:-1],levels[1:]))+[(0,vals[-1])]
  c.add(legend(100,20,c.a,t('Balance','余额')),legend(440,20,c.b,t('Added','追加')),legend(780,20,c.c,t('Used','使用')),txt(1640,20,t('Staff-hours','单位：人时'),27,anchor='end'));c.yaxis(100,1640,base,maximum,400,[0,maximum/4,maximum/2,maximum*3/4,maximum])
  for j,(x,v,(a,b),label) in enumerate(zip(centers,vals,spans,c.labels('water_labels'))):
   top=base-max(a,b)*scale;h=abs(b-a)*scale;col=c.a if j in [0,4] else c.b if v>0 else c.c
   c.add(motion(rect(x-70,top,140,h,col),'grow-y',j),motion(txt(x,top-23,f'+{v}' if j==1 else v,39,anchor='middle'),'fade',j+1),txt(x,566,label,29,anchor='middle'))
   if j<4:c.add(motion(line(x+70,base-b*scale,centers[j+1]-70,base-b*scale,c.fg,.65,1.4,'7 6'),'wipe-x',j+1))
  c.data={'values':vals,'balances':levels+[vals[-1]],'axis':[0,maximum],'unit':'staff-hours'};c.unit='staff-hours'
 elif i==7:
  a,b=cfg['line_a'],cfg['line_b'];unit=t('minutes','分钟') if cfg['name']=='INDEX' else t('days','天');x=lambda j:100+j*210;y=lambda v:500-v*30
  c.add(txt(100,22,t('Median time · ','中位耗时 · ')+unit,27));c.yaxis(100,1150,500,12,360,[0,3,6,9,12])
  for j in range(6):c.add(txt(x(j),556,t(f'R{j+1}',f'第{j+1}轮'),26,anchor='middle'))
  for k,(vals,col) in enumerate([(a,c.b),(b,c.a)]):
   d=points([(x(j),y(v))for j,v in enumerate(vals)]);c.add(motion(path(d,stroke=col,width=4,extra='stroke-dasharray="10 7"' if k==0 else ''),'wipe-x' if k==0 else 'draw',k))
   for j,v in enumerate(vals):c.add(motion(circle(x(j),y(v),6,c.bg,col),'pop',j))
  c.add(line(1240,30,1240,550),motion(txt(1300,230,b[-1],168,c.a,display=True),'fade',3),txt(1310,320,unit,30),txt(1300,365,pair(cfg['line_labels'][1],z),29),txt(1300,455,t(f'{a[-1]} {unit}: reference',f'参照：{a[-1]} {unit}'),28));c.add(legend(100,609,c.b,pair(cfg['line_labels'][0],z)),legend(600,609,c.a,pair(cfg['line_labels'][1],z)))
  c.data={'a':a,'b':b,'axis':[0,12],'unit':unit};c.unit=unit
 elif i==8:
  vals=cfg['area'];maximum=cfg['area_max'];x=lambda j:100+j*215;y=lambda v:500-v/maximum*380
  c.add(txt(100,20,pair(cfg['area_unit'],z),27));c.yaxis(100,1605,500,maximum,380,[0,maximum/4,maximum/2,maximum*3/4,maximum])
  ps=[(x(j),y(v)) for j,v in enumerate(vals)];d=f'M100 500 L'+ ' L'.join(f'{f(a)} {f(b)}'for a,b in ps)+' L1605 500Z'
  c.add(motion(path(d,c.a,extra='fill-opacity=".24"'),'wipe-x',0),motion(path(points(ps),stroke=c.a,width=4),'draw',1))
  for j,v in enumerate(vals):c.add(motion(circle(x(j),y(v),5,c.a),'pop',j),motion(txt(x(j),y(v)-22,v,29,anchor='middle'),'fade',j),txt(x(j),557,t(f'W{j+1}',f'第{j+1}周'),27,anchor='middle'))
  c.data={'values':vals,'axis':[0,maximum],'cumulative':False,'unit':pair(cfg['area_unit'],z)};c.unit=pair(cfg['area_unit'],z)
 elif i==9:
  cx,cy,r=410,310,210;angles=[-pi/2+j*2*pi/5 for j in range(5)];labels=c.labels('radar_labels')
  pos=lambda j,v:(cx+cos(angles[j])*r*v/100,cy+sin(angles[j])*r*v/100)
  for v in [25,50,75,100]:c.add(path(points([pos(j,v)for j in range(5)])+'Z',stroke=c.fg,width=1,extra='stroke-opacity=".2"'))
  for j,label in enumerate(labels):
   x,y=pos(j,120);c.add(line(cx,cy,*pos(j,100),opacity=.2),txt(x,y+10,label,29,anchor='middle'))
  for k,(vals,col) in enumerate([(cfg['radar_a'],c.b),(cfg['radar_b'],c.a)]):c.add(motion(path(points([pos(j,v)for j,v in enumerate(vals)])+'Z',stroke=col,width=3.5,extra='stroke-dasharray="9 7"' if k==0 else ''),'wipe-x' if k==0 else 'draw',k))
  c.add(txt(910,56,t('Dimension','维度'),28),txt(1270,56,t('Before','调整前'),28,anchor='middle'),txt(1540,56,t('After','调整后'),28,anchor='middle'))
  for j,(label,a,b) in enumerate(zip(labels,cfg['radar_a'],cfg['radar_b'])):
   y=135+j*84;c.add(line(880,y-49,1660,y-49),txt(910,y,label,32),txt(1270,y,a,34,anchor='middle'),motion(txt(1540,y,b,36,c.a,'middle'),'fade',j))
  c.add(txt(905,592,t('Equal 0–100 scales; do not rank by area.','各维度均为百分制，不按面积判断整体优劣。'),25));c.data={'before':cfg['radar_a'],'after':cfg['radar_b'],'labels':labels,'axis':[0,100]};c.unit='rubric points'
 elif i==10:
  aa,bb=cfg['sankey_a'],cfg['sankey_b'];groups=[[40,35,25],[60,40],[65,35]];labels=[c.labels('source_labels'),c.labels('mid_labels'),c.labels('out_labels')];xs=[40,750,1420];w=190;scale=4;positions=[]
  for vals in groups:
   gap=(510-sum(vals)*scale)/(len(vals)-1);yy=55;pos=[]
   for v in vals:pos.append(yy);yy+=v*scale+gap
   positions.append(pos)
  for layer,matrix in enumerate([aa,bb]):
   left=[0]*len(matrix);right=[0]*len(matrix[0])
   for a,row in enumerate(matrix):
    for b,v in enumerate(row):
     x1=xs[layer]+w;x2=xs[layer+1];y1=positions[layer][a]+left[a]*scale;y2=positions[layer+1][b]+right[b]*scale;h=v*scale;left[a]+=v;right[b]+=v
     d=f'M{x1} {y1}C{x1+200} {y1} {x2-200} {y2} {x2} {y2}V{y2+h}C{x2-200} {y2+h} {x1+200} {y1+h} {x1} {y1+h}Z'
     c.add(motion(path(d,c.a if a==0 else c.b,extra='fill-opacity=".42"'),'wipe-x',layer*3+a),motion(txt(x1+130,y1+(y2-y1)*.123904+h/2+9,v,27,c.fg,'middle'),'fade',layer*3+a+1))
  for k,vals in enumerate(groups):
   for j,v in enumerate(vals):
    yy=positions[k][j];fill=c.a if k!=1 else c.b;fg=c.bg if k!=1 else cfg['ink'];c.add(motion(rect(xs[k],yy,w,v*scale,fill)+txt(xs[k]+w/2,yy+v*scale/2-8,labels[k][j],25,fg,'middle')+txt(xs[k]+w/2,yy+v*scale/2+29,v,31,fg,'middle'),'fade',k*2))
  c.data={'inputs':groups[0],'middle':groups[1],'outputs':groups[2],'a':aa,'b':bb,'total':100,'scale':scale};c.unit='items'
 elif i==11:
  ps=cfg['scatter'];x=lambda v:110+v/14*1450;y=lambda v:505-v/100*400
  c.yaxis(110,1560,505,100,400,[0,25,50,75,100]);c.add(txt(110,25,t('Estimated usefulness · points','预计价值 · 分'),27))
  for v in [0,2,4,6,8,10,12,14]:c.add(txt(x(v),555,v,27,anchor='middle'))
  for j,((a,b),label) in enumerate(zip(ps,c.labels('scatter_labels'))):c.add(motion(circle(x(a),y(b),10,c.a),'pop',j),motion(txt(x(a)+20,y(b)-12,label,27),'fade',j+1))
  c.add(txt(1560,609,t('Estimated effort · hours','预计投入 · 小时'),26,anchor='end'));c.data={'points':ps,'labels':c.labels('scatter_labels'),'x_axis':[0,14],'y_axis':[0,100],'x_unit':'hours','y_unit':'rubric points','causal':False};c.unit='hours / points'
 elif i==12:
  vals=cfg['heatmap'];x0,y0,cw,ch=360,90,210,105;rows=[t('Purpose','目标'),t('Evidence','证据'),t('Structure','结构'),t('Next step','下一步')]
  for j in range(6):c.add(txt(x0+j*cw+cw/2,46,t(f'Set {j+1}',f'集合 {j+1}'),27,anchor='middle'))
  for r,row in enumerate(vals):
   c.add(txt(305,y0+r*ch+61,rows[r],31,anchor='end'))
   cells=''
   for j,v in enumerate(row):
    col=c.c if v<50 else c.b if v<75 else c.a;fg=cfg['ink'] if v<75 else c.bg;cells+=rect(x0+j*cw,y0+r*ch,cw-7,ch-7,col)+txt(x0+j*cw+(cw-7)/2,y0+r*ch+60,v,34,fg,'middle')
   c.add(motion(cells,'fade',r))
  for j,(col,lab) in enumerate([(c.c,'0–49'),(c.b,'50–74'),(c.a,'75–100')]):c.add(legend(600+j*320,592,col,lab))
  c.data={'values':vals,'range':[0,100],'bands':[[0,49],[50,74],[75,100]]};c.unit='readiness points'
 elif i==13:
  vals,goals=cfg['targets'],cfg['goals']
  for j,(v,g,label) in enumerate(zip(vals,goals,c.labels('target_labels'))):
   x=j*575;w=490;scale=w/100
   c.add(txt(x,50,label,31),motion(txt(x-5,242,f'{v}%',145,c.a,display=True),'fade',j),rect(x,335,w,16,c.b,extra='opacity=".25"'),motion(rect(x,335,v*scale,16,c.a),'grow-x',j),motion(line(x+g*scale,314,x+g*scale,372,c.fg,.9,2)+txt(x+g*scale,288,t(f'Goal {g}%',f'目标 {g}%'),25,anchor='middle'),'fade',j+1))
   for tick in [0,50,100]:c.add(txt(x+tick*scale,426,f'{tick}%',25,anchor='middle'))
   delta=v-g;c.add(line(x,475,x+w,475),txt(x,540,t(f'{delta:+d} percentage points',f'与目标相差 {delta:+d} 个百分点'),27))
  c.data={'actual':vals,'targets':goals,'axis':[0,100],'differences':[a-b for a,b in zip(vals,goals)]};c.unit='percent'
 elif i==14:
  cols=[0,700,1060,1460];headers=[t('Record','记录'),t('Trials','试验次数'),t('Successes','成功次数'),t('Success rate','成功率')]
  for x,label in zip(cols,headers):c.add(txt(x,53,label,28,anchor='start' if x==0 else 'middle'))
  c.add(line(0,84,1660,84,c.a,.8,2))
  for j,(label,n,s) in enumerate(zip(c.labels('table_labels'),cfg['table_trials'],cfg['table_success'])):
   y=170+j*105;c.add(motion(txt(0,y,label,34,display=True)+txt(700,y,n,35,anchor='middle')+txt(1060,y,s,35,anchor='middle')+txt(1460,y,f'{s/n*100:g}%',40,c.a,'middle',True),'fade',j),line(0,y+34,1660,y+34))
  total=sum(cfg['table_trials']);ok=sum(cfg['table_success']);c.add(txt(0,609,t(f'Total: {ok}/{total} successful trials ({ok/total*100:.1f}%).',f'合计：{total} 次试验中成功 {ok} 次，总成功率 {ok/total*100:.1f}%。'),28));c.data={'trials':cfg['table_trials'],'successes':cfg['table_success'],'rates':[s/n*100 for n,s in zip(cfg['table_trials'],cfg['table_success'])],'total_rate':ok/total*100};c.unit='count / percent'
 elif i==15:
  cols=[0,650,1070,1490];labels=c.labels('compare_labels');c.add(txt(0,55,t('Decision factor','决策因素'),28))
  for x,label in zip(cols[1:],labels):c.add(txt(x,55,label,32,anchor='middle',display=True))
  c.add(line(0,95,1660,95,c.a,.8,2));rows=[(t('Lead time · days','周期 · 天'),cfg['compare_days']),(t('Effort · staff-hours','投入 · 人时'),cfg['compare_hours']),(t('Coverage · %','覆盖率 · %'),cfg['compare_coverage'])]
  for j,(label,vals) in enumerate(rows):
   y=200+j*135;c.add(txt(0,y,label,31))
   for k,v in enumerate(vals):c.add(motion(txt(cols[k+1],y,v,52,c.a if k==1 else c.fg,'middle',True),'fade',j+k))
   c.add(line(0,y+45,1660,y+45))
  c.add(txt(0,609,t('Coverage is a planning estimate; more is not automatically better.','覆盖率是计划估计，并非越大就一定越合适。'),27));c.data={'labels':labels,'days':cfg['compare_days'],'staff_hours':cfg['compare_hours'],'coverage':cfg['compare_coverage']};c.unit='days / staff-hours / percent'
 elif i==16:
  vals=cfg['timeline'];labels=c.labels('time_labels');total=sum(vals);left=80;width=1520;scale=width/total
  for day in range(total+1):
   x=left+day*scale;c.add(line(x,352,x,370,c.fg,.5),txt(x,417,day,26,anchor='middle'))
  x=left;colors=[c.a,c.b,c.a,c.b]
  for j,(v,label) in enumerate(zip(vals,labels)):
   w=v*scale;fg=c.bg if j%2==0 else cfg['ink'];c.add(motion(rect(x,200,w,135,colors[j])+txt(x+w/2,250,label,30,fg,'middle')+txt(x+w/2,303,t(f'{v} days',f'{v} 天'),30,fg,'middle'),'wipe-x',j));x+=w
  c.add(motion(txt(80,120,t(f'{total} working days',f'共 {total} 个工作日'),70,c.a,display=True),'fade',0),txt(1600,496,t('Elapsed working days','累计工作日'),27,anchor='end'),txt(80,581,t('The phases are consecutive and do not overlap.','各阶段连续执行，不重叠计算。'),28));c.data={'durations':vals,'total':total,'overlap':False,'width_per_day':scale};c.unit='working days'
 elif i==17:
  labels=c.labels('branch_labels');positions=[(0,230,290,110),(420,190,330,190),(920,80,330,110),(920,430,330,110),(1370,80,300,110)]
  for j,(x,y,w,h) in enumerate(positions):
   if j==1:shape=path(f'M{x+w/2} {y}L{x+w} {y+h/2}L{x+w/2} {y+h}L{x} {y+h/2}Z',c.a);fg=c.bg
   else:shape=rect(x,y,w,h,c.paper,cfg['muted']);fg=cfg['ink']
   shape+=txt(x+w/2,y+h/2+10,labels[j],28,fg,'middle');c.add(motion(shape,'fade',j))
  edges=[('M290 285H420',0),('M750 285H825V135H920',1),('M750 285H825V485H920',2),('M1250 135H1370',3)]
  for d,step in edges:c.add(motion(path(d,stroke=c.a,width=2.2),'draw',step))
  c.add(txt(845,190,t('Yes','是'),27,c.a),txt(845,423,t('No','否'),27,c.a),txt(0,593,t('The branch is a decision rule, not a measured conversion rate.','此分支表示行动规则，不表示实测转化率。'),27));c.data={'nodes':labels,'edges':[[0,1],[1,2],[1,3],[2,4]],'conditions':['yes','no']};c.unit='decision rule'
 elif i==18:
  vals=cfg['donut'];labels=c.labels('donut_labels');cx,cy,r,sw=410,300,210,68;circ=2*pi*r;off=0;colors=[c.a,c.b,c.c]
  for j,v in enumerate(vals):
   d=circ*v/100;c.add(motion(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{colors[j]}" stroke-width="{sw}" stroke-dasharray="{d} {circ-d}" stroke-dashoffset="{-off}" transform="rotate(-90 {cx} {cy})"/>','fade',j));off+=d
  c.add(txt(cx,cy+25,'100%',75,c.fg,'middle',True),txt(cx,cy+80,t('one whole','同一整体'),28,c.fg,'middle'))
  for j,(v,label,col) in enumerate(zip(vals,labels,colors)):
   y=135+j*155;c.add(rect(870,y-22,22,22,col),txt(920,y,label,36),motion(txt(1630,y+16,f'{v}%',68,c.fg,'end',True),'fade',j+1),line(870,y+64,1640,y+64))
  c.data={'values':vals,'labels':labels,'total':sum(vals)};c.unit='percent of one total'
 elif i==19:
  vals=cfg['funnel'];labels=c.labels('funnel_labels');scale=10;cx=850
  for j,(v,label) in enumerate(zip(vals,labels)):
   y=40+j*135;w=v*scale;c.add(txt(0,y+50,label,33,display=True),motion(rect(cx-w/2,y,w,78,c.a if j==3 else c.b),'wipe-x',j),motion(txt(1630,y+51,v,47,c.a,'end',True),'fade',j+1))
  c.add(txt(0,609,t('Same cohort; bar width represents count.','同一批候选；条形宽度表示数量。'),26),txt(1640,609,t('24% of the initial cohort reaches the last stage.','最终保留量为最初候选的 24%。'),26,c.a,'end'));c.data={'values':vals,'labels':labels,'final_share':vals[-1]/vals[0]*100,'nested':True,'width_per_item':scale};c.unit='items'
 return c.finish()


def get_slides(lang='en'):return [make(i,lang in ('zh','zh-CN')) for i in range(20)]

def validate_data():
 import re,xml.etree.ElementTree as ET
 cfg=CONFIG
 assert len(KINDS)==len(cfg['copy'])==20
 assert all(v>=0 for v in cfg['columns']) and max(cfg['columns'])<=cfg['column_max']
 assert cfg['ranking']==sorted(cfg['ranking'],reverse=True) and max(cfg['ranking'])<=cfg['rank_max']
 assert all(v%cfg['per_unit']==0 for v in cfg['pictorial'])
 assert all(0<=v<=100 for v in cfg['group_before']+cfg['group_after'])
 assert all(sum(row)==100 for row in cfg['stacks'])
 assert sum(cfg['waterfall'][:-1])==cfg['waterfall'][-1]
 assert max(cfg['line_a']+cfg['line_b'])<=12 and min(cfg['line_a']+cfg['line_b'])>=0
 assert all(0<=v<=cfg['area_max'] for v in cfg['area'])
 assert all(0<=v<=100 for v in cfg['radar_a']+cfg['radar_b'])
 aa,bb=cfg['sankey_a'],cfg['sankey_b'];assert [sum(r)for r in aa]==[40,35,25];assert [sum(r[j]for r in aa)for j in range(2)]==[60,40];assert [sum(r)for r in bb]==[60,40];assert [sum(r[j]for r in bb)for j in range(2)]==[65,35]
 assert all(0<=x<=14 and 0<=y<=100 for x,y in cfg['scatter'])
 assert len(cfg['heatmap'])==4 and all(len(r)==6 and all(0<=v<=100 for v in r)for r in cfg['heatmap'])
 assert all(0<=v<=100 for v in cfg['targets']+cfg['goals'])
 assert all(0<=s<=n for n,s in zip(cfg['table_trials'],cfg['table_success']))
 assert sum(cfg['timeline'])==14 and all(v>0 for v in cfg['timeline'])
 assert sum(cfg['donut'])==100 and cfg['funnel']==sorted(cfg['funnel'],reverse=True) and cfg['funnel'][-1]/cfg['funnel'][0]==.24
 langs={}
 for lang in ['en','zh']:
  slides=get_slides(lang);assert len(slides)==20;hooks=0
  for s in slides:
   xml=re.search(r'<svg\b.*?</svg>',s,re.S).group();root=ET.fromstring(xml)
   assert root.get('viewBox')=='0 0 1680 610' and 'data-information-visual' in root.attrib
   assert all(e.tag.rsplit('}',1)[-1] not in {'script','image','foreignObject'} for e in root.iter())
   hooks+=sum('data-chart-motion' in e.attrib for e in root.iter())
   assert 'artwork-slot' not in s and '示例数据' not in s
  assert slides[3].count('data-unit=')==sum(cfg['pictorial'])//cfg['per_unit']
  langs[lang]={'slides':20,'motion_hooks':hooks,'math':'PASS','sankey_conservation':'PASS','symbols':sum(cfg['pictorial'])//cfg['per_unit']}
 return {'passed':True,'theme':cfg['name'],'languages':langs,'provenance':'locally authored illustrative data; not externally sourced'}

if __name__=='__main__':
 import argparse
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--lang',default='en',choices=['en','zh','zh-CN']);ap.add_argument('--output');args=ap.parse_args();report=validate_data()
 if args.output:Path(args.output).write_text('\n'.join(get_slides(args.lang)))
 print(json.dumps(report,ensure_ascii=False,indent=2))
