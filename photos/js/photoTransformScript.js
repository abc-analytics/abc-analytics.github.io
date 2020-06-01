//call when photo-page loads
//this script randomizes a few photo attributes, rotation/translateX/scaling
function photoTransformScript() {

var films = document.getElementsByClassName("film");

for (var i = 0; i < films.length; i++) {
  films[i].style.transform = "rotate("+randomRotateBy()+"deg) translateX("+randomTranslateBy()+"%) scale("+randomScaleBy()+")";
}

//return a factor between -10 and 10
function randomRotateBy() {
  var rotateBy = Math.floor( (Math.random()-0.5) * 21 );
  return rotateBy;
}

//return a factor between -10 and 10
function randomTranslateBy() {
  var translateBy = Math.floor( (Math.random()-0.5) * 21 );
  return translateBy;
}

//get a scale factor of [-0.1, 0.1], plus 1 and return
function randomScaleBy() {
  var scaleFactor = ( (Math.random()-0.5) / 5 );
  return (1+scaleFactor);
}

}