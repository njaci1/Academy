
// Condition Initialization
var nameCondition = false
var ageCondition = false
var heightCondition = false
var petCondition = false



// Input collection
var f_name = prompt("F_name")

var l_name = prompt("L_name")

var age = prompt("age")

var height = prompt("Height")

var petname = prompt("petname")

alert("Ok. Check on the console for result")

// Condition evaluation

if (f_name[0] == f_name[f_name.length-1] || l_name[0] == l_name[l_name.length-1])
    nameCondition = true
if (age > 20 && age < 30)
    ageCondition = true
if (height >= 170)
    heightCondition = true
if (petname[petname.length-1]== "y")
    petCondition = true

// output determination

if (nameCondition && ageCondition && heightCondition && petCondition)
    console.log("You're a spy")
else
console.log("You're not a spy");


     
