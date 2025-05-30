from flask import Blueprint, request, jsonify
from main.Aluno import alunos_model
from main.Aluno.alunos_model import AlunoNaoEncontrado

from config import db

alunos_blueprint = Blueprint('alunos', __name__)


@alunos_blueprint.route("/conexao", methods=['GET'])
def testa_conexao():
    return jsonify({"message":"conexao com api"}), 200


		
@alunos_blueprint.route('/alunos', methods=['POST'])
def cria_alunos():
    dados = request.get_json()
    try:
        novo_aluno, erro = alunos_model.create_alunos(dados)
        if erro:
            return jsonify({'erro': erro}), 400
        return jsonify(novo_aluno), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
 

@alunos_blueprint.route('/alunos', methods=['GET'])
def le_alunos():
    try:
        alunos,erro = alunos_model.read_alunos()
        return jsonify(alunos), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@alunos_blueprint.route('/alunos/<int:id_aluno>', methods =['GET'])
def le_alunos_id(id_aluno):
    try:
        aluno = alunos_model.read_alunos_id(id_aluno)
        return jsonify(aluno), 200
    except AlunoNaoEncontrado:
        return jsonify({'erro': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualiza_alunos(id_aluno):
    dados = request.get_json()
    try:
        atualizado = alunos_model.update_alunos(id_aluno, dados)
        if atualizado:
            return jsonify(alunos_model.read_alunos_id(id_aluno)), 200
        else:
            return jsonify({'erro': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400
                

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods = ['DELETE'])
def deleta_aluno(id_aluno):
    try:
        deletado = alunos_model.delete_aluno(id_aluno)
        if deletado:
            return jsonify({'mensagem': 'Aluno deletado com sucesso'}), 200
        else:
            return jsonify({'erro': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

    
@alunos_blueprint.route('/alunos', methods = ['DELETE'])
def deleta_alunos():
    try:
        deletado, erro = alunos_model.delete_alunos()
        if erro:
            return jsonify({'erro': erro}), 400
        return jsonify({'mensagem': 'Todos os alunos foram deletados com sucesso'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500