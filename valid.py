from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():

    return '''
    <h1>Validation using AJAX</h1>

    Username :
    <input type="text" id="name">

    <br><br>

    <button onclick="check()">Validate</button>

    <p id="result"></p>

    <script>

    function check()
    {
        // Get username
        var name = document.getElementById("name").value;

        // Create AJAX object
        var xhr = new XMLHttpRequest();

        // Handle response
        xhr.onload = function()
        {
            document.getElementById("result").innerHTML =
            this.responseText;
        };

        // Send request
        xhr.open("GET", "/check?name=" + name, true);

        xhr.send();
    }

    </script>
    '''

@app.route('/check')
def check():

    name = request.args.get("name")

    if name == "admin":
        return "Username Already Taken"

    else:
        return "Username Available"


if __name__ == "__main__":
    app.run(debug=True)