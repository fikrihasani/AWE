from flask import Flask
from flask import render_template

class Web:
    def __init__(self):
        self.flask = Flask(__name__)
        self.a = 0

    def home(self):
        self.flask.route("/")
        return render_template("home.html")