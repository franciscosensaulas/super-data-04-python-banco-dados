
CREATE DATABASE loja_db;

-- Apagar o banco de dados
-- DROP DATABASE loja_db;

USE loja_db;

CREATE TABLE produtos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(200),
    nome VARCHAR(50) NOT NULL
);
-- Apagar a tabela de produtos
-- DROP TABLE produtos;

SELECT id, nome, descricao FROM produtos;

INSERT INTO produtos (nome, descricao) VALUE 
("Samsung Neo QLED 4k 65", "TV mais linda do mundo");

INSERT INTO produtos (nome, descricao) VALUES
("Positivo Dual Core 2Gb", "Computador Melhor que tem"),
("Garmin Instict", NULL),
("Garmin Instict", "");

SELECT id, nome, descricao FROM produtos;

SELECT id, nome, descricao FROM produtos WHERE id = 4;

DELETE FROM produtos WHERE id = 4;

INSERT INTO produtos (nome, descricao) VALUE 
("Sony Ericson w 200i", "Celular Infravermelho");

SELECT id, nome, descricao FROM produtos;

-- Consultar os produtos que tem NULL na descricao
SELECT id, nome, descricao 
    FROM produtos 
    WHERE descricao IS NULL;

UPDATE produtos 
    SET descricao = "GPS, laranja" 
    WHERE id = 3;

-- CRUD (registros na tabela)
-- Create   INSERT
-- Read     SELECT
-- Update   UPDATE
-- Delete   DELETE

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cnpj VARCHAR(18) NOT NULL UNIQUE,
    endereco VARCHAR(255),
    telefone VARCHAR(15),
    email VARCHAR(150),
    limite_credito DECIMAL(15,2) DEFAULT 0.00
);

USE loja_db;

CREATE TABLE fornecedores(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cnpj VARCHAR(18) NOT NULL,
    razao_social VARCHAR(100) NOT NULL,
    nome_fantasia VARCHAR(100) NOT NULL,
    cep VARCHAR(10) NOT NULL,
    numero VARCHAR(10)
);

INSERT INTO fornecedores (
    cnpj,
    razao_social,
    nome_fantasia,
    cep,
    numero
) VALUES (
    '12.345.678/0001-90',
    'Empresa Exemplo Ltda',
    'Empresa Exemplo',
    '88000-000',
    '123'
);

ALTER TABLE produtos 
ADD COLUMN id_fornecedor INT,
ADD CONSTRAINT produtos_fornecedor_fk
FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id);
