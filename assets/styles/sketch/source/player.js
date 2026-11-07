/* === PRESENTATION STATE === */
(()=>{const $=s=>document.querySelector(s),slides=[...document.querySelectorAll('.slide')],stage=$('#stage'),controls=$('.controls');const meta=JSON.parse($('#deck-meta').textContent);let current=0,enabled=!matchMedia('(prefers-reduced-motion: reduce)').matches,animations=[],editing=false,timer,pdfBusy=false;
const dictionaries=JSON.parse($('#deck-ui').textContent),ui=dictionaries[(meta.ui_lang||meta.lang||'en').startsWith('zh')?'zh':'en'];
const label=(key,values={})=>ui[key].replace(/\{(\w+)\}/g,(_,k)=>values[k]??'');
[['#prev','prev'],['#next','next'],['#count','count'],['.controls','tools'],['.slide-dots','navigation']].forEach(([q,k])=>$(q).setAttribute('aria-label',label(k)));
$('#tools-toggle').setAttribute('aria-label',label('tools')+' (T)');$('#tools-toggle').title=label('tools_short');
[['#download-pdf','pdf'],['#edit','edit'],['#save','save'],['#close-overview','close']].forEach(([q,k])=>$(q).textContent=label(k));

function fit(){const full=!!document.fullscreenElement,w=document.documentElement.clientWidth,h=document.documentElement.clientHeight,reserve=full?0:78,scale=Math.min((w-(full?0:24))/1920,(h-reserve-(full?0:24))/1080);document.documentElement.style.setProperty('--scale',scale);document.documentElement.style.setProperty('--ui-scale',Math.min(1/scale,2));document.documentElement.style.setProperty('--touch-ui-scale',1/scale);stage.style.top=(h-reserve)/2+'px'}

function finish(){animations.forEach(a=>{try{a.finish();a.cancel()}catch{a.cancel()}});animations=[]}
const tiltOrigins=new Map([...document.querySelectorAll('[data-tilt]')].map(e=>[e,e.style.transform]));
function resetTilts(){tiltOrigins.forEach((initial,e)=>e.style.transform=initial)}
/* SKETCH: quick ink reveals, a small paper tilt, and strokes drawn into place. */
function play(){finish();if(!enabled||editing)return;const s=slides[current],ease='cubic-bezier(.2,.8,.2,1)';
const enter=(e,frames,duration,delay)=>animations.push(e.animate(frames,{duration,delay,easing:ease,fill:'both'}));
s.querySelectorAll('.reveal:not([data-chart-container])').forEach((e,i)=>enter(e,[{opacity:0,translate:'0 12px'},{opacity:1,translate:'0 0'}],450,40+Math.min(i,7)*45));
s.querySelectorAll('.art-entrance').forEach((e,i)=>enter(e,[{opacity:0,rotate:'-3deg'},{opacity:1,rotate:'0deg'}],600,90+i*70));
s.querySelectorAll('.draw-line').forEach((e,i)=>enter(e,[{scale:'0 1'},{scale:'1 1'}],500,120+i*55));
s.querySelectorAll('[data-chart-container]').forEach(e=>animations.push(e.animate([{opacity:0},{opacity:1}],{duration:260,delay:160,easing:'ease-out',fill:'both'})));
animations.push(...(window.animateDeckCharts?.(s,meta.style)||[]));
}
function go(n){if(pdfBusy)return;finish();current=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,i)=>{s.classList.toggle('active',i===current);s.setAttribute('aria-hidden',String(i!==current))});$('#count').textContent=String(current+1).padStart(2,'0')+' / '+String(slides.length).padStart(2,'0');[...$('.slide-dots').children].forEach((b,i)=>{b.dataset.passed=String(i<current);if(i===current)b.setAttribute('aria-current','step');else b.removeAttribute('aria-current')});$('#prev').disabled=current===0;$('#next').disabled=current===slides.length-1;stage.dataset.navTone=slides[current].dataset.tone==='dark'?'dark':(slides[current].dataset.navTone||(slides[current].dataset.tone==='orange'?'warm':'light'));document.body.dataset.pointerTone=stage.dataset.navTone;document.title=slides[current].dataset.title+' · '+meta.title;if(location.hash!=='#'+(current+1))history.replaceState(null,'','#'+(current+1));play()}
function overview(open){finish();hidePointer();setTools(false);$('.overview').classList.toggle('open',open);$('.overview').setAttribute('aria-hidden',String(!open));if(open)$('#close-overview').focus();else $('#tools-toggle').focus()}
function toast(text){$('.toast').textContent=text;$('.toast').classList.add('show');setTimeout(()=>$('.toast').classList.remove('show'),2600)}
$('.overview header span').textContent=meta.title+' / '+label('contents');$('.slide-dots').replaceChildren();slides.forEach((s,i)=>{const dot=document.createElement('button');dot.type='button';const tip=document.createElement('span');tip.className='nav-tip';tip.textContent=String(i+1).padStart(2,'0')+' / '+slides.length+' · '+s.dataset.title;dot.append(tip);dot.setAttribute('aria-label',label('slide_label',{n:i+1,total:slides.length,title:s.dataset.title}));dot.onclick=()=>go(i);$('.slide-dots').append(dot);const button=document.createElement('button');const number=document.createElement('b'),titleNode=document.createElement('span');number.textContent=String(i+1).padStart(2,'0');titleNode.textContent=s.dataset.title;button.append(number,titleNode);button.onclick=()=>{overview(false);go(i)};$('.overview-grid').append(button)});
$('#prev').onclick=()=>go(current-1);$('#next').onclick=()=>go(current+1);$('#count').onclick=()=>overview(true);$('#close-overview').onclick=()=>overview(false);$('#motion').onclick=()=>{enabled=!enabled;$('#motion').textContent=label(enabled?'motion_on':'motion_off');$('#motion').setAttribute('aria-pressed',String(enabled));enabled?play():finish();if(!enabled){hidePointer();resetTilts()}};$('#motion').textContent=label(enabled?'motion_on':'motion_off');$('#motion').setAttribute('aria-pressed',String(enabled));
async function fullscreen(){try{if(document.fullscreenElement)await document.exitFullscreen();else if(document.documentElement.requestFullscreen)await document.documentElement.requestFullscreen();else toast(label('fullscreen_hint'))}catch{toast(label('fullscreen_hint'))}}
$('#full').onclick=fullscreen;
let toolsTimer=null;
function cancelToolsHide(){clearTimeout(toolsTimer);toolsTimer=null}
function setTools(open){const visible=!document.fullscreenElement||editing||matchMedia('(hover:none)').matches||open;document.body.classList.toggle('tools-open',visible);$('#tools-toggle').setAttribute('aria-expanded',String(visible));controls.setAttribute('aria-hidden',String(!visible));controls.inert=!visible}
function hideToolsLater(){if(!document.fullscreenElement||toolsTimer!==null)return;toolsTimer=setTimeout(()=>{toolsTimer=null;if(!controls.matches(':hover')&&!controls.querySelector(':focus-visible'))setTools(false)},120)}
function fullLabel(root=document,full=!!document.fullscreenElement){const button=root.querySelector('#full');button.querySelector('.full-label').textContent=label(full?'exit_full':'full');button.setAttribute('aria-label',label(full?'exit_full':'full'));button.title=label(full?'exit_full':'full')+' (F)';button.querySelector('path').setAttribute('d',full?'M3 8h5V3M16 3v5h5M21 16h-5v5M8 21v-5H3':'M8 3H3v5M16 3h5v5M21 16v5h-5M8 21H3v-5')}
fullLabel();
$('#tools-toggle').onclick=()=>{setTools(!document.body.classList.contains('tools-open'));hideToolsLater()};
controls.addEventListener('pointerenter',cancelToolsHide);controls.addEventListener('pointerleave',hideToolsLater);
document.addEventListener('pointermove',e=>{if(!document.fullscreenElement)return;if(e.clientY>document.documentElement.clientHeight-88||controls.contains(e.target)){cancelToolsHide();setTools(true)}else if(document.body.classList.contains('tools-open'))hideToolsLater()});
document.documentElement.addEventListener('pointerleave',hideToolsLater);
document.addEventListener('fullscreenchange',()=>{cancelToolsHide();document.body.classList.toggle('presenting',!!document.fullscreenElement);if(document.activeElement===$('#full'))document.activeElement.blur();setTools(false);fullLabel();fit()});
/* === LOCAL EDITING AND DOWNLOAD === */
document.querySelectorAll('.slide h1,.slide h2,.slide h3,.slide p,.slide .eyebrow').forEach(e=>e.dataset.edit='true');
function edit(){editing=!editing;finish();hidePointer();setTools(false);document.body.classList.toggle('editing',editing);document.querySelectorAll('[data-edit]').forEach(e=>e.contentEditable=String(editing));$('#edit').textContent=label(editing?'done':'edit');if(editing)toast(label('edit_hint'))}
$('#edit').onclick=edit;
$('#save').onclick=()=>{finish();const clone=document.documentElement.cloneNode(true);window.artworkEditor?.prepareClone(clone);clone.querySelectorAll('[data-tilt]').forEach(e=>e.style.transform='');clone.querySelector('body').classList.remove('editing','presenting','controls-on','tools-open');clone.querySelectorAll('[contenteditable]').forEach(e=>e.removeAttribute('contenteditable'));clone.querySelector('.overview').classList.remove('open');clone.querySelector('.overview-grid').innerHTML='';clone.querySelector('.slide-dots').replaceChildren();themeCursor?.prepareClone(clone);clone.querySelector('.toast').classList.remove('show');clone.querySelector('.toast').textContent='';clone.querySelector('#tools-toggle').setAttribute('aria-expanded','false');clone.querySelector('.controls').setAttribute('aria-hidden','true');clone.querySelector('#edit').textContent=label('edit');fullLabel(clone,false);const blob=new Blob(['<!doctype html>\n'+clone.outerHTML],{type:'text/html'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=(meta.download_name||'presentation.html');a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)};
$('#download-pdf').onclick=async()=>{if(pdfBusy)return;window.artworkEditor?.close();pdfBusy=true;hidePointer();finish();const buttons=[...controls.querySelectorAll('button')],states=buttons.map(b=>b.disabled);buttons.forEach(b=>b.disabled=true);try{await exportDeckPDF({slides,meta,progress:(n,total)=>$('#download-pdf').textContent=label('pdf_progress',{n,total})});toast(label('pdf_done'))}catch(error){console.error(error);toast(label('pdf_error'))}finally{pdfBusy=false;buttons.forEach((b,i)=>b.disabled=states[i]);$('#download-pdf').textContent=label('pdf')}};
/* === KEYBOARD / TOUCH / POINTER === */
document.addEventListener('keydown',e=>{if(window.artworkEditor?.isOpen||pdfBusy||e.isComposing||e.keyCode===229)return;if(editing&&e.key!=='Escape')return;if(e.ctrlKey||e.metaKey||e.altKey)return;if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){if(e.key===' '&&e.target.closest('button'))return;e.preventDefault();go(current+1)}else if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();go(current-1)}else if(e.key==='Home')go(0);else if(e.key==='End')go(slides.length-1);else if(e.key.toLowerCase()==='t'){setTools(!document.body.classList.contains('tools-open'));if(document.body.classList.contains('tools-open'))$('#count').focus()}else if(e.key.toLowerCase()==='f')fullscreen();else if(e.key.toLowerCase()==='o')overview(!$('.overview').classList.contains('open'));else if(e.key.toLowerCase()==='e')edit();else if(e.key==='Escape'){if(editing)edit();setTools(false);overview(false)}});
/* One slide per vertical wheel gesture; ignore inertia, editing, zoom and scrollable UI. */
let wheelLast=0,wheelTotal=0,wheelUsed=false,wheelFlip=-Infinity;
document.addEventListener('wheel',e=>{
 if(window.artworkEditor?.isOpen||pdfBusy||editing||$('.overview').classList.contains('open')||e.ctrlKey||e.metaKey||e.altKey||e.target.closest('input,textarea,select,[contenteditable="true"],.controls,.overview'))return;
 if(Math.abs(e.deltaY)<=Math.abs(e.deltaX)||!e.deltaY)return;
 e.preventDefault();const now=performance.now();
 if(now-wheelLast>120){wheelTotal=0;wheelUsed=false}wheelLast=now;
 if(wheelUsed||now-wheelFlip<300)return;
 const delta=e.deltaY*(e.deltaMode===1?16:e.deltaMode===2?innerHeight:1);
 if(wheelTotal&&Math.sign(delta)!==Math.sign(wheelTotal))wheelTotal=0;
 wheelTotal+=delta;if(Math.abs(wheelTotal)<2)return;
 wheelUsed=true;wheelFlip=now;go(current+(wheelTotal>0?1:-1));
},{passive:false});
let touch;stage.addEventListener('touchstart',e=>touch=e.touches[0].clientX,{passive:true});stage.addEventListener('touchend',e=>{if(editing||window.artworkEditor?.isOpen)return;const dx=e.changedTouches[0].clientX-touch;if(Math.abs(dx)>50)go(current+(dx<0?1:-1))},{passive:true});
document.querySelectorAll('[data-tilt]').forEach(el=>{const initial=el.style.transform;el.addEventListener('pointermove',e=>{if(!enabled||editing||window.artworkEditor?.isOpen)return;const r=el.getBoundingClientRect();el.style.transform=`perspective(1300px) rotateX(${(e.clientY-r.top-r.height/2)/r.height*-2.4}deg) rotateY(${(e.clientX-r.left-r.width/2)/r.width*3.2}deg)`});el.addEventListener('pointerleave',()=>el.style.transform=initial)});

/* Approved compact theme cursor. Editing and controls keep native affordances. */
const themeCursor=window.createThemeCursor?.({stage,theme:meta.style,canUse:()=>enabled&&!editing&&!pdfBusy&&!window.artworkEditor?.isOpen&&!$('.overview').classList.contains('open')});
function hidePointer(){themeCursor?.hide()}


document.querySelectorAll('[data-restart]').forEach(b=>b.onclick=()=>go(0));matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change',e=>{if(e.matches){enabled=false;finish();resetTilts();$('#motion').textContent=label('motion_off');$('#motion').setAttribute('aria-pressed','false')}});window.addEventListener('resize',fit);window.deck={go,finish,get current(){return current},get motion(){return enabled},get busy(){return pdfBusy}};setTools(false);fit();go(Math.max(0,(parseInt(location.hash.slice(1))||1)-1));document.fonts.ready.then(fit);
})();
