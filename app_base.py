from flask import Flask, jsonify

app = Flask(__name__)

usuarios = {
    "Alunos": [
        {"id": 1, "nome":'Murillo', "idade": 20, "turma_id": 1, "data_nascimento": "15/01/2005", "nota_primeiro_semestre": 2.0, "nota_segundo_semestre": 10.0, "media_final": 6.0},
        {"id": 2, "nome":'Pablo', "idade": 50, "turma_id":1, "data_nascimento": "03/03/1994", "nota_primeiro_semestre": 6.5, "nota_segundo_semestre": 10.0, "media_final": 6.0},
        {"id": 3, "nome":'Ana', "idade": 34, "turma_id":2, "data_nascimento": "30/03/1963", "nota_primeiro_semestre": 6.5, "nota_segundo_semestre": 10.0, "media_final": 6.0}
    ],
    "Professores":[
        {"id": 1, "nome": "Caio", "idade": 31,"materia": "API e microsserviços", "observacoes": "Ama dar aula"},
        {"id": 2, "nome": "Odair", "idade": 63,"materia": "DEVOPS", "observacoes": "ama mais ou menos dar aula"}
    ],
    "Turma":[
        {"id": 1, "descricao": "ensina usar pyhton pra construir api, muito legal", "professor_id": 1, "ativo": True},
        {"id": 2, "descricao": "ensina usar a cultura devops, e fala das expericências dele, COOL!", "professor_id": 2, "ativo": True}    
    ]
}

@app.route('/', methods = ["GET"])
def msg():
    dados = {'Mensagem': 'Seja bem vindo ao programa Flask'}
    return jsonify(dados)

@app.route('/users', methods = ["GET"])
def getUsers():
    dados = {'Mensagem': 'Seja bem vindo ao programa Flask'}
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)




"""
1. perguntar como vai funcionar o relacionamento entre turma_id, e professor_id

2. perguntar sobre a númeração automática de id aluno, id materia e id professor

3. perguntar sobre o cálculo de média final
"""