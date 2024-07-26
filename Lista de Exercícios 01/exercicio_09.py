'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.'''

horasTreinoSemanal = float(input("Quantas horas você treinou por semana? "))
calMinuto = 5

calQueimadasMes = (horasTreinoSemanal * 60 * 4) * calMinuto

print(f"Com um treino de {horasTreinoSemanal}hrs/semana, você queimou uma média de {calQueimadasMes:.2f} em um mês.")