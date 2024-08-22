import sqlite3

conexao = sqlite3.connect('./banco-dados/banco')
cursor = conexao.cursor()

# criação da tabela usuarios
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(ID INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR (100));')

# renomeei o nome da tabela para usuário (singular)
cursor.execute('ALTER TABLE usuarios RENAME TO usuario')

# adicionei uma nova coluna na tabela
cursor.execute('ALTER TABLE usuario ADD COLUMN telefone VARCHAR(12)')

# adicionando um usuário na tabela
cursor.execute('INSERT INTO usuario(ID, nome, endereco, email, telefone) VALUES (5, "Lay", "Brasil", "lay@cipriano.com", "12345678");')

show = cursor.execute('SELECT * FROM usuario')

for user in show:
    print(user)

# exclusao da tabela que criei de teste
# cursor.execute('DROP TABLE outra')


conexao.commit()
conexao.close