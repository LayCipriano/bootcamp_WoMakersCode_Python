# Exercícios Classes e Objetos
# 1. Crie uma classe que modele o objeto "carro".
class Carro:
    # 2. Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
    def __init__(self):
        self.ligado = True
        self.cor = "Verde Musgo"
        self.modelo = "Fusca"
        self.velocidade = 0
        self.velocidadeMax = 144
        
    # 3. Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
    def ligar(self):
        self.ligado = True
        print("CARRO LIGADO")
        
    def desligar(self):
        self.ligado = False
        print("CARRO DESLIGADO")
    
    def acelerar(self):
        if not self.ligado:
            return

        if self.velocidade < self.velocidadeMax:
            self.velocidade += 12
            
    def desacelerar(self):
        if not self.ligado:
            return
        
        if self.velocidade >= 12:
            self.velocidade -= 12

# 4. Crie uma instância da classe carro.
carroLay = Carro()

# 5. Faça o carro "andar" utilizando os métodos da sua classe.
print()
carroLay.ligar()

for _ in range(1):
    carroLay.acelerar()

print(f"O carro está andando. Velocidade: {carroLay.velocidade}Km/h")
print()

# 6. Faça o carro "parar" utilizando os métodos da sua classe.

for _ in range(3):
    carroLay.desacelerar()

if carroLay.velocidade == 0:
    carroLay.desligar()
    print(f"Velocidade: {carroLay.velocidade}")
else:
    print(f"O carro está parando. Velocidade: {carroLay.velocidade}Km/h")
