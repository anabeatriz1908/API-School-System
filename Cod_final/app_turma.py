from flask import Flask, jsonify, request
app = Flask(__name__)
from random import randint
import test_turmas_crud

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
    "Turmas":[        
        {"id" : 300,"descricao": "Fundamentos de Banco de Dados", "professor_id": 200, "ativo": True},
        {"id" : 310, "descricao": "Introdução a Estatística", "professor_id": 210, "ativo": True} 
    ]
}


id_usuarios = {
    "id_alunos" : [45, 3],
    "id_professores" : [200, 201],
    "id_turmas" : [300, 301]
}

#ROTAS TURMAS 
#CREATE CREATE CREATE CREATE CREATE CREATE CREATE CREATE CREATE CREATE CREATE CREATE CREATE CREATE CREATE CREATE 
@app.route('/turmas', methods=['POST'])
def create_turmas():
    # Pegando as informações do corpo da requisição
    dados_turmas = request.get_json()

    # Verificação de valores nulos ou atributos faltando
    if "descricao" not in dados_turmas:
        return jsonify({"erro": "turma sem descricao"}), 400
    
    if "id" not in dados_turmas:
        return jsonify({"erro": "turma sem id"}), 400
    
    if "professor_id" not in dados_turmas:
        return jsonify({"erro": "turma sem professor"}), 400

    cria_id = dados_turmas["id"]
    # Verifica se o ID já existe
    if cria_id in id_usuarios["id_alunos"]:
        #print("IDs de alunos já cadastrados:", id_usuarios["id_alunos"])
        return jsonify({"erro" : "id ja utilizado"}), 400
 

    # Adiciona o ID à lista para evitar duplicação
    id_usuarios["id_alunos"].append(cria_id)

    # Criando um dicionário para o novo aluno
    nova_turma = dados_turmas.copy()
    print(nova_turma)

    # Adicionando novo aluno à lista de usuários
    usuarios["Turmas"].append(nova_turma)

    print("Novo turma cadastrada:", nova_turma)

    # Retorna o novo aluno criado
    return jsonify(nova_turma), 200

# READ READ READ READ READ READ READ READ READ READ READ READ READ READ READ READ READ READ READ READ READ READ
@app.route('/turmas', methods=['GET'])
def read_turmas():
    print(usuarios["Turmas"])
    return jsonify(usuarios["Turmas"]), 200

@app.route('/turmas/<int:id_turma>', methods=['GET'])
def read_turma_id(id_turma):
    # Buscar turma na lista de turmas
    informacoes_turma = next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turma), None)
    
    if informacoes_turma is None:
        return jsonify({"erro" : "turma não encontrada"}), 400
    else:
        return jsonify(informacoes_turma), 200 

# UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE UPDATE 
@app.route('/turmas/<int:id_turma>', methods=['PUT'])
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


# DELETE DELELTE DELETE DELELTE DELETE DELELTE DELETE DELELTE DELETE DELELTE DELETE DELELTE 
@app.route('/turmas/<int:id_turma>', methods=['DELETE'])
def delete_turma(id_turma):
    a_deletar = next((turma for turma in usuarios["Turmas"] if turma["id"] == id_turma), None)
    if a_deletar is None:
        return jsonify({"erro" : "turma não encontrada"}), 400
    else:
        usuarios["Turmas"].remove(a_deletar)
        return jsonify({"message": "turma deletada com sucesso"}), 200

#-----------------------------------------------------------------------------------------------

@app.route('/reseta/turmas', methods=['POST'])
def reseta_api():
    usuarios["Turmas"].clear()
    id_usuarios["id_turmas"].clear()
    return jsonify({"message": "A lista de turmas foi resetada"}), 200

if __name__ == '__main__':
    app.run(debug=False,port=5002)