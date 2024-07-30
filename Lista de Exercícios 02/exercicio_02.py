# Exercícios Tomada de Decisão
'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso'''

turno = input('''Em que turno você estuda?
Digite a letra correspondente: M (Matutino) | V (Vespertino) | N (Noturno): ''').upper()

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor inválido!")
    
    
# CASOS DE TESTE

# Inserir letra M maiúscula
# Inserir letra m minúscula

# Inserir letra V maiúscula
# Inserir letra v minúscula

# Inserir letra N maiúscula
# Inserir letra n minúscula

# Inserir qualquer outra letra : laço else
