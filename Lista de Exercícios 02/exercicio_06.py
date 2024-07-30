# Exercícios Tomada de Decisão
'''Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.'''

user = input("Informe seu usuário: ")
password = input("Informe sua senha: ")

while True:
    try:
        if user == "admin" and password == "admin123":
            print("Login realizado com sucesso!")
        else:
            print("Login incorreto, tente novamente!") 
        break
    except ValueError:
        print("Entrada inválida!")