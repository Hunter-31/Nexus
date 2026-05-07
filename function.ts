function add(a: number, b: number): number {
    return a+b;
}
console.log("Add: "+add(5,20));
let sub = function(a: number, b: number): number {
    return a-b;
}
console.log("Sub: "+sub(20,5));
let mul = (a: number, b: number): number => {
    return a*b;
}
console.log("Mul: "+mul(5,20));
function greet(name: string = "User") {
    console.log("Hello" + name);
}
greet();
// ===============================
// 4. Function with Optional Parameter
// ===============================

function greeting(name: string, age?: number): void {

    if(age)
        console.log("Name:", name, "Age:", age);

    else
        console.log("Name:", name);
}
greeting("Sahil", 21);