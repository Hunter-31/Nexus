function showMessage(): void {
    let message: string = "Hello Sahil! This is TypeScript working with HTML.";

    document.getElementById("output")!.innerHTML = message;
}