$(document).ready(function(){
  $(".container").resizable();
  $(".container").draggable({
    stop: function(event, ui){
      $.post("/save", {
        id: ui.helper[0].id, 
        left: ui.helper[0].style.left,
        top: ui.helper[0].style.top,
      });
    }
  });
});
