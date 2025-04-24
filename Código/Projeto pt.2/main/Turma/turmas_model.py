from flask import Flask, request
import random

usuarios = {
    "Alunos": [
        {"id":45,"nome":"Marcos", "idade": 20, "turma_id":300 , "data_nascimento": "15/01/2005", "nota_primeiro_semestre": 9.6, "nota_segundo_semestre": 8.6, "media_final": 9.1},
        {"id":3, "nome": "Ana", "idade": 31, "turma_id":300, "data_nascimento": "03/03/1994", "nota_primeiro_semestre": 5.9, "nota_segundo_semestre": 10.0, "media_final": 7.95}
    ],
    "Professores": [
        {"id": 200, "nome": "Vitor Furlan", "idade": 31, "materia": "Fundamentos de Banco de Dados", "observacoes": "Chega no horário e é super competente"},
        {"id": 201, "nome": "Katrina Catarina", "idade": 63, "materia": "Introdução a Estatística", "observacoes": "Tem uma didática excelente e os alunos a amam"}
    ],
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


def create_turmas(dados_turmas):
    if "descricao" not in dados_turmas:
        return None, "Turma sem descrição"
    
    if "id" not in dados_turmas:
        return None, "Turma sem ID"
    
    if "professor_id" not in dados_turmas:
        return None,"Turma sem professor"
    
    if "ativo" not in dados_turmas:
        return None,"Turma sem estado"
    
    if dados_turmas["professor_id"] not in id_usuarios["id_professores"]:
        return None, "ID do professor não encontrado"

    if "id" in dados_turmas:
        cria_id = dados_turmas["id"]
        if cria_id in id_usuarios["id_turmas"]:
            return None, "id ja utilizada"
    else:
        while True:
            cria_id = random.randint(100, 199)
            if cria_id not in id_usuarios["id_turmas"]:
                break

    id_usuarios["id_turmas"].append(cria_id)


    nova_turma = {"id": cria_id, 
                "descricao": dados_turmas["descricao"], 
                "professor_id": dados_turmas["professor_id"], 
                "ativo": dados_turmas["ativo"]
                      }


    usuarios["Turmas"].append(nova_turma)

    return nova_turma, None


def read_turmas():
    return usuarios["Turmas"], None


def read_turma_id(id_turma):
    return next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turma), None)
    

def update_turma(id_turma, dados_turmas):
    turma = next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turma), None)

    if turma is None:
        return None, "Turma não encontrada"
    
    if dados_turmas is None:
        return None, "A atualização de turma precisa de novas informações"
    else:
        for chave, valor in dados_turmas.items():
            turma[chave] = valor
    
    return turma, None


def delete_turma_por_id(id_turma):
    a_deletar = next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turma), None)

    if a_deletar is None:
        return None, "Turma não encontrada"
    else:
        usuarios["Turmas"].remove(a_deletar)
        return "Turma deletada com sucesso", None


def deleta_turmas():
    usuarios["Turmas"].clear()
    id_usuarios["id_turmas"].clear()
    return True, None
