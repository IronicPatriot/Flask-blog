
let btn = document.getElementById("menuBtn");
let print = document.getElementById("print");

function kill(e) {
    alert("BOO");
    print.innerHTML = "boo again";
    document.querySelector("h1").style.color = "green";
    console.log(e);
}

btn.addEventListener("click", kill );

let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");
let add = document.getElementById("add");

num1.addEventListener("input", sum);
num2.addEventListener("input", sum);


numberTotal.innerHTML = "Your sum is: ";

function sum(){
    let one = parseFloat(num1.value) || 0;
    let two = parseFloat(num2.value) || 0;
    let total = one+two
    numberTotal.innerHTML = "Your sum is: "+total;

}

