/* Local, offline PDF export. DOM snapshots preserve the deck's fonts, SVG and layout. */
window.exportDeckPDF=async function({slides,meta,progress}){
 await document.fonts.ready;
 const doc=await PDFLib.PDFDocument.create();doc.setTitle(meta.title);doc.setCreator('zhouxing-ppt-skill');
 const fontCSS=[...document.styleSheets].flatMap(sheet=>{try{return [...sheet.cssRules].filter(rule=>rule.type===CSSRule.FONT_FACE_RULE).map(rule=>rule.cssText)}catch{return []}}).join('\n');
 const host=document.createElement('div');host.id='pdf-export-host';host.setAttribute('aria-hidden','true');host.style.cssText='position:fixed;left:-24000px;top:0;width:1920px;height:1080px;pointer-events:none;';document.body.append(host);
 try{
  for(let i=0;i<slides.length;i++){
   progress(i+1,slides.length);await new Promise(r=>setTimeout(r,30));
   const copy=slides[i].cloneNode(true);copy.classList.add('active');copy.style.cssText+=';position:relative;inset:auto;width:1920px;height:1080px;visibility:visible;opacity:1;transform:none;translate:none;scale:none;';
   copy.querySelectorAll('.restart,.slide-dots,#tools-toggle').forEach(e=>e.remove());copy.querySelectorAll('[contenteditable]').forEach(e=>e.removeAttribute('contenteditable'));copy.querySelectorAll('[data-tilt]').forEach(e=>e.style.transform='');host.replaceChildren(copy);
   // html-to-image deep-clones SVG without resolving its descendants' styles.
   // Freeze CSS paints on the export copy so class-based diagrams stay intact.
   const svgPaint=['color','fill','fill-opacity','fill-rule','stroke','stroke-opacity','stroke-width','stroke-linecap','stroke-linejoin','stroke-miterlimit','stroke-dasharray','stroke-dashoffset','opacity','paint-order','vector-effect','stop-color','stop-opacity','flood-color','flood-opacity'];
   copy.querySelectorAll('svg *').forEach(node=>{const computed=getComputedStyle(node);const paint=svgPaint.map(property=>[property,computed.getPropertyValue(property)]);paint.forEach(([property,value])=>{if(value)node.style.setProperty(property,value)})});
   const textProperties=['font-family','font-size','font-weight','font-style','font-stretch','font-variation-settings','font-feature-settings','font-kerning','font-synthesis','letter-spacing','word-spacing','text-anchor','dominant-baseline','alignment-baseline','fill','fill-opacity','stroke','stroke-width','stroke-opacity','paint-order','opacity'];
   const textStyles=[...copy.querySelectorAll('svg text,svg tspan')].map(element=>({element,values:textProperties.map(property=>[property,getComputedStyle(element).getPropertyValue(property)])}));
   textStyles.forEach(({element,values})=>values.forEach(([property,value])=>element.style.setProperty(property,value)));
   const data=await htmlToImage.toJpeg(copy,{width:1920,height:1080,pixelRatio:1.5,quality:.96,fontEmbedCSS:fontCSS,skipAutoScale:true});
   const image=await doc.embedJpg(data);const page=doc.addPage([960,540]);page.drawImage(image,{x:0,y:0,width:960,height:540});host.replaceChildren();
  }
  const bytes=await doc.save();const url=URL.createObjectURL(new Blob([bytes],{type:'application/pdf'}));const a=document.createElement('a');a.href=url;a.download=(meta.download_name||meta.title||'presentation').replace(/\.html?$/i,'')+'.pdf';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),60000);
 }finally{host.remove()}
};
