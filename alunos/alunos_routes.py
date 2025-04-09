from flask import Blueprint, request, jsonify
from model_alunos import AlunoNaoEncontrado, create_alunos, read_alunos, read_alunos_id, update_alunos, delete_aluno, delete_alunos


alunos_blueprint = Blueprint('alunos', __name__)

		
@alunos_blueprint.route('/alunos', methods=['POST'])
def create_alunos():
    dados_alunos = request.get_json()
    create_alunos(dados_alunos)
    return read_alunos()


@alunos_blueprint.route('/alunos', methods=['GET'])
def read_alunos():
    return read_alunos()


@alunos_blueprint.route('/alunos/<int:id_aluno>', methods =['GET'])
def read_alunos_id(id_aluno):
    try:
        aluno = read_alunos_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404 


@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['PUT'])
def update_alunos(id_aluno):
    read_alunos_id(id_aluno)
    aluno = request.get_json()
    update_alunos(aluno)
    return read_alunos_id(id_aluno)
                

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods = ['DELETE'])
def delete_aluno(id_aluno):
    read_alunos_id(id_aluno)
    delete_aluno(id_aluno)

    

@alunos_blueprint.route('/alunos', methods = ['DELETE'])
def delete_alunos():
    delete_alunos()

