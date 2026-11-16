window.animateDeckCharts=function(slide){const animations=[];const line=slide.querySelector('[data-lens-line]');if(line){const length=line.getTotalLength();animations.push(line.animate([{strokeDasharray:`${length} ${length}`,strokeDashoffset:length},{strokeDasharray:`${length} ${length}`,strokeDashoffset:0}],{duration:1050,delay:180,easing:'cubic-bezier(.22,.7,.2,1)',fill:'both'}));}slide.querySelectorAll('[data-lens-area]').forEach(e=>animations.push(e.animate([{opacity:0},{opacity:1}],{duration:850,delay:250,fill:'both'})));slide.querySelectorAll('[data-lens-point]').forEach((e,i)=>animations.push(e.animate([{opacity:0},{opacity:1}],{duration:240,delay:200+i*65,fill:'both'})));slide.querySelectorAll('[data-lens-bar]').forEach((e,i)=>animations.push(e.animate([{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)'}],{duration:750,delay:120+i*110,easing:'cubic-bezier(.22,.7,.2,1)',fill:'both'})));animations.forEach(a=>a.finished.then(()=>a.cancel()).catch(()=>{}));return animations};
;(()=>{
 const original=window.animateDeckCharts;
 window.animateDeckCharts=function(slide){
  const animations=original?.(slide)||[];
  slide.querySelectorAll('[data-lens-motion]').forEach(el=>{
   const kind=el.dataset.lensMotion,step=Number(el.dataset.lensStep)||0;
   let frames;
   if(kind==='draw'&&el.firstElementChild?.getTotalLength){
    el=el.firstElementChild;const length=el.getTotalLength();
    frames=[{strokeDasharray:`${length} ${length}`,strokeDashoffset:length},{strokeDasharray:`${length} ${length}`,strokeDashoffset:0}];
   }else if(kind==='up')frames=[{clipPath:'inset(100% 0 0 0)'},{clipPath:'inset(0% 0 0 0)'}];
   else if(kind==='right')frames=[{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)'}];
   else frames=[{opacity:0},{opacity:1}];
   const a=el.animate(frames,{duration:kind==='fade'?420:900,delay:160+Math.min(step,8)*85,easing:'cubic-bezier(.22,.7,.2,1)',fill:'both'});
   animations.push(a);a.finished.then(()=>a.cancel()).catch(()=>{});
  });
  return animations;
 };
})();

/* Finite, constant-speed radar strokes; cancellation restores the complete chart. */
;(()=>{
 const original=window.animateDeckCharts;
 window.animateDeckCharts=function(slide,...args){
  const animations=original?.(slide,...args)||[];
  function animate(element,frames,timing){
   const a=element.animate(frames,{...timing,easing:'linear',fill:'both'});
   animations.push(a);a.finished.then(()=>a.cancel()).catch(()=>{});
  }
  slide.querySelectorAll('[data-radar-trace]').forEach(el=>{
   const length=el.getTotalLength(),series=el.dataset.radarTrace==='series';
   animate(el,[{strokeDasharray:`${length} ${length}`,strokeDashoffset:length},{strokeDasharray:`${length} ${length}`,strokeDashoffset:0}],{
    duration:series?1250:650,delay:series?Number(el.dataset.radarDelay):120
   });
  });
  slide.querySelectorAll('[data-radar-fill]').forEach(el=>{
   const data=el.dataset.radarFill==='data';
   animate(el,[{opacity:0},{opacity:1}],{duration:data?500:450,delay:data?1200:120});
  });
  slide.querySelectorAll('[data-radar-point]').forEach(el=>{
   animate(el,[{opacity:0},{opacity:1}],{duration:180,delay:Number(el.dataset.radarDelay)});
  });
  return animations;
 };
})();

/* The player owns both loops, so navigation, edit, export and motion-off cancel them. */
;(()=>{
 function coverLayers(slide){
  if(!slide.classList.contains('lens-cover'))return null;
  const slot=slide.querySelector('[data-artwork-slot="lens-cover"]');
  if(slot?.dataset.artworkId!=='layered-lenses')return null;
  let body=slot.querySelector('.lens-cover-body'),shadow=slot.querySelector('.lens-cover-shadow');
  if(body&&shadow)return {body,shadow};
  const original=slot.querySelector('img');
  if(!original)return null;
  const source=original.getAttribute('src'),comma=source.indexOf(',');
  if(!source.startsWith('data:image/svg+xml'))return null;
  const xml=source.slice(0,comma).includes(';base64')
   ?new TextDecoder().decode(Uint8Array.from(atob(source.slice(comma+1)),c=>c.charCodeAt(0)))
   :decodeURIComponent(source.slice(comma+1));
  const svg=new DOMParser().parseFromString(xml,'image/svg+xml').documentElement;
  if(svg.localName!=='svg'||!svg.querySelector('[data-ground-shadow]'))return null;
  const bodySvg=svg.cloneNode(true),shadowSvg=svg.cloneNode(true);
  bodySvg.querySelectorAll('[data-ground-shadow]').forEach(el=>el.remove());
  [...shadowSvg.children].forEach(el=>{if(el.localName!=='defs'&&!el.hasAttribute('data-ground-shadow'))el.remove()});
  function layer(svg,kind){
   const img=new Image();img.className=`lens-cover-${kind}`;img.draggable=false;
   img.alt=kind==='body'?original.alt:'';
   if(kind==='shadow')img.setAttribute('aria-hidden','true');
   img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(new XMLSerializer().serializeToString(svg));
   return img;
  }
  body=layer(bodySvg,'body');shadow=layer(shadowSvg,'shadow');
  original.classList.add('lens-cover-original');
  slot.append(shadow,body);
  return {body,shadow};
 }
 const original=window.animateDeckCharts;
 window.animateDeckCharts=function(slide,...args){
  const animations=original?.(slide,...args)||[],layers=coverLayers(slide);
  if(!layers)return animations;
  const timing={duration:5600,delay:600,iterations:Infinity,easing:'ease-in-out'};
  const body=layers.body.animate([
   {transform:'translateY(0px)'},{transform:'translateY(-12px)'},{transform:'translateY(0px)'}
  ],timing);
  const shadow=layers.shadow.animate([
   {transform:'scale(1)',opacity:1},
   {transform:'scale(1.075,1.1)',opacity:.74},
   {transform:'scale(1)',opacity:1}
  ],timing);
  body.id='lens-cover-float';shadow.id='lens-cover-ground';
  // Use the same clock so both phases remain aligned even after long playback.
  body.startTime=shadow.startTime=document.timeline.currentTime;
  return animations.concat(body,shadow);
 };
})();

/* Finite entrance owned by the player: replay on entry, cancel for static output. */
;(()=>{
 const previous=window.animateDeckCharts;
 window.animateDeckCharts=function(slide,...args){
  const animations=previous?.(slide,...args)||[];
  const art=slide.querySelector('.principles-art');
  if(art){
   const animation=art.animate([
    {opacity:0,transform:'translateY(24px) scale(.94)'},
    {opacity:1,transform:'translateY(0) scale(1)'}
   ],{duration:900,delay:160,easing:'cubic-bezier(.2,.8,.2,1)',fill:'both'});
   animation.id='lens-principles-entry';
   animations.push(animation);
   animation.finished.then(()=>animation.cancel()).catch(()=>{});
  }
  return animations;
 };
})();
