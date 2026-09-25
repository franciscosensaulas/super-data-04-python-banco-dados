
from banco_dados import conectar


def cadastrar_cliente():

    nome = input("Digite o nome do cliente: ")

    cnpj = input("Digite o CNPJ: ")
    cnpj = formatar_cnpj(cnpj)

    endereco = input("Digite o endereço: ")

    telefone = input("Digite o telefone: ")
    telefone = formatar_telefone(telefone)

    email = input("Digite o e-mail: ")

    limite_credito = float(input("Digite o limite de crédito: "))

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO clientes
        (nome, cnpj, endereco, telefone, email, limite_credito)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        nome,
        cnpj,
        endereco,
        telefone,
        email,
        limite_credito
    )

    cursor.execute(sql, valores)
    conexao.commit()
    print("Cliente cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def formatar_cnpj(cnpj):

    cnpj = cnpj.replace(".", "")
    cnpj = cnpj.replace("/", "")
    cnpj = cnpj.replace("-", "")
    cnpj = cnpj.replace(" ", "")

    if len(cnpj) != 14:
        print("CNPJ inválido!")
        return None

    cnpj_formatado = (
        cnpj[:2] + "." +
        cnpj[2:5] + "." +
        cnpj[5:8] + "/" +
        cnpj[8:12] + "-" +
        cnpj[12:14]
    )

    return cnpj_formatado


def formatar_telefone(telefone):

    telefone = telefone.replace(" ", "")
    telefone = telefone.replace("(", "")
    telefone = telefone.replace(")", "")
    telefone = telefone.replace("-", "")

    if len(telefone) != 11:
        print("Telefone inválido!")
        return None

    telefone_formatado = (
        "(" + telefone[:2] + ") " +
        telefone[2:7] + "-" +
        telefone[7:11]
    )

    return telefone_formatado


def consultar_clientes():

    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
        SELECT
            id,
            nome,
            cnpj,
            endereco,
            telefone,
            email,
            limite_credito
        FROM clientes
    """

    cursor.execute(sql)

    clientes = cursor.fetchall()

    print("\n========== CLIENTES ==========")

    for cliente in clientes:

        print("ID:", cliente[0])
        print("Nome:", cliente[1])
        print("CNPJ:", cliente[2])
        print("Endereço:", cliente[3])
        print("Telefone:", cliente[4])
        print("E-mail:", cliente[5])
        print("Limite de crédito:", cliente[6])
        print("-----------------------------")

    cursor.close()

    conexao.close()


def editar_cliente():

    id_cliente = int(input("Digite o ID do cliente que deseja editar: "))

    nome = input("Digite o novo nome: ")

    cnpj = input("Digite o novo CNPJ: ")

    endereco = input("Digite o novo endereço: ")

    telefone = input("Digite o novo telefone: ")

    email = input("Digite o novo e-mail: ")

    limite_credito = float(
        input("Digite o novo limite de crédito: ")
    )

    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
        UPDATE clientes
        SET
            nome = %s,
            cnpj = %s,
            endereco = %s,
            telefone = %s,
            email = %s,
            limite_credito = %s
        WHERE id = %s
    """

    valores = (
        nome,
        cnpj,
        endereco,
        telefone,
        email,
        limite_credito,
        id_cliente
    )

    cursor.execute(sql, valores)

    conexao.commit()

    if cursor.rowcount > 0:

        print("Cliente atualizado com sucesso!")

    else:

        print("Cliente não encontrado.")

    cursor.close()

    conexao.close()


def apagar_cliente():

    id_cliente = int(
        input("Digite o ID do cliente que deseja apagar: ")
    )

    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
        DELETE FROM clientes
        WHERE id = %s
    """

    cursor.execute(sql, (id_cliente,))

    conexao.commit()

    if cursor.rowcount > 0:

        print("Cliente apagado com sucesso!")

    else:

        print("Cliente não encontrado.")

    cursor.close()

    conexao.close()