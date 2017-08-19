from flask import request
from flask_restful import Resource


class ReceiveMail(Resource):
    def post(self):
        content = request.get_json()
        mail_from = content['envelope']['from']
        mail_to = content['envelope']['to']
        mail_text = content['plain']
        print(mail_from, mail_to, mail_text)
        return
