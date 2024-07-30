'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''


def calculoINSS(salBruto):
    salMin = 1412
    inss1 = inss2 = inss3 =  inss4 = 0
    
    if salBruto < salMin: #faixa de cálculo 1
      inss1 = salMin * 0.075     
    elif salBruto >= 1412.01 and salBruto <= 2666.68: #faixa de cálculo 2
        inss1 = salMin * 0.075    
        inss2 = (salBruto - salMin) * 0.09
    elif salBruto >= 2666.69 and salBruto <= 4000.03: #faixa de cálculo 3
        inss1 = salMin * 0.075    
        inss2 = (2666.68 - salMin) * 0.09
        inss3 = (salBruto - 2666.69) * 0.12
    else: #faixa de cálculo 4
        if salBruto <= 7786.02:
            inss4 = (salBruto - 4000.04) * 0.14
            inss3 = (4000.04 - 2666.69) * 0.12
            inss2 = (2666.68 - salMin) * 0.09
            inss1 = salMin * 0.075    
        else:
            inss4 = (7786.02 - 4000.04) * 0.14
            inss3 = (4000.04 - 2666.69) * 0.12
            inss2 = (2666.68 - salMin) * 0.09
            inss1 = salMin * 0.075 
        
    
    descontosINSS = inss1 + inss2 + inss3 + inss4
    salLiquido = salBruto - descontosINSS

    return salLiquido, descontosINSS, inss1, inss2, inss3, inss4

def calculoIRRF(salLiquido, salBruto):
    irrf1 = irrf2 = irrf3 = irrf4 = irrf5 = 0
    
    if salBruto <= 2259.20: #faixa de cálculo 1
        irrf1 = 0
    elif salBruto >= 2259.21 and salBruto <= 2826.65: #faixa de cálculo 2
        irrf1 = 0
        irrf2 = (2826.65 - 2259.20) * 0.075
    elif salBruto >= 2826.66 and salBruto <= 3751.05: #faixa de cálculo 3
        irrf1 = 0
        irrf2 = (2826.65 - 2259.20) * 0.075
        irrf3 = (3751.05 - 2826.65) * 0.15
    elif salBruto >= 3751.06 and salBruto <= 4664.68: #faixa de cálculo 4
        irrf1 = 0
        irrf2 = (2826.65 - 2259.20) * 0.075
        irrf3 = (3751.05 - 2826.65) * 0.15
        irrf4 = (4664.68 - 3751.05) * 0.225
    else:
        irrf1 = 0
        irrf2 = (2826.65 - 2259.20) * 0.075
        irrf3 = (3751.05 - 2826.65) * 0.15
        irrf4 = (4664.68 - 3751.05) * 0.225
        irrf5 = (4664.68 - salLiquido) * 0.275
        
    descontosIRRF = irrf1 + irrf2 + irrf3 + irrf4 + irrf5
    salFinal = salLiquido - descontosIRRF
    
    return descontosIRRF, salFinal, irrf1, irrf2, irrf3, irrf4, irrf5
    
def main():
    salBruto = float(input("Informe o seu salário BRUTO: R$"))
    
    salLiquido, descontosINSS, inss1, inss2, inss3, inss4 = calculoINSS(salBruto)
    descontosIRRF, salFinal, irrf1, irrf2, irrf3, irrf4, irrf5 = calculoIRRF(salLiquido, salBruto)
    
    print(f'''
        Salário Bruto: {salBruto}
        Salário Líquido: {salLiquido:.2f}
            
        ____ CÁLCULO DO INSS ____
        Faixa 1: R${inss1:.2f}
        Faixa 2: R${inss2:.2f}
        Faixa 3: R${inss3:.2f}
        Faixa 4: R${inss4:.2f}
        Total de Descontos: R${descontosINSS:.2f}
        
        ____ CÁLCULO DO IRRF ____
        Faixa 1: R${irrf1:.2f}
        Faixa 2: R${irrf2:.2f}
        Faixa 3: R${irrf3:.2f}
        Faixa 4: R${irrf4:.2f}
        Faixa 5: R${irrf5:.2f}
        Total de Descontos: R${descontosIRRF:.2f}
        
        Salário Líquido Final: R${salFinal:.2f}
        ''')  
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
# TABELA CÁLCULO IRRF 
'''
Até R$ 2.259,20	                Isento
De R$ 2.259,21 até R$ 2.826,65	7,5%
De R$ 2.826,66 até R$ 3.751,05	15%
De R$ 3.751,06 até R$ 4.664,68	22,5%
Acima de R$ 4.664,68	        27,5%   
'''
    
    
    
    
    
    
# TABELA CÁLCULO INSS 
'''
f1 - até 1.412,00	            7,5%
f2 - de 1.412,01 até 2.666,68	9%
f3 - de 2.666,69 até 4.000,03	12%
f4 - de 4.000,04 até 7.786,02	14%
'''