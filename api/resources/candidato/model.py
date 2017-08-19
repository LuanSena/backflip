from flask_restful import fields

candidato_fields = {
    'nome':     fields.String,
    'idade':    fields.Integer,
    'email':    fields.String,
    'telefone': fields.String,
    'linkedin': fields.String,
    'github':   fields.String,
    'cidade':   fields.String,
    'estado':   fields.String,
    'area':     fields.String,
    'subarea':  fields.String,
    'status':   fields.String,
    'tags':     fields.String
}

class Candidato(object):
    def __init__(self):
        pass