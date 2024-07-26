'''Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''

altura = float(input("Qual a sua altura? "))
peso = float(input("Qual o seu peso? "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Baseado no seu peso {peso} e altura {altura} informados, seu índice IMC é de {imc:.2f}")
    print("Você está na classificação MAGREZA")
elif imc < 24.9:
    print(f"Baseado no seu peso {peso} e altura {altura} informados, seu índice IMC é de {imc:.2f}")
    print("Você está na classificação NORMAL")
elif imc < 29.9:
    print(f"Baseado no seu peso {peso} e altura {altura} informados, seu índice IMC é de {imc:.2f}")
    print("Você está na classificação SOBREPESO")
elif imc < 39.9:
    print(f"Baseado no seu peso {peso} e altura {altura} informados, seu índice IMC é de {imc:.2f}")
    print("Você está na classificação OBESIDADE")
else:
    print(f"Baseado no seu peso {peso} e altura {altura} informados, seu índice IMC é de {imc:.2f}")
    print("Você está na classificação OBESIDADE GRAVE")
