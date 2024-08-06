'''Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".'''

perguntas = ["1. Telefonou para a vítima?", 
             "2. Esteve no local do crime?", 
             "3. Mora perto da vítima?", 
             "4. Devia para a vítima?",
             "5. Já trabalhou com a vítima?"]

print("Responda com S (para sim) e N (para não)")

yes = no = 0

for i in perguntas:
    print(i)
    answer = input("Sua resposta: ").upper()
    if answer == "S":
        yes += 1
    elif answer == "N":
        no += 1
    else:
        print("Digite uma resposta válida S (para sim) e N (para não)!")
    
    if yes == 2:
        classificacao = "SUSPEITA(O)"
    elif yes >= 3 and yes <= 4:
        classificacao = "CÚMPLICE"
    elif yes == 5:
        classificacao = "ASSASSINO(A)"
    else:
        classificacao = "INOCENTE"
    
print(f"Respostas positivas: {yes}")
print(f"Respostas negativas: {no}")
print(f"Você foi classificado como {classificacao}")