from flask import Blueprint, request, jsonify
import professor_model

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/professores', methods=['POST'])
def cria_professor():
    dados = request.json
    novo_professor = professor_model.create_professor(dados)
    return jsonify(novo_professor)

@professores_blueprint.route('/professores', methods=['GET'])
def get_professor():
    return jsonify(professor_model.read_professor())

@professores_blueprint.route('/professores/<int:id_professor>', methods=['GET'])
def get_professorID(id_professor):
    professor = professor_model.read_professor_id(id_professor)
    return jsonify(professor)

@professores_blueprint.route('/professores/<int:id_professor>', methods=['PUT'])
def atualiza_professor(id_professor):
    dados = request.json
    professor_model.update_professores(id_professor, dados)
    return jsonify(professor_model.read_professor_id(id_professor))

@professores_blueprint.route('/professores/<int:id_professor>', methods=['DELETE'])
def deleta_professor(id_professor):
    professor_model.delete_professor(id_professor)