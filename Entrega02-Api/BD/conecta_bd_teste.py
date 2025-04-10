import pyodbc

# Dados da conexão
server = 'DESKTOP-2L7LLFG'  # Ex: 'localhost' ou 'DESKTOP-ABC123\\SQLEXPRESS'
database = 'AP2'
# String de conexão usando autenticação do Windows
conn_string = f'''
    DRIVER={{ODBC Driver 17 for SQL Server}};
    SERVER={server};
    DATABASE={database};
    Trusted_Connection=yes;
'''

try:
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    print("Conexão bem-sucedida!")

    # Exemplo de consulta
    cursor.execute("SELECT * FROM CLIENTE")  # Substitua pela sua tabela
    for row in cursor.fetchall():
        print(row)

    conn.close()

except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)