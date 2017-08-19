from flask import request
from flask_restful import Resource

from api.db import pg_db_manager


class ReceiveMail(Resource):
    def post(self):
        content = request.get_json()
        if "headers" in content:
            mail_from = content['envelope']['from']
            mail_to = content['envelope']['to']
            mail_text = content['plain']
            print(mail_from, mail_to, mail_text)
        else:
            nome = content['nome']
            idade = content['idade']
            cidade = content['cidade']
            estado = content['estado']
            area = content['area']
            subarea = content['subarea']
            tags = content['tags']
            email = content['email']
            telefone = "123"#content['telefone']
            linkedin = content['linkedin']
            github = content['github']

            pg_db_manager.insert_candidato(nome, idade, cidade, estado, area, subarea, tags, email, telefone,
                                           linkedin, github)
        return

    def put(self):
        content = request.get_json()
        candidato_id = content['id']
        candidato_status = content['status']
        pg_db_manager.update_candidato_status(candidato_id, candidato_status)
        return
