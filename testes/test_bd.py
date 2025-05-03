import unittest
from config import app, db  # Importe o app e db do seu config
from sqlalchemy import text
from sqlalchemy.exc import OperationalError, SQLAlchemyError

class TestDatabaseConnection(unittest.TestCase):
    def test_db_connection(self):
        """Testa se a conexão com o banco de dados está funcionando"""
        with app.app_context():  # Usa o contexto do app do seu config
            connection = None
            try:
                # Teste 1: Verifica se a engine está acessível
                self.assertIsNotNone(db.engine, "A engine do banco de dados não foi criada")
                
                # Teste 2: Estabelece conexão
                connection = db.engine.connect()
                self.assertFalse(connection.closed, "A conexão deveria estar aberta")
                
                # Teste 3: Executa uma query simples
                result = connection.execute(text("SELECT 1"))
                self.assertEqual(result.scalar(), 1, "A query de teste deveria retornar 1")
                
                # Teste 4: Verifica se pode listar tabelas (opcional)
                inspector = db.inspect(db.engine)
                tables = inspector.get_table_names()
                self.assertIsInstance(tables, list, "Deveria retornar lista de tabelas")
                
                print(" Conexão com o banco de dados estabelecida com sucesso!")
                
            except OperationalError as e:
                self.fail(f" Falha na conexão com o banco de dados: {str(e)}")
            except SQLAlchemyError as e:
                self.fail(f" Erro no SQLAlchemy: {str(e)}")
            except Exception as e:
                self.fail(f" Erro inesperado: {str(e)}")
            finally:
                if connection:
                    connection.close()
                    self.assertTrue(connection.closed, "A conexão deveria estar fechada")

if __name__ == '__main__':
    unittest.main()