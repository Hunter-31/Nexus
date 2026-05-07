import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h2>Login</h2>
        <form action="/login">
            Username: <input name="user">
            <input type="submit">
        </form>
    '''

@app.route("/login")
def login():

    user = request.args.get("user")

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + user + "'"

    cursor.execute(query)
    data = cursor.fetchall()

    return str(data)

if __name__ == "__main__":
    app.run(debug=True)