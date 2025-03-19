from flask import Flask, jsonify, request
app = Flask(__name__)
from random import randint
import test_
from random import randint,random

'''--------------------------------------------------------------'''
usuarios = {
    "Alunos": [
        {"id":45,"nome":"Marcos", "idade": 20, "turma_id":300 , "data_nascimento": "15/01/2005", "nota_primeiro_semestre": 9.6, "nota_segundo_semestre": 8.6, "media_final": 9.1},
        {"id":3, "nome": "Ana", "idade": 31, "turma_id":300, "data_nascimento": "03/03/1994", "nota_primeiro_semestre": 5.9, "nota_segundo_semestre": 10.0, "media_final": 7.95}
    ],
    "Professores":[
        {"id": 200,"nome": "Vitor Furlan", "idade": 31,"materia": "Fundamentos de Banco de Dados", "observacoes": "Chega no horário e é super competente"},
        {"id": 201, "nome": "Katrina Catarina",  "idade": 63,"materia": "Introdução a Estatística", "observacoes": "Tem uma didática excelente e os alunos a amam"}
    ],
    "Turma":[        
        {"id" : 300,"descricao": "Fundamentos de Banco de Dados", "professor_id": 200, "ativo": True},
        {"id" 310, "descricao": "Introdução a Estatística", "professor_id": 210, "ativo": True} 
    ]
}


id_usuarios = {
    "id_alunos" : [45, 3],
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
        return jsonify({"erro": "aluno sem nome"}), 400

    # Se o usuário forneceu um ID, usamos esse ID
    if "id" in dados_alunos:
        cria_id = dados_alunos["id"]
        # Verifica se o ID já existe
        if cria_id in id_usuarios["id_alunos"]:
            #print("IDs de alunos já cadastrados:", id_usuarios["id_alunos"])
            return jsonify({"erro" : "id ja utilizada"}), 400
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
    return jsonify(novo_aluno), 200


@app.route('/alunos', methods = ['GET'])
def read_alunos():
    return jsonify(usuarios['Alunos'])


@app.route('/alunos/<int:id_aluno>', methods =['GET'])
def read_alunos_id(id_aluno):
    # Buscar aluno na lista de alunos
    informacoes_aluno = next((aluno for aluno in usuarios["Alunos"] if aluno["id"] == id_aluno), None)
    
    if informacoes_aluno is None:
        return  jsonify({"erro" : "aluno nao encontrado"}), 400 #REESCRITA DESSA MENSAGEM
    else:
        return jsonify(informacoes_aluno), 200  
    

@app.route('/alunos/<int:id_aluno>', methods = ['PUT'])
def update_alunos(id_aluno):
    informacoes_aluno = next((aluno for aluno in usuarios["Alunos"] if aluno["id"] == id_aluno), None)
    if informacoes_aluno is None:
        return jsonify({"erro":"aluno nao encontrado"}), 400
    else:
        dados_alunos = request.get_json()
        if "nome" not in dados_alunos: 
            return jsonify({"erro": "aluno sem nome"}), 400
    
        for aluno in usuarios["Alunos"]:
            if aluno["id"] == id_aluno:
                atualiza_aluno = aluno # {"id", "nome"}
                for valor in dados_alunos:
                    atualiza_aluno[valor] = dados_alunos[valor]
                usuarios["Alunos"].remove(aluno)
                usuarios["Alunos"].append(atualiza_aluno)
        return jsonify(atualiza_aluno), 200  


@app.route('/alunos/<int:id_aluno>', methods = ['DELETE'])
def delete_aluno(id_aluno):
    #busca o aluno na lisa dos alunos
    A_deletar = next((aluno for aluno in usuarios["Alunos"] if aluno["id"] == id_aluno), None)
    if A_deletar is None:
        return  jsonify({"erro" : "aluno nao encontrado"}), 400 #REESCRITA DESSA MENSAGEM
    else:
        usuarios["Alunos"].remove(A_deletar)
        return


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
    novo_professor = {
        "id": cria_id,
        "nome": dados_professores["nome"]
    }

    # Adicionando novo professor à lista de usuários
    usuarios["Professores"].append(novo_professor)

    print("Novo professor cadastrado:", novo_professor)
    print("Lista atualizada de :", usuarios["Professores"])

    # Retorna o novo professor criado
    return jsonify(novo_professor), 200



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

###### turmas

@app.route('/turmas', methods=['POST'])
def create_turma():
    # Pegando as informações do corpo da requisição
    dados_turmas = request.get_json()

    # Verificação de valores nulos ou atributos faltando
    if "nome" not in dados_turmas:
        return jsonify({"erro": "turma sem nome"}), 400 

    # Se o usuário forneceu um ID, usamos esse ID
    if "id" in dados_turmas:
        cria_id = dados_turmas["id"]
        # Verifica se o ID já existe
        if cria_id in id_usuarios["id_professores"]:
            return jsonify({"erro" : "id já utilizada"}), 400
    else:
        # Se o ID não foi fornecido, geramos um automaticamente
        while True:
            cria_id = random.randint(100, 199)  # Evita conflitos com IDs existentes
            if cria_id not in id_usuarios["id_professores"]:
                break

    # Adiciona o ID à lista para evitar duplicação
    id_usuarios["id_professores"].append(cria_id)

    # Criando um dicionário para a nova turma
    nova_turma = {
        "id": cria_id,
        "nome": dados_turmas["nome"]
    }

    # Adicionando nova turma à lista de usuários
    usuarios["Professores"].append(nova_turma)

    print("Nova turma cadastrada:", nova_turma)
    print("Lista atualizada de turmas:", usuarios["Professores"])

    # Retorna a nova turma criada
    return jsonify(nova_turma), 200


@app.route('/turmas/<int:id_turma>', methods=['GET'])
def read_turma_id(id_turma):
    # Buscar turma na lista de turmas
    informacoes_turma = next((turma for turma in usuarios["Professores"] if turma["id"] == id_turma), None)
    
    if informacoes_turma is None:
        return jsonify({"erro" : "turma não encontrada"}), 400
    else:
        return jsonify(informacoes_turma), 200 


@app.route('/turmas/<int:id_turma>', methods=['PUT'])
def update_turma(id_turma):
    informacoes_turma = next((turma for turma in usuarios["Professores"] if turma["id"] == id_turma), None)
    if informacoes_turma is None:
        return jsonify({"erro":"turma não encontrada"}), 400
    else:
        dados_turmas = request.get_json()
        if "nome" not in dados_turmas: 
            return jsonify({"erro": "turma sem nome"}), 400
    
        for turma in usuarios["Professores"]:
            if turma["id"] == id_turma:
                atualiza_turma = turma
                for valor in dados_turmas:
                    atualiza_turma[valor] = dados_turmas[valor]
                usuarios["Professores"].remove(turma)
                usuarios["Professores"].append(atualiza_turma)
        return jsonify(atualiza_turma), 200  


@app.route('/turmas/<int:id_turma>', methods=['DELETE'])
def delete_turma(id_turma):
    a_deletar = next((turma for turma in usuarios["Professores"] if turma["id"] == id_turma), None)
    if a_deletar is None:
        return jsonify({"erro" : "turma não encontrada"}), 400
    else:
        usuarios["Professores"].remove(a_deletar)
        return jsonify({"message": "turma deletada com sucesso"}), 200



if __name__ == '__main__':
    app.run(debug=False,port=5002)