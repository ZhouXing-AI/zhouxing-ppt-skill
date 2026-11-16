"""Composable native SVG bar/line panels. No dependencies; styling is caller-owned.
One panel can contain any number of bar and/or line series on a shared scale.
Use independent panels for incompatible units; renderer never invents a second axis.
"""
from html import escape
from math import ceil,isfinite

def panel_boxes(count, width=1680, height=590, gap=90):
 if count<1:raise ValueError('At least one panel is required')
 cols=1 if count==1 else 2;rows=ceil(count/cols)
 w=(width-gap*(cols-1))/cols;h=(height-gap*(rows-1))/rows
 return [(i%cols*(w+gap),i//cols*(h+gap),w,h) for i in range(count)]

def cartesian(labels,series,*,width=795,height=590,maximum=100,step=25,title='',unit='',note='',number_format='g',label_size=25):
 if width<480 or height<420:raise ValueError('Panel too small; recompose or split the page')
 if not labels or not isfinite(maximum) or not isfinite(step) or maximum<=0 or step<=0:raise ValueError('Nonempty labels and positive scale required')
 if not series:raise ValueError('At least one series required')
 for s in series:
  if s['type'] not in ('bar','line') or len(s['values'])!=len(labels):raise ValueError('Series type or length mismatch')
  if any(not isfinite(v) or v<0 or v>maximum for v in s['values']):raise ValueError('Values must fit explicit nonnegative scale')
 def text(x,y,v,size=25,anchor='start',color='#394953'):
  return f'<text x="{x:g}" y="{y:g}" font-size="{size}" text-anchor="{anchor}" fill="{color}">{escape(str(v))}</text>'
 out=text(0,12,title,32)+text(0,53,unit,23,color='#7C929E')
 left=50;right=width-20;top=140;base=height-95;plot=right-left
 out+=f'<g class="panel-legend">'
 for i,s in enumerate(series):
  if not s.get('name'):continue
  x=i*min(220,width/len(series))
  out+=f'<rect x="{x}" y="78" width="15" height="15" rx="3" fill="{s["fill"]}"/>'+text(x+25,92,s['name'],23,color='#7C929E')
 out+='</g>'
 for i in range(int(maximum/step)+1):
  v=i*step;y=base-v/maximum*(base-top)
  out+=f'<line x1="{left}" y1="{y}" x2="{right}" y2="{y}" class="grid-line"/>'+text(left-14,y+8,v,22,'end','#7C929E')
 bars=[s for s in series if s['type']=='bar'];band=plot/len(labels);group=band*.65;bw=group/max(1,len(bars))
 for k,s in enumerate(series):
  xy=[]
  for i,v in enumerate(s['values']):
   cx=left+band*(i+.5);y=base-v/maximum*(base-top);xy.append((cx,y))
   if s['type']=='bar':
    j=bars.index(s);x=cx-group/2+j*bw;w=bw*.78
    out+=f'<g data-lens-motion="up" data-lens-step="{i+k}"><rect class="panel-bar" data-value="{v}" x="{x:g}" y="{y:g}" width="{w:g}" height="{base-y:g}" rx="5" fill="{s["fill"]}" stroke="#E9F6FB" stroke-width="1.3"/><path d="M{x+5:g} {y+3:g}H{x+w-5:g}" stroke="#FFFFFF" stroke-opacity=".7" fill="none"/></g>'
    out+=text(x+w/2,y-13,format(v,number_format)+s.get('suffix',''),label_size,'middle',s.get('color','#47738B'))
  if s['type']=='line':
   d='M'+' L'.join(f'{x:g},{y:g}' for x,y in xy)
   out+=f'<g data-lens-motion="draw"><path d="{d}" fill="none" stroke="{s.get("color","#47738B")}" stroke-width="3"/></g>'
   for x,y in xy:out+=f'<circle cx="{x}" cy="{y}" r="4" fill="{s.get("color","#47738B")}"/>'
 for i,label in enumerate(labels):out+=text(left+band*(i+.5),base+42,label,25,'middle')
 if note:out+=text(0,height-2,note,22,color='#7C929E')
 return out
