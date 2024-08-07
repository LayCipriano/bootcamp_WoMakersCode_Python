'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.'''

carrinhoCompras = {}

while True:
    produto = input("Informe um produto (ou digite 'sair' para encerrar): ")
    
    if produto.upper() == 'SAIR':
        break
    
    try:
        quantidade = int(input(f"Qual a quantidade de {produto}? "))
        
        if quantidade > 0:
            carrinhoCompras[produto] = quantidade
        else:
            print("Informe uma quantidade maior que 0!")
            
    except ValueError:
        print("Insira uma quantidade válida.")
        
totalCarrinho = sum(carrinhoCompras.values())
print(f"Carrinho de compras finalizado: {totalCarrinho} itens")


# CASOS DE TESTE

# Caso: Inserir um produto e após, inserir uma quantidade negativa
# Ação: Irá informar ao usuário que a quantidade deve ser > 0. Solicitará nova inserção de produto.

# Caso: Inserir um valor string no input de quantidade.
# Ação: Irá informar ao usuário que deve inserir uma quantidade válida. Solicitará nova inserção de produto.

# Caso: Inserir "sair" em suas diversas variações de escrita.
# Ação: Encerrar a inserção de itens no carrinho. Apresentar somatório dos itens adicionados.