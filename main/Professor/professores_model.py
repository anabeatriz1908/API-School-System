import random

usuarios = {
    "Professores": [
        {"id": 200, "nome": "Vitor Furlan", "idade": 31, "materia": "Fundamentos de Banco de Dados", "observacoes": "Chega no horário e é super competente"},
        {"id": 201, "nome": "Katrina Catarina", "idade": 63, "materia": "Introdução a Estatística", "observacoes": "Tem uma didática excelente e os alunos a amam"}
    ]
}

id_usuarios = {
    "id_alunos": [45, 3],
    "id_professores": [200, 201],
    "id_turmas": [300, 301]
}

def create_professor(dados_professores):
    if "nome" not in dados_professores or dados_professores["nome"].strip() == "":
        raise ValueError("Professor sem nome")
    
    
    if "id" in dados_professores:
        cria_id = dados_professores["id"]
        if cria_id in id_usuarios["id_professores"]:
            raise ValueError("Id já utilizada")
    else:
        while True:
            cria_id = random.randint(100, 199)
            if cria_id not in id_usuarios["id_professores"]:
                break

    id_usuarios["id_professores"].append(cria_id)

    novo_professor = {
        "id": cria_id,
        "nome": dados_professores["nome"],
        "idade": dados_professores["idade"],
        "materia": dados_professores["materia"],
        "observacoes": dados_professores["observacoes"]
    }

    usuarios["Professores"].append(novo_professor)
    return novo_professor, None


def read_professor():
    return usuarios["Professores"]


def read_professor_id(id_professor):
    return next((p for p in usuarios["Professores"] if p["id"] == id_professor), None)


def update_professores(id_professor, dados_professores):
    professor = next((p for p in usuarios["Professores"] if p["id"] == id_professor), None)
    if not professor:
        return None, "professor não encontrado"
    

    for chave, valor in dados_professores.items():
        professor[chave] = valor
    
    return professor, None


def delete_professor(id_professor):
    professor = next((p for p in usuarios["Professores"] if p["id"] == id_professor), None)
    if not professor:
        return False
    usuarios["Professores"].remove(professor)
    return True