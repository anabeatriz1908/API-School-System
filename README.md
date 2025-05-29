
# 📚 API-School-System

Este repositório contém a **API-School-System**, desenvolvida com **Flask** e **SQLAlchemy**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API-School-System é responsável exclusivamente pelo gerenciamento de Alunos, Professores e Turmas.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- PostgreSQL (como banco de dados Web)
- Requests (para consumo da API externa)

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/anabeatriz1908/API-School-System.git
cd Reservas
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:5036`

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

Alunos:
    - `GET /alunos` – Lista todas os alunos
    - `POST /alunos` – Cria um novo aluno
    - `GET /alunos/<id>` – Detalha um aluno por id
    - `DELETE /alunos/<id>` – Deleta aluno por id
    - `PUT /alunos/<id>` – Altera aluno por id


Professores:
    - `GET /professores` – Lista todas os professores
    - `POST /professores` – Cria um novo professor
    - `GET /professores/<id>` – Detalha um professor por id
    - `DELETE /professores/<id>` – Deleta professor
    - `PUT /professores/<id>` – Altera um professor por id


Turmas:
    - `GET /turmas` – Lista todas as turmas
    - `POST /turmas` – Cria uma nova turma
    - `GET /turmas/<id>` – Detalha uma turma por id
    - `DELETE /turmas/<id>` – Deleta uma turma por id
    - `PUT /turmas/<id>` – Altera uma turma por id



### Exemplo de corpo JSON para criação:

```json
{
  "turma_id": 1,
  "sala": "101",
  "data": "2025-05-06",
  "hora_inicio": "14:00",
  "hora_fim": "16:00"
}
```

---


## 📦 Estrutura do Projeto

```
API-School-System/
├── main
| ├── Aluno
| | ├── alunos_controller.py
| | ├── alunos_model.py
| ├── Professor
| | ├── professores_controller.py
| | ├── professores_model.py
| ├── Turma
| | ├── turmas_controller.py
| | ├── turmas_model.py
├── services
| ├── services_reservas.py
├── swagger
| ├── namespaces
| | ├── alunos_namespaces.py
| | ├── professores_namespaces.py
| | ├── turmas_namespaces.py
├── testes
| ├── test_.py
| ├── test_bd.py
| ├── test_unidade.py
├── app.py
├── config.py
├── dockerfie
├── requirements.txt
└── README.md
```

---

## 🌐 A Api está disponível para consumo na web

Disponível através do link:
📍 `https://apischoolsystem.onrender.com/docs`


Disponível imagem com docker através do link:
📍 `https://devapi-latest-2w6v.onrender.com/docs`

---

## 🧑‍💻 Autores

Grupo 10:

Ana Beatriz Silva Santos - RA: 2401228

Luiz Otávio Santos Silva - RA: 2401300

Murillo Rodrigues Santos Pereira - RA: 2400338

Pablo Neves Vavrik - RA: 2400125

Uatila dos Santos Silva - RA: 2400250

– Projeto educativo de arquitetura com Flask e microsserviços.

