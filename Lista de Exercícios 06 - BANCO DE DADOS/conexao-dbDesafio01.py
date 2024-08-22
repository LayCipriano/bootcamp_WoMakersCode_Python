import sqlite3

conn = sqlite3.connect('./banco-dados/banco')
cursor = conn.cursor()

'''1. Crie uma tabela chamada "alunos" com os seguintes campos: id
(inteiro), nome (texto), idade (inteiro) e curso (texto).'''

# cursor.execute('DROP TABLE alunos')
cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INT, nome VARCHAR, idade INT, curso VARCHAR)')

'''2. Insira pelo menos 5 registros de alunos na tabela que você criou no
exercício anterior.'''

cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Laysa Cipriano", 26, "Sistemas para Internet")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Ruan Santos", 22, "Engenharia de Software")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Izabella Silvano", 29, "Sistemas para Internet")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Laysa Cipriano", 26, "Análise e Desenvolvimento de Sistemas")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (05, "Regina Mardoso", 19, "Sistemas para Internet")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (6, "Cléber Santoso", 18, "Engenharia de Software")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (7, "Ana Sousa", 18, "Tecnologia da Informação")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (8, "Betina Santoso", 32, "Governança em TI")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (9, "Ruan Santos", 22, "Análise e Desenvolvimento de Sistemas")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (10, "Izabella Silvano", 29, "Design de UI/UX")')

'''Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".'''

show = cursor.execute('SELECT * FROM alunos')
for aluno in show:
    print(aluno)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
idadeMaiorVinte = cursor.execute('SELECT * FROM alunos WHERE idade > 20')
for aluno in idadeMaiorVinte:
    print(aluno)



# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
cursoEngenhariaOrdemAlfabetica = cursor.execute('SELECT * FROM alunos WHERE curso LIKE "%Engenharia%" ORDER BY nome ASC')
for aluno in cursoEngenhariaOrdemAlfabetica:
    print(aluno)


# d) Contar o número total de alunos na tabela
contarAlunos = cursor.execute('SELECT * FROM alunos')
contador = 0
for alunos in contarAlunos:
    contador += 1
print(f'Quantidade de alunos cadastrados: {contador}')

'''4. Atualização e Remoção
a) Atualize a idade de um aluno específico na tabela.'''

cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (11, "Regina Mardoso", 19, "Sistemas para Internet")')
cursor.execute('UPDATE alunos SET idade=30 where id=11')


# b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id=11')

conn.commit()
conn.close()