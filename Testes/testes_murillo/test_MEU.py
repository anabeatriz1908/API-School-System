import requests
import unittest
import app

class TestStringMethods(unittest.TestCase):
    def test_006c_id_inexistente_no_delete(self):
        #reseto
        r_reset = requests.post('http://localhost:5002/reseta')
        #vejo se nao deu pau resetar
        self.assertEqual(r_reset.status_code,200)
        r = requests.delete('http://localhost:5002/alunos/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'aluno nao encontrado')

        #404 usuário tentou acessar um recurso inexistente
        #400 usuário fez alguma besteira
        #toda vez que o servidor retorna 404, ele
        #poderia, se quisesse, retornar o erro MENOS INFORMATIVO
        #400. Talvez fosse sacanagem com o programador do outro
        #lado, mas nao seria mentira

        #tento criar 2 caras com a  mesma id
    def test_007_criar_com_id_ja_existente(self):

        #dou reseta e confiro que deu certo
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)

        #crio o usuario bond e confiro
        r = requests.post('http://localhost:5002/alunos',json={'nome':'bond','id':7})
        self.assertEqual(r.status_code,200)

        #tento usar o mesmo id para outro usuário
        r = requests.post('http://localhost:5002/alunos',json={'nome':'james','id':7})
        # o erro é muito parecido com o do teste anterior
        self.assertEqual(r.status_code,400)
        self.assertEqual(r.json()['erro'],'id ja utilizada')

    def test_008a_post_sem_nome(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)

        #tentei criar um aluno, sem enviar um nome
        r = requests.post('http://localhost:5002/alunos',json={'id':8})
        self.assertEqual(r.status_code,400)
        self.assertEqual(r.json()['erro'],'aluno sem nome')

    def test_008b_put_sem_nome(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)

        #criei um aluno sem problemas
        r = requests.post('http://localhost:5002/alunos',json={'nome':'maximus','id':7})
        self.assertEqual(r.status_code,200)

        #mas tentei editar ele sem mandar o nome
        r = requests.put('http://localhost:5002/alunos/7',json={'id':7})
        self.assertEqual(r.status_code,400)
        self.assertEqual(r.json()['erro'],'aluno sem nome')

    def test_100_professores_retorna_lista(self):
        r = requests.get('http://localhost:5002/professores')
        self.assertEqual(type(r.json()),type([]))


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()