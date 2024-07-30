# Exercícios Tomada de Decisão
'''Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.'''

while True:
    try:
        idade = int(input("Informe sua idade, por favor: "))
        if idade >= 0:
            if idade >= 0 and idade <= 12:
                print("Você é uma criança!")
            elif idade >= 13 and idade <= 17:
                print("Você é um adolescente!")
            elif idade >= 18 and idade <= 64:
                print("Você é um adulto!")
            else:
                print("Você é um idoso!")
        else:
            print("Sua idade deve ser maior que 0!")
    except ValueError:
        print("Informe um valor numérico!")
        
        
# CASOS DE TESTE #

# Inserir idade entre 0 e 12
# Retorno: mensagem informando que é criança

# Inserir idade entre 13 e 17
# Retorno: mensagem informando que é adolescente

# Inserir idade entre 18 e 64
# Retorno: mensagem informando que é adulto

# Inserir idade maior igual a 65
# Retorno: mensagem informando que é idoso

# Inserir valor menor que 0
# Retorno: mensagem informando que deve ser maior igual que 0

# Inserir uma letra
# Retorno: mensagem solicitando um valor numérico