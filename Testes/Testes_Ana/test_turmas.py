import requests
import unittest

class TestStringMethods(unittest.TestCase):
    #Criando duas turmas
    def test_create_turma(self):
        #Criando a Turma
        turma_a = requests.post('http://localhost:5002/turmas', json={"id" : 320, "descricao": "Lógica da Programação", "professor_id": 200, "ativo": True})
        r_turma_a = requests.get('http://localhost:5002/turmas/320')
        #Vendo de a turma foi criada
        self.assertEqual(r_turma_a.status_code,200)
        turma_b = requests.post('http://localhost:5002/turmas', json={"id" : 399, "descricao": "Soft Skills", "professor_id": 200, "ativo": True})
        r_turma_b = requests.get('http://localhost:5002/turmas/399')
    #Tentando criar uma turma com valores nulos
    def test_create_turma_valores_nulos(self):
        #Não foi passado Id
        turma = requests.post('http://localhost:5002/turmas', json={"descricao": "Lógica da Programação", "professor_id": 200, "ativo": True})
        self.assertEqual(turma.status_code, 400)

        #Não foi passado professor_id
        turma_a = requests.post('http://localhost:5002/turmas', json={"id": 360, "descricao": "Lógica da Programação", "ativo": True})
        self.assertEqual(turma_a.status_code, 400)

        #Não foi passado descricao
        turma_b = turma_a = requests.post('http://localhost:5002/turmas', json={"id": 360, "professor_id": 200, "ativo": True})
        self.assertEqual(turma_b.status_code, 400)

    #Lendo a lista de turmas
    def test_read_turmas(self):
         turma_total = requests.get('http://localhost:5002/turmas')
         self.assertEqual(turma_total.status_code,200)

    #Aqui eu vou tentar ler uma lista de turmas que não existe
    def test_read_turmas_id(self):
         turma = requests.get('http://localhost:5002/turmas/7800')
         self.assertEqual(turma.status_code,400)

    #Atualizando informações de turmas
    def test_upload_turmas(self):
         #Vou criar uma turma
         turma = requests.post('http://localhost:5002/turmas', json={"id":378, "descricao": "Introdução ao Calculo IO", "ativo":True,"professor_id":200})
         self.assertEqual(turma.status_code,200) #Vejo se minha turma foi criada
         p_turma = requests.put('http://localhost:5002/turmas/378', json = {"descricao": "Introdução a Calculo II"})
         self.assertEqual(p_turma.status_code,200)

    #Procurando uma turma por id que não existe
    def test_upload_turmas_id_nao_encontrado(self):
        turma = requests.put('http://localhost:5002/turmas/478', json={"ativo": False})
        self.assertEqual(turma.status_code,400)

    #Deletando uma turma
    def test_delete_turmas(self):
        requests.post('http://localhost:5002/turmas', json={"id":369, "descricao": "Engenharia de Requisitos", "professor_id": 210, "ativo": True} )
        c_turma = requests.get('http://localhost:5002/turmas/369')
        self.assertEqual(c_turma.status_code, 200) #Criação da turma deu certo

        d_turma = requests.delete('http://localhost:5002/turmas/369')
        self.assertEqual(d_turma.status_code, 200)
    
    def test_reseta_turmas(self):
        reseta = requests.post('http://localhost:5002/reseta/turmas')
        self.assertEqual(reseta.status_code,200)
   

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()
