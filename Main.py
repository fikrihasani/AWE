from flask import Flask
import sqlite3
from flask import render_template, url_for
from controllers.Web import Web
from Database import Database
from Models.Users import Users
app = Flask(__name__)
app.secret_key="__privatekey"

web = Web()
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def homepage():
    return render_template("home.html",articles=articles)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/otp")
def otp():
    return render_template("otp.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/essay")
def essay():
    result = web.result()
    return render_template("essay.html", result = result)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('homepage'))
    return render_template('create.html')

if __name__=='__main__':
    app.run(debug=True)
    

