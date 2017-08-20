from flask_cors import CORS
from flask import Flask

from api.resources.candidato import candidato_blueprint

import requests, os

app = Flask(__name__)
app.register_blueprint(candidato_blueprint)

CORS(app)

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (user, ", ".join(recipient), subject, body)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, recipient, message)
        server.close()
    except Exception as e:
        print(str(e))