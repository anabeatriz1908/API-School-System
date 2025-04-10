from flask import Blueprint, request, jsonify
from main.model import turmas

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/turmas', methods=['POST'])
def cria_turmas():
    dados = request.json
    nova_turma = turmas.create_turma(dados)
    return nova_turma

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    return turmas.read_turmas()

@turmas_blueprint.route('/turmas/<int:id_turmas>', methods=['GET'])
def get_turmasID(id_turmas):
    turma = turmas.read_turmas_id(id_turmas)
    return turma

@turmas_blueprint.route('/turmas/<int:id_turmas>', methods=['PUT'])
def atualiza_turma(id_turmas):
    dados = request.json
    turmas.update_turmas(id_turmas, dados)
    return turmas.read_turmas_id(id_turmas)

@turmas_blueprint.route('/turmas/<int:id_turmas>', methods=['DELETE'])
def deleta_turma(id_turmas):
    return turmas.delete_turma(id_turmas)