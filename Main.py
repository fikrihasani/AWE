from flask import Flask
import sqlite3
from flask import render_template, url_for, request, redirect
from controllers.Web import Web
from Database import Database
from Models.Users import Users
from Models.Article import Article

app = Flask(__name__)
app.secret_key="__privatekey__"

web = Web()
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def homepage():
    article = Article()
    data = article.getOne(1)
    return render_template("home.html", articles=data)
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=('GET', 'POST'))
def register():

    if request.method == 'POST':
        username  = request.form['username']
        email  =  request.form['email']
        password = request.form['password']

        user = Users()
        user.insert(username, email, password)

        return redirect(url_for('homepage'))

    return render_template("register.html")

@app.route("/otp")
def otp():
    return render_template("otp.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/essay", methods=('GET', 'POST'))
def essay():
    result = web.result()

    if request.method == 'POST':
        essay  = request.form['essayInput']
        userID = 1

        article = Article()
        article.insert(essay, userID)

        return redirect(url_for('essay'))
    
    return render_template("essay.html", result = result)

@app.route("/printEssay")
def printEssay():
    article = Article()
    data = article.getAll2()
    return render_template("printEssay.html", essays=data)

@app.route('/users')
def users():
    user = Users()
    data = user.getAll()
    return render_template('users.html', users=data)

if __name__=='__main__':
    app.run(debug=True)
    

