from flask import Flask, jsonify, request
from random import random

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


class AlunoNaoEncontrado(Exception):
    pass #palavra-chave que serve como uma instrução nula, ou seja, não faz nada


def create_alunos(aluno):
    if "nome" not in aluno:
        return None, "Aluno sem nome"

    if "turma_id" not in aluno:
        return None, "Aluno sem turma"

    turma_ids = [turma["id"] for turma in usuarios["Turmas"]]
    if aluno["turma_id"] not in turma_ids:
        return None, "Turma não encontrada"

    if "id" in aluno:
        cria_id = aluno["id"]
        if cria_id in id_usuarios["id_alunos"]:
            return None, "Id já utilizado"
    else:
        while True:
            cria_id = int(random() * 100) + 100
            if cria_id not in id_usuarios["id_alunos"]:
                break

    id_usuarios["id_alunos"].append(cria_id)

    try:
        nota1 = float(aluno["nota_primeiro_semestre"])
        nota2 = float(aluno["nota_segundo_semestre"])
    except ValueError:
        return None, "Notas devem ser números"

    media_final = (nota1 + nota2) / 2

    novo_aluno = {
        "id": cria_id,
        "nome": aluno["nome"],
        "idade": aluno["idade"],
        "turma_id": aluno["turma_id"],
        "data_nascimento": aluno["data_nascimento"],
        "nota_primeiro_semestre": nota1,
        "nota_segundo_semestre": nota2,
        "media_final": media_final
    }

    usuarios["Alunos"].append(novo_aluno)
    return novo_aluno, None

def read_alunos():
    return usuarios["Alunos"], None

def read_alunos_id(id_aluno):
    return next((p for p in usuarios["Alunos"] if p["id"] == id_aluno), None)

def update_alunos(id_aluno, dados_atualizados):
    aluno = next((a for a in usuarios["Alunos"] if a["id"] == id_aluno), None)
    if not aluno:
        return None, "aluno não encontrado"

    if "nome" not in dados_atualizados:
        return None, "aluno sem nome"

    campos_editaveis = ["nome", "idade", "data_nascimento", "turma_id", "nota_primeiro_semestre", "nota_segundo_semestre"]
    for campo in dados_atualizados:
        if campo in campos_editaveis:
            aluno[campo] = dados_atualizados[campo]

    try:
        nota1 = float(aluno["nota_primeiro_semestre"])
        nota2 = float(aluno["nota_segundo_semestre"])
        aluno["media_final"] = (nota1 + nota2) / 2
    except (ValueError, KeyError):
        return None, "notas inválidas para calcular a média"

    return aluno, None

def delete_aluno(id_aluno):
    aluno = next((p for p in usuarios["Alunos"] if p["id"] == id_aluno), None)
    if not aluno:
        return False
    usuarios["Alunos"].remove(aluno)
    if id_aluno in id_usuarios["id_alunos"]:
        id_usuarios["id_alunos"].remove(id_aluno)
    return True

def delete_alunos():
    usuarios["Alunos"].clear()
    id_usuarios["id_alunos"].clear()
    return True, None