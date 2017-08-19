import os

from flask import render_template
from flask_restful import Resource

from api.resources.todo.model import Todo


class HelloWorld(Resource):
    def get(self):
        path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(path, "index.html")
        with open(file_path) as file:
            content = file.read()
        return render_template(file_path)
