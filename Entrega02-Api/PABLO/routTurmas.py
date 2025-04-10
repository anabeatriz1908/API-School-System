from flask import Flask, jsonify, request, Blueprint
from random import randint, random
import modelTurmas

turmas_blueprint = Blueprint('turmas',__name__)

#-------------------------------------------------------------------------------------
@turmas_blueprint.route('/turmas', methods=['POST'])                 
def create_turmas():                                    #TUDO REFERENTE A /TURMAS
    dados_turmas = request.get_json()
    modelTurmas.create_turmas(dados_turmas)
    return modelTurmas.create_turmas()

#DONE
#-------------------------------------------------------------------------------------

variavel_x = modelTurmas.id_usuarios

@turmas_blueprint.route('/turmas', methods=['GET'])
def read_turmas():
    return modelTurmas.create_turmas()

#DONE
#-------------------------------------------------------------------------------------

@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['GET'])
def read_turma_id(variavel_x["id_turmas"]):    #talvez esta linha dê erro. o parâmetro pode estar definido errado
    return modelTurmas.read_turma_id()

#DONE
#-------------------------------------------------------------------------------------


@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['PUT'])
def update_turma(id_turma):
    return modelTurmas.update_turma()
    
#DONE
#-------------------------------------------------------------------------------------

 
@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['DELETE'])
def delete_turma_por_id(id_turma):
    return modelTurmas.delete_turma_por_id()
    
#DONE
#-------------------------------------------------------------------------------------

@turmas_blueprint.route('/turmas', methods=['DELETE'])
def deleta_turmas():
    return modelTurmas.deleta_turmas()

#DONE
#-------------------------------------------------------------------------------------
