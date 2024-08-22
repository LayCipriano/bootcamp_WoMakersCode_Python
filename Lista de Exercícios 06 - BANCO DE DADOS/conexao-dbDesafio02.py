import sqlite3

conn = sqlite3.connect('./banco-dados/banco')
cursor = conn.cursor()


'''5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
registros de clientes na tabela.'''

cursor.execute('CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY, nome VARCHAR, idade INT, saldo FLOAT)')

cursor.execute("INSERT INTO clientes (nome, idade, saldo) VALUES ('Ana Silva', 28, 1500.75)")
cursor.execute("INSERT INTO clientes (nome, idade, saldo) VALUES ('Bruno Santos', 35, 2300.00)")
cursor.execute("INSERT INTO clientes (nome, idade, saldo) VALUES ('Carlos Oliveira', 42, 1200.50)")
cursor.execute("INSERT INTO clientes (nome, idade, saldo) VALUES ('Daniela Costa', 25, 3300.00)")
cursor.execute("INSERT INTO clientes (nome, idade, saldo) VALUES ('Eduardo Pereira', 31, 1000.25)")
cursor.execute("INSERT INTO clientes (nome, idade, saldo) VALUES ('Fernanda Lima', 27, 5400.40)")
cursor.execute("INSERT INTO clientes (nome, idade, saldo) VALUES ('Gabriel Mendes', 38, 2750.60)")
cursor.execute("INSERT INTO clientes (nome, idade, saldo) VALUES ('Helena Alves', 29, 3200.80)")
cursor.execute("INSERT INTO clientes (nome, idade, saldo) VALUES ('Igor Nascimento', 34, 150.20)")
cursor.execute("INSERT INTO clientes (nome, idade, saldo) VALUES ('Juliana Ramos', 22, 4000.00)")



'''6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superior a
30 anos.'''

maisTrinta = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for cliente in maisTrinta :
    print(cliente)




# b) Calcule o saldo médio dos clientes.
countSaldo = cursor.execute('SELECT SUM(saldo) FROM clientes')
somaSaldo = cursor.fetchone()[0]

countClientes = cursor.execute('SELECT COUNT(*) FROM clientes') 
somaClientes = cursor.fetchone()[0]

media = somaSaldo/somaClientes

print(f'Saldo total dos clientes: R${somaSaldo:.2f}')
print(f'Saldo médio dos clientes: R${media:.2f}')




# c) Encontre o cliente com o saldo máximo.
cursor.execute('SELECT min(saldo) FROM clientes')
exibirMaximo = cursor.fetchone()[0]

cursor.execute('SELECT * FROM clientes WHERE saldo == ?', (exibirMaximo,)) #, ao final para indicar que desejo esses dados em uma tupla, para correta exibição dos valores...
exibirCliente = cursor.fetchone()

print(exibirCliente)




# d) Conte quantos clientes têm saldo acima de 1000.
saldoMaiorQueMil = cursor.execute('SELECT * FROM clientes WHERE saldo > 1000')
for cliente in saldoMaiorQueMil:
    print(cliente)



'''7. Atualização e Remoção com Condições
a) Atualize o saldo de um cliente específico.'''
cursor.execute('UPDATE clientes SET saldo = 12000 where id = 9')
clienteIgor = cursor.execute('SELECT * FROM clientes WHERE id = 9')
for cliente in clienteIgor:
    print(cliente)


# b) Remova um cliente pelo seu ID
cursor.execute('DELETE FROM clientes WHERE id = 2')

clientes = cursor.execute('SELECT * FROM clientes')
for item in clientes:
    print(item)

conn.commit()
conn.close()