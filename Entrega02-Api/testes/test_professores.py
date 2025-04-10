import requests
import unittest
import app

class TestStringMethods(unittest.TestCase):
    def test_professores_read_06(self):
            dados = requests.get("http://localhost:5036/professores")
            self.assertEqual(dados.status_code, 200)

    def test_professores_read_id_07(self):
        dados = requests.get("http://localhost:5036/professores/200")
        self.assertEqual(type(dados.json()), dict)
        
    def test_professores_criar_08(self):
        dados = requests.post("http://localhost:5036/professores", json = {
             "id": 2, 
             "nome": "Murillo", 
             "idade": 20, 
             "materia": "APIs", 
             "observacoes": "Provavelmente não dormiu hoje"
        })
        resposta = requests.get("http://localhost:5036/professores/2")
        self.assertEqual(type(resposta.json()), dict)

    def test_professores_update_09(self):
        antigo = requests.get("http://localhost:5036/professores/200")
        dados = requests.put("http://localhost:5036/professores/200", json = {"nome": "Outro nome"})
        atualizado = requests.get("http://localhost:5036/professores/200")
        self.assertNotEqual (antigo.json(), atualizado.json()) 

    def test_professores_delete_10(self):
        deletar = requests.delete("http://localhost:5036/professores/2")
        r = requests.get("http://localhost:5036/professores/2")
        self.assertEqual(r.status_code, 404)

    def test_professores_criar_id_existente_11(self):
        create1 = requests.post("http://localhost:5036/professores", json = {
             "id": 4,
            "nome": "Murillo", 
            "idade": 20, 
            "materia": "APIs", 
            "observacoes": "Provavelmente não dormiu hoje"
        })
        self.assertEqual(create1.status_code, 201) 
        create2 = requests.post("http://localhost:5036/professores", json = {
             "id": 4, 
             "nome": "Caio", 
             "idade": 25, 
             "materia": "APIs", 
             "observacoes": "Tatuagens maneiras"
        })
        self.assertEqual(create2.status_code, 400)

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()