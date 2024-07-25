'''Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros'''

qntKm = float(input("Informe a quilometragem: "))

kmMetro = qntKm * 1000
kmCentimetro = kmMetro * 100
kmMilimetro = kmCentimetro * 10

print(f"O valor de {qntKm}Km equivale a:")
print(f"uma distância de {kmMetro:,}m (metros)")
print(f"uma distância de {kmCentimetro:,}cm (centímetros)")
print(f"uma distância de {kmMilimetro:,}mm (milímetros)")