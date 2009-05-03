function save(event, ui){
  $.post("/save", {
    id: ui.helper[0].id, 
    left: ui.helper[0].style.left,
    top: ui.helper[0].style.top,
    width: ui.helper[0].style.width,
    height: ui.helper[0].style.height,
  });
}

function saveContent(event){
  $.post("/save/content", {
    text: event.currentTarget.childNodes[0].data,
    dom_id: event.currentTarget.id,
  });
}

$(document).ready(function(){
  $(".container").resizable({
    stop: save
  });
  $(".container").draggable({
    stop: save
  });
  $(".editable").editable();
  $(".post").keydown(function(event){
    saveContent(event);
  });
  $(".comment").keydown(function(event){
    saveContent(event);
  });
});
