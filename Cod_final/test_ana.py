import requests
import unittest
import app


class TestStringMethods(unittest.TestCase):
    def test_create_alunos(self):
        return
    
    def test_create_professores(self):
        return
    
    def test_create_turmas(self):
        return
    
    def test_read_alunos(self):
        return
    
    def tet_read_professores(self):
        return
    
    def test_read_turmas(self):
        return
    
    def test_update_alunos(self):
        #Criação de um aluno
        requests.post('http://localhost:5002/alunos',json={"id": 103, "nome":"Gabrielle Souza","idade": 20, "turma_id":300 , "data_nascimento": "19/03/2005", "nota_primeiro_semestre": 9.0, "nota_segundo_semestre": 9.0, "media_final": 9.0})

        #Mudança da nota do 1 semestre
        requests.put('http://localhost:5002/alunos/103', json={'nota_primeiro_semestre':10.0})
        requests.put('http://localhost:5002/alunos/103', json={'media_final':9.5})

        #Exibindo informações da Aluna
        r_informacoes = requests.get('http://localhost:5002/alunos/103')
        
        #A nota do 1 º semestre e a media devem ter mudado
        self.assertEqual(r_informacoes.json()['nota_primeiro_semestre'],10.0)
        self.assertEqual(r_informacoes.json()['media_final'],9.5)
        
    
    def test_update_professores(self):
        return
    
    def test_update_turmas(self):
        return
    
    def test_delete_alunos(self):
        return
    
    def test_delete_professores(self):
        return
    
    def test_delete_turmas(self):
        return
    
    def test_004_deleta(self):
        #apago tudo -> OK
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
    
        #crio 3 alunos -> OK
        requests.post('http://localhost:5002/alunos',json={'nome':'cicero','id':29})
        requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':28})
        requests.post('http://localhost:5002/alunos',json={'nome':'marta','id':27})
    
        #pego a lista completa -> OK
        r_lista = requests.get('http://localhost:5002/alunos')
        lista_retornada = r_lista.json()
    
        #a lista completa tem que ter 3 elementos -> OK
        self.assertEqual(len(lista_retornada),3)
    
        #faço um request com delete, pra deletar o aluno de id 28 - OK
        requests.delete('http://localhost:5002/alunos/28')
    
        #pego a lista de novo
        r_lista2 = requests.get('http://localhost:5002/alunos')
        lista_retornada2 = r_lista2.json()
        
        #e vejo se ficou só um elemento
        self.assertEqual(len(lista_retornada2),2) 

        acheiMarta = False
        acheiCicero = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'marta':
                acheiMarta=True
            if aluno['nome'] == 'cicero':
                acheiCicero=True
        if not acheiMarta or not acheiCicero:
            self.fail("voce parece ter deletado o aluno errado!")

        requests.delete('http://localhost:5002/alunos/27')

        r_lista3 = requests.get('http://localhost:5002/alunos')
        lista_retornada3 = r_lista3.json()
        #e vejo se ficou só um elemento
        self.assertEqual(len(lista_retornada3),1) 

        if lista_retornada3[0]['nome'] == 'cicero':
            pass
        else:
            self.fail("voce parece ter deletado o aluno errado!")


    #cria um usuário, depois usa o verbo PUT
    #para alterar o nome do usuário
    def test_005_edita(self):
        #resetei
        r_reset = requests.post('http://localhost:5002/reseta')
        #verifiquei se o reset foi
        self.assertEqual(r_reset.status_code,200)

        #criei um aluno
        requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':28})
        
        #e peguei o dicionario dele
        r_antes = requests.get('http://localhost:5002/alunos/28')

        #o nome enviado foi lucas, o nome recebido tb
        self.assertEqual(r_antes.json()['nome'],'lucas')

        #vou editar. Vou mandar um novo dicionario p/ corrigir o dicionario
        #que já estava no 28 (note que só mandei o nome)
        #para isso, uso o verbo PUT
        requests.put('http://localhost:5002/alunos/28', json={'nome':'lucas mendes'})
        #pego o novo dicionario do aluno 28
        r_depois = requests.get('http://localhost:5002/alunos/28')
        #agora o nome deve ser lucas mendes
        self.assertEqual(r_depois.json()['nome'],'lucas mendes')
        #mas o id nao mudou
        self.assertEqual(r_depois.json()['id'],28)

    #tenta fazer GET, PUT e DELETE num aluno que nao existe
    def test_006a_id_inexistente_no_put(self):
        #reseto
        r_reset = requests.post('http://localhost:5002/reseta')
        #vejo se nao deu pau resetar
        self.assertEqual(r_reset.status_code,200)
        #estou tentando EDITAR um aluno que nao existe (verbo PUT)
        r = requests.put('http://localhost:5002/alunos/15',json={'nome':'bowser','id':15})
        #tem que dar erro 400 ou 404
        #ou seja, r.status_code tem que aparecer na lista [400,404]
        self.assertIn(r.status_code,[400,404])
        #qual a resposta que a linha abaixo pede?
        #um json, com o dicionario {"erro":"aluno nao encontrado"}
        self.assertEqual(r.json()['erro'],'aluno nao encontrado')
    
    def test_006b_id_inexistente_no_get(self):
        #reseto
        r_reset = requests.post('http://localhost:5002/reseta')
        #vejo se nao deu pau resetar
        self.assertEqual(r_reset.status_code,200)

        #agora faço o mesmo teste pro GET, a consulta por id
        r = requests.get('http://localhost:5002/alunos/15')
        self.assertIn(r.status_code,[400,404])
        
        #olhando pra essa linha debaixo, o que está especificado que o servidor deve retornar
        self.assertEqual(r.json()['erro'],'aluno nao encontrado')
        #                ------
        #                string json
        #                ----------------
        #                que representa um dicionario
        #                o dict tem a chave erro
        #                                 ----------------------
        #                                 o valor da chave erro

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)
if __name__ == '__main__':
    runTests()