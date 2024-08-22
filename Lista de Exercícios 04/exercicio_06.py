# Exercícios Tomada de Decisão
'''Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício'''

from random import choice

listaPalavras = ['Tecnologia', 'Programação', 'FrontEnd', 'BackEnd'] # lista e sorteio de uma palavra
sorteio = choice(listaPalavras).upper() # sorteio da palavra de acordo com a lista acima, em letras maiúsculas

palavraSorteada =  ["_" for _ in sorteio] # palavra com espaços em branco
tentativas = 6  # quantidade de tentativas
letrasIncorretas = [] # lista para armazenar as letras incorretas


print("Bem Vindo(a) ao Jogo da Forca!")
print(" ".join(palavraSorteada)) # exibe a palavra com espacinhos em branco


while tentativas > 0 and "_" in palavraSorteada:

    # verifica se a letra está ou não presente na palavra
    chute = input("Faça o chute de uma letra: ").upper()


    if chute in letrasIncorretas or chute in palavraSorteada:
        print(f"Você já tentou a letra {chute}!")
        continue
    
    if chute in sorteio:
        for i, letra in enumerate(sorteio):    
            if letra == chute:
                palavraSorteada[i] = chute
        print(f"A letra {chute} está presente na palavra!")
        
    else:
        letrasIncorretas.append(chute) # vai adicionar a letra incorreta na lista
        tentativas -= 1 # vai reduzir -1 das tentativas  
        print(f"Desculpe, essa letra não está presente na palavra!")
        print(f" Você ainda tem {tentativas} restantes...")
        
    print(" ".join(palavraSorteada)) # exibe a palavra atualizada
    print(f" Letras erradas: {', '.join(letrasIncorretas)}")
    

if "_" not in palavraSorteada:
    print("PARABÉNS! Você ganhou 🎉")
else:
    print(f"Você perdeu 😭 A palavra era: {sorteio}")