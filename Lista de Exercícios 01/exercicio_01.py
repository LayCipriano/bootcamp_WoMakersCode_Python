'''Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão'''

n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))


# Soma +
soma = n1 + n2
print(f"SOMA: {n1} + {n2} = {soma}")


# Subtração -
sub = n1 - n2
print(f"SUBTRAÇÃO: {n1} - {n2} = {sub}")


# Multiplicação *
mult = n1 * n2
print(f"MULTIPLICAÇÃO: {n1} * {n2} = {mult}")


# Divisão /
div = n1 / n2
print(f"DIVISÃO: {n1} / {n2} = {div}")


# Divisão Inteira //
# não retorna casa decimal após a vírgula
# não arredonda valores
divInt = n1 // n2
print(f"DIVISÃO INTEIRA: {n1} / {n2} = {divInt}")