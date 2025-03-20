from flask import Flask, jsonify, request
app = Flask(__name__)
from random import randint,random
import requests
import unittest


'''--------------------------------------------------------------'''
usuarios = {
    "Alunos": [
        {"id": 45, "nome": "Marcos", "idade": 20, "turma_id": 200, "data_nascimento": "15/01/2005", "nota_primeiro_semestre": 9.6, "nota_segundo_semestre": 8.6, "media_final": 9.1},
        {"id": 3, "nome": "Ana", "idade": 31, "turma_id": 201, "data_nascimento": "03/03/1994", "nota_primeiro_semestre": 5.9, "nota_segundo_semestre": 10.0, "media_final": 7.95}
    ],
    "Professores": [
        {"id": 200, "nome": "Vitor Furlan", "idade": 31, "materia": "Fundamentos de Banco de Dados", "observacoes": "Chega no horário e é super competente"},
        {"id": 201, "nome": "Katrina Catarina", "idade": 63, "materia": "Introdução a Estatística", "observacoes": "Tem uma didática excelente e os alunos a amam"}
    ],
    "Turma": [
        {"id": 300, "descricao": "Fundamentos de Banco de Dados", "professor_id": 200, "ativo": True}
        ]
}


id_usuarios = {
    "id_alunos" : [45],
    "id_professores" : [200, 201],
    "id_turmas" : [300]
}


@app.route('/professores', methods=['POST'])
def create_professor():
    # Pegando as informações do corpo da requisição
    dados_professores = request.get_json()

    # Verificação de valores nulos ou atributos faltando
    if "nome" not in dados_professores:
        return jsonify({"erro": "professor sem nome"}), 400 

    # Se o usuário forneceu um ID, usamos esse ID
    if "id" in dados_professores:
        cria_id = dados_professores["id"]
        # Verifica se o ID já existe
        if cria_id in id_usuarios["id_professores"]:
            return jsonify({"erro" : "id ja utilizada"}), 400
    else:
        # Se o ID não foi fornecido, geramos um automaticamente
        while True:
            cria_id = random.randint(100, 199)  # Evita conflitos com IDs existentes
            if cria_id not in id_usuarios["id_professores"]:
                break

    # Adiciona o ID à lista para evitar duplicação
    id_usuarios["id_professores"].append(cria_id)

    # Criando um dicionário para o novo professor
    novo_professor = {"id": cria_id, 
                      "nome": dados_professores["nome"], 
                      "idade": dados_professores["idade"], 
                      "materia": dados_professores["materia"], 
                      "observacoes": dados_professores["observacoes"]
                      }

    # Adicionando novo professor à lista de usuários
    usuarios["Professores"].append(novo_professor)

    # Retorna o novo professor criado
    return jsonify(novo_professor), 200


@app.route('/professores', methods = ['GET'])
def read_professor():
    return jsonify(usuarios["Professores"])


@app.route('/professores/<int:id_professor>', methods =['GET'])
def read_professor_id(id_professor):
    # Buscar professor na lista de professores
    informacoes_professor = next((professor for professor in usuarios["Professores"] if professor["id"] == id_professor), None)
    
    if informacoes_professor is None:
        return  jsonify({"erro" : "professor nao encontrado"}), 400 #REESCRITA DESSA MENSAGEM
    else:
        return jsonify(informacoes_professor), 200 
        

@app.route('/professores/<int:id_professor>', methods = ['PUT'])
def update_professores(id_professor):
    informacoes_professor = next((professor for professor in usuarios["Professores"] if professor["id"] == id_professor), None)
    if informacoes_professor is None:
        return jsonify({"erro":"professor nao encontrado"}), 400
    else:
        dados_professores = request.get_json()
        if "nome" not in dados_professores: 
            return jsonify({"erro": "professor sem nome"}), 400
    
        for professor in usuarios["Professores"]:
            if professor["id"] == id_professor:
                atualiza_professor = professor # {"id", "nome"}
                for valor in dados_professores:
                    atualiza_professor[valor] = dados_professores[valor]
                usuarios["Professores"].remove(professor)
                usuarios["Professores"].append(atualiza_professor)
        return jsonify(atualiza_professor), 200  


@app.route('/professores/<int:id_professor>', methods = ['DELETE'])
def delete_professor(id_professor):
    A_deletar = next((professor for professor in usuarios["Professores"] if professor["id"] == id_professor), None)
    if A_deletar is None:
        return  jsonify({"erro" : "professor nao encontrado"}), 400 #REESCRITA DESSA MENSAGEM
    else:
        usuarios["Professores"].remove(A_deletar)
        


if __name__ == '__main__':
    app.run(debug=False,port=5002)


if __name__ == '__main__':
    app.run(debug=False,port=5002)
