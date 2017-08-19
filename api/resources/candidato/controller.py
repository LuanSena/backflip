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

        for candidato in candidatos:
            obs_list = pg_db_manager.select_candidato_obs(candidato.id)
            candidato.obs = obs_list

        return candidatos

class CandidatoController(Resource):
    def __init__(self):
        pass

    @marshal_with(candidato_fields)
    def get(self, candidato_id):
        candidato = pg_db_manager.select_candidato_by_id(candidato_id)
        if candidato is None:
            abort(404)

        obs_list = pg_db_manager.select_candidato_obs(candidato_id)

        candidato.obs = obs_list

        return candidato

    def post(self):
        content = request.get_json()
        if "headers" in content:
            mail_from = content['envelope']['from']
            mail_to = content['envelope']['to']
            mail_text = content['plain']
            print(mail_from, mail_to, mail_text)
        else:
            nome = content.get('nome')
            idade = content.get('idade', 18)
            cidade = content.get('cidade', "Não informado")
            estado = content.get('estado', "Não informado")
            area = content.get('area', "Não informado")
            subarea = content.get('subarea', "Não informado")
            tags = content.get('tags', "Não informado")
            email = content.get('email', "Não informado")
            telefone = content.get('telefone', "Não informado")
            linkedin = content.get('linkedin', "Não informado")
            github = content.get('github', "Não informado")
            filecontent = content.get('filecontent', "Não informado")
            filetype = content.get('filetype', "Não informado")
            filename = content.get('filename', "Não informado")


            pg_db_manager.insert_candidato(nome, idade, cidade, estado, area, subarea, tags, email, telefone,
                                           linkedin, github, filecontent, filetype, filename)
        return

    def put(self, candidato_id):
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

class CandidatoStatusController(Resource):
    def __init__(self):
        pass

    def put(self, candidato_id):
        content = request.get_json()
        candidato_status = content['status']
        candidato_obs = content['obs']
        pg_db_manager.update_candidato_status(candidato_id, candidato_status, candidato_obs)
        return