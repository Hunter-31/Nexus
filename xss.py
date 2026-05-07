from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h2>XSS Demo</h2>
        <form action="/show">
            Name: <input name="name">
            <input type="submit">
        </form>
    '''

@app.route("/show")
def show():
    name = request.args.get("name")
    return "<h1>Hello " + name + "</h1>"

if __name__ == "__main__":
    app.run(debug=True)