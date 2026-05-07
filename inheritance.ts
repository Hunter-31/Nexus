//single level multi level heirarchical 
class Animal {
    sound(){
        console.log("Animal Sound");
    }
}
class Dog extends Animal {
    bark() {
        console.log("Bark");
    }
}
let s1 = new Dog;
s1.sound();
s1.bark();
class A {
    display1() {
        console.log("Class A");
    }
}
class B extends A {
    display2() {
        console.log("Class 2");
    }
}
class C extends B {
    display3() {
        console.log("Class 3");
    }
}
let m1 = new C;
m1.display1();
m1.display2();
m1.display3();
class Parent {
    show1() {
        console.log("Parent Class")
    }
}
class child1 extends Parent {
    show2() {
        console.log("Child1 Class")
    }
}
class child2 extends Parent {
    show3() {
        console.log("Child2 Class")
    }
}
let h1 = new child1();
h1.show1();
h1.show2();
let h2 = new child2();
h2.show1();
h2.show3();
