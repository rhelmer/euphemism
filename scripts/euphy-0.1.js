$(document).ready(function(){
  $(".container").resizable();
  $(".container").draggable();
  $(".droppable").droppable({
    drop: function() { console.log('dropped'); }
  });
});
