from flask import Flask
from config import app
from routTurmas import turmas_blueprint
#from random import randint, random

app = Flask(__name__)

app.register_blueprint(turmas_blueprint)
app.register_blueprint(professor_blueprint)
app.register_blueprint(aluno_blueprint)


if __name__ == '__main__':
    app.run(port=app.config["PORT"], debug= app.config['DEBUG'])