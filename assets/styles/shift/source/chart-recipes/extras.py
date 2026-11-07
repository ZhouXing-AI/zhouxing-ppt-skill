from html import escape

def get_slides(lang):
 z=lang=='zh'
 h='四个方向，独立推进。' if z else 'Four tracks. One shared rhythm.'
 cards=[('01','发现','把一个观察变成清楚的问题。','问题定义') ,('02','组合','让不同线索形成新的关系。','关系草图'),('03','试验','用最小版本验证一个假设。','初步原型'),('04','发布','记录反馈，决定下一步。','真实回应')] if z else [('01','Discover','Turn an observation into a clear question.','A clear brief'),('02','Connect','Bring distant clues into a useful relationship.','A working map'),('03','Prototype','Test one assumption with a small version.','A first version'),('04','Release','Gather feedback and decide what comes next.','A real response')]
 a=f'<section class="slide data-slide four-tracks" data-title="{h}" data-tone="silver"><header class="data-heading"><h2 class="reveal">{h}</h2></header><div class="track-grid">'
 for no,title,copy,end in cards:a+=f'<article class="reveal"><span class="track-number dot">{no}</span><h3 class="reveal">{title}</h3><p>{copy}</p><div class="track-output">{end}<span>↗</span></div></article>'
 a+='</div></section>'
 vals=[('原型完成率','Prototypes completed',72,85),('访谈覆盖率','Interviews covered',90,80),('反馈处理率','Feedback resolved',56,75)]
 title='离目标，还有多远？' if z else 'How far from the target?'
 subtitle='把当前进度，放回明确的承诺里。' if z else 'Put today’s progress against a clear commitment.'
 b=f'<section class="slide data-slide target-progress dark" data-title="{title}" data-tone="dark" data-chart-kind="target"><header class="data-heading"><h2 class="reveal">{title}</h2><p class="data-subtitle reveal">{subtitle}</p></header><div class="target-chart reveal" data-chart-container="true" data-information-visual><svg viewBox="0 0 1720 620" role="img" aria-label="{"实际进度与目标，共用零到百分之百的量尺" if z else "Actual progress and targets on a shared zero to one hundred percent scale"}"><title>{title}</title><desc>Actual: 72%, 90%, 56%. Targets: 85%, 80%, 75%. Differences: -13, +10, -19 percentage points.</desc>'
 for i,(zh,en,v,t) in enumerate(vals):
  y=i*200
  delta=v-t; note=(f'{"超出" if delta>0 else "尚差"} {abs(delta)} 个百分点' if z else f'{abs(delta)} points {"above" if delta>0 else "below"} target')
  b+=f'<line x1="0" y1="{y}" x2="1720" y2="{y}" stroke="#e3e3d9" stroke-opacity=".22"/><text x="0" y="{y+62}" class="target-index">0{i+1}</text><text x="100" y="{y+54}" class="target-name">{zh if z else en}</text><g data-chart-motion="fade" data-chart-step="{i}"><text x="100" y="{y+161}" class="target-value {"target-hit" if v>=t else ""}">{v}<tspan class="target-percent">%</tspan></text><text x="310" y="{y+149}" class="target-note">{note}</text></g>'
  b+=f'<rect x="680" y="{y+103}" width="1040" height="16" fill="#e3e3d9" opacity=".15"/><g data-chart-motion="grow-x" data-chart-step="{i}"><rect x="680" y="{y+103}" width="{v*10.4}" height="16" fill="#ff661a"/></g><g data-chart-motion="fade" data-chart-step="{i+1}"><path d="M{680+t*10.4} {y+84}v54" stroke="#e3e3d9" stroke-width="3"/><text x="{680+t*10.4}" y="{y+63}" text-anchor="middle" class="target-label">{"目标" if z else "Target"} {t}%</text></g>'
  for tick in (0,25,50,75,100):
   x=680+tick*10.4
   b+=f'<line x1="{x}" y1="{y+145}" x2="{x}" y2="{y+151}" stroke="#e3e3d9" stroke-opacity=".3"/><text x="{x}" y="{y+179}" text-anchor="middle" class="target-tick">{tick}{"%" if tick==100 else ""}</text>'
 b+='</svg></div></section>'
 return [a,b]

def validate_data():
 assert [72-85,90-80,56-75]==[-13,10,-19]
 for actual,target in [(72,85),(90,80),(56,75)]:
  assert 0<=actual<=100 and 0<=target<=100
  assert abs(actual*10.4/1040-actual/100)<1e-10
