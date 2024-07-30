# Exercícios Tomada de Decisão
'''Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas'''

left = float(input("Informe as medidas do lado esquerdo do triângulo: "))
right = float(input("Informe as medidas do lado esquerdo do triângulo: "))
bottom = float(input("Informe as medidas da base do triângulo: "))

if left == right == bottom:
    print("Triângulo Equilátero: todos os lados com o mesmo valor")
elif left == right or left == bottom or right == bottom:
    print("Triângulo Isósceles: dois lados com o mesmo valor")
else:
    print("Triângulo Escaleno: todos os lados com medidas distintas")
    

# CASOS DE TESTE

# Inserir 3 valores iguais
# Resultado: triângulo equilátero

# Inserir 2 valores iguais
# Resultado: triângulo isósceles

# Inserir 3 valores distintos
# Resultado: triângulo escaleno