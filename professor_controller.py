from flask import Blueprint, request, jsonify
import professor_model

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/professores', methods=['POST'])
def cria_professor():
    dados = request.json
    try:
        novo_professor = professor_model.create_professor(dados)
        return jsonify(novo_professor), 201
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400

@professores_blueprint.route('/professores', methods=['GET'])
def get_professor():
    try:
        professores = professor_model.read_professor()
        return jsonify(professores), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@professores_blueprint.route('/professores/<int:id_professor>', methods=['GET'])
def get_professorID(id_professor):
    professor = professor_model.read_professor_id(id_professor)
    if professor:
        return jsonify(professor), 200
    else:
        return jsonify({'erro': 'Professor não encontrado'}), 404

@professores_blueprint.route('/professores/<int:id_professor>', methods=['PUT'])
def atualiza_professor(id_professor):
    dados = request.json
    try:
        atualizado = professor_model.update_professores(id_professor, dados)
        if atualizado:
            return jsonify(professor_model.read_professor_id(id_professor)), 200
        else:
            return jsonify({'erro': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

@professores_blueprint.route('/professores/<int:id_professor>', methods=['DELETE'])
def deleta_professor(id_professor):
    try:
        deletado = professor_model.delete_professor(id_professor)
        if deletado:
            return jsonify({'mensagem': 'Professor deletado com sucesso'}), 200
        else:
            return jsonify({'erro': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400
