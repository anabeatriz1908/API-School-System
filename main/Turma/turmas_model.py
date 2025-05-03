from flask import Flask, request
from config import db
from main.Professor.professores_model import Professores


class Turmas(db.Model):
    __tablename__ = "turmas"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    alunos = db.relationship("Alunos", back_populates="turmas")
    professor_id = db.Column(db.Integer, db.ForeignKey("professores.id"), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "ativo": self.ativo,
            "professor_id": self.professor_id
        }



class TurmaNaoEncontrada(Exception):
    pass


class ProfessorNaoEncontrado(Exception):
    pass 



def create_turmas(dados_turmas):
    professor = Professores.query.get(dados_turmas['professor_id'])
    if(professor is None):
        raise ProfessorNaoEncontrado
        ## ou return "O professor não existe", None #ver se vai retornar certo


    nova_turma = Turmas(
        descricao = dados_turmas["descricao"],
        ativo = dados_turmas["ativo"],
        professor_id = dados_turmas["professor_id"]
    )

    db.session.add(nova_turma)
    db.session.commit()

    return {'message': "Turma criada com sucesso!"}


def read_turmas():
    turmas = Turmas.query.all()
    print(turmas) # esse print aparece no termina, para verificar se esta puxando todos os objetos do bd corretamente
    return [turma.to_dict() for turma in turmas]


def read_turma_id(id_turma):
    turma = Turmas.query.get(id_turma)
    if turma is None:
        raise TurmaNaoEncontrada
    else:
        return turma.to_dict()


def update_turma(id_turma, dados_turmas):
   
    turma = Turmas.query.get(id_turma)
    if turma is None:
        raise TurmaNaoEncontrada

    turma.descricao = dados_turmas["descricao"]
    turma.ativo = dados_turmas["ativo"]
    turma.professor_id = dados_turmas["professor_id"]

    db.session.commit()

    return {"message": "Turma atualizada com sucesso!"}


def delete_turma_por_id(id_turma):
    turma = Turmas.query.get(id_turma)
                             
    if turma is None:
        raise TurmaNaoEncontrada

    db.session.delete(turma)
    db.session.commit()

    return {"message":"Turma excluida com sucesso!"}

def deleta_turmas():
    turmas = Turmas.query.all()
    for turma in turmas:
        db.session.delete(turma)
    db.session.commit()
    return {"message":"Turmas excluidas com sucesso!"}