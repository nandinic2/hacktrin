function homeClick() {
  document.getElementById("p1").innerHTML = "Enter info about home.";
  document.getElementById("p1").style.display = "inline";
  document.getElementById("events").style.display = "none";

}

function newsClick(){
  document.getElementById("p1").innerHTML = "Add api here.";
  document.getElementById("p1").style.display = "inline";
  document.getElementById("events").style.display = "none";
}
function events() {
  document.getElementById("events").style.display = "inline";
  document.getElementById("p1").style.display = "none";
}
function washdc() {
  //document.getElementById("washdc").style.display = "inline";
  document.getElementById("washdc").style.visibility = "visible";
}

function ny() {
  document.getElementById("ny").style.display = "inline";
}
