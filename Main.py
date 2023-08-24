from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__=='__main__':
    app.run(debug=True)
    

