import random
from flask import jsonify

usuarios = {
    "Turmas": [
        {"id": 300, "descricao": "Fundamentos de Banco de Dados", "professor_id": 200, "ativo": True},
        {"id": 310, "descricao": "Introdução a Estatística", "professor_id": 201, "ativo": True} 
    ]
}

id_usuarios = {
    "id_professores" : [200, 201],
    "id_turmas" : [300, 310]
}

def create_turma(dados_turmas):
    #Vendo se a turma tem ou não descricao
    if "descricao" not in dados_turmas:
        return jsonify({"erro": "turma sem descricao"}), 400
    
    # Vendo se a turma tem ou não professor
    if "professor_id" not in dados_turmas:
        return jsonify({"erro": "turma sem professor"}), 400
         
    #Vendo se o professor passado está na lista de professores
    if dados_turmas["professor_id"] not in id_usuarios["id_professores"]:
        return jsonify({"erro": "professor não encontrado"}), 404
    
    if "ativo" not in dados_turmas:
        return jsonify({"erro": "turma sem situacao (true ou false)"}), 400
    
    if "id" in dados_turmas:
        cria_id = dados_turmas["id"]
        if cria_id in id_usuarios["id_turmas"]:
            return jsonify({"erro" : "id ja utilizada"}), 400
    else:
        while True:
            cria_id = random.randint(100, 199)
            if cria_id not in id_usuarios["id_turmas"]:
                break
    # Adiciona o ID à lista para evitar duplicação
    id_usuarios["id_turmas"].append(cria_id)

    # Criando um dicionário para a nova turma
    nova_turma = {"id": cria_id, 
                "descricao": dados_turmas["descricao"], 
                "professor_id": dados_turmas["professor_id"], 
                "ativo": dados_turmas["ativo"]
                      }

    # Adicionando nova turma à lista de usuários
    usuarios["Turmas"].append(nova_turma)

    # Retorna o nova turna criado
    return jsonify({"Nova Turma": nova_turma}), 200


def read_turmas():
    return jsonify(usuarios["Turmas"]), 200


def read_turmas_id(id_turmas):
    # Buscar turma por id
    informacoes_turmas = next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turmas), None)
    
    if informacoes_turmas is None:
        return jsonify({"erro" : "turma nao encontrado"}), 404
    else:
        return jsonify (informacoes_turmas), 200 
        

def update_turmas(id_turmas, dados_turmas):
    informacoes_turmas = next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turmas), None)

    if informacoes_turmas is None:
        return jsonify({"erro":"turma nao encontrado"}), 404
    
    else:
            #Vendo se a turma tem ou não descricao
        if "descricao" not in dados_turmas:
            return jsonify({"erro": "turma sem descricao"}), 400
        
        # Vendo se a turma tem ou não professor
        if "professor_id" not in dados_turmas:
            return jsonify({"erro": "turma sem professor"}), 400
            
        #Vendo se o professor passado está na lista de professores
        if dados_turmas["professor_id"] not in id_usuarios["id_professores"]:
            return jsonify({"erro": "professor não encontrado"}), 404
        
        if "ativo" not in dados_turmas:
            return jsonify({"erro": "turma sem situacao (true ou false)"}), 400
        
    
        for turma in usuarios["Turmas"]:
            if turma["id"] == id_turmas:
                atualiza_turma = turma # {"id", "nome"}

                for valor in informacoes_turmas:
                    atualiza_turma[valor] = informacoes_turmas[valor]
                usuarios["Turmas"].remove(turma)
                usuarios["Turmas"].append(atualiza_turma)
        return jsonify({atualiza_turma}), 200  


def delete_turma(id_turmas):
    A_deletar = next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turmas), None)
    if A_deletar is None:
        return  jsonify({"erro" : "truma nao encontrada"}), 400
    else:
        usuarios["Turmas"].remove(A_deletar)
        id_usuarios["Turmas"].remove(id_turmas) # Ver se essa porra tá funcionando.AJDNFJSNDFJGNSJDNFGJNDFJGNSJDFNGJSDNGJNSDFJG

        if A_deletar not in usuarios["Turmas"]:
            return jsonify({"mensagem":"turma deletada"}), 200
        else:
            return jsonify({"erro": "turma não deletada"}), 400