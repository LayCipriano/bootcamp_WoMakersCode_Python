'''Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.'''

medias = []

for alunos in range(5):
    somaNotas = 0
    
    for item in range(4):
        while True:
            try: # validação da inserção de apenas números
                notas = float(input(f"Digite a nota {item+1} do aluno {alunos+1}: ")) 
                if 0 <= notas <= 10: # validação de notas dentro do intervalo de 0.0 e 10.0
                    somaNotas += notas
                    break
                else:
                    print("A nota deve estar entre 0 e 10.0! Tente novamente.")    
            except ValueError:
                print("Erro: Digite um número válido!")

        media = somaNotas / 4
        medias.append(media)


alunoAprovado = 0
for media in medias:
    if media >= 7.0:
        alunoAprovado += 1

print(f"Número de alunos com média maior igual a 7.0: {alunoAprovado}")

# CASOS DE TESTE

# Caso: Inserir um valor string
# Ação: Mensagem informando número inválido é disparada. Nova inserção é solicitada.

# Caso: Inserir um número negativo
# Ação: Mensagem informando range aceito é disparada. Nova inserção é solicitada.