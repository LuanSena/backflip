from flask import request
from flask_restful import Resource, marshal_with, abort

from api.common import hash_generator
from api.resources.candidato.model import Candidato, candidato_fields

from api.db import pg_db_manager

from api import app

import uuid
import os
            
class ListaCandidatosController(Resource):

    def get(self):
        return pg_db_manager.select_candidatos()

class GetCandidatoController(Resource):

    @marshal_with(candidato_fields)
    def get(self, candidato_id):
        candidato = pg_db_manager.select_candidato_by_id(candidato_id)
        if candidato is None:
            abort(404)

        obs_list = pg_db_manager.select_candidato_obs(candidato_id)

        candidato.obs = obs_list

        return candidato

class CandidatosController(Resource):

    def post(self):
        try:
            content = request.get_json()
            
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

            candidato_id = pg_db_manager.insert_candidato(nome, idade, cidade, estado, area, subarea, tags, email, telefone,
                                            linkedin, github, filecontent, filetype, filename)

            fromEmail = content.get('from')
            if fromEmail is None:
                return

            client_hash = uuid.uuid4().hex
            pg_db_manager.insert_linkback(client_hash, candidato_id)

            message = "Ola, complete o seu cadastro utilizando o seguinte link {url}?hash={hash}".format(
                url=os.environ['LINK_BACK_ADDRESS'], 
                hash=client_hash)

            app.send_email(user="hackamunddi@gmail.com", pwd=os.environ['MAIL_PASSWORD'], 
                recipient=fromEmail, subject="Hello HackathonMunddi", body=message)

        except Exception as e:
            print(str(e))

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
        self.update_attr(candidato, content, 'responsavel')
        self.update_attr(candidato, content, 'tags')

        pg_db_manager.update_candidato(candidato)

    def update_attr(self, candidato, content, field):
        if field in content and content[field] is not None: 
            setattr(candidato, field, content[field])

class CandidatoStatusController(Resource):
    
    def put(self, candidato_id):
        content = request.get_json()
        candidato_status = content['status']
        candidato_obs = content['obs']
        pg_db_manager.update_candidato_status(candidato_id, candidato_status, candidato_obs)
        return