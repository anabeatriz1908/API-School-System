import random
from datetime import datetime, date
from config import db


class Professores(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100),nullable=False)
    observacoes = db.Column(db.String(100),nullable=False)


    def to_dict(self):  
        return {
            "id": self.id, 
            "nome": self.nome, 
            "idade": self.idade, 
            "materia": self.materia, 
            "observacoes": self.observacoes}

class ProfessorNaoEncontrado(Exception):
    pass


def create_professor(dados_professores):
    
    novo_professor = Professores(
        nome = dados_professores['nome'],
        idade = dados_professores["idade"],
        materia = dados_professores["materia"],
        observacoes = dados_professores["observacoes"]
    )

    db.session.add(novo_professor)
    db.session.commit()
    return "Professor adicionado com sucesso!", None #verificar se essa mensagem funciona


def read_professor():
    professores = Professores.query.all()
    print(professores)
    return [professor.to_dict() for professor in professores]


def read_professor_id(id_professor):
    professor = Professores.query.get(id_professor)
    if not professor :
        raise ProfessorNaoEncontrado 
    else:
        return professor.to_dict()


def update_professores(id_professor, dados_professor):
    professor = Professores.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado


    professor.nome = dados_professor["nome"]
    professor.idade = dados_professor["idade"]
    professor.materia = dados_professor["materia"]
    professor.observacoes = dados_professor["observacoes"]

    db.session.commit()


def deleta_professores():
    professores = Professores.query.all()
    for professor in professores:
        db.session.delete(professor)
    db.session.commit()


def delete_professor(id_professor):
    professor = Professores.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado
    
    db.session.delete(professor)
    db.session.commit()
