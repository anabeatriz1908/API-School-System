import requests
import unittest
import test_professores

class TestStringMethods(unittest.TestCase):
    def test_001_read_professores(self):
         dados = requests.get("http://localhost:5002/professores")
         self.assertEqual(dados.status_code, 200)

    def test_001_read_professor_id(self):
         dados = requests.get("http://localhost:5002/professores/200")
         self.assertEqual(type(dados.json()), dict)
         
    def test_003_criar_professor(self):
         dados = requests.post("http://localhost:5002/professores", json = {"id": 2, "nome": "Murillo", "idade": 20, "materia": "APIs", "observacoes": "Provavelmente não dormiu hoje"})
         resposta = requests.get("http://localhost:5002/professores/2")
         self.assertEqual(type(resposta.json()), dict)

    def test_004_update_professor(self):
         antigo = requests.get("http://localhost:5002/professores/200")
         dados = requests.put("http://localhost:5002/professores/200", json = {"nome": "Outro nome"})
         atualizado = requests.get("http://localhost:5002/professores/200")
         self.assertNotEqual (antigo.json(), atualizado.json()) 

    def test_005_delete_professor(self): #Já serve de teste para buscar por um id inexistente
         deletar = requests.delete("http://localhost:5002/professores/2")
         r = requests.get("http://localhost:5002/professores/2")
         self.assertEqual(r.status_code, 400)

    def test_006_criar_professor_id_existente(self):
         create1 = requests.post("http://localhost:5002/professores", json = {"id": 4, "nome": "Murillo", "idade": 20, "materia": "APIs", "observacoes": "Provavelmente não dormiu hoje"})
         self.assertEqual(create1.status_code, 200) #Conferir se realmente criou
         create2 = requests.post("http://localhost:5002/professores", json = {"id": 4, "nome": "Caio", "idade": 25, "materia": "APIs", "observacoes": "Tatuagens maneiras"})
         self.assertEqual(create2.status_code, 400)


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()
