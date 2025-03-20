import requests
import unittest
import app


class TestStringMethods(unittest.TestCase):

    def test_alunos_read_alunos_01(self):
        r = requests.get('http://localhost:5036/alunos')
        self.assertEqual(r.status_code,200)
        
        
    def test_alunos_read_aluno_por_id_02(self):
        r = requests.post('http://localhost:5036/alunos',json={
            "id": 93,
            "nome": "Jonas Adalberto",
            "idade": 47, 
            "turma_id": 310, 
            "data_nascimento": "27/03/1979", 
            "nota_primeiro_semestre": 8.4, 
            "nota_segundo_semestre": 9.2
        })
        resposta = requests.get('http://localhost:5036/alunos/93')
        self.assertEqual(resposta.status_code,200)
        dict_retornado = resposta.json() 
        self.assertEqual(type(dict_retornado),dict)
        self.assertIn("nome",dict_retornado)
        self.assertEqual(dict_retornado["nome"], "Jonas Adalberto")


    def test_alunos_update_03(self):

        r_reset = requests.delete('http://localhost:5036/alunos')
        self.assertEqual(r_reset.status_code,200)

        r_post = requests.post('http://localhost:5036/alunos',json={
            "id": 87, 
            "nome": "Cícero", 
            "idade": 47, 
            "turma_id": 310, 
            "data_nascimento": "26/03/1978", 
            "nota_primeiro_semestre": 8.4, 
            "nota_segundo_semestre": 9.2
        })

        self.assertEqual(r_post.status_code, 200, f"Erro ao criar aluno: {r_post.text}")

        r_antes = requests.get('http://localhost:5036/alunos/87')
        self.assertEqual(r_antes.status_code,200)
        requests.put('http://localhost:5036/alunos/87', json={ "nome": "Cícero Gonçalves"})

        r_depois = requests.get('http://localhost:5036/alunos/87')
        self.assertEqual(r_depois.json()["nome"],"Cícero Gonçalves")


    def test_alunos_deleta_todos_alunos_04(self):
        r = requests.post('http://localhost:5036/alunos',json={
            "id": 87, 
            "nome": "Cícero Gonçalves", 
            "idade": 47, 
            "turma_id": 310, 
            "data_nascimento": "26/03/1978", 
            "nota_primeiro_semestre": 8.4, 
            "nota_segundo_semestre": 9.2
        })
        r_lista = requests.get('http://localhost:5036/alunos')
        r_reset = requests.delete('http://localhost:5036/alunos')
        self.assertEqual(r_reset.status_code,200)

        r_lista_depois = requests.get('http://localhost:5036/alunos')
        self.assertEqual(len(r_lista_depois.json()),1)
        self.assertEqual(r_lista_depois.status_code,404)


    def test_alunos_deleta_por_id_05(self):

        r_reset = requests.delete('http://localhost:5036/alunos')
        self.assertEqual(r_reset.status_code,200)

        requests.post('http://localhost:5036/alunos',json={
            "id": 87, 
            "nome": "Cícero Gonçalves", 
            "idade": 47, "turma_id": 310, 
            "data_nascimento": "26/03/1978", 
            "nota_primeiro_semestre": 8.4, 
            "nota_segundo_semestre": 9.2
        })
        r_lista = requests.get('http://localhost:5036/alunos')
        lista_retornada = r_lista.json()
        self.assertEqual(len(lista_retornada),1)

        requests.delete('http://localhost:5036/alunos/87')
        self.assertEqual(r_reset.status_code,200)

        r_lista2 = requests.get('http://localhost:5036/alunos')
        self.assertEqual(r_lista2.status_code,404) 

# --------------------------------------------------------------------#

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
        self.assertEqual(r.status_code, 400)

    def test_professores_criar_id_existente_11(self):
        create1 = requests.post("http://localhost:5036/professores", json = {
             "id": 4,
            "nome": "Murillo", 
            "idade": 20, 
            "materia": "APIs", 
            "observacoes": "Provavelmente não dormiu hoje"
        })
        self.assertEqual(create1.status_code, 200) 
        create2 = requests.post("http://localhost:5036/professores", json = {
             "id": 4, 
             "nome": "Caio", 
             "idade": 25, 
             "materia": "APIs", 
             "observacoes": "Tatuagens maneiras"
        })
        self.assertEqual(create2.status_code, 400)

# --------------------------------------------------------------------#

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
         self.assertEqual(turma.status_code,400)


    def test_turmas_upload_16(self):
         #Vou criar uma turma
         turma = requests.post('http://localhost:5036/turmas', json={"id":378, "descricao": "Introdução ao Calculo IO", "ativo":True,"professor_id":200})
         self.assertEqual(turma.status_code,200) #Vejo se minha turma foi criada
         p_turma = requests.put('http://localhost:5036/turmas/378', json = {"descricao": "Introdução a Calculo II"})
         self.assertEqual(p_turma.status_code,200)


    def test_turmas_upload_id_nao_encontrado_17(self):
        turma = requests.put('http://localhost:5036/turmas/478', json={"ativo": False})
        self.assertEqual(turma.status_code,400)


    def test_turmas_delete_18(self):
        requests.post('http://localhost:5036/turmas', json={"id":369, "descricao": "Engenharia de Requisitos", "professor_id": 210, "ativo": True} )
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
