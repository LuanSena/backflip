from flask_restful import Resource

from api.resources.todo.model import Todo


class HelloWorld(Resource):
    def get(self):
        todo = Todo
        return todo.get_name()
