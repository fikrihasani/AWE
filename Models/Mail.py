from flask import Flask, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'emily.heart112@gmail.com'
app.config['MAIL_PASSWORD'] = 'hjea btfl hxwe zune'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

class Mail:
    def send_verification(self, email, token):
        msg = Message('AAPE Verification', sender = 'aape.binus@gmail.com', recipients = [email])
        link = url_for('confirm_email', token = token, _external = True)
        msg.body = "Click on this link to verify your account: {}".format(link)
        mail.send(msg)