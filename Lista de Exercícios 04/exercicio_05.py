'''Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais'''


def contarVogais(frase):
    contador = 0
    vogais = ('a', 'e', 'i', 'o', 'u')
    
    for letra in frase:
        if letra in vogais:
            contador += 1
            
    return contador

frase = input("Digite uma frase, vou contar quantas vogais há: ").lower()
contador = contarVogais(frase)

print(f"SUA FRASE: {frase}")
print(f"Quantidade de vogais: {contador}")