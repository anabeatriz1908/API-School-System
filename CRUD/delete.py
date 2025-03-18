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

@app.route('/delete/alunos/<int:id_aluno>', methods = ['DELETE'])
def delete_aluno(id_aluno):
    usuarios["Alunos"].pop(id_aluno)

    if id_aluno not in usuarios["Alunos"]:
        return "Aluno excluído com sucesso"
    else:
        return "Não foi possível excluir o aluno"

@app.route('/delete/professores/<int:id_professor>', methods = ['DELETE'])
def delete_professores(id_professores):
    usuarios["Professores"].pop(id_professores)

    if id_professores not in usuarios["Professores"]:
        return "Professor excluído com sucesso"
    else:
        return "Não foi possível excluir o professor"
    
@app.route('/delete/turmas/<int:id_turmas>', methods = ['DELETE'])
def delete_turmas(id_turmas):
    usuarios["Alunos"].pop(id_turmas)

    if id_turmas not in usuarios["Turmas"]:
        return "Turma excluída com sucesso"
    else:
        return "Não foi possível excluir a turma"

if __name__ == '__main__':
    app.run()