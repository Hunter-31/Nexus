class Student {
    public name: string;
    private age: number;
    protected marks: number;
    constructor(name: string, age: number, marks: number){
        this.name = name;
        this.age = age;
        this.marks = marks;
    }
    public display(): void {
        console.log("Name: " +this.name);
        console.log("Name: " +this.age);
        console.log("Name: " +this.marks);
    }
}
class Result extends Student {
    showMarks() {
        console.log("Result: "+this.marks);
    }
}
let s1 = new Result("Sahil", 21, 85);
console.log("Public Name:" +s1.name);
s1.display();
s1.showMarks();