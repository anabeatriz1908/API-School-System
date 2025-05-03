from flask import Blueprint, request, jsonify
from main.Professor import professores_model
from main.Professor.professores_model import ProfessorNaoEncontrado

professores_blueprint = Blueprint('professores', __name__)


@professores_blueprint.route('/professores', methods=['POST'])
def cria_professor():
    dados = request.json
    try:
        novo_professor = professores_model.create_professor(dados)
        return jsonify(novo_professor), 201
    except ValueError as e:
        return jsonify({'erro': str(e)}), 400
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@professores_blueprint.route('/professores', methods=['GET'])
def get_professor():
    try:
        professores = professores_model.read_professor()
        return jsonify(professores), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@professores_blueprint.route('/professores/<int:id_professor>', methods=['GET'])
def get_professorID(id_professor):
    try:
        professor = professores_model.read_professor_id(id_professor)
        return jsonify(professor), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@professores_blueprint.route('/professores/<int:id_professor>', methods=['PUT'])
def atualiza_professor(id_professor):
    dados = request.json
    try:
        professores_model.update_professores(id_professor, dados)
        professor_atualizado = professores_model.read_professor_id(id_professor)
        return jsonify(professor_atualizado), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

from main.Professor.professores_model import ProfessorNaoEncontrado

@professores_blueprint.route('/professores/<int:id_professor>', methods=['DELETE'])
def deleta_professor(id_professor):
    try:
        deletado = professores_model.delete_professor(id_professor)
        return jsonify(deletado), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 400