
  $("dropdown-menu").change(function() {

    $("#photo-showcase-container").empty();
    var filePath = "html/"+$(this).val()+".html";
    alert("this file to get is "+filePath);
    $("#photo-showcase-container").load(filePath);
  });

