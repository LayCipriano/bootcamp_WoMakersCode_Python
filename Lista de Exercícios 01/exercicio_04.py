'''Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.'''

distPercorrida = float(input("Informe a distância percorrida (em Km): "))
combConsumido = float(input("Informe a quantidade de combustível consumido (em Litros): "))
consumoMedio = distPercorrida / combConsumido

print(f"O consumo médio de combustível, baseado nos dados informados foi de {consumoMedio:.2f}km/l")