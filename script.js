"use strict";
let count = 0;
function increment() {
    count++;
    document.getElementById("count").innerText = count.toString();
}