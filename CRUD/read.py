from flask import Flask, jsonify, request
app = Flask(__name__)
from random import randint

# Lista de Usuarios
usuarios = {
    "Alunos": {
        100 : {"nome":'Paloma Santos de Sá',"idade": 20, "turma_id":300 , "data_nascimento": "15/01/2005", "nota_primeiro_semestre": 9.6, "nota_segundo_semestre": 8.6, "media_final": 9.1},
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

#Lista de ID dos usuarios
id_usuarios = {
    "id_alunos" : [100, 101, 102],
    "id_professores" : [200, 201],
    "id_turmas" : [300, 301]
}

# READ
@app.route('/read/alunos/<int:id_aluno>', methods =['GET'])
def read_alunos(id_aluno):
    informacoes_aluno = usuarios["Alunos"].get(id_aluno)
    if informacoes_aluno is None:
        return  jsonify("O aluno não foi encontrado no sistema")
    else:
        return jsonify(informacoes_aluno)

@app.route('/read/professores/<int:id_professor>', methods =['GET'])
def read_professor(id_professor):
    informacoes_professor = usuarios["Professores"].get(id_professor)
    if informacoes_professor is None:
        return  jsonify("O professor não foi encontrado no sistema")
    else:
        return jsonify(informacoes_professor)
    
@app.route('/read/turma/<int:id_turma>', methods =['GET'])
def read_turma(id_turma):
    informacoes_turma = usuarios["Turma"].get(id_turma)
    if informacoes_turma is None:
        return  jsonify("A turma não foi encontrado no sistema")
    else:
        return jsonify(informacoes_turma)

if __name__ == '__main__':
    app.run()
