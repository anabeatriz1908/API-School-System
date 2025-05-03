from flask_restx import Api

api = Api(
    version="1.0",
    title="API Escolar",
    description=" Desenvolvimento de API para Alunos, Professores e Turmas",
    doc="/docs",
    mask_swagger=False,
    prefix="/api"
)


