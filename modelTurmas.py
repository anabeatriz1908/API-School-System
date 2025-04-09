from flask import Flask, jsonify, request



usuarios = {
    
    "Turmas": [
        {"id": 300, "descricao": "Fundamentos de Banco de Dados", "professor_id": 200, "ativo": True},
        {"id": 310, "descricao": "Introdução a Estatística", "professor_id": 201, "ativo": True} 
    ]
}

id_usuarios = {
    "id_alunos" : [45, 3],
    "id_professores" : [200, 201],
    "id_turmas" : [300, 301]
}


class  AlunoNaoEncontrado(Exception):
    pass

#---------------------------------------------------
#CREATE

def create_turmas(dados_turmas):
    if "descricao" not in dados_turmas:
        return jsonify({"erro": "turma sem descricao"}), 400
    
    if "id" not in dados_turmas:
        return jsonify({"erro": "turma sem id"}), 400
    
    if "professor_id" not in dados_turmas:
        return jsonify({"erro": "turma sem professor"}), 400

    cria_id = dados_turmas["id"]

    if cria_id in id_usuarios["id_alunos"]:
        return jsonify({"erro" : "id ja utilizado"}), 400
 
    id_usuarios["id_alunos"].append(cria_id)
    nova_turma = dados_turmas.copy()
    print(nova_turma)
    usuarios["Turmas"].append(nova_turma)
    print("Novo turma cadastrada:", nova_turma)
    return jsonify(nova_turma), 200

#---------------------------------------------------
#READ

def read_turmas():
    print(usuarios["Turmas"])
    return jsonify(usuarios["Turmas"]), 200

#---------------------------------------------------
#READ POR ID

def read_turma_id(id_turma):
    informacoes_turma = next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turma), None)
    
    if informacoes_turma is None:
        return jsonify({"erro" : "turma não encontrada"}), 400
    else:
        return jsonify(informacoes_turma), 200 
    
#---------------------------------------------------
#UPDATE_TURMA

def update_turma(id_turma):
    informacoes_turma = next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turma), None)

    if informacoes_turma is None:
        return jsonify({"erro": "turma não encontrada"}), 400
    
    dados_turmas = request.get_json()
    if "descricao" in dados_turmas:
        informacoes_turma["descricao"] = dados_turmas["descricao"]
    if "professor_id" in dados_turmas:
        informacoes_turma["professor_id"] = dados_turmas["professor_id"]
    if "ativo" in dados_turmas:
        informacoes_turma["ativo"] = dados_turmas["ativo"]

    return jsonify(informacoes_turma), 200

#---------------------------------------------------
#DELETA_TURMA_POR_ID

def delete_turma_por_id(id_turma):
    a_deletar = next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turma), None)

    if a_deletar is None:
        return jsonify({"erro" : "turma não encontrada"}), 400
    else:
        usuarios["Turmas"].remove(a_deletar)
        return jsonify({"message": "turma deletada com sucesso"}), 200

#---------------------------------------------------
#DELETA_TURMA

def deleta_turmas():
    usuarios["Turmas"].clear()
    id_usuarios["id_turmas"].clear()
    return jsonify({"message": "A lista de turmas foi resetada"}), 200
