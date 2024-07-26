'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
'''

salHora = float(input("Qual o valor da sua hora? R$"))
horaMes = float(input("Quantas horas você trabalha por mês? "))

salFinal = salHora * horaMes

print(f'''
      Valor da sua hora: R${salHora}
      Horas trabalhadas: {horaMes}hrs
      
      Você tem um salário de R${salFinal} diante dos dados informados!
      ''')