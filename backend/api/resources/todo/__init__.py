import flask_restful as restful

from flask import Blueprint

from api.resources.todo.controller import HelloWorld

todo_blueprint = Blueprint("Todo", __name__)
app = restful.Api()
app.init_app(todo_blueprint)

app.add_resource(HelloWorld, '/')
