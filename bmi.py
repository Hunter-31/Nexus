from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == "POST":
        weight = float(request.form['weight'])
        height = float(request.form["height"])
        result = weight/(height*height)
    return render_template("bmi.html", result=result)
app.run(debug=True)
