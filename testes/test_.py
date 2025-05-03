import unittest
from unittest.mock import patch
from app import app
from main.Professor.professores_model import ProfessorNaoEncontrado

class TestProfessorController(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

#TESTES PROFESSORES
    @patch('main.Professor.professores_model.create_professor')
    def test_create_professor_success(self, mock_create):
        mock_create.return_value = {"message": "Professor adicionado com sucesso!"}
        payload = {
            "nome": "Ana", "idade": 35, "materia": "Química", "observacoes": "Muito boa"
        }

        response = self.client.post('/professores', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.get_json())

    @patch('main.Professor.professores_model.read_professor')
    def test_get_professores(self, mock_read):
        mock_read.return_value = [
            {"id": 1, "nome": "João", "idade": 40, "materia": "Física", "observacoes": "Atencioso"}
        ]
        response = self.client.get('/professores')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0]['nome'], "João")

    @patch('main.Professor.professores_model.read_professor_id')
    def test_get_professor_id_found(self, mock_read_id):
        mock_read_id.return_value = {
            "id": 1, "nome": "João", "idade": 40, "materia": "Física", "observacoes": "Atencioso"
        }
        response = self.client.get('/professores/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['nome'], "João")

    @patch('main.Professor.professores_model.read_professor_id')
    def test_get_professor_id_not_found(self, mock_read_id):
        mock_read_id.side_effect = ProfessorNaoEncontrado
        response = self.client.get('/professores/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.get_json())

    @patch('main.Professor.professores_model.create_professor')
    def test_create_professor_erro(self, mock_create):
        mock_create.side_effect = ValueError("Dados inválidos")
        response = self.client.post('/professores', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.get_json())

    @patch('main.Professor.professores_model.update_professores')
    @patch('main.Professor.professores_model.read_professor_id')
    def test_update_professor_sucesso(self, mock_read, mock_update):
        mock_update.return_value = {"message": "Professor atualizado com sucesso!"}
        mock_read.return_value = {
            "id": 1, "nome": "João", "idade": 45, "materia": "Física", "observacoes": "Atualizado"
        }
        payload = {
            "nome": "João", "idade": 45, "materia": "Física", "observacoes": "Atualizado"
        }
        response = self.client.put('/professores/1', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['idade'], 45)

    @patch('main.Professor.professores_model.update_professores')
    def test_update_professor_nao_encontrado(self, mock_update):
        mock_update.side_effect = ProfessorNaoEncontrado
        response = self.client.put('/professores/999', json={
            "nome": "X", "idade": 22, "materia": "História", "observacoes": "Nada"
        })
        self.assertEqual(response.status_code, 404)

    @patch('main.Professor.professores_model.delete_professor')
    def test_delete_professor_sucesso(self, mock_delete):
        mock_delete.return_value = {"message": "Professor excluido com sucesso!"}
        response = self.client.delete('/professores/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

    @patch('main.Professor.professores_model.delete_professor')
    def test_delete_professor_nao_encontrado(self, mock_delete):
        mock_delete.side_effect = ProfessorNaoEncontrado
        response = self.client.delete('/professores/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.get_json())

#TESTES DE TURMAS
    @patch("main.Turma.turmas_model.create_turmas")
    def test_create_turma_sucesso(self, mock_create):
        mock_create.return_value = {"message": "Turma criada com sucesso!"}
        response = self.client.post('/turmas', json={
            "descricao": "Lógica da Programação",
            "professor_id": 200,
            "ativo": True
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

    @patch("main.Turma.turmas_model.create_turmas")
    def test_create_turma_valores_nulos(self, mock_create):
        mock_create.side_effect = Exception("dados inválidos")
        response = self.client.post('/turmas', json={})
        self.assertEqual(response.status_code, 500)

    @patch("main.Turma.turmas_model.read_turmas")
    def test_read_turmas(self, mock_read):
        mock_read.return_value = ([{"id": 1, "descricao": "Test", "ativo": True, "professor_id": 200}], None)
        response = self.client.get('/turmas')
        self.assertEqual(response.status_code, 200)

    @patch("main.Turma.turmas_model.read_turma_id")
    def test_read_turma_id_nao_encontrado(self, mock_read):
        mock_read.return_value = None
        response = self.client.get('/turmas/999')
        self.assertEqual(response.status_code, 404)

    @patch("main.Turma.turmas_model.update_turma")
    @patch("main.Turma.turmas_model.read_turma_id")
    def test_update_turma_sucesso(self, mock_read, mock_update):
        mock_update.return_value = ({"message": "Turma atualizada com sucesso!"}, None)
        mock_read.return_value = {"id": 378, "descricao": "Nova descrição", "ativo": True, "professor_id": 200}
        response = self.client.put('/turmas/378', json={
            "descricao": "Nova descrição",
            "ativo": True,
            "professor_id": 200
        })
        self.assertEqual(response.status_code, 200)

    @patch("main.Turma.turmas_model.update_turma")
    def test_update_turma_nao_encontrado(self, mock_update):
        mock_update.return_value = (None, "Turma não encontrada")
        response = self.client.put('/turmas/999', json={
            "descricao": "Nova",
            "ativo": True,
            "professor_id": 200
        })
        self.assertEqual(response.status_code, 404)

    @patch("main.Turma.turmas_model.delete_turma_por_id")
    def test_delete_turma_sucesso(self, mock_delete):
        mock_delete.return_value = True
        response = self.client.delete('/turmas/369')
        self.assertEqual(response.status_code, 200)

    @patch("main.Turma.turmas_model.delete_turma_por_id")
    def test_delete_turma_nao_encontrado(self, mock_delete):
        mock_delete.return_value = None
        response = self.client.delete('/turmas/999')
        self.assertEqual(response.status_code, 404)

    @patch("main.Turma.turmas_model.deleta_turmas")
    def test_delete_turmas_todas(self, mock_delete):
        mock_delete.return_value = (True, None)
        response = self.client.delete('/turmas')
        self.assertEqual(response.status_code, 200)