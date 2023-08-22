from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/about")
def about():
    return "<p>Hello oke oke<p>"



