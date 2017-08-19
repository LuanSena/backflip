from flask import request
from flask_restful import Resource, marshal_with, abort
from api.resources.candidato.model import Candidato, candidato_fields

from api.db import pg_db_manager

class CandidatosController(Resource):
    def __init__(self):
        pass

    @marshal_with(candidato_fields)
    def get(self):

        candidatos = pg_db_manager.select_candidatos()
        if len(candidatos) == 0:
            return []

        return candidatos

class CandidatoController(Resource):
    def __init__(self):
        pass

    @marshal_with(candidato_fields)
    def get(self, candidato_id):
        candidato = pg_db_manager.select_candidato_by_id(candidato_id)
        if candidato is None:
            abort(404)

        return candidato

    def post(self, candidato_id):
        content = request.get_json()
        
        candidato = pg_db_manager.select_candidato_by_id(candidato_id)
        if candidato is None:
            abort(404)

        self.update_attr(candidato, content, 'nome')
        self.update_attr(candidato, content, 'email')
        self.update_attr(candidato, content, 'idade')
        self.update_attr(candidato, content, 'telefone')
        self.update_attr(candidato, content, 'linkedin')
        self.update_attr(candidato, content, 'github')
        self.update_attr(candidato, content, 'cidade')
        self.update_attr(candidato, content, 'estado')
        self.update_attr(candidato, content, 'area')
        self.update_attr(candidato, content, 'subarea')
        self.update_attr(candidato, content, 'tags')

        pg_db_manager.update_candidato(candidato)

    def update_attr(self, candidato, content, field):
        if field in content and content[field] is not None: 
            setattr(candidato, field, content[field])