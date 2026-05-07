from flask import Flask, render_template, request
app = Flask(__name__)
feedbacks = []
@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == "POST":
        Feedback = request.form['Feedback']
        feedbacks.append(Feedback)
    return render_template('feedback.html', data = feedbacks)
app.run(debug=True)