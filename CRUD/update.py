from flask import Flask, jsonify, request
app = Flask(__name__)

# Lista de Usuarios, Alunos, Professores e Turmas
usuarios = {
    "Alunos": {
        100 : {"nome":"Paloma Santos de Sá","idade": 20, "turma_id":300 , "data_nascimento": "15/01/2005", "nota_primeiro_semestre": 9.6, "nota_segundo_semestre": 8.6, "media_final": 9.1},
        101 : {"nome":'Gabriel de Souza Araújo', "idade": 31, "turma_id":300, "data_nascimento": "03/03/1994", "nota_primeiro_semestre": 5.9, "nota_segundo_semestre": 10.0, "media_final": 7.95},
        102 : {"nome":'Yasmim Pessoa Siquiera', "idade": 19, "turma_id":310, "data_nascimento": "19/08/2005", "nota_primeiro_semestre": 8.7, "nota_segundo_semestre": 10.0, "media_final": 9.35}
    },
    "Professores":{
        200 : {"nome": "Vitor Furlan", "idade": 31,"materia": "Fundamentos de Banco de Dados", "observacoes": "Chega no horário e é super competente"},
        201 : {"nome": "Katrina Catarina", "idade": 63,"materia": "Introdução a Estatística", "observacoes": "Tem uma didática excelente e os alunos a amam"}
    },
    "Turmas":{
        300 : {"descricao": "Fundamentos de Banco de Dados", "professor_id": 200, "ativo": True},
        301 :  {"descricao": "Introdução a Estatística", "professor_id": 210, "ativo": True}    
    }
}

@app.route('/update/alunos/<int:id_aluno>', methods = ['PUT'])
def update_alunos(id_aluno):
    # criando uma variavel para registrar o aluno por id. Vamos sobreescrever sobre ela
    atualiza_aluno = usuarios["Alunos"][id_aluno]
    
    # pegando as informações do body no postman
    dados_alunos = request.get_json()

    # Atualizando as informações
    for i in dados_alunos:
        if dados_alunos[i] is not None:
            atualiza_aluno[i] = dados_alunos[i]
       
    return jsonify(usuarios["Alunos"]) # Para a gente ver a lista


@app.route('/update/professores/<int:id_professores>', methods = ['PUT'])
def update_professores(id_professores):
        # criando uma variavel para registrar o aluno por id. Vamos sobreescrever sobre ela
    atualiza_professores = usuarios["Professores"][id_professores]
    
    # pegando as informações do body no postman
    dados_professores = request.get_json()

    # Atualizando as informações
    for i in dados_professores:
        if dados_professores[i] is not None:
            atualiza_professores[i] = dados_professores[i]
       
    
    return jsonify(usuarios["Professores"]) # Para a gente ver a lista

    
@app.route('/update/turmas/<int:id_turmas>', methods = ['PUT'])
def update_turma(id_turmas):
    # criando uma variavel para registrar o aluno por id. Vamos sobreescrever sobre ela
    atualiza_turma = usuarios["Turmas"][id_turmas]
    
    # pegando as informações do body no postman
    dados_turmas = request.get_json()

    # Atualizando as informações
    for i in dados_turmas:
        if dados_turmas[i] is not None:
            atualiza_turma[i] = dados_turmas[i]
       
    
    return jsonify(usuarios["Turmas"]) # Para a gente ver a lista

if __name__ == '__main__':
    app.run()
