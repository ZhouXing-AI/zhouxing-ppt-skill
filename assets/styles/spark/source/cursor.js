/* SPARK solid lightning wedge at two-thirds size (~23px), with a finite two-slice trail. */
window.createThemeCursor=function({stage,theme,canUse}){
 const source=document.getElementById('cursor-art');if(!source||!stage)return null;
 const config=JSON.parse(source.textContent),fine=matchMedia('(hover:hover) and (pointer:fine)'),reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const renderScale=config.renderScale??1,hotspot=config.hotspot.map(v=>v*renderScale);
 const cursor=document.createElement('div');cursor.className='theme-cursor';cursor.dataset.theme=theme;
 cursor.style.setProperty('--cursor-size',(config.frameSize*renderScale)+'px');
 cursor.dataset.hotspotX=hotspot[0];cursor.dataset.hotspotY=hotspot[1];cursor.dataset.bodySize=config.bodySize*renderScale;
 cursor.setAttribute('aria-hidden','true');document.body.append(cursor);
 let art,body,tail,particles=[],variant='',visible=false,hasPosition=false,x=0,y=0,mx=0,my=0,mt=0,moving=false;
 let dirX=.707,dirY=.707,lastToneCheck=-Infinity,fade=null,clickAnimations=[];
 const interactive='button,a,input,textarea,select,[contenteditable="true"],[role="button"],.slide-dots,#tools-toggle';
 const svgNode=(tag,attrs)=>{const node=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.entries(attrs).forEach(([k,v])=>node.setAttribute(k,v));return node};
 function stopTail(){if(fade){fade.cancel();fade=null}if(tail)tail.style.opacity='0'}
 function cancelClick(){clickAnimations.forEach(a=>a.cancel());clickAnimations=[]}
 function hide(){if(document.body.classList.contains('themed-pointer'))document.body.classList.remove('themed-pointer');cursor.classList.remove('visible');visible=false;moving=false;stopTail();cancelClick()}
 function eligible(target){return fine.matches&&!reduced.matches&&canUse()&&target instanceof Element&&stage.contains(target)&&!target.closest(interactive)}
 function fallbackTone(){return stage.querySelector('.slide.active')?.dataset.tone==='dark'?'dark':'light'}
 function pickTone(target){
  const override=target.closest('[data-cursor-tone]')?.dataset.cursorTone;if(config.variants[override])return override;
  // Split layouts can have transparent text/SVG layers spanning both fields.
  // Resolve the field beneath the pointer before using the event target's ancestors.
  const split=stage.querySelector('.slide.active.split,.slide.active[data-cursor-split]');
  if(split){
   const field=[...split.querySelectorAll('[data-cursor-half],.contrast-half')].find(node=>{const r=node.getBoundingClientRect();return x>=r.left&&x<r.right&&y>=r.top&&y<=r.bottom});
   if(field){
    const tone=field.dataset.cursorTone;if(config.variants[tone])return tone;
    const color=getComputedStyle(field).backgroundColor.match(/[\d.]+/g)?.map(Number);
    if(color&&color.length>=3&&(color.length<4||color[3]>.85)){const [r,g,b]=color;return (.2126*r+.7152*g+.0722*b)/255<.3?'dark':'light'}
   }
   const r=split.getBoundingClientRect(),sides=(split.dataset.cursorSplit||'light-dark').split('-'),side=x<r.left+r.width/2?0:1;
   if(config.variants[sides[side]])return sides[side];
  }
  let node=target;
  while(node&&stage.contains(node)){
   const color=getComputedStyle(node).backgroundColor.match(/[\d.]+/g)?.map(Number);
   if(color&&color.length>=3&&(color.length<4||color[3]>.85)){
    const [r,g,b]=color,luma=(.2126*r+.7152*g+.0722*b)/255;return luma<.3?'dark':'light';
   }
   if(node===stage)break;node=node.parentElement;
  }
  return fallbackTone();
 }
 function setVariant(next){
  if(next===variant)return;
  stopTail();cancelClick();variant=next;cursor.dataset.tone=next;
  cursor.innerHTML=config.variants[next]||config.svg;art=cursor.querySelector('svg');body=art.querySelector('[data-part="body"]');
  body.style.transformOrigin=config.hotspot.join('px ')+'px';
  tail=svgNode('g',{'class':'cursor-trail','data-part':'trail','aria-hidden':'true'});tail.style.opacity='0';
  art.insertBefore(tail,body);particles=[];
  const color=config.trailColors[next];
  // Two small oblique chips follow movement and disappear completely after 160 ms.
  if(theme==='spark')particles=[1,.75].map((size,i)=>svgNode('path',{d:`M${-3*size} ${-1.7*size}H${1.2*size}L${3*size} ${1.7*size}H${-1.2*size}Z`,fill:color,opacity:i?.28:.5}));
  particles.forEach((node,i)=>{node.dataset.trailPiece=i;tail.append(node)});
 }
 function updateTone(target,force=false){const now=performance.now(),split=stage.querySelector('.slide.active.split,.slide.active[data-cursor-split]');if(force||split||now-lastToneCheck>45){setVariant(pickTone(target));lastToneCheck=now}}
 function sync(e){
  if(e.pointerType&&e.pointerType!=='mouse'){hasPosition=false;hide();return false}
  x=e.clientX;y=e.clientY;hasPosition=true;
  if(!eligible(e.target)){hide();return false}
  updateTone(e.target,!visible);cursor.style.transform=`translate3d(${x-hotspot[0]}px,${y-hotspot[1]}px,0)`;
  visible=true;cursor.classList.add('visible');if(!document.body.classList.contains('themed-pointer'))document.body.classList.add('themed-pointer');return true;
 }
 function drawTail(dx,dy,dt){
  const distance=Math.hypot(dx,dy);if(distance<.25)return;
  const nx=-dx/distance,ny=-dy/distance;
  if(dirX*nx+dirY*ny<.2){dirX=nx;dirY=ny}else{dirX=dirX*.3+nx*.7;dirY=dirY*.3+ny*.7;const length=Math.hypot(dirX,dirY);dirX/=length;dirY/=length}
  const center=config.center||[20,20];
  const edge=Math.max(...config.outline.map(([a,b])=>(a-center[0])*dirX+(b-center[1])*dirY));
  const gaps=[4.5,11],angle=Math.atan2(dirY,dirX)*180/Math.PI;
  particles.forEach((node,i)=>{const d=edge+gaps[i],px=center[0]+dirX*d,py=center[1]+dirY*d;node.setAttribute('transform',`translate(${px} ${py}) rotate(${angle})`)});
  // One reusable finite animation, not a stream of new DOM particles or an idle RAF loop.
  const strength=Math.min(1,Math.max(.4,distance/Math.max(8,dt)*2));
  if(fade){fade.effect.setKeyframes([{opacity:strength},{opacity:0}]);fade.currentTime=0;fade.play()}
  else{fade=tail.animate([{opacity:strength},{opacity:0}],{duration:config.trailDuration||160,easing:'ease-out'});const active=fade;active.onfinish=()=>{active.cancel();if(fade===active)fade=null}}
 }
 function animate(node,frames,duration=200){if(!node?.animate)return;const a=node.animate(frames,{duration,easing:'cubic-bezier(.2,.7,.3,1)'});clickAnimations.push(a);a.onfinish=()=>{a.cancel();clickAnimations=clickAnimations.filter(v=>v!==a)}}
 function pulse(){
  cancelClick();
  if(theme==='spark')animate(body,[{transform:'scale(1)'},{transform:'scale(.94)',offset:.35},{transform:'scale(1)'}],150);
 }
 setVariant('light');
 document.addEventListener('pointermove',e=>{
  const previouslyVisible=visible;if(!sync(e))return;const now=performance.now();
  if(previouslyVisible&&moving)drawTail(x-mx,y-my,now-mt);mx=x;my=y;mt=now;moving=true;
 });
 document.addEventListener('pointerover',sync);
 document.addEventListener('pointerdown',e=>{if(sync(e))pulse()});
 document.addEventListener('pointercancel',hide);
 document.documentElement.addEventListener('pointerleave',()=>{hasPosition=false;hide()});
 window.addEventListener('blur',()=>{hasPosition=false;hide()});
 document.addEventListener('visibilitychange',()=>{if(document.hidden){hasPosition=false;hide()}});
 document.addEventListener('focusin',hide);document.addEventListener('fullscreenchange',hide);window.addEventListener('resize',hide);
 fine.addEventListener('change',hide);reduced.addEventListener('change',hide);
 const observer=new MutationObserver(()=>{
  if(!canUse()){hide();return}
  if(visible&&hasPosition){const target=document.elementFromPoint(x,y);if(!eligible(target)){hide();return}updateTone(target,true)}
 });
 observer.observe(document.body,{attributes:true,attributeFilter:['class']});
 const overview=document.querySelector('.overview');if(overview)observer.observe(overview,{attributes:true,attributeFilter:['class']});
 observer.observe(stage,{attributes:true,attributeFilter:['data-nav-tone']});
 return {hide,prepareClone(root){root.querySelector('body').classList.remove('themed-pointer');root.querySelectorAll('.theme-cursor').forEach(node=>node.remove())}};
};
