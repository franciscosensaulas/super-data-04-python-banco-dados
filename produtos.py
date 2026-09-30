
import questionary
from rich.console import Console
from rich.table import Table

from banco_dados import conectar
from fornecedores import consultar_fornecedores


# função privada n deveria ser chamada fora deste script
def carregar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""SELECT
    produtos.id,
    produtos.nome,
    produtos.descricao,
    fornecedores.id,
    fornecedores.razao_social
FROM produtos
LEFT JOIN fornecedores ON (produtos.id_fornecedor = fornecedores.id);""")
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()
    return registros


def consultar_produtos():
    registros = carregar_produtos()

    tabela = Table(title="Produtos")
    tabela.add_column("Código")
    tabela.add_column("Fornecedor")
    tabela.add_column("Nome")
    tabela.add_column("Descrição")
    for produto in registros:
        tabela.add_row(
            str(produto[0]),
            produto[4],
            produto[1],
            produto[2]
        )
    console = Console()
    console.print(tabela)


def cadastrar_produto():
    consultar_fornecedores()

    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição: ")
    id_fornecedor = int(input("Digite o código do fornecedor: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, descricao, id_fornecedor) VALUES (%s, %s, %s)",
        (nome, descricao, str(id_fornecedor))
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
    consultar_fornecedores()
    id_produto = (int(input("Digite o id do produto para editar: ")))
    novo_nome = input("Digite o nome do produto: ")
    nova_descricao = input("Digite a descrição: ")
    id_fornecedor = int(input("Digite o código do fornecedor: "))


    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE produtos SET nome = %s, descricao = %s, id_fornecedor = %s WHERE id = %s",
        (novo_nome, nova_descricao, id_fornecedor, id_produto)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto alterado com sucesso")


def menu():
    menus = ["Consultar", "Cadastrar", "Editar", "Apagar", "Voltar"]
    opcao_desejada = ""
    while opcao_desejada != "Voltar":
        opcao_desejada = questionary.select("Escolhe um menu", choices=menus).ask()
        if opcao_desejada == "Consultar":
            consultar_produtos()
        elif opcao_desejada == "Cadastrar":
            cadastrar_produto()
        elif opcao_desejada == "Editar":
            editar_produto()
        elif opcao_desejada == "Apagar":
            apagar_produto()
        