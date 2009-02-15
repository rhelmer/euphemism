function drag(target,e){
  e.dataTransfer.setData('Text',target.id);
}
function drop(target,e){
  var id = e.dataTransfer.getData('Text');
  target.appendChild(document.getElementById(id));
  e.preventDefault();
}
