# Exercícios Tomada de Decisão
'''Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.'''

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3
    
print(f"O maior entre os número {num1}, {num2} e {num3} é o número {maior}")
    
# CASOS DE TESTE

# Número 1 é o maior de todos
# Número 2 é o maior de todos
# Número 3 é o maior de todos