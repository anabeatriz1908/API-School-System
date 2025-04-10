from flask import Blueprint, request, jsonify
from main.Aluno.alunos_model import *

alunos_blueprint = Blueprint('alunos', __name__)

		
@alunos_blueprint.route('/alunos', methods=['POST'])
def cria_alunos():
    dados = request.get_json()
    try:
        novo_aluno, erro = create_alunos(dados)
        if erro:
            return jsonify({'erro': erro}), 400
        return jsonify(novo_aluno), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
 

@alunos_blueprint.route('/alunos', methods=['GET'])
def le_alunos():
    try:
        alunos,erro = read_alunos()
        return jsonify(alunos), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@alunos_blueprint.route('/alunos/<int:id_aluno>', methods =['GET'])
def le_alunos_id(id_aluno):
    aluno = read_alunos_id(id_aluno)
    if aluno:
        return jsonify(aluno), 200
    else:
        return jsonify({'erro': 'Aluno não encontrado'}), 404 


@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualiza_alunos(id_aluno):
    dados = request.get_json()
    try:
        atualizado = update_alunos(id_aluno, dados)
        if atualizado:
            return jsonify(read_alunos_id(id_aluno)), 200
        else:
            return jsonify({'erro': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400
                

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods = ['DELETE'])
def deleta_aluno(id_aluno):
    try:
        deletado = delete_aluno(id_aluno)
        if deletado:
            return jsonify({'mensagem': 'Aluno deletado com sucesso'}), 200
        else:
            return jsonify({'erro': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

    
@alunos_blueprint.route('/alunos', methods = ['DELETE'])
def deleta_alunos():
    try:
        deletado, erro = delete_alunos()
        if erro:
            return jsonify({'erro': erro}), 400
        return jsonify({'mensagem': 'Todos os alunos foram deletados com sucesso'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500