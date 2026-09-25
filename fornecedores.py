from rich.console import Console
from rich.table import Table
from requests import get

from banco_dados import conectar


def consultar_fornecedores():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id, cnpj, razao_social, nome_fantasia, cep, numero FROM fornecedores")
            registros = cursor.fetchall()

    tabela = Table(title="Fornecedores")
    tabela.add_column("Código")
    tabela.add_column("CNPJ")
    tabela.add_column("Razão Social")
    tabela.add_column("Nome Fantasia")
    tabela.add_column("CEP")
    tabela.add_column("Número")

    for fornecedor in registros:
        tabela.add_row(
            str(fornecedor[0]),
            str(fornecedor[1]),
            str(fornecedor[2]),
            str(fornecedor[3]),
            str(fornecedor[4]),
            str(fornecedor[5]),
        )

    console = Console()
    console.print(tabela)

# Requisição é uma forma de uma página/mobile/sistema fazer 
# uma consulta para outro sistema
# Tipos de requisições API RESTful
# GET:      Consultar todos/Consultar específico
# POST:     Cadastro
# PUT:      Alterar dados
# DELETE:   APAGAR

# HTTP Status Code: resposta da requisição
# 200       OK  (deu boa)
# 201       CREATED (criado com sucesso)
# 204       NO CONTENT (deu boa, mas o back n trouxe nada de resposta)
# 400       BAD REQUEST 
# 401       UNAUTHORIZED (não está logado)
# 403       FORBIDEN (não tem permissão para acessar o recurso)
# 422       UNPROCESSABLE ENTITY
# 404       NOT FOUND (recurso não encontrado, tipo tentou procurar um clietne com um id que não existe)
# 500       INTERNAL SERVER ERROR (deu 'm' no back-end)
def consultar_fornecedor_por_cnpj(cnpj: str):
    print("Consultando dados do fornecedor...")
    resposta = get("https://api.opencnpj.org/" + cnpj)
    if resposta.status_code != 200:
        print("Não foi possível consultar o CNPJ")
        return None, None, None, None
    else:
        dados = resposta.json()
        razao_social = dados["razao_social"]
        nome_fantasia = dados["nome_fantasia"]
        cep = dados["cep"]
        numero = dados["numero"]
        return razao_social, nome_fantasia, cep, numero


def cadastrar_fornecedor():
    cnpj = input("Digite o CNPJ: ")
    razao_social, nome_fantasia, cep, numero = consultar_fornecedor_por_cnpj(cnpj)
    if razao_social is None:
        return

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
            INSERT INTO fornecedores 
            (cnpj, razao_social, nome_fantasia, cep, numero) 
            VALUES(%s, %s, %s, %s, %s)
            """, (cnpj, razao_social, nome_fantasia, cep, numero))
            conexao.commit()
    print("Fornecedor cadastrado com sucesso")
