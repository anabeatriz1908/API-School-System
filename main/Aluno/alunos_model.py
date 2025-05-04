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


class AlunoNaoEncontrado(Exception):
    pass 



def create_alunos(aluno):
    # verificando se turma existe
    turma = Turmas.query.get(aluno["turma_id"])
    if(turma is None):
        return {"message":"Turma não existe"}

    novo_aluno = Alunos(
        nome = aluno["nome"],
        data_nascimento = datetime.strptime(aluno["data_nascimento"],"%Y-%m-%d").date(),
        nota_primeiro_semestre= float(aluno["nota_primeiro_semestre"]),
        nota_segundo_semestre= float(aluno["nota_segundo_semestre"]),
        turma_id= int(aluno["turma_id"])
    )

    db.session.add(novo_aluno)
    db.session.commit()
    return {"message":"Aluno adicionado com sucesso"} 

    

def read_alunos():
    alunos = Alunos.query.all()
    print(alunos)
    return [aluno.to_dict() for aluno in alunos]


def read_alunos_id(id_aluno):
    aluno = Alunos.query.get(id_aluno)

    if not aluno:
        raise  AlunoNaoEncontrado(f'Aluno não encontrado.')
    return aluno.to_dict()


def update_alunos(id_aluno, dados_atualizados):
    aluno = Alunos.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    
    data_nasc = dados_atualizados.get("data_nascimento")
    
    aluno.nome = dados_atualizados["nome"]
    aluno.data_nascimento = datetime.strptime(data_nasc, "%Y-%m-%d").date() if isinstance(data_nasc, str) else data_nasc
    aluno.nota_primeiro_semestre = dados_atualizados["nota_primeiro_semestre"]
    aluno.nota_segundo_semestre = dados_atualizados["nota_segundo_semestre"]
    aluno.media_final = aluno.calcular_media()
    aluno.turma_id = dados_atualizados["turma_id"]
    aluno.idade = aluno.calcular_idade()

    db.session.commit()

    return {"message": "Aluno atualizado com sucesso!"}

def delete_aluno(id_aluno):
    aluno = Alunos.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(f'Aluno não encontrado.')
    db.session.delete(aluno)
    db.session.commit()
    return {"message":"Aluno deletado com sucesso!"}


# Verificar se essa função funciona corretamente
def delete_alunos():
    alunos = Alunos.query.all()
    for aluno in alunos:
        db.session.delete(aluno)
    db.session.commit()
    return {'message':"Alunos deletados com sucesso!"}