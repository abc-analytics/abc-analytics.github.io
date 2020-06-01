
$(document).ready(function() {

  $("#dropdown-menu").change(function() {
    
    var filePath = "html/"+$(this).val()+".html"; //string of the path to the relevant year html file
    $("#photo-showcase-container").load(filePath); //load that html file in the showcase area
    setTimeout(function(){photoTransformScript()}, 100);
    
  });

});
