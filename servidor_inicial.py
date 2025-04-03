from flask import Flask, request
import model_alunos


app = Flask(__name__) 

		
@app.route('/alunos', methods=['POST'])
def create_alunos():
    dados_alunos = request.get_json()
    model_alunos.create_alunos(dados_alunos)
    return model_alunos.read_alunos()


@app.route('/alunos', methods=['GET'])
def read_alunos():
    return model_alunos.read_alunos()


@app.route('/alunos/<int:id_aluno>', methods =['GET'])
def read_alunos_id(id_aluno):
    model_alunos.read_alunos_id(id_aluno) 


@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def update_alunos(id_aluno):
    model_alunos.read_alunos_id(id_aluno)
    aluno = request.get_json()
    model_alunos.update_alunos(aluno)
    return model_alunos.read_alunos_id(id_aluno)
                

@app.route('/alunos/<int:id_aluno>', methods = ['DELETE'])
def delete_aluno(id_aluno):
    model_alunos.read_alunos_id(id_aluno)
    model_alunos.delete_aluno(id_aluno)

    

@app.route('/alunos', methods = ['DELETE'])
def delete_alunos():
    model_alunos.delete_alunos()

if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)