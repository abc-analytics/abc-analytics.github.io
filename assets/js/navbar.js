//script to include navigation bar (navbar) and its associated css in the page
$(document).ready(function() {
  
  //inserting css and external icon api inside head
  $("head").append('<link rel="stylesheet" href="../assets/css/navbar.css" type="text/css">');
  $("head").append('<script src="https://code.iconify.design/1/1.0.6/iconify.min.js"></script>');
  //inserting navbar html to nav-menu container
  $("#nav-menu-container").load("../assets/html/navbar.html"); 

}); 