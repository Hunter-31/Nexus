let num1 = Number(prompt("Enter first number"));
let num2 = Number(prompt("Enter second number"));

let choice = Number(prompt(
    "1.Addition\n2.Subtraction\n3.Multiplication\n4.Division"
));

switch(choice) {

    case 1:
        alert("Addition = " + (num1 + num2));
        break;

    case 2:
        alert("Subtraction = " + (num1 - num2));
        break;

    case 3:
        alert("Multiplication = " + (num1 * num2));
        break;

    case 4:
        alert("Division = " + (num1 / num2));
        break;

    default:
        alert("Invalid Choice");
}