import random

usuarios = {
    "Professores": [
        {"id": 200, "nome": "Vitor Furlan", "idade": 31, "materia": "Fundamentos de Banco de Dados", "observacoes": "Chega no horário e é super competente"},
        {"id": 201, "nome": "Katrina Catarina", "idade": 63, "materia": "Introdução a Estatística", "observacoes": "Tem uma didática excelente e os alunos a amam"}
    ]
}

id_usuarios = {
    "id_alunos" : [45, 3],
    "id_professores" : [200, 201],
    "id_turmas" : [300, 301]
}

def create_professor(dados_professores):
    if "nome" not in dados_professores:
        return {"erro": "professor sem nome"}, 400 

    if "id" in dados_professores:
        cria_id = dados_professores["id"]
        if cria_id in id_usuarios["id_professores"]:
            return {"erro" : "id ja utilizada"}, 400
    else:
        while True:
            cria_id = random.randint(100, 199)
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
    return novo_professor, 200


def read_professor():
    return usuarios["Professores"]


def read_professor_id(id_professor):
    # Buscar professor na lista de professores
    informacoes_professor = next((professor for professor in usuarios["Professores"] if professor["id"] == id_professor), None)
    
    if informacoes_professor is None:
        return {"erro" : "professor nao encontrado"}, 400 #REESCRITA DESSA MENSAGEM
    else:
        return informacoes_professor, 200 
        

def update_professores(id_professor, dados_professores):
    informacoes_professor = next((professor for professor in usuarios["Professores"] if professor["id"] == id_professor), None)
    if informacoes_professor is None:
        return {"erro":"professor nao encontrado"}, 400
    else:
        if "nome" not in dados_professores: 
            return {"erro": "professor sem nome"}, 400
    
        for professor in usuarios["Professores"]:
            if professor["id"] == id_professor:
                atualiza_professor = professor # {"id", "nome"}
                for valor in dados_professores:
                    atualiza_professor[valor] = dados_professores[valor]
                usuarios["Professores"].remove(professor)
                usuarios["Professores"].append(atualiza_professor)
        return atualiza_professor, 200  


def delete_professor(id_professor):
    A_deletar = next((professor for professor in usuarios["Professores"] if professor["id"] == id_professor), None)
    if A_deletar is None:
        return  {"erro" : "professor nao encontrado"}, 400 #REESCRITA DESSA MENSAGEM
    else:
        usuarios["Professores"].remove(A_deletar)