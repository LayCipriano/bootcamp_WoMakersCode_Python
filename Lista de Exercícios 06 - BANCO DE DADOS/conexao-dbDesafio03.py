import sqlite3

conn = sqlite3.connect('./banco-dados/banco')
cursor = conn.cursor()

'''8. Junção de Tabelas
Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real). 
'''

# cursor.execute('DROP TABLE compras')
cursor.execute('CREATE TABLE IF NOT EXISTS compras(id INTEGER PRIMARY KEY, cliente_id INT, produto VARCHAR, valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')


'''Insira algumas compras associadas a clientes existentes na tabela "clientes".'''

cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (1, "Fones de Ouvido", 259.80)')
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (6, "Teclado Mecânico", 399.99)')
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (3, "Monitor 24 polegadas", 849.90)')
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (9, "Mouse Gamer", 199.50)')
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (7, "Cadeira Ergonômica", 1150.00)')
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (5, "Smartphone", 2349.00)')


'''Escreva uma consulta para exibir o nome do cliente, o produto e o
valor de cada compra.'''

cursor.execute('''
               SELECT
                    clientes.nome
                    ,compras.produto
                    ,compras.valor
                FROM compras
                INNER JOIN clientes ON clientes.id = compras.cliente_id
               ''')

comprasIdentificadas = cursor.fetchall()
for compra in comprasIdentificadas:
    print(compra)

conn.commit()
conn.close()