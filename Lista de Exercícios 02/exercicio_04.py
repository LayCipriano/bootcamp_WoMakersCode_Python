# Exercícios Tomada de Decisão
'''Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.'''
    
while True:
    try:
        notaAluno = float(input("Informe a nota atingida: "))
        
        if notaAluno >= 0 and notaAluno < 10:
            if notaAluno >= 7:
                print("Aluno Aprovado!")
            else:
                print("Aluno Reprovado!")    
            break
        else:
            print("Nota inválida. Por favor, insira um valor entre 0 e 10!")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número!")