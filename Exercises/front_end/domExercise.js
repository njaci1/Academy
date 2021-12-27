// var tdText1 = document.querySelector("td");
//
// tdText1.addEventListener('click', function(){tdText1.innerText = "X";tdText1.style.color = "blue"});
// tdText1.addEventListener()

// tdText1.addEventListener("click", function () {
//   tdText1.style.color = 'red';
// })


//restart button
var restart = document.querySelector("button");


//grab all the cells
var cells = document.querySelectorAll("td");

//clear cell content
function clearCells(){
  for (var i = 0; i < cells.length; i++) {
    cells[i].textContent = "";
  }
}

//call clearCells Function with addEventListener

restart.addEventListener('click', clearCells);

//Change cell Text Function
function changeMaker(){
  if (this.textContent === "") {
    this.textContent ="X";
  }else if (this.textContent ==="X") {
    this.textContent = "O";
  }else {
    this.textContent = "";
  }
}

//call changeMaker upon click on any cells
for (var i = 0; i < cells.length; i++) {
  cells[i].addEventListener('click',changeMaker);
}
