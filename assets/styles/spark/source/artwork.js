/* SPARK: local artwork library. Assets and selections travel with downloaded HTML. */
(()=>{
'use strict';
const payload=document.querySelector('#artwork-library');
const trigger=document.querySelector('#replace-artwork');
if(!payload||!trigger)return;
let catalog;try{catalog=JSON.parse(payload.textContent)}catch{return}
const meta=JSON.parse(document.querySelector('#deck-meta').textContent);
const zh=(meta.ui_lang||meta.lang||'en').startsWith('zh');
const L=zh?{
 title:'替换素材',total:n=>n+' 张',close:'关闭素材库',target:'替换位置',preview:'所选素材预览',hint:'仅预览，点击「应用替换」后生效。',collection:'内置素材',filter:'筛选素材',list:'素材列表',save:'替换后，下载 HTML 可保留修改与完整素材库。',reset:'恢复默认',cancel:'取消',apply:'应用替换',all:'全部',defaultPreview:'已预览默认素材，点击应用即可恢复。',current:'这是该页当前使用的素材。',selected:n=>'已选择「'+n+'」。',empty:'当前页没有配图。请选择需要替换的页面。',fit:'素材保持原有位置与比例，页面排版不变。',error:'这张素材暂时无法载入，请重试。'
}:{
 title:'Replace artwork',total:n=>n+' assets',close:'Close artwork library',target:'Replace on',preview:'Selected artwork preview',hint:'Preview only. Apply to update the slide.',collection:'Built-in artwork',filter:'Filter artwork',list:'Artwork collection',save:'Download HTML to keep your changes and the complete library.',reset:'Reset to default',cancel:'Cancel',apply:'Apply artwork',all:'All',defaultPreview:'Default artwork previewed. Apply to restore it.',current:'This artwork is currently used on the slide.',selected:n=>'Selected '+n+'.',empty:'This slide has no artwork. Choose a slide with an illustration.',fit:'The artwork keeps its position and fits the existing layout.',error:'This artwork could not load. Please try again.'
};
const categoryNames={start:{en:'Start',zh:'启动'},shape:{en:'Shape',zh:'塑形'},test:{en:'Test',zh:'试验'},advance:{en:'Advance',zh:'推进'}};
const themeName=(zh?catalog.theme?.zh:catalog.theme?.en)||meta.theme_name_en||meta.title;
const categoryLabel=value=>categoryNames[value]?.[zh?'zh':'en']||value;
const assetLabel=asset=>zh?(asset.name_zh||asset.name_en):asset.name_en;
const assets=catalog.assets||[],byId=new Map(assets.map(asset=>[asset.id,asset]));
trigger.lastChild.textContent=L.title;
trigger.setAttribute('aria-label',L.title);
const slots=[...document.querySelectorAll('.slide [data-artwork-slot]')].filter(slot=>!slot.closest('.text-led'));
const slides=[...document.querySelectorAll('.slide')];
const root=document.querySelector('#artwork-editor-root')||document.body.appendChild(Object.assign(document.createElement('div'),{id:'artwork-editor-root'}));
root.replaceChildren();
let dialog=null,target=null,pending=null,returnFocus=null,filter='all',applying=false;
const $=selector=>dialog.querySelector(selector);
const pageNumber=slot=>slides.indexOf(slot.closest('.slide'))+1;
const slotLabel=slot=>String(pageNumber(slot)).padStart(2,'0')+' · '+(slot.dataset.artworkLabel||slot.closest('.slide').dataset.title);
// Original fluorescent artwork keeps its source palette in every slot.
function sourceFor(asset,slot){return asset.data_url}
function imageFor(asset,slot){const img=new Image();img.src=sourceFor(asset,slot);img.alt=assetLabel(asset)||asset.id;img.draggable=false;return img}
function renderSlot(slot,id){const asset=byId.get(id);if(!asset)return false;slot.dataset.artworkId=id;slot.replaceChildren(imageFor(asset,slot));slot.setAttribute('aria-label',assetLabel(asset)||asset.id);return true}
function refresh(){slots.forEach(slot=>{const id=slot.dataset.artworkId||slot.dataset.artworkDefault;if(byId.has(id)&&(!slot.querySelector('img')||slot.querySelector('img').getAttribute('src')!==sourceFor(byId.get(id),slot)))renderSlot(slot,id)});trigger.disabled=assets.length===0||slots.length===0}
function element(tag,className,text){const node=document.createElement(tag);if(className)node.className=className;if(text!==undefined)node.textContent=text;return node}
function build(){
 dialog=element('dialog','artwork-dialog');dialog.setAttribute('aria-labelledby','artwork-title');
 dialog.innerHTML=`<header class="artwork-header"><div><div class="artwork-eyebrow"></div><h2 id="artwork-title">${L.title} <span class="artwork-total"></span></h2></div><button type="button" class="artwork-close" aria-label="${L.close}">×</button></header>
 <div class="artwork-target-row"><label for="artwork-target">${L.target}</label><select id="artwork-target"></select><p id="artwork-context"></p></div>
 <div class="artwork-workspace"><section class="artwork-preview-panel" aria-label="${L.preview}"><div class="artwork-preview"><img id="artwork-preview-image" alt=""></div><div class="artwork-preview-copy"><span class="artwork-preview-category"></span><h3 id="artwork-preview-title"></h3><p id="artwork-preview-english"></p><p class="artwork-preview-hint">${L.hint}</p></div></section>
 <section class="artwork-collection" aria-label="${L.collection}"><div class="artwork-filters" aria-label="${L.filter}"></div><div class="artwork-grid" aria-label="${L.list}"></div></section></div>
 <footer class="artwork-footer"><div class="artwork-footer-note"><span class="artwork-status" role="status" aria-live="polite"></span><span>${L.save}</span></div><div class="artwork-actions"><button type="button" class="artwork-reset">${L.reset}</button><button type="button" class="artwork-cancel">${L.cancel}</button><button type="button" class="artwork-apply">${L.apply} <span aria-hidden="true">↗</span></button></div></footer>`;
 $('.artwork-eyebrow').textContent=themeName+' / '+(zh?'素材库':'ARTWORK LIBRARY');
 $('.artwork-total').textContent=L.total(assets.length);
 slots.forEach((slot,index)=>{const option=element('option','',slotLabel(slot));option.value=String(index);$('#artwork-target').append(option)});
 $('#artwork-target').addEventListener('change',()=>{target=slots[Number($('#artwork-target').value)];window.deck?.go(pageNumber(target)-1);selectTarget(false)});
 const categories=[...new Set(assets.map(asset=>asset.category).filter(Boolean))];
 [['all',L.all],...categories.map(category=>[category,categoryLabel(category)])].forEach(([value,text])=>{
  const button=element('button','artwork-filter',text);button.type='button';button.dataset.filter=value;button.addEventListener('click',()=>{filter=value;renderGrid()});$('.artwork-filters').append(button);
 });
 $('.artwork-close').onclick=close;$('.artwork-cancel').onclick=close;
 $('.artwork-reset').onclick=()=>{selectAsset(target.dataset.artworkDefault);$('.artwork-status').textContent=L.defaultPreview};
 $('.artwork-apply').onclick=apply;
 dialog.addEventListener('cancel',event=>{event.preventDefault();close()});
 dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)close()}});
 dialog.addEventListener('close',()=>{document.body.classList.remove('artwork-open');if(returnFocus?.isConnected)returnFocus.focus({preventScroll:true})});
 root.append(dialog);
}
function renderGrid(){
 const grid=$('.artwork-grid');grid.replaceChildren();
 dialog.querySelectorAll('.artwork-filter').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.filter===filter)));
 assets.filter(asset=>filter==='all'||asset.category===filter).forEach(asset=>{
  const button=element('button','artwork-card');button.type='button';button.dataset.assetId=asset.id;button.setAttribute('aria-pressed',String(asset.id===pending));button.setAttribute('aria-label',assetLabel(asset)+' / '+asset.name_en);button.title=asset.name_en;
  const visual=element('span','artwork-card-visual'),img=imageFor(asset);img.alt='';img.loading='lazy';visual.append(img);
  const name=element('span','artwork-card-name',assetLabel(asset)),en=element('span','artwork-card-english',zh?asset.name_en:categoryLabel(asset.category)),check=element('span','artwork-card-check','✓');check.setAttribute('aria-hidden','true');
  button.append(visual,name,en,check);button.addEventListener('click',()=>selectAsset(asset.id));grid.append(button);
 });
}
function selectAsset(id){
 const asset=byId.get(id);if(!asset)return;pending=id;
 const image=$('#artwork-preview-image');image.src=sourceFor(asset,target);image.alt=assetLabel(asset);
 $('#artwork-preview-title').textContent=assetLabel(asset);$('#artwork-preview-english').textContent=zh?asset.name_en:(asset.keywords||[]).filter(keyword=>!/[\u3400-\u9fff]/u.test(keyword)).join(' · ');
 $('.artwork-preview-category').textContent=categoryLabel(asset.category)||themeName;
 dialog.querySelectorAll('.artwork-card').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.assetId===id)));
 $('.artwork-status').textContent=id===target.dataset.artworkId?L.current:L.selected(assetLabel(asset));
 $('.artwork-reset').disabled=!byId.has(target.dataset.artworkDefault);
}
function selectTarget(noCurrentArt){
 $('#artwork-target').value=String(slots.indexOf(target));
 const slide=target.closest('.slide');
 $('.artwork-preview').classList.toggle('on-dark',slide.dataset.tone==='dark');
 $('#artwork-context').textContent=noCurrentArt?L.empty:L.fit;
 selectAsset(target.dataset.artworkId||target.dataset.artworkDefault);
}
function open(slot){
 if(window.deck?.busy||applying||!assets.length||!slots.length)return;
 if(dialog?.open)return;
 window.deck?.finish();returnFocus=document.activeElement;
 if(!dialog)build();
 const currentSlide=slides[window.deck?.current||0],currentSlot=slots.find(slot=>slot.closest('.slide')===currentSlide);
 target=slots.includes(slot)?slot:currentSlot||slots[0];filter='all';
 selectTarget(!currentSlot&&!slots.includes(slot));renderGrid();
 document.body.classList.add('artwork-open');dialog.showModal();
 $('.artwork-close').focus({preventScroll:true});
}
function close(){if(applying)return;if(dialog?.open)dialog.close();document.body.classList.remove('artwork-open')}
async function apply(){
 if(applying||!target||!byId.has(pending))return;applying=true;
 const button=$('.artwork-apply');button.disabled=true;
 try{
  const id=pending,asset=byId.get(id),image=imageFor(asset,target);await image.decode();
  target.dataset.artworkId=id;target.replaceChildren(image);target.setAttribute('aria-label',assetLabel(asset)||id);
  window.deck?.go(pageNumber(target)-1);
  target.dispatchEvent(new CustomEvent('artworkchange',{bubbles:true,detail:{slot:target.dataset.artworkSlot,asset:id}}));
  applying=false;close();
 }catch(error){$('.artwork-status').textContent=L.error;console.error(error)}finally{applying=false;button.disabled=false}
}
function prepareClone(clone){
 clone.querySelector('#artwork-editor-root')?.replaceChildren();
 clone.querySelector('body').classList.remove('artwork-open');
 clone.querySelectorAll('[data-artwork-slot]').forEach(slot=>slot.removeAttribute('data-artwork-selected'));
}
trigger.onclick=()=>open();
document.addEventListener('click',event=>{const slot=event.target.closest('[data-artwork-slot]');if(slot&&document.body.classList.contains('editing')){event.preventDefault();open(slot)}});
/* Modal events must never reach presentation hotkeys, swipe or wheel navigation. */
document.addEventListener('keydown',event=>{
 if(!dialog?.open)return;
 if(event.key==='Escape'){event.preventDefault();event.stopImmediatePropagation();close();return}
 if(event.key==='Tab'){
  const focusable=[...dialog.querySelectorAll('button:not(:disabled),select,input,[tabindex="0"]')].filter(node=>node.getClientRects().length);
  const first=focusable[0],last=focusable[focusable.length-1];
  if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus()}else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus()}
 }
 event.stopPropagation();
},true);
document.addEventListener('wheel',event=>{if(dialog?.open)event.stopPropagation()},{capture:true,passive:true});
document.addEventListener('touchend',event=>{if(dialog?.open)event.stopPropagation()},{capture:true,passive:true});
window.artworkEditor={open,close,refresh,prepareClone,get isOpen(){return !!dialog?.open}};
refresh();
})();
