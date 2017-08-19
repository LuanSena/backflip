import flask_restful as restful
from flask import Blueprint

from api.resources.email.controller import ReceiveMail

email_blueprint = Blueprint("Email", __name__)
app = restful.Api()
app.init_app(email_blueprint)

app.add_resource(ReceiveMail, '/email')
