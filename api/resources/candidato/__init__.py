import flask_restful as restful

from flask import Blueprint

from api.resources.candidato.controller import CandidatoController
from api.resources.candidato.controller import CandidatosController
from api.resources.candidato.controller import CandidatoStatusController

candidato_blueprint = Blueprint("Candidato", __name__)
app = restful.Api()
app.init_app(candidato_blueprint)

app.add_resource(CandidatosController, '/candidatos/')
app.add_resource(CandidatoController, '/candidato/', '/candidato/<candidato_id>')
app.add_resource(CandidatoStatusController, '/candidato/<candidato_id>/status')