// var lbs = prompt("Enter Weight in lb")
// var kgs = lbs * 0.454
// alert("Weight in kilos = "+kgs+" " )
// console.log("Converted")

// var x = 0;
//
// for (var x = 0; x < 5; x++) {
//   console.log("Whello!");
// }
//
// while (x <= 4) {
//   console.log("Hello");
//
//   x++;
//
// }
//
// var i = 0;
//
// for (var i = 0; i <= 25; i++) {
//   if (i%2) {
//     console.log(i);
//
//   }
// }
//
// while (i <= 25) {
//   if (i%2==0) {
//     console.log(i);
//
//   }
//   i++;
//
// }

// var fname = prompt("What's your first name?");
// var lname = prompt("What's your last name?");
// var height = prompt("How tall are you in cm?");
// var age = prompt("How old are you?");
//
// alert("Thank you for your time, see console");
//
// if (fname[0] === lname[0] && age >20 && age <30 && height>=170 ){
//   console.log("You're a spy");
// }else {
//   console.log("nothing here");
// }

// function stringTimes(str, n) {
//   var newStr = "";
//
//   for (var i = 0; i <= n; i++) {
//     newStr += str;
//   }
//     return newStr;
// }
var arr=[];
function classPush(){

  console.log(arr);
  var x = prompt("Type name to add here");
  arr.push(x);
  alert(x + " added to class list!");
  var nextName = prompt("Do you want to add more,display, remove or quit?")
  if (nextName=="add") {
    classPush();
  }else if (nextName=="display") {
    display();
  }else if (nextName=="remove") {
    classPop();
  }else {
    quit();
  }
  console.log(arr);
  return arr;
}

function classPop(){

  var a = prompt("Which name do you want to remove? "+ arr);
  // for (var i = 0; i < array.length; i++) {
  //   if (array[i]==a) {
  //     arr.splice(i,1);
  //   }
  var index = arr.indexOf(a);
  arr.splice(index,1);
  alert(a + " Removed form class list");
  var nextName = prompt("Do you want to add more,display, remove or quit?");

  if (nextName=="add") {
    classPush();
  }else if (nextName=="display") {
    display();
  }else if (nextName=="remove") {
    classPop();
  }else {
    quit();
  }

  console.log(arr);
  return arr;
}

function display(){
  if (arr.length<=0) {
    var response = prompt("No names yet, do you want to add y/n");
    if (response =="y") {
      classPush();
    }else {
      quit();
    }

  }else {
    alert(arr);
    var nextName = prompt("Do you want to add more,display, remove or quit?")
    if (nextName=="add") {
      classPush();
    }else if (nextName=="display") {
      display();
    }else if (nextName=="remove") {
      classPop();
    }else {
      quit();
    }
    console.log(arr);
  }
  return arr;
}

function quit(){
  alert("Thank you and good bye");
  console.log("lefting");
}


var start = prompt("Do you want to add a name y/n");
console.log(start);
if (start =="n" || start =="") {
  quit();
}else if (start ==="y") {
  var next = prompt("Do yo want to add,display,remove or quit");
  if (next=="add") {
    classPush();

  }else if (next=="remove") {
    classPop();

  }else if (next=="display") {
    display();

  }else {
    quit();
  }

}
