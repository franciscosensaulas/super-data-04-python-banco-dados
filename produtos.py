
from banco_dados import conectar


def consultar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, descricao FROM produtos")
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()

    print("Produtos:")
    for produto in registros:
        # print("Id:", produto[0], "\nNome:", produto[1], "\nDescrição:", produto[2], "\n\n")
        print(produto[0], "=>", produto[1], "=>", produto[2])


def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, descricao) VALUES (%s, %s)",
        (nome, descricao)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto cadastrado com sucesso")

def apagar_produto():
    id_produto = int(input("Digite o id do produto para apagar: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto apagado com sucesso")


def editar_produto():
    id_produto = (int(input("Digite o id do produto para editar: ")))
    novo_nome = input("Digite o nome do produto: ")
    nova_descricao = input("Digite a descrição: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE produtos SET nome = %s, descricao = %s WHERE id = %s",
        (novo_nome, nova_descricao, id_produto)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto alterado com sucesso")
