from flask import Flask
from flask import render_template, url_for
from controllers.Web import Web
app = Flask(__name__)

web = Web()

@app.route("/")
def homepage():
    articles = web.home()
    return render_template("home.html",articles=articles)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/essay")
def essay():
    result = web.result()
    return render_template("essay.html", result = result)

if __name__=='__main__':
    app.run(debug=True)
    

