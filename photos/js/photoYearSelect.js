
$(document).ready(function() {

$("#dropdown-menu").change(function() {

  $("#photo-showcase-container").empty();
  var filePath = "html/"+$(this).val()+".html";
  $("#photo-showcase-container").load(filePath);
});

});

