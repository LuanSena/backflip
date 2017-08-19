import flask_restful as restful

from flask import Blueprint

from api.resources.candidato.controller import CandidatosController
from api.resources.candidato.controller import ListaCandidatosController
from api.resources.candidato.controller import CandidatoStatusController

candidato_blueprint = Blueprint("Candidato", __name__)
app = restful.Api()
app.init_app(candidato_blueprint)

app.add_resource(CandidatosController, '/candidatos', '/candidatos/<candidato_id>')
app.add_resource(ListaCandidatosController, '/candidatos')
app.add_resource(CandidatoStatusController, '/candidatos/<candidato_id>/status')