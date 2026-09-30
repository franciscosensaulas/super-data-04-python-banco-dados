import questionary
from rich.console import Console
from rich.table import Table

from banco_dados import conectar
from produtos import carregar_produtos


def listar_pedidos():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id, total, data_pedido, status FROM pedidos")
            registros = cursor.fetchall()

    if len(registros) == 0:
        print("Nenhum pedido cadastrado")
        return

    tabela = Table(title="Lista de Pedidos")
    tabela.add_column("Código")
    tabela.add_column("Data do Pedido")
    tabela.add_column("Total")
    tabela.add_column("Status")

    for pedido in registros:
        tabela.add_row(
            str(pedido[0]),
            str(pedido[2]),
            str(pedido[1]),
            pedido[3]
        )

    console = Console()
    console.print(tabela)


def criar_pedido():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("INSERT INTO pedidos (total, status) VALUES (0, 'ABERTO')")
            conexao.commit()
            id_pedido = cursor.lastrowid
            return id_pedido


def consultar_pedidos_abertos():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id, total, data_pedido, status FROM pedidos WHERE status = 'ABERTO'")
            pedido = cursor.fetchone()
            return pedido


def obter_id_pedido_aberto():
    pedido = consultar_pedidos_abertos()
    if pedido is None:
        id_pedido_gerado = criar_pedido()
        return id_pedido_gerado
        # print("Criado pedido", id_pedido_gerado)
    else:
        # print("Pedido já existia ", pedido[0])
        return pedido[0]

def escolher_produto():
    produtos = carregar_produtos()

    # list comprehension python
    produtos_opcoes = [questionary.Choice(title=produto[1], value=produto[0]) for produto in produtos]

    # produtos_opcoes = []
    # for produto in produtos:
    #     produtos_opcoes.append(
    #         questionary.Choice(title=produto[1], value=produto[2])
    #     )

    id_produto = questionary.select("Escolha o produto", choices=produtos_opcoes).ask()
    return id_produto


def adicionar_produto_pedido():
    id_pedido = obter_id_pedido_aberto()
    id_produto = escolher_produto()
    quantidade = int(input("Digite a quantidade deseja: "))
    preco = float(input("Digite o preço deseja: "))
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "INSERT INTO itens_pedidos (id_produto, id_pedido, valor, quantidade) VALUES (%s, %s, %s, %s);",
                (id_produto, id_pedido, preco, quantidade)
            )
            conexao.commit()
            print("Produto adicionado ao pedido")


def fechar_pedido():
    id_pedido = obter_id_pedido_aberto()
    
    print("Calculando total pedido")
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT valor, quantidade FROM itens_pedidos WHERE id_pedido = %s", (id_pedido,))
            registros = cursor.fetchall()
    total_pedido = 0
    for item_pedido in registros:
        valor, quantidade = item_pedido
        total = valor * quantidade
        total_pedido += total
    print("Total do pedido é:", total_pedido)

    # Atualizar o pedido com o total e definir o status como CONCLUIDO
    with conectar() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "UPDATE pedidos SET total = %s, status = %s WHERE id = %s",
                    (total_pedido, "CONCLUIDO", id_pedido)
                )
                conexao.commit()
    print("Pedido concluído com sucesso")


def cancelar_pedido():
    id_pedido = obter_id_pedido_aberto()
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("UPDATE pedidos SET status = 'CANCELADO' WHERE id = %s", (id_pedido,))
            conexao.commit()

    print("Pedido cancelado com sucesso")


def consultar_pedido():
    id_pedido = obter_id_pedido_aberto()
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
            SELECT
                itens_pedidos.valor,
                itens_pedidos.quantidade,
                produtos.nome
            FROM itens_pedidos
            INNER JOIN produtos ON (itens_pedidos.id_produto = produtos.id)
            WHERE itens_pedidos.id_pedido = %s;""", (id_pedido,))
            registros = cursor.fetchall()
    tabela = Table(title="Itens do pedido")
    tabela.add_column("Produto")
    tabela.add_column("Quantidade")
    tabela.add_column("Preço")
    tabela.add_column("Total")

    for item_pedido in registros:
        valor, quantidade, produto = item_pedido
        tabela.add_row(
            produto,
            str(quantidade),
            str(valor),
            str(quantidade * valor),
        )

    console = Console()
    console.print(tabela)


def menu():
    menus = ["Listar pedidos", "Comprar produto", "Consultar", "Fechar", "Cancelar", "Voltar"]
    opcao_desejada = ""
    while opcao_desejada != "Voltar":
        opcao_desejada = questionary.select("Submenu de Pedidos", choices=menus).ask()
        if opcao_desejada == "Listar pedidos":
            listar_pedidos()
        elif opcao_desejada == "Comprar produto":
            adicionar_produto_pedido()
        elif opcao_desejada == "Consultar":
            consultar_pedido()
        elif opcao_desejada == "Fechar":
            fechar_pedido()
        elif opcao_desejada == "Cancelar":
            cancelar_pedido()
        
        