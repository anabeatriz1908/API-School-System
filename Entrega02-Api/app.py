from config import app

#Importando as blueprints
#turma
from main.Turma.turmas_controller import turmas_blueprint
app.register_blueprint(turmas_blueprint)

#professor
from main.Professor.professores_controller import professores_blueprint
app.register_blueprint(professores_blueprint)

#alunos
from main.Aluno.alunos_controller import alunos_blueprint
app.register_blueprint(alunos_blueprint)

if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
)



