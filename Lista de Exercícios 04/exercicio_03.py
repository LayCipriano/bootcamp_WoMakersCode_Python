'''Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.
Extra: Crie uma terceira, que é um menu para o usuário escolher a
opção desejada, onde esse menu chama a função de conversão
correta.'''


# 1. perguntar ao usuário:
    # 1.1 o valor a ser convertido
    # 1.2 para qual medida ele deseja converter: Celsius ou Fahrenheit
# 2. Criar um menu para o usuário


# Função Celsius -> Fahrenheit
def celsiusToFahrenheit(medida):
    resfahrenheit = (medida * 9/5) + 32
    print(f"A conversão de {medida}°C é igual a {resfahrenheit}°F")
    
def fahrenheitToCelsius(medida):
    resCelsius = (medida - 32) * 5/9
    print(f"A conversão de {medida}°F é igual a {resCelsius}°C")
    
def main():
# Valor inputado pelo usuário
    print("_____ CALCULADORA DE CONVERSÃO DE GRAUS _____")
    print("Qual operação deseja realizar?")
    print("1. Converter Celsius para Fahrenheit")
    print("2. Converter Fahrenheit para Celcius")
    choice = int(input("Digite o número correspondente à sua escolha: "))
    
    if choice == 1:
        medida = float(input("Informe sua temperatura: "))
        celsiusToFahrenheit(medida)
    elif choice == 2:
        medida = float(input("Informe sua temperatura: "))
        fahrenheitToCelsius(medida)
    else:
        print("Opção inválida. Por favor, escolha entre 1 e 2.")
        
if __name__ == "__main__":
    main()