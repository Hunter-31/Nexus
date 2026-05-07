from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def home():

    html = """
    <h1>Protected Page</h1>
    <p>Clickjacking protection enabled.</p>
    """

    response = make_response(html)

    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "frame-ancestors 'none'"

    return response


if __name__ == "__main__":
    app.run(debug=True)