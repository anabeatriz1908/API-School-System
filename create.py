from flask import Flask, jsonify
#import testes_Create

from flask import Flask, jsonify, request
app = Flask(__name__)
from random import randint

# Lista de Usuarios
usuarios = {
    "Alunos": {
        100 : {"nome":"Paloma Santos de Sá","idade": 20, "turma_id":300 , "data_nascimento": "15-01-2005", "nota_primeiro_semestre": 9.6, "nota_segundo_semestre": 8.6, "media_final": 9.1},
        101 : {"nome":'Gabriel de Souza Araújo', "idade": 31, "turma_id":300, "data_nascimento": "03-03-1994", "nota_primeiro_semestre": 5.9, "nota_segundo_semestre": 10.0, "media_final": 7.95},
        102 : {"nome":'Yasmim Pessoa Siquiera', "idade": 19, "turma_id":310, "data_nascimento": "19-08-2005", "nota_primeiro_semestre": 8.7, "nota_segundo_semestre": 10.0, "media_final": 9.35}
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

@app.route('/create/alunos', methods = ['POST'])
def create_alunos():
    #Criando um id para os alunos
    while True:
        cria_id = randint(100,199)
        if cria_id not in id_usuarios["id_alunos"]:
            id_usuarios["id_alunos"].append(cria_id) #aqui já garante que o id vai para a lista de IDs
            break
    
    #criando um dicionário para o novo aluno
    novo_aluno = {
        "nome":"",
        "idade": 00, 
        "turma_id":000 , 
        "data_nascimento": "00-00-0000", 
        "nota_primeiro_semestre": 0.0, 
        "nota_segundo_semestre": 0.0, 
        "media_final": 0.0
        }

    # pegando as informações do body no postman
    dados_alunos = request.get_json()

    #Verificação de valores null ou atributos faltando
    if novo_aluno.keys() == dados_alunos.keys():
        for chave in dados_alunos:
            novo_aluno[chave] = dados_alunos[chave]
    else:
        for chave in novo_aluno:
            if chave not in dados_alunos.keys():
                print("Não é possível a criação de um novo aluno sem o valor da chave" + chave)
    
    #adicionando novo aluno a usuarios
    usuarios["Alunos"].update({cria_id : novo_aluno})

    # Ver a lista completa dos alunos
    if 2 > 1:
        return usuarios["Alunos"]
    
    # Verificando se o novo aluno foi adicionado a lista
    if cria_id in usuarios["Alunos"]:
        return "Aluno criado com sucesso!"
    else:
        return "Não foi possível criar o aluno"

@app.route('/create/professores', methods = ['POST'])
def create_professores():
    #Criando um id para os professores
    while True:
        cria_id = randint(200,299)
        if cria_id not in id_usuarios["id_professores"]:
            id_usuarios["id_aprofessores"].append(cria_id) #aqui já garante que o id vai para a lista de IDs
            break
    
    #criando um dicionário para o novo aluno
    novo_professor = {
        "nome":"",
        "idade": 00, 
        "materia": "", 
        "observacoes": "00-00-0000", 
        }

    # pegando as informações do body no postman
    dados_professores = request.get_json()

    #Verificação de valores null ou atributos faltando
    if novo_professor.keys() == dados_professores.keys():
        for chave in dados_professores:
            novo_professor[chave] = dados_professores[chave]
    else:
        for chave in novo_professor:
            if chave not in dados_professores.keys():
                print("Não é possível a criação de um novo professor sem o valor da chave" + chave)
    
    #adicionando novo professor a usuarios
    usuarios["Professores"].update({cria_id : novo_professor})

    # Ver a lista completa dos professores
    if 2 > 1:
        return usuarios["Professores"]
    
    # Verificando se o novo professor foi adicionado a lista
    if cria_id in usuarios["Professores"]:
        return "Professor criado com sucesso!"
    else:
        return "Não foi possível criar o professor"
    
@app.route('/create/turmas', methods = ['POST'])
def create_turmas():
    #Criando um id para os turmas
    while True:
        cria_id = randint(100,199)
        if cria_id not in id_usuarios["id_turmas"]:
            id_usuarios["id_turmas"].append(cria_id) #aqui já garante que o id vai para a lista de IDs
            break
    
    #criando um dicionário para o novo aluno
    nova_turma = {
        "descricap":"",
        "professor_id": 000, 
        "ativo": False
        }

    # pegando as informações do body no postman
    dados_turmas = request.get_json()

    #Verificação de valores null ou atributos faltando
    if nova_turma.keys() == dados_turmas.keys():
        for chave in dados_turmas:
            nova_turma[chave] = dados_turmas[chave]
    else:
        for chave in nova_turma:
            if chave not in dados_turmas.keys():
                print("Não é possível a criação de um nova turma sem o valor da chave" + chave)
    
    #adicionando novo aluno a usuarios
    usuarios["Turmas"].update({cria_id : nova_turma})

    # Ver a lista completa dos alunos
    if 2 > 1:
        return usuarios["Turmas"]
    
    # Verificando se o novo aluno foi adicionado a lista
    if cria_id in usuarios["Turmas"]:
        return "Turma criada com sucesso!"
    else:
        return "Não foi possível criar a turma"
    

if __name__ == '__main__':
    app.run()