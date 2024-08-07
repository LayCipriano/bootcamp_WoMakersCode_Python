'''Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.'''

contatos = {
    'Amanda' : 8736452729,
    'João' : 8736452729,
    'Sérgio' : 8736452729,
    'Rodolfo' : 8736452729,
    'Bruna' : 8736452729,
    'Joana' : 8736452729
}

busca = input("Digite o nome do contato para buscar: ")
 
if busca in contatos:
    print(f"Contato: {busca}, Telefone: {contatos[busca]}")
else:
    print("Contato não encontrado!")
    
    
# CASOS DE TESTE

# Caso: Inserir um contato existente na lista
# Ação: Retorna o contato adicionado e o número de telefone

# Caso: Inserir um contato não existente na lista
# Ação: Retorna mensagem de contato não encontrado e encerra a execução do programa