from flask_cors import CORS
from flask import Flask

from api.resources.candidato import candidato_blueprint

app = Flask(__name__)
app.register_blueprint(candidato_blueprint)

CORS(app)
