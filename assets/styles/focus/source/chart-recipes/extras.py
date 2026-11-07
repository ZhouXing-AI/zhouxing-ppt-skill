from html import escape
import json
TARGETS=[('Evidence reviewed','证据复核率',78,85),('Interviews covered','访谈覆盖率',92,80),('Assumptions tested','假设验证率',64,75)]
def get_slides(lang):
 z=lang in ('zh','zh-CN');t=lambda en,zh:zh if z else en
 title=t('Four lenses. One clear decision.','四个视角，一个清楚的决定。')
 cards=[('Observe','Look closely before you name the problem.','Evidence','观察','在定义问题前，<br>先认真看清。','事实线索'),('Frame','Make the question specific enough to act on.','A clear question','界定','把问题缩小到<br>可以行动的范围。','明确问题'),('Test','Turn one important assumption into a small trial.','A useful result','试验','用一次小尝试<br>验证关键假设。','有效结果'),('Decide','Choose a step and make the trade explicit.','A next action','决定','选定下一步，<br>说清楚取舍。','下一步行动')]
 heading=t("Four lenses. One <em>clear decision.</em>",'四个视角，一个<span class="fd-accent">清楚的决定。</span>')
 a=f'<section class="slide focus-data fd-four-cards" data-title="{title}" data-tone="light"><header class="fd-heading"><h2 class="reveal">{heading}</h2><p class="fd-subtitle reveal">{t("Give each part of the decision its own space.","让每个环节，都有独立而明确的空间。")}</p></header><div class="fd-card-grid">'
 for i,(en,ep,eo,zh,zp,zo) in enumerate(cards):
  a+=f'<article class="reveal"><span class="fd-card-number">0{i+1}</span><h3 class="reveal">{t(en,zh)}</h3><p>{t(ep,zp)}</p><div class="fd-card-output">{t(eo,zo)}<span aria-hidden="true">↗</span></div></article>'
 a+='</div></section>'
 title=t('Close the gap with evidence.','用证据，缩小与目标的距离。')
 heading=t('Close the gap with <em>evidence.</em>','用<span class="fd-accent">证据</span>，缩小与目标的距离。')
 b=f'<section class="slide focus-data fd-target dark-page" data-title="{title}" data-tone="dark" data-chart-kind="target" data-chart-unit="percent" data-provenance="illustrative" data-chart-values=\'{json.dumps(TARGETS,ensure_ascii=False)}\'><header class="fd-heading"><h2 class="reveal">{heading}</h2><p class="fd-subtitle reveal">{t("Put progress beside the promise. Decide where attention goes next.","把进展与目标放在一起，确定下一步的着力点。")}</p></header><div class="fd-chart" data-chart-container="true"><svg viewBox="0 0 1680 610" role="img" aria-label="{t("Actual progress and targets share a 0 to 100 percent scale","实际进度与目标使用同一0到100%量尺")}" data-information-visual><title>{title}</title>'
 for i,(en,zh,v,target) in enumerate(TARGETS):
  x=i*580;w=490;scale=w/100;delta=v-target
  if i:b+=f'<line x1="{x-45}" y1="0" x2="{x-45}" y2="590" stroke="#bfd8ca" stroke-opacity=".3"/>'
  b+=f'<text x="{x}" y="43" fill="#e5eee4" font-size="32">{t(en,zh)}</text><g data-chart-motion="fade" data-chart-step="{i}"><text x="{x-4}" y="245" fill="#e5eee4" class="fd-target-big">{v}<tspan class="fd-target-percent">%</tspan></text></g>'
  b+=f'<rect x="{x}" y="343" width="{w}" height="18" fill="#a0d4b6" opacity=".18"/><g data-chart-motion="grow-x" data-chart-step="{i}"><rect x="{x}" y="343" width="{v*scale}" height="18" fill="#a0d4b6"/></g><g data-chart-motion="fade" data-chart-step="{i+1}"><path d="M{x+target*scale} 325v54" fill="none" stroke="#ededeb" stroke-width="3"/><text x="{x+target*scale}" y="301" text-anchor="middle" fill="#e5eee4" font-size="25">{t("Target","目标")} {target}%</text></g>'
  for tick in [0,50,100]:b+=f'<line x1="{x+tick*scale}" y1="390" x2="{x+tick*scale}" y2="399" stroke="#bfd8ca" stroke-opacity=".5"/><text x="{x+tick*scale}" y="433" text-anchor="middle" font-size="23" fill="#bfd8ca">{tick}%</text>'
  note=t(f'{abs(delta)} points {"above" if delta>0 else "below"} target',f'高于目标 {abs(delta)} 个百分点' if delta>0 else f'距目标还差 {abs(delta)} 个百分点')
  b+=f'<line x1="{x}" y1="492" x2="{x+w}" y2="492" stroke="#bfd8ca" stroke-opacity=".3"/><text x="{x}" y="554" font-size="30" fill="#a0d4b6">{note}</text>'
 b+='</svg></div></section>'
 return [a,b]
def validate_data():
 assert all(0<=v<=100 and 0<=t<=100 for _,_,v,t in TARGETS)
 assert TARGETS[1][2]>TARGETS[1][3]
 return {'targets':TARGETS,'axis':[0,100],'over_target_preserved':True,'passed':True}
