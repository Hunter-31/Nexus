from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    title = ""
    content = ""
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
    return render_template("blog.html", title=title, content=content)
app.run(debug=True)