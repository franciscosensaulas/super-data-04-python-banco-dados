# Super Data 04 — Python + Banco de Dados

Projeto de aula: um sistema de loja em Python que conversa com um banco de dados **MySQL**. O objetivo é praticar o **CRUD** (Create, Read, Update, Delete) saindo do SQL puro e chegando no código Python.

---

## 📚 Documentação

| Documento | Sobre o que é |
|---|---|
| [Guia: pip e instalação de bibliotecas](docs/GUIA_PIP.md) | Como instalar bibliotecas, travar versões, usar o `requirements.txt` e resolver os erros mais comuns |

---

## Estrutura do projeto

```
.
├── main.py             # menu principal da aplicação
├── banco_dados.py      # conexão com o MySQL
├── produtos.py         # CRUD de produtos
├── clientes.py         # CRUD de clientes
├── fornecedores.py     # CRUD de fornecedores
├── estrutura.sql       # scripts SQL: criação do banco, tabelas e exemplos
├── requirements.txt    # dependências do projeto
└── docs/               # material de apoio da aula
```

---

## Como rodar

### 1. Preparar o banco de dados

Com o MySQL rodando, execute os comandos do arquivo `estrutura.sql` para criar o banco `loja_db` e as tabelas `produtos`, `clientes` e `fornecedores`.

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

> Não entendeu o que esse comando faz? Está tudo explicado no [guia de pip](docs/GUIA_PIP.md).

### 3. Conferir os dados de conexão

Abra o `banco_dados.py` e ajuste `host`, `port`, `user`, `password` e `database` para os do seu MySQL.

### 4. Executar

```bash
python main.py
```

---

## O menu

```
1   - Consultar produtos
2   - Cadastrar produto
3   - Apagar produto
4   - Editar produto
5   - Consultar clientes
6   - Cadastrar cliente
7   - Apagar cliente
8   - Editar cliente
99  - Sair
```

---

## Conteúdos praticados

- Conexão com MySQL a partir do Python (`mysql.connector`)
- `SELECT`, `INSERT`, `UPDATE` e `DELETE` — o ciclo CRUD
- Uso de `cursor` e context manager (`with`)
- Organização do código em módulos (um arquivo por entidade)
- Saída formatada no terminal com a biblioteca `rich`
- Gerenciamento de dependências com `pip` e `requirements.txt`
