'''Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos.'''

def soma(num1 , num2, num3):
    return num1 + num2 + num3

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))

somar = soma(numero1, numero2, numero3)

print(f"A soma entre os valores informados {numero1}  + {numero2} + {numero3} = {somar}")