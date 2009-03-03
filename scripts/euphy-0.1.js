function save(event, ui){
  $.post("/save", {
    id: ui.helper[0].id, 
    left: ui.helper[0].style.left,
    top: ui.helper[0].style.top,
    width: ui.helper[0].style.width,
    height: ui.helper[0].style.height,
  });
}

$(document).ready(function(){
  $(".container").resizable({
    stop: save
  });
  $(".container").draggable({
    stop: save
  });
/*
  $(".container").keydown(function(event){
    save('test');
  });
*/
});
