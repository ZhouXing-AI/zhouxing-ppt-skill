/* Finite data-chart entrances. Static SVG geometry is always the complete result.
   All effects are returned to the deck, so finish(), editing, HTML save and PDF
   export cancel them without leaving hidden nodes or modified source values. */
window.animateDeckCharts=function(slide,theme){
 const effects=[],focus=theme==='focus';
 const ease=focus?'cubic-bezier(.2,.65,.25,1)':'cubic-bezier(.22,1,.36,1)';
 const duration=focus?1000:850;
 const sankey=slide.matches('.chart-sankey,.fd-sankey'),heatmap=slide.matches('.chart-heatmap,.fd-heatmap'),scatter=slide.matches('.chart-scatter,.fd-scatter');
 const trend=slide.matches('.chart-line,.fd-line,.chart-area,.fd-area');
 const trendBox=trend?slide.querySelector('path[data-chart-motion=draw]')?.getBBox():null;
 slide.querySelectorAll('[data-chart-motion]').forEach((element,index)=>{
  const mode=element.dataset.chartMotion;
  const raw=Number(element.dataset.chartStep??index);
  const step=Number.isFinite(raw)?Math.max(0,Math.min(24,raw)):0;
  let delay=260+step*(heatmap?140:scatter?75:40);
  if(sankey)delay=180+step*220;
  if(trendBox&&(mode==='pop'||mode==='fade')){const b=element.getBBox(),position=Math.max(0,Math.min(1,(b.x+b.width/2-trendBox.x)/trendBox.width));delay=300+position*duration*.9}
  const opacity=getComputedStyle(element).opacity;
  let frames,ms=sankey?520:duration;
  if(mode==='draw'&&typeof element.getTotalLength==='function'){
   const length=element.getTotalLength();
   if(length>0&&Number.isFinite(length))frames=[{strokeDasharray:`${length} ${length}`,strokeDashoffset:length,opacity},{strokeDasharray:`${length} ${length}`,strokeDashoffset:0,opacity}];
  }else if(mode==='grow-y'){
   frames=[{clipPath:'inset(100% 0% 0% 0%)'},{clipPath:'inset(-8px -8px -8px -8px)'}];
  }else if(mode==='grow-x'||mode==='wipe-x'){
   frames=[{clipPath:'inset(0% 100% 0% 0%)'},{clipPath:'inset(-8px -8px -8px -8px)'}];
  }else if(mode==='pop'&&typeof element.getBBox==='function'){
   const box=element.getBBox(),origin=`${box.x+box.width/2}px ${box.y+box.height/2}px`;
   frames=[{opacity:0,scale:'.35',transformOrigin:origin},{opacity,scale:'1',transformOrigin:origin}];ms=focus?650:550;
  }
  if(!frames){frames=[{opacity:0},{opacity}];ms=sankey?380:focus?600:500}
  const effect=element.animate(frames,{duration:ms,delay,easing:mode==='draw'?'ease-in-out':ease,fill:'both'});
  effect.id=`chart-${mode}-${index}`;effect.onfinish=()=>effect.cancel();effects.push(effect);
 });
 return effects;
};
