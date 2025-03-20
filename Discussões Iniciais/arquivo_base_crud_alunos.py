'''
Arquivo base, feito na aula de Flask
'''
#%%
#Importações
from flask import Flask, jsonify

import request 
import unittest

#%%
# Lista de Usuarios
usuarios = {
    "Alunos": {
        100 : {"nome":'Paloma Santos de Sá', "idade": 20, "turma_id":300 , "data_nascimento": "15/01/2005", "nota_primeiro_semestre": 9.6, "nota_segundo_semestre": 8.6, "media_final": 9.1},
        110 : {"nome":'Gabriel de Souza Araújo', "idade": 31, "turma_id":300, "data_nascimento": "03/03/1994", "nota_primeiro_semestre": 5.9, "nota_segundo_semestre": 10.0, "media_final": 7.95},
        120 : {"nome":'Yasmim Pessoa Siquiera', "idade": 19, "turma_id":310, "data_nascimento": "19/08/2005", "nota_primeiro_semestre": 8.7, "nota_segundo_semestre": 10.0, "media_final": 9.35}
    },
    "Professores":{
        200 : {"nome": "Vitor Furlan", "idade": 31,"materia": "Fundamentos de Banco de Dados", "observacoes": "Chega no horário e é super competente"},
        210 : {"nome": "Katrina Catrai", "idade": 63,"materia": "Introdução a Estatística", "observacoes": "Tem uma didática excelente e os alunos a amam"}
    },
    "Turma":{
        300 : {"descricao": "Fundamentos de Banco de Dados", "professor_id": 200, "ativo": True},
        310 :  {"descricao": "Introdução a Estatística", "professor_id": 210, "ativo": True}    
    }
}
#%%
#Criando alunos
@app.route('/create/alunos', method=['POST'])
def create_alunos():
    novo_aluno = request.json
    alunos.append(novo_aluno)
    return jsonify({'mensagem': 'Aluno criado com sucesso!'})

# Lendo alunos
@app.route('/read/alunos{id_aluno}', methods=['GET'])
def read_alunos(id_aluno):
      read_aluno = usuarios["Alunos"][id_aluno]
      return jsonify(read_aluno)
      

#Atualizando alunos por ID
@app.route('/update/alunos/{id_aluno}', method=['PUT'])
def update_aluno(): #ATENÇÃO: INFORMAÇÕES CHUMBADAS
    novos_dados_alunos = {
         novo_nome = "Novo nome",
         nova_turma = 000, #Id da turma
         nova_nota_um_semestre = 0.0,
         nova_nota_dois_semestre = 0.0,
         nova_media = (nova_nota_um_semestre + nova_nota_dois_semestre)/2
    }


#Deletando um aluno por ID
@app.route('/delete/alunos', method=['DELETE'])
def delete_alunos(id):
     alunos[id].remove()


if __name__ == '__main__':
    app.run(debug=True)

