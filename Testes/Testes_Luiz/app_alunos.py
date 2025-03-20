from flask import Flask, jsonify, request
app = Flask(__name__)
from random import randint, random
import test_alunos


usuarios = {
    "Alunos": [
        {"id":45,"nome":"Marcos", "idade": 20, "turma_id":300 , "data_nascimento": "15/01/2005", "nota_primeiro_semestre": 9.6, "nota_segundo_semestre": 8.6, "media_final": 9.1},
        {"id":3, "nome": "Ana", "idade": 31, "turma_id":300, "data_nascimento": "03/03/1994", "nota_primeiro_semestre": 5.9, "nota_segundo_semestre": 10.0, "media_final": 7.95}
    ],
    "Professores": [
        {"id": 200, "nome": "Vitor Furlan", "idade": 31, "materia": "Fundamentos de Banco de Dados", "observacoes": "Chega no horário e é super competente"},
        {"id": 201, "nome": "Katrina Catarina", "idade": 63, "materia": "Introdução a Estatística", "observacoes": "Tem uma didática excelente e os alunos a amam"}
    ],
    "Turma": [
        {"id": 300, "descricao": "Fundamentos de Banco de Dados", "professor_id": 200, "ativo": True},
        {"id": 310, "descricao": "Introdução a Estatística", "professor_id": 201, "ativo": True} 
    ]
}


id_usuarios = {
    "id_alunos" : [45, 3],
    "id_professores" : [200, 201],
    "id_turmas" : [300, 301]
}
    

@app.route('/alunos', methods=['POST'])
def create_alunos():

    dados_alunos = request.get_json()

    if "nome" not in dados_alunos:
        return jsonify({"erro": "Aluno sem nome"}), 400

    if "turma_id" not in dados_alunos:
        return jsonify({"erro": "Aluno sem turma"}), 400
    
    turma_ids = [turma["id"] for turma in usuarios["Turma"]]
    if dados_alunos["turma_id"] not in turma_ids:
        return jsonify({"erro": "Turma não encontrada"}), 400

    if "id" in dados_alunos:
        cria_id = dados_alunos["id"]
        if cria_id in id_usuarios["id_alunos"]:
            return jsonify({"erro" : "Id já utilizado"}), 400
    else:
        while True:
            cria_id = random.randint(100, 199)
            if cria_id not in id_usuarios["id_alunos"]:
                break
    
    id_usuarios["id_alunos"].append(cria_id)

    try:
        nota1 = float(dados_alunos["nota_primeiro_semestre"])
        nota2 = float(dados_alunos["nota_segundo_semestre"])
    except ValueError:
        return jsonify({"erro": "Notas devem ser números"}), 400

    media_final = (nota1 + nota2) / 2


    novo_aluno = {
        "id": cria_id,
        "nome": dados_alunos["nome"],
        "idade": dados_alunos["idade"],
        "turma_id": dados_alunos["turma_id"],
        "data_nascimento": dados_alunos["data_nascimento"],
        "nota_primeiro_semestre": dados_alunos["nota_primeiro_semestre"],
        "nota_segundo_semestre": dados_alunos["nota_segundo_semestre"],
        "media_final": media_final
    }

    usuarios["Alunos"].append(novo_aluno)

    print("Novo aluno cadastrado:", novo_aluno)
    print("Lista atualizada de alunos:", usuarios["Alunos"])

    return jsonify(novo_aluno), 201


@app.route('/alunos', methods=['GET'])
def read_alunos():
    if usuarios["Alunos"]:
        return jsonify(usuarios["Alunos"]), 200
    else:
        return jsonify({"erro":"Nenhum aluno encontrado"}),404


@app.route('/alunos/<int:id_aluno>', methods =['GET'])
def read_alunos_id(id_aluno):
    # Buscar aluno na lista de alunos
    informacoes_aluno = next((aluno for aluno in usuarios["Alunos"] if aluno["id"] == id_aluno), None)
    
    if informacoes_aluno is None:
        return  jsonify({"erro" : "aluno nao encontrado"}), 400
    else:
        return jsonify(informacoes_aluno), 200   


@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def update_alunos(id_aluno):
    informacoes_aluno = next((aluno for aluno in usuarios["Alunos"] if aluno["id"] == id_aluno), None)
    if informacoes_aluno is None:
        return jsonify({"erro": "aluno nao encontrado"}), 400
    dados_alunos = request.get_json()
    if "nome" not in dados_alunos:
        return jsonify({"erro": "aluno sem nome"}), 400
    informacoes_aluno.update(dados_alunos)

    return jsonify(informacoes_aluno), 200
                

@app.route('/alunos/<int:id_aluno>', methods = ['DELETE'])
def delete_aluno(id_aluno):
    #busca o aluno na lisa dos alunos
    A_deletar = next((aluno for aluno in usuarios["Alunos"] if aluno["id"] == id_aluno), None)
    if A_deletar is None:
        return  jsonify({"erro" : "Aluno nao encontrado"}), 400
    else:
        usuarios["Alunos"].remove(A_deletar)
        return jsonify({"message" : "Aluno deletado com sucesso"}), 200
    

@app.route('/alunos', methods = ['DELETE'])
def delete_alunos():
    usuarios["Alunos"].clear()
    id_usuarios["id_alunos"].clear()
    return jsonify({"message": "A lista de Alunos foi deletada"}), 200

if __name__ == '__main__':
    app.run(debug=True,port=5002)
