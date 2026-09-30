import questionary

import clientes
import fornecedores
import pedidos
import produtos


def limpar_terminal():
    import os
    os.system("cls")

menus_acoes = {
    "Clientes": clientes.menu,
    "Fornecedores": fornecedores.menu,
    "Produtos": produtos.menu,
    "Pedidos": pedidos.menu
}


if __name__ == "__main__":
    menus = ["Clientes", "Fornecedores", "Pedidos", "Produtos", "Sair"]
    opcao_desejada = ""
    while opcao_desejada != "Sair":
        opcao_desejada = questionary.select("Escolhe um menu", choices=menus).ask()
        if opcao_desejada == "Sair":
            continue
        if opcao_desejada not in menus_acoes:
            print("Opção escolhida não implementada")
        else:
            menus_acoes[opcao_desejada]()