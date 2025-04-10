import requests
import unittest
import app


class TestStringMethods(unittest.TestCase):
    def test_turmas_create_12(self):

        turma_a = requests.post('http://localhost:5036/turmas', json={"id" : 320, "descricao": "Lógica da Programação", "professor_id": 200, "ativo": True})
        r_turma_a = requests.get('http://localhost:5036/turmas/320')
        self.assertEqual(r_turma_a.status_code,200)

        turma_b = requests.post('http://localhost:5036/turmas', json={"id" : 399, "descricao": "Soft Skills", "professor_id": 200, "ativo": True})
        r_turma_b = requests.get('http://localhost:5036/turmas/399')

    def test_turmas_create_valores_nulos_13(self):

        turma = requests.post('http://localhost:5036/turmas', json={"descricao": "Lógica da Programação", "professor_id": 200, "ativo": True})
        self.assertEqual(turma.status_code, 400)

        turma_a = requests.post('http://localhost:5036/turmas', json={"id": 360, "descricao": "Lógica da Programação", "ativo": True})
        self.assertEqual(turma_a.status_code, 400)

        turma_b = turma_a = requests.post('http://localhost:5036/turmas', json={"id": 360, "professor_id": 200, "ativo": True})
        self.assertEqual(turma_b.status_code, 400)


    def test_turmas_read_14(self):
         turma_total = requests.get('http://localhost:5036/turmas')
         self.assertEqual(turma_total.status_code,200)


    def test_turmas_read_id_15(self):
         turma = requests.get('http://localhost:5036/turmas/7800')
         self.assertEqual(turma.status_code,404)


    def test_turmas_upload_16(self):
         #Vou criar uma turma
         turma = requests.post('http://localhost:5036/turmas', json={"id":378, "descricao": "Introdução ao Calculo IO", "ativo":True,"professor_id":200})
         self.assertEqual(turma.status_code,200) #Vejo se minha turma foi criada
         p_turma = requests.put('http://localhost:5036/turmas/378', json = {"descricao": "Introdução a Calculo II"})
         self.assertEqual(p_turma.status_code,200)


    def test_turmas_upload_id_nao_encontrado_17(self):
        turma = requests.put('http://localhost:5036/turmas/478', json={"ativo": False})
        self.assertEqual(turma.status_code,404)


    def test_turmas_delete_18(self):
        requests.post('http://localhost:5036/turmas', json={"id":369, "descricao": "Engenharia de Requisitos", "professor_id": 201, "ativo": True} )
        c_turma = requests.get('http://localhost:5036/turmas/369')
        self.assertEqual(c_turma.status_code, 200)

        d_turma = requests.delete('http://localhost:5036/turmas/369')
        self.assertEqual(d_turma.status_code, 200)
    
    def test_turmas_reseta_19(self):
        limpa = requests.delete('http://localhost:5036/turmas')
        self.assertEqual(limpa.status_code,200)


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()