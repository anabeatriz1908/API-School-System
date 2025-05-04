import unittest
from unittest.mock import patch
from app import app
from main.Professor.professores_model import ProfessorNaoEncontrado
from main.Aluno.alunos_model import AlunoNaoEncontrado

class TestProfessorController(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()


    @patch('main.Professor.professores_model.create_professor')
    def test_create_professor_success_01(self, mock_create):
        mock_create.return_value = {"message": "Professor adicionado com sucesso!"}
        payload = {
            "nome": "Ana", "idade": 35, "materia": "Química", "observacoes": "Muito boa"
        }
        response = self.client.post('/professores', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.get_json())

    @patch('main.Professor.professores_model.read_professor')
    def test_get_professores_02(self, mock_read):
        mock_read.return_value = [
            {"id": 1, "nome": "João", "idade": 40, "materia": "Física", "observacoes": "Atencioso"}
        ]
        response = self.client.get('/professores')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0]['nome'], "João")

    @patch('main.Professor.professores_model.read_professor_id')
    def test_get_professor_id_found_03(self, mock_read_id):
        mock_read_id.return_value = {
            "id": 1, "nome": "João", "idade": 40, "materia": "Física", "observacoes": "Atencioso"
        }
        response = self.client.get('/professores/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['nome'], "João")

    @patch('main.Professor.professores_model.read_professor_id')
    def test_get_professor_id_not_found_04(self, mock_read_id):
        mock_read_id.side_effect = ProfessorNaoEncontrado
        response = self.client.get('/professores/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.get_json())

    @patch('main.Professor.professores_model.create_professor')
    def test_create_professor_erro_05(self, mock_create):
        mock_create.side_effect = ValueError("Dados inválidos")
        response = self.client.post('/professores', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.get_json())

    @patch('main.Professor.professores_model.update_professores')
    @patch('main.Professor.professores_model.read_professor_id')
    def test_update_professor_sucesso_06(self, mock_read, mock_update):
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
    def test_update_professor_nao_encontrado_07(self, mock_update):
        mock_update.side_effect = ProfessorNaoEncontrado
        response = self.client.put('/professores/999', json={
            "nome": "X", "idade": 22, "materia": "História", "observacoes": "Nada"
        })
        self.assertEqual(response.status_code, 404)

    @patch('main.Professor.professores_model.delete_professor')
    def test_delete_professor_sucesso_08(self, mock_delete):
        mock_delete.return_value = {"message": "Professor excluido com sucesso!"}
        response = self.client.delete('/professores/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

    @patch('main.Professor.professores_model.delete_professor')
    def test_delete_professor_nao_encontrado_09(self, mock_delete):
        mock_delete.side_effect = ProfessorNaoEncontrado
        response = self.client.delete('/professores/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.get_json())

class TestTurmaController(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch("main.Turma.turmas_model.create_turmas")
    def test_create_turma_sucesso_10(self, mock_create):
        mock_create.return_value = {"message": "Turma criada com sucesso!"}
        response = self.client.post('/turmas', json={
            "descricao": "Lógica da Programação",
            "professor_id": 200,
            "ativo": True
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

    @patch("main.Turma.turmas_model.create_turmas")
    def test_create_turma_valores_nulos_11(self, mock_create):
        mock_create.side_effect = Exception("dados inválidos")
        response = self.client.post('/turmas', json={})
        self.assertEqual(response.status_code, 500)

    @patch("main.Turma.turmas_model.read_turmas")
    def test_read_turmas_12(self, mock_read):
        mock_read.return_value = ([{"id": 1, "descricao": "Test", "ativo": True, "professor_id": 200}], None)
        response = self.client.get('/turmas')
        self.assertEqual(response.status_code, 200)

    @patch("main.Turma.turmas_model.read_turma_id")
    def test_read_turma_id_nao_encontrado_13(self, mock_read):
        mock_read.return_value = None
        response = self.client.get('/turmas/999')
        self.assertEqual(response.status_code, 404)

    @patch("main.Turma.turmas_model.update_turma")
    @patch("main.Turma.turmas_model.read_turma_id")
    def test_update_turma_sucesso_14(self, mock_read, mock_update):
        mock_update.return_value = ({"message": "Turma atualizada com sucesso!"}, None)
        mock_read.return_value = {"id": 378, "descricao": "Nova descrição", "ativo": True, "professor_id": 200}
        response = self.client.put('/turmas/378', json={
            "descricao": "Nova descrição",
            "ativo": True,
            "professor_id": 200
        })
        self.assertEqual(response.status_code, 200)

    @patch("main.Turma.turmas_model.update_turma")
    def test_update_turma_nao_encontrado_15(self, mock_update):
        mock_update.return_value = (None, "Turma não encontrada")
        response = self.client.put('/turmas/999', json={
            "descricao": "Nova",
            "ativo": True,
            "professor_id": 200
        })
        self.assertEqual(response.status_code, 404)

    @patch("main.Turma.turmas_model.delete_turma_por_id")
    def test_delete_turma_sucesso_16(self, mock_delete):
        mock_delete.return_value = True
        response = self.client.delete('/turmas/369')
        self.assertEqual(response.status_code, 200)

    @patch("main.Turma.turmas_model.delete_turma_por_id")
    def test_delete_turma_nao_encontrado_17(self, mock_delete):
        mock_delete.return_value = None
        response = self.client.delete('/turmas/999')
        self.assertEqual(response.status_code, 404)


class TestAlunoController(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch('main.Aluno.alunos_model.create_alunos')
    def test_criar_aluno_sucesso_18(self, mock_create):
        mock_create.return_value = ({"message": "Aluno adicionado com sucesso"}, None)
        payload = {
            "nome": "Maria Silva",
            "data_nascimento": "2005-05-15",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 7.5,
            "turma_id": 1
        }
        response = self.client.post('/alunos', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())

    @patch('main.Aluno.alunos_model.create_alunos')
    def test_criar_aluno_falha_validacao_19(self, mock_create):
        mock_create.return_value = (None, "Dados inválidos")
        response = self.client.post('/alunos', json={})
        self.assertEqual(response.status_code, 400)

    @patch('main.Aluno.alunos_model.read_alunos')
    def test_listar_alunos_21(self, mock_read):
        mock_read.return_value = ([{
            "id": 1,
            "nome": "Maria Silva",
            "data_nascimento": "2005-05-15",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 7.5,
            "turma_id": 1
        }], None)
        response = self.client.get('/alunos')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    @patch('main.Aluno.alunos_model.read_alunos_id')
    def test_obter_aluno_por_id_21(self, mock_read):
        mock_read.return_value = {
            "id": 1,
            "nome": "Maria Silva",
            "data_nascimento": "2005-05-15",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 7.5,
            "turma_id": 1
        }
        response = self.client.get('/alunos/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], 1)

    @patch('main.Aluno.alunos_model.update_alunos')
    @patch('main.Aluno.alunos_model.read_alunos_id')
    def test_atualizar_aluno_sucesso_22(self, mock_read, mock_update):
        aluno_atualizado = {
            "id": 1,
            "nome": "Maria Silva",
            "data_nascimento": "2005-05-15",
            "nota_primeiro_semestre": 9.0,
            "nota_segundo_semestre": 8.0,
            "turma_id": 1
        }
        mock_update.return_value = aluno_atualizado
        mock_read.return_value = aluno_atualizado
        
        response = self.client.put('/alunos/1', json=aluno_atualizado)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["nota_primeiro_semestre"], 9.0)

    @patch('main.Aluno.alunos_model.update_alunos') 
    def test_atualizar_aluno_nao_encontrado_23(self, mock_update):
        mock_update.side_effect = AlunoNaoEncontrado("Aluno não encontrado")
        response = self.client.put('/alunos/999', json={})
        self.assertEqual(response.status_code, 400)

    @patch('main.Aluno.alunos_model.delete_aluno')
    def test_remover_aluno_sucesso_24(self, mock_delete):
        mock_delete.return_value = {"message": "Aluno deletado com sucesso!"}
        response = self.client.delete('/alunos/1')
        self.assertEqual(response.status_code, 200)

    @patch('main.Aluno.alunos_model.delete_aluno') 
    def test_remover_aluno_nao_encontrado_25(self, mock_delete):
        mock_delete.side_effect = AlunoNaoEncontrado("Aluno não encontrado")
        response = self.client.delete('/alunos/999')
        self.assertEqual(response.status_code, 400)



if __name__ == '__main__':
    unittest.main()