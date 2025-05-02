from flask_restx import Namespace, Resource, fields
from main.Professor.professores_model import *

professor_ns = Namespace("professores", description="Operações relacionadas aos professores")

professores_model = professor_ns.model("Professores", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "materia": fields.String(required=True, description="Materia lecionada"),
    "observacoes": fields.String(required=True, description="Observacoes acerca do professor"),
    "descricao": fields.String(required=True, description="Descricao da materia"),
    
    
})

#output. É o que vamos enviar/retornar ao usuario. Note que idade e média estão presentes aqui
professores_output_model = professor_ns.model("ProfessoresOutput", {
    "id": fields.Integer(description="ID do aluno"),
    "nome": fields.String(required=True, description="Nome do professor"),
    "materia": fields.String(required=True, description="Materia lecionada"),
    "observacoes": fields.String(required=True, description="Observacoes acerca do professor"),
    "descricao": fields.String(required=True, description="Descricao da materia"),
})

@professor_ns.route('/')
class Professores(Resource):
    #uso marshal_list_with para retornar uma lista de objetos
    @professor_ns.marshal_list_with(professores_output_model)
    def get(self):
        return read_professor()
    
    @professor_ns.expect(professores_model)
    def post(self):
        dados_turmas = professor_ns.payload
        resposta, status_code = create_professor(dados_turmas)
        return resposta, status_code
    
    #Deletar todos as turmas
    def deleta(self):
        resposta, status_code = deleta_professores()
        return resposta, status_code

# GET ID
#DELETA ID
#PUT
@professor_ns.route('/<int:id_professor>')
class ProfessoresId(Resource):

    @professor_ns.marshal_with(professores_output_model)
    def get(self, id_professor):
        return read_professor_id(id_professor)
    
    @professor_ns.expect(professores_model)
    def post(self, id_professor):
        dados_turmas = professor_ns.payload
        resposta, status_code = update_professores(id_professor, dados_turmas)
        return resposta, status_code
    
    def delete(self, id_professor):
        resposta, status_code = delete_professor(id_professor)
        return resposta, status_code