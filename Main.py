from flask import Flask
import sqlite3
from flask import render_template, url_for, request, redirect
from controllers.Web import Web
from Database import Database
from Models.Users import Users

app = Flask(__name__)
app.secret_key="__privatekey__"

web = Web()
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def homepage():
    articles=web.home()
    return render_template("home.html",articles=articles)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=('GET', 'POST'))
def register():

    if request.method == 'POST':
        username  = request.form['username']
        email  =  request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        # cursor = conn.cursor()
        conn.execute('INSERT INTO user (username, email, pass) VALUES (?, ?, ?)',
                       (username, email, password))
        
        conn.commit()
        conn.close()

        return redirect(url_for('homepage'))

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

@app.route('/users')
def users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user')
    users = cursor.fetchall()
    conn.close()
    
    return render_template('users.html', users=users)

    # user = Users()
    # data = user.getAll()
    # for dat in data:
    #     print(dat['email'])
    # return []

if __name__=='__main__':
    app.run(debug=True)
    

