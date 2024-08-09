'''Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.'''

while True:
    try: 
        def reverso(conteudo):
            conteudo = str(conteudo) #convertendo valor em str
            conteudo = conteudo[::-1] #revertendo o valor ainda como str
            return conteudo #retornando o valor final

        numero = int(input("Informe um número: "))

        result = reverso(numero)
        print(f"O reverso de {numero} é {result}")
        
        break
    except ValueError:
        print("Somente números são permitidos!")