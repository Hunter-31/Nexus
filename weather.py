from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == "POST":
        city = request.form['city']
        if city == "Mumbai":
            result = "Temperature is 32 degree Celcius"
        elif city == "Delhi":
            result = "Temperature is 42 degree Celcius"
        else:
            result = "City Not Found"
    return render_template("weather.html", result=result)
app.run(debug=True)