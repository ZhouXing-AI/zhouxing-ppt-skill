"""EDIT's four proof leaves and final review ledger; bilingual final-state SVG."""
from html import escape
import json
TARGETS=[('Facts checked','事实核验',86,90),('Sources linked','来源标注',96,95),('Final proof read','终稿校阅',74,85)]
PAPER='#f2eee7';BRIGHT='#fcf8f0';INK='#352129';RED='#b64032';BLUSH='#e8a496';MUTED='#d8d1c9'

def get_slides(lang):
 z=lang in ('zh','zh-CN');t=lambda a,b:b if z else a
 title=t('Four passes. One clear voice.','四次校阅，留下清楚的表达。')
 heading=t('Four passes. <em>One clear voice.</em>','四次校阅，留下<span class="ed-accent">清楚的表达。</span>')
 cards=[('Select','Keep the idea the reader needs most.','One central idea','选稿','留下读者<br>最需要的一个想法。','一个核心'),('Order','Give each part a reason to follow the last.','A reading path','编排','让每一部分，<br>都有承接上文的理由。','阅读顺序'),('Cut','Remove repetition. Keep the meaning.','Less friction','精简','删除重复，<br>保留完整的意思。','减少阻力'),('Check','Verify the detail before you call it done.','Ready to share','校阅','在宣布完成之前，<br>核实每个细节。','安心交付')]
 a=f'<section class="slide edit-data ed-four-cards" data-title="{title}" data-tone="light"><header class="ed-heading"><h2 class="reveal">{heading}</h2><p class="ed-subtitle reveal">{t("A separate pass for each kind of judgment.","每次校阅，只专注一种判断。")}</p></header><div class="ed-card-grid">'
 for i,(en,body,end,zh,zb,ze) in enumerate(cards):
  a+=f'<article class="paper-enter"><div class="ed-card-top"><span class="ed-card-number">{["I.","II.","III.","IV."][i]}</span></div><h3>{t(en,zh)}</h3><p>{t(body,zb)}</p><div class="ed-card-output">{t(end,ze)}<span aria-hidden="true">↗</span></div></article>'
 a+='</div></section>'
 title=t('Ready means reviewed.','校阅完成，才算准备就绪。')
 heading=t('Ready means <em>reviewed.</em>','<span class="ed-accent">校阅完成，</span>才算准备就绪。')
 b=f'<section class="slide edit-data ed-target dark-page" data-title="{title}" data-tone="dark" data-chart-kind="target" data-chart-values=\'{json.dumps(TARGETS,ensure_ascii=False)}\'><header class="ed-heading"><h2 class="reveal">{heading}</h2><p class="ed-subtitle reveal">{t("Each check has its own threshold. A strong average cannot replace a missing check.","每项检查都有自己的门槛，平均进度不能代替遗漏的环节。")}</p></header><div class="ed-chart" data-chart-container><svg viewBox="0 0 1680 610" role="img" aria-label="{t("Three editorial completion checks, all measured from zero to 100 percent.","三项编辑检查，均使用0%至100%的完成率刻度。")}" data-information-visual>'
 # A single bright proof sheet leaves ample white space around every measurement.
 b+=f'<rect x="7" y="8" width="1666" height="556" fill="{BLUSH}" opacity=".14"/><rect x="0" y="0" width="1666" height="552" fill="{BRIGHT}"/><path d="M30 28V521" stroke="{RED}" stroke-opacity=".55"/>'
 for i,(en,zh,value,target) in enumerate(TARGETS):
  y=18+i*174;x=887;scale=6.7;step=i*3;delta=value-target
  note=t(f'{abs(delta)} percentage {"point" if abs(delta)==1 else "points"} {"above" if delta>=0 else "below"} target',f'{"高于目标" if delta>=0 else "距目标还差"} {abs(delta)} 个百分点')
  if i:b+=f'<path d="M65 {y-5}H1620" stroke="{INK}" stroke-opacity=".16"/>'
  b+=f'<text x="65" y="{y+62}" fill="{INK}" class="ed-check-title">{t(en,zh)}</text><text x="65" y="{y+117}" font-size="26" fill="{RED}">{note}</text>'
  b+=f'<text x="600" y="{y+112}" class="ed-check-value" fill="{INK}" data-chart-motion="fade" data-chart-step="{step+1}">{value}<tspan class="ed-check-percent">%</tspan></text>'
  b+=f'<rect x="{x}" y="{y+67}" width="670" height="14" fill="{MUTED}"/><rect x="{x}" y="{y+67}" width="{value*scale}" height="14" fill="{RED}" data-chart-motion="grow-x" data-chart-step="{step}"/>'
  b+=f'<path d="M{x+target*scale} {y+49}v50" stroke="{INK}" stroke-width="2" data-chart-motion="fade" data-chart-step="{step+2}"/><text x="{x+target*scale}" y="{y+31}" text-anchor="middle" font-size="25" fill="{INK}" data-chart-motion="fade" data-chart-step="{step+2}">{t("Target","目标")} {target}%</text>'
  for v in (0,50,100):b+=f'<text x="{x+v*scale}" y="{y+133}" text-anchor="middle" font-size="23" fill="#78676c">{v}%</text>'
 b+='</svg></div></section>'
 return [a,b]

def validate_data():
 assert all(0<=v<=100 and 0<=g<=100 for _,_,v,g in TARGETS)
 assert TARGETS[1][2]>TARGETS[1][3]
 assert [v-t for _,_,v,t in TARGETS]==[-4,1,-11]
 return {'passed':True,'axis':[0,100],'targets':TARGETS,'over_target_preserved':True,'differences_percentage_points':[-4,1,-11]}
