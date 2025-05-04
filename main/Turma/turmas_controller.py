from flask import Blueprint, request, jsonify
from main.Turma import turmas_model
from config import db

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/turmas', methods=['POST'])
def cria_turmas():
    dados = request.get_json()
    try:
        novo_turma = turmas_model.create_turmas(dados)
        return jsonify(novo_turma), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@turmas_blueprint.route('/turmas', methods=['GET'])
def le_turmas():
    try:
        turmas, erro = turmas_model.read_turmas()
        return jsonify(turmas), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['GET'])
def le_turma_id(id_turma):
    turma = turmas_model.read_turma_id(id_turma)
    if turma:
        return jsonify(turma), 200
    else:
        return jsonify({'erro': 'Turma não encontrado'}), 404 
    


@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['PUT'])
def atualiza_turmas(id_turma):
    dados = request.get_json()
    try:
        atualizado, erro = turmas_model.update_turma(id_turma, dados)
        if erro:
            if erro == "Turma não encontrada":
                return jsonify({'erro': erro}), 404
            elif erro == "A atualização de turma precisa de novas informações":
                return jsonify({"erro": erro}), 400
            else:
                return jsonify({'erro': "desconhecido"}), 500
        
        return jsonify(atualizado), 200
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    
 
@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['DELETE'])
def deleta_turma(id_turma):
    try:
        deletada = turmas_model.delete_turma_por_id(id_turma)
        if deletada:
            return jsonify({'mensagem': 'Turma deletada com sucesso'}), 200
        else:
            return jsonify({'erro': 'Turna não encontrada'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400
    


@turmas_blueprint.route('/turmas', methods=['DELETE'])
def deleta_turmas():
    try:
        deletada, erro = turmas_model.deleta_turmas()
        if erro:
            return jsonify({'erro': erro}), 400
        return jsonify({'mensagem': 'Todas as turmas foram deletadas com sucesso'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


