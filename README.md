
# 📚 API-School-System

Este repositório contém a **API-School-System**, desenvolvida com **Flask** e **SQLAlchemy**, baseada na arquitetura MVC.

## 🧩 Arquitetura

A API-School-System é responsável exclusivamente pelo gerenciamento das entidades Alunos, Professores e Turmas.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- PostgreSQL (como banco de dados Web)
- Requests (para consumo da API externa)
- Docker
- Render
- Flaskrestx
  
---

## ▶️ Como Executar a API localmente

### 1. Clone o repositório

```bash
git clone https://github.com/anabeatriz1908/API-School-System.git
cd API-School-System
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

    - `GET /alunos/<id>` – Detalha um aluno por id

    - `POST /alunos` – Cria um novo aluno

    - `PUT /alunos/<id>` – Altera aluno por id

    - `DELETE /alunos/<id>` – Deleta aluno por id

    - `DELETE /alunos` – Deleta todos os alunos

Professores:

    - `GET /professores` – Lista todas os professores

    - `GET /professores/<id>` – Detalha um professor por id

    - `POST /professores` – Cria um novo professor

    - `PUT /professores/<id>` – Altera um professor por id

    - `DELETE /professores/<id>` – Deleta professor pelo id

    - `DELETE /professores/` – Deleta todos os professores


Turmas:

    - `GET /turmas` – Lista todas as turmas
    
    - `GET /turmas/<id>` – Detalha uma turma por id

    - `POST /turmas` – Cria uma nova turma

    - `PUT /turmas/<id>` – Altera uma turma por id

    - `DELETE /turmas/<id>` – Deleta uma turma por id

    - `DELETE /turmas` – Deleta todas as turmas
    

### Exemplo de corpo JSON do Post:

Alunos:
```json
{
  "nome": "string",
  "turma_id": 0,
  "data_nascimento": "string",
  "nota_primeiro_semestre": 0,
  "nota_segundo_semestre": 0
}
```

Professores:
```json
{
  "nome": "string",
  "materia": "string",
  "observacoes": "string",
  "idade": 0
}
```

Turmas:
```json
{
  "descricao": "string",
  "professor_id": 0,
  "ativo": true
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
| ├── services.py
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
├── dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```
---

## 🐳 Como Executar a API com Docker

1. **Clone o repositório**

```bash
git clone https://github.com/anabeatriz1908/API-School-System.git
cd API-School-System
```

2. Construa a imagem Docker

```bash
docker build -t api-school-system .
```

3. Execute o container

```bash
docker run -d -p 5036:5036 api-school-system
```

4. A aplicação estará disponível em:
📍 `http://localhost:5036`


---

## 🌐 A Api está disponível para consumo na web

Disponível através do link:
📍 `https://apischoolsystem.onrender.com`


Disponível imagem com docker através do link:
📍 `https://devapi-latest-2w6v.onrender.com`

---

## 🧑‍💻 Autores

Grupo 10:

Ana Beatriz Silva Santos - RA: 2401228

Luiz Otávio Santos Silva - RA: 2401300

Murillo Rodrigues Santos Pereira - RA: 2400338

Pablo Neves Vavrik - RA: 2400125

Uatila dos Santos Silva - RA: 2400250


– Projeto educativo de arquitetura com Flask.

