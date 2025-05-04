import unittest
from datetime import date
from main.Aluno.alunos_model import *

class TestAlunoCalculos(unittest.TestCase):
    def setUp(self):

        class MockAluno:
            def __init__(self):
                self.data_nascimento = date(2000, 1, 15)
                self.nota_primeiro_semestre = 7.0
                self.nota_segundo_semestre = 8.0
            
            def calcular_idade(self, today=None):
                today = today or date.today()
                return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
            
            def calcular_media(self):
                return f"{(self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2:.2f}"

        self.aluno = MockAluno()
    

    def test_calcular_idade_apos_aniversario_01(self):
        hoje_mock = date(2023, 1, 16)
        idade = self.aluno.calcular_idade(hoje_mock)
        self.assertEqual(idade, 23)
    
    def test_calcular_idade_antes_aniversario_02(self):
        hoje_mock = date(2023, 1, 14) 
        idade = self.aluno.calcular_idade(hoje_mock)
        self.assertEqual(idade, 22)
    
    def test_calcular_media_valores_normais_03(self):
        self.aluno.nota_primeiro_semestre = 6.0
        self.aluno.nota_segundo_semestre = 8.0
        media = float(self.aluno.calcular_media())
        self.assertEqual(media, 7.0)
    
    def test_calcular_media_arredondamento_04(self):
        self.aluno.nota_primeiro_semestre = 7.333
        self.aluno.nota_segundo_semestre = 8.666
        media = float(self.aluno.calcular_media())
        self.assertEqual(media, 8.0) 

if __name__ == '__main__':
    unittest.main()