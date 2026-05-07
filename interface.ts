interface Person {
    name: string;
    age: number;
    display(): void;
}
class Employee implements Person {
    name: string;
    age: number;
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
    display(): void {
        console.log("Name: "+this.name);
        console.log("Age: "+this.age);
    }
}
let e1 = new Employee("Sahil", 21);
e1.display();