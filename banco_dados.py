from mysql.connector import connect


def conectar():
    conexao = connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin",
        database="loja_db"
    )
    print("Conexão aberta com sucesso")
    return conexao
