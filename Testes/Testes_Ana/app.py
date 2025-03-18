from flask import Flask, jsonify, request
app = Flask(__name__)
from random import randint,random
import requests
import unittest

import test_ana

'''--------------------------------------------------------------'''
usuarios = {
    "Alunos": [
        {"id":45,"nome":"Marcos"},
        {"id":3, "nome": "Ana"}
    ],
    "Professores":[
        {"id": 200,"nome": "Vitor Furlan"},
        {"id": 201, "nome": "Katrina Catarina"}
    ]
}


id_usuarios = {
    "id_alunos" : [45],
    "id_professores" : [200, 201],
    "id_turmas" : [300, 301]
}

@app.route('/reseta', methods=['POST'])
def reseta_api():
    usuarios["Alunos"].clear()  # Limpa diretamente a lista
    usuarios["Professores"].clear()
    id_usuarios["id_alunos"].clear()
    id_usuarios["id_professores"].clear()
    return jsonify({"message": "A lista de Alunos e professores foi resetada"}), 200

@app.route('/alunos', methods=['POST'])
def create_alunos():
    # Pegando as informações do corpo da requisição
    dados_alunos = request.get_json()

    # Verificação de valores nulos ou atributos faltando
    if "nome" not in dados_alunos:
        return jsonify({"message": "O campo 'nome' é obrigatório"}), 400

    # Se o usuário forneceu um ID, usamos esse ID
    if "id" in dados_alunos:
        cria_id = dados_alunos["id"]
        # Verifica se o ID já existe
        if cria_id in id_usuarios["id_alunos"]:
            print("IDs de alunos já cadastrados:", id_usuarios["id_alunos"])
            return jsonify({"message": f"ID {cria_id} já está em uso"}), 400
    else:
        # Se o ID não foi fornecido, geramos um automaticamente
        while True:
            cria_id = random.randint(100, 199)  # Evita conflitos com IDs existentes
            if cria_id not in id_usuarios["id_alunos"]:
                break

    # Adiciona o ID à lista para evitar duplicação
    id_usuarios["id_alunos"].append(cria_id)

    # Criando um dicionário para o novo aluno
    novo_aluno = {
        "id": cria_id,
        "nome": dados_alunos["nome"]
    }

    # Adicionando novo aluno à lista de usuários
    usuarios["Alunos"].append(novo_aluno)

    print("Novo aluno cadastrado:", novo_aluno)
    print("Lista atualizada de alunos:", usuarios["Alunos"])

    # Retorna o novo aluno criado
    return jsonify(novo_aluno), 201


################################################################
#ROTAS REESCRITAS PELA ANA
@app.route('/alunos/<int:id_aluno>', methods =['GET'])
def read_alunos_id(id_aluno):
    # Buscar aluno na lista de alunos
    informacoes_aluno = next((aluno for aluno in usuarios["Alunos"] if aluno["id"] == id_aluno), None)
    
    if informacoes_aluno is None:
        return  jsonify({"erro" : "aluno nao encontrado"}), 400 #REESCRITA DESSA MENSAGEM
    else:
        return jsonify(informacoes_aluno), 200   

@app.route('/alunos', methods=['GET'])
def read_alunos():
    # Retorna todos os alunos
    if usuarios["Alunos"]:
        return jsonify(usuarios["Alunos"]), 200
    else:
        return jsonify({"erro":"aluno nao encontrado"}),404 #REESCRITA DESSA MENSAGEM
        
################################################################
#ROTAS CRIADAS PELA ANA
@app.route('/alunos/<int:id_aluno>', methods = ['DELETE'])
def delete_aluno(id_aluno):
    
    for aluno in usuarios["Alunos"]:
        if aluno["id"] == id_aluno:
            usuarios["Alunos"].remove(aluno)
    else:
        return "Aluno não encontrado"
    
@app.route('/alunos/<int:id_aluno>', methods = ['PUT'])
def update_alunos(id_aluno):
    informacoes_aluno = next((aluno for aluno in usuarios["Alunos"] if aluno["id"] == id_aluno), None)
    if informacoes_aluno is None:
        return jsonify({"erro":"aluno nao encontrado"}), 400
    else:
        dados_alunos = request.get_json()
        for aluno in usuarios["Alunos"]:
            if aluno["id"] == id_aluno:
                atualiza_aluno = aluno # {"id", "nome"}
                for valor in dados_alunos:
                    atualiza_aluno[valor] = dados_alunos[valor]
                usuarios["Alunos"].remove(aluno)
                usuarios["Alunos"].append(atualiza_aluno)
        return jsonify(atualiza_aluno), 200   
                



if __name__ == '__main__':
    app.run(debug=False,port=5002)
