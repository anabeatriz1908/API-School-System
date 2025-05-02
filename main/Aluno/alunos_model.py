from flask import Flask, jsonify, request
from datetime import datetime, date
from config import db
from main.Turma.turmas_model import Turmas


class Alunos(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False)

    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=False)
    turmas = db.relationship("Turmas", back_populates="alunos")

    def __init__(self, nome, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, turma_id):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.turma_id = turma_id
        self.media_final = self.calcular_media()
        self.idade = self.calcular_idade()

    #fazer teste unitário, para ver se a média e idade são calculadas certas, com testes errados e certos

    def calcular_media(self):
        media_final = (self.nota_primeiro_semestre+self.nota_segundo_semestre)/2
        return f"{media_final:.2f}"
    
    def calcular_idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def to_dict(self):  
        return {
            "id": self.id,
            "nome": self.nome, 
            "idade": self.idade, 
            "data_nascimento": self.data_nascimento.isoformat(), 
            "nota_primeiro_semestre": self.nota_primeiro_semestre, 
            "nota_segundo_semestre": self.nota_segundo_semestre, 
            "turma_id": self.turma_id, 
            "media_final": self.media_final
            }
    # pra retornar um novo aluno, como dicionário, formatado



class AlunoNaoEncontrado(Exception):
    pass 



def create_alunos(aluno):
    # verificando se turma existe
    turma = Turmas.query.get(aluno["turma_id"])  #rever essa parte, pode dar erro no BD
    if(turma is None):
        return "Turma não existe", None

    novo_aluno = Alunos(
        nome = aluno["nome"],
        data_nascimento = datetime.strptime(aluno["data_nascimento"],),
        nota_primeiro_semestre= float(aluno["nota_primeiro_semestre="]),
        nota_segundo_semestre= float(aluno["nota_segundo_semestre="]),
        turma_id= int(aluno["turma_id"])
    )

    db.session.add(novo_aluno)
    db.session.commit()
    return "Aluno adicionado com sucesso", None # verificar se essa mensagem vai passar

    
    # professor colocou igual em baixo
    # return {"message": "Aluno adicionado com sucesso"},201  

def read_alunos():
    alunos = Alunos.query.all()
    print(alunos)
    return [aluno.to_dict() for aluno in alunos]


def read_alunos_id(id_aluno):
    aluno = Alunos.query.get(id_aluno)

    if not aluno:
        raise  AlunoNaoEncontrado(f'Aluno não encontrado.')
    return Alunos.to_dict()


def update_alunos(id_aluno, dados_atualizados):
    aluno = Alunos.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado

    aluno.nome = dados_atualizados["nome"]
    aluno.data_nascimento = dados_atualizados["data_nascimento"]
    aluno.nota_primeiro_semestre = dados_atualizados["nota_primeiro_semestre"]
    aluno.nota_segundo_semestre = dados_atualizados["nota_segundo_semestre"]
    aluno.media_final = aluno.calcular_media()
    aluno.turma_id = aluno["turma_id"]
    aluno.idade = aluno.calcular_idade()

    db.session.commit()


def delete_aluno(id_aluno):
    aluno = Alunos.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(f'Aluno não encontrado.')
    db.session.delete(aluno)
    db.session.commit()
    return True


# Verificar se essa função funciona corretamente
def delete_alunos():
    alunos = Alunos.query.all()
    for aluno in alunos:
        db.session.delete(aluno)
    db.session.commit
    return True, None