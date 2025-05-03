import unittest
from config import app, db 
from sqlalchemy import text
from sqlalchemy.exc import OperationalError, SQLAlchemyError

class TestDatabaseConnection(unittest.TestCase):
    def test_db_connection(self):
        with app.app_context(): 
            connection = None
            try:

                self.assertIsNotNone(db.engine, "A engine do banco de dados não foi criada")


                connection = db.engine.connect()
                self.assertFalse(connection.closed, "A conexão deveria estar aberta")
                

                result = connection.execute(text("SELECT 1"))
                self.assertEqual(result.scalar(), 1, "A query de teste deveria retornar 1")
                

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