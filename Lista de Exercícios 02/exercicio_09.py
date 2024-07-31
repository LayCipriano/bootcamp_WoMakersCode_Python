# Exercícios Tomada de Decisão
'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
'''

par = 0
impar = 0

while True:
    try:
        num = int(input("Informe um número: "))
        if num > 0:          
            while num != 0:
                resultado = num % 2
                if resultado == 0:
                    par += 1
                    num = int(input("Informe outro número: "))
                else:
                    impar += 1
                    num = int(input("Informe outro número: "))
            break
        else:
            print("Por favor, insira um número positivo!")
    except ValueError:
        print("Por favor, insira um número válido!")

print("_____ RESULTADO FINAL _____")
print(f"Número pares: {par}")
print(f"Números ímpares: {impar}")