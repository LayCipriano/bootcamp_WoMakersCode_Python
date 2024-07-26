'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

aviao = 600
carro = 100
onibus = 80

percurso = float(input("Informe a distância a ser viajada (em Km): "))

tempoViagemAviao = percurso / aviao
tempoViagemCarro = percurso / carro
tempoViagemOnibus = percurso / onibus

print(f'''
      O tempo de viagem para o percurso informado será de:
      
      AVIÃO: O tempo de viagem será de {tempoViagemAviao:.2f}hrs.
      CARRO: O tempo de viagem será de {tempoViagemCarro}hrs.
      ÔNIBUS: O tempo de viagem será de {tempoViagemOnibus}hrs.
      ''')



