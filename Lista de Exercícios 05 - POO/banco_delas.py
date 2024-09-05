from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome:str, telefone:str, genero:str, rendaMensal:float):
        self.nome = nome
        self.telefone = telefone
        self.genero = genero.lower()
        self.rendaMensal = rendaMensal
        
    def possuiChequeEspecial(self):
        return self.genero == 'feminino'
        
class ContaCorrente:
    def __init__(self, clientes: list[Cliente]):
        self.clientes = clientes
        self.saldo = 0.0
        self.operacoes = []
        
    def depositarValores(self, valor:float):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(f"Depósito: +R${valor:.2f}")
        else:
            print("Valor para depósito deve ser positivo!")
            
    def sacarValores(self, valor:float):
        valorDisponivel = self.saldo + self.chequeEspecial()
        
        if 0 < valor <= valorDisponivel:
            self.saldo -= valor
            self.operacoes.append(f"Saque: -R${valor:.2f}. Utilizado cheque especial*")
        else:
            print("Saldo insuficiente para o saque!")
            
    def chequeEspecial(self):
        chequeEspecialAprovado =  [cliente.rendaMensal for cliente in self.clientes if cliente.possuiChequeEspecial()]
        
        if chequeEspecialAprovado:
            return max(chequeEspecialAprovado)
        else:
            return 0 
    
    def exibirChequeEspecial(self):
        exibirChequeEspecial = [cliente.rendaMensal for cliente in self.clientes if cliente.possuiChequeEspecial()]
        chequeTotal = self.saldo + self.chequeEspecial()
        
        if exibirChequeEspecial:
            print("Cheque Especial:")
            for rendas in exibirChequeEspecial:
                print(f"R${rendas:.2f}")
                
            print(f"Saldo da Conta + Cheque Especial: R${chequeTotal:.2f} ")
        else:
            print("Cliente não possui cheque especial")
    
    def exibirSaldo(self):
        print(f"Saldo Atual: R${self.saldo:.2f}")
        
    def exibirExtrato(self):
        for operacao in self.operacoes:
            print(operacao)

cliente1 = Cliente("Laysa Cipriano", "(44)9 8403-5017", "Feminino", 2650.80)
cliente2 = Cliente("Laysa Cipriano", "(44)9 8403-5017", "Masculino", 7650.80)

conta = ContaCorrente([cliente1])

conta.depositarValores(8000)
conta.exibirSaldo()
conta.exibirChequeEspecial()
print()
print()
conta.sacarValores(10000)
print()
print()
conta.exibirExtrato()
print()
print()
conta.exibirSaldo()
conta.exibirChequeEspecial()