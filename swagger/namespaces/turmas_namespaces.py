from flask_restx import Namespace, Resource, fields
from main.Turma.turmas_model import *

turmas_ns = Namespace("turmas", description="Operações relacionadas com as turmas")

turmas_model= turmas_ns.model("Turmas", {
    "descricao": fields.String(required=True, description="Matéria ofertada na turma"),
    "professor_id": fields.Integer(required=True, description="ID do professor que leciona a disciplina"),
    "ativo": fields.Boolean(required=True, description="Estado da Turma, se está ativa ou não"),
})

turmas_output_model = turmas_ns.model("TurmaOutput", {
    "id": fields.Integer(description="ID da Turma"),
    "descricao": fields.String(description='Matéria ofertada na turma'),
    "professor_id": fields.Integer(description="ID do professor que leciona a disciplina"),
    "ativo": fields.Boolean(description="Estado da Turma, se está ativa ou não"),
    
})
@turmas_ns.route('/')
class Turmas(Resource):
    @turmas_ns.marshal_list_with(turmas_output_model)
    def get(self):
        return read_turmas()
    
    @turmas_ns.expect(turmas_model)
    def post(self):
        dados_turmas = turmas_ns.payload
        resposta = create_turmas(dados_turmas)
        return resposta
    
    def deleta(self):
        resposta = deleta_turmas()
        return resposta

@turmas_ns.route('/<int:id_turma>')
class TurmasID(Resource):

    @turmas_ns.marshal_with(turmas_output_model)
    def get(self, id_turma):
        return read_turma_id(id_turma)
    
    @turmas_ns.expect(turmas_model)
    def put(self, id_turma):
        dados_turmas = turmas_ns.payload
        resposta = update_turma(id_turma, dados_turmas)
        return resposta
    
    def delete(self, id_turma):
        resposta = delete_turma_por_id(id_turma)
        return resposta
