from flask import Flask

from api.resources.todo import todo_blueprint

app = Flask(__name__)

app.register_blueprint(todo_blueprint)
