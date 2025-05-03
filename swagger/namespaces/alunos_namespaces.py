from flask_restx import Namespace, Resource, fields
from main.Aluno.alunos_model import *

alunos_ns = Namespace("alunos", description="Alunos do sistema escolar")

#Usamos isso para ver os dados que vamos receber do usuario. Note que idade e media não estão presentes aqui
# logo vamos ter que calcular
aluno_model = alunos_ns.model("Alunos", {
    "nome": fields.String(required=True, description="Nome do aluno"),
    "turma_id": fields.Integer(required=True, description="ID da turma associada"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (DD/MM/YYYY)"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre"),
    
})

#output. É o que vamos enviar/retornar ao usuario. Note que idade e média estão presentes aqui
aluno_output_model = alunos_ns.model("AlunoOutput", {
    "id": fields.Integer(description="ID do aluno"),
    "nome": fields.String(description="Nome do aluno"),
    "idade": fields.Integer(description="Idade do aluno"),
    "data_nascimento": fields.String(description="Data de nascimento (DD/MM/YYYY)"),
    "nota_primeiro_semestre": fields.Float(description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(description="Nota do segundo semestre"),
    "media_final": fields.Float(description="Média final do aluno"),
    "turma_id": fields.Integer(description="ID da turma associada"),
})
# -------------------------------------------------------------------------------------------------------------


@alunos_ns.route("/")
class Alunos(Resource):
    # os nomes das funções vão ser os nomes dos verbos http

    # marshal_list_with -> quando a api vai devolver uma lista de objetos
    @alunos_ns.marshal_list_with(aluno_output_model)
    def get(self):
        #Lista com todos os alunos
        return read_alunos()

    #expect -> esperamos que o usuario envie dados para a gente. O body da requisição    
    @alunos_ns.expect(aluno_model)
    def post(self):
        """Cria um novo aluno"""
        data = alunos_ns.payload
        return create_alunos(data) 
    def delete(sef):
        return delete_alunos()

@alunos_ns.route("/<int:id_aluno>")
class AlunoId(Resource):

    #marshal_with -> quando a api vai devolver alguma coisa
    @alunos_ns.marshal_with(aluno_output_model)
    def get(self, id_aluno):
        return read_alunos_id(id_aluno)
    
    @alunos_ns.expect(aluno_model)
    def get(self, id_aluno):
        """Obtém um aluno pelo ID"""
        return read_alunos_id(id_aluno)

    #ATUALIZAR ALUNO POR ID
    @alunos_ns.expect(aluno_model)
    def put(self, id_aluno):
        data = alunos_ns.payload
        return update_alunos(id_aluno, data)



    #DELETAR ALUNO POR ID
    def delete(self, id_aluno):
        return delete_aluno(id_aluno)