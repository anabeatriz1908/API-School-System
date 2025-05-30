from config import app,db
from flask_restx import Api
from swagger.__init__ import api
from swagger import swagger_config

from main.Turma.turmas_controller import turmas_blueprint
from main.Professor.professores_controller import professores_blueprint
from main.Aluno.alunos_controller import alunos_blueprint

#Importando as rotas de conexão com as API
from services.services_reserva import api_bp

app.register_blueprint(api_bp)


app.register_blueprint(turmas_blueprint)
app.register_blueprint(professores_blueprint)
app.register_blueprint(alunos_blueprint)

swagger_config.configure_swagger(app)

api.add_namespace(swagger_config.alunos_ns)
api.add_namespace(swagger_config.professor_ns)
api.add_namespace(swagger_config.turmas_ns)


if __name__ == "__main__":
    with app.app_context():
        if app.config['DEBUG']:
            db.create_all()


    app.run(
        
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )
    