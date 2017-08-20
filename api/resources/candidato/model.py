from flask_restful import fields

candidato_fields = {
    'id':           fields.Integer,
    'nome':         fields.String,
    'idade':        fields.Integer,
    'email':        fields.String,
    'telefone':     fields.String,
    'linkedin':     fields.String,
    'github':       fields.String,
    'cidade':       fields.String,
    'estado':       fields.String,
    'area':         fields.String,
    'subarea':      fields.String,
    'status':       fields.String,
    'tags':         fields.String,
    'filename':     fields.String,
    'filetype':     fields.String,
    'filecontent':  fields.String,
    'obs':          fields.List(fields.String)
}

class Candidato(object):
    def __init__(self):
        pass