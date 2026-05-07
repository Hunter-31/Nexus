from flask import Flask, render_template, request
app =Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home():
    name =""
    skills=""
    if request.method == "POST":
        name = request.form['name']
        skills = request.form['skills']
    return render_template("portfolio.html", name=name, skills=skills)
app.run(debug=True)