from flask import Flask
import sqlite3
from flask import render_template, url_for, request, redirect, session
from controllers.Web import Web
from Database import Database
from Models.Users import Users
from Models.Article import Article
from Models.Mail import Mail
from random import randint
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'private_key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False


web = Web()
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def homepage():
   # if not session.get("username"):
        #return redirect("/login")
    #article = Article()
   # data = article.getOne(1)
    return render_template("home.html", articles= None, username= None, email= None, password= None)
    

@app.route("/about")
def about():
    if not session.get("username"):
        return redirect("/login")
    return render_template("about.html", username=session['username'], email=session['email'], password=session['pass'])

@app.route("/register", methods=('GET', 'POST'))
def register():

    if request.method == 'POST':
        username  = request.form['username']
        email  =  request.form['email']
        password = request.form['password']

        user = Users()
        randomCode = session['randomcode'] = randint(100000, 999999)
        user_id = user.insert(username, email, password, randomCode)

        return redirect(url_for('otp', email=email, randomCode=randomCode))

    return render_template("register.html")

@app.route("/otp")
def otp():
    email = request.args['email']
    randomCode = request.args['randomCode']
    mail = Mail()
    mail.send_verification(email, randomCode)
    return render_template("otp.html")

@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username  = request.form['username']
        password = request.form['password']

        user = Users()
        tempUser = user.authenticate(username, password)

        if tempUser and tempUser['DefiniteUser'] == 1:
            # make if tempuser definiteuser not == 1, error message for not verified user
            session['username']  = tempUser['username']
            session['email'] = tempUser['email']
            session['pass'] = tempUser['pass']

            return redirect(url_for('homepage'))
        else:
            # error message for username not found
            print('wrong')

    return render_template("login.html")

@app.route("/essay", methods=('GET', 'POST'))
def essay():
    if not session.get("username"):
        return redirect("/login")
    
    result = web.result()

    if request.method == 'POST':
        essay  = request.form['essayInput']
        userID = 1

        article = Article()
        article.insert(essay, userID)

        mdl = SentenceTransformer('all-MiniLM-L6-v2')
        model1 = pickle.load(open("finalized_model_svm_style.model","rb"))
        model2 = pickle.load(open("finalized_model_svm.model","rb"))
        score1 = model1.predict(np.array([mdl.encode(essay)]))[0]
        score2 = model2.predict(np.array([mdl.encode(essay)]))[0]
        print("score 1: " + str(score1) + " score 2: " + str(score2))

        return redirect(url_for('essay'))
    
    

    return render_template("essay.html", result = result, username=session['username'], email=session['email'], password=session['pass'])

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

@app.route('/layout')
def layout():
    return render_template('layout.html', username= None, email= None, password= None)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/confirm/<token>')
def confirm_email(token):
    print(token)
    user = Users()
    tempUser = user.getCode(token)
    if tempUser:
        user.setDefinite(token)
        session['username']  = tempUser['username']
        session['email'] = tempUser['email']
        session['pass'] = tempUser['pass']

        return redirect(url_for('homepage'))

if __name__=='__main__':
    app.run(debug=True)
    

