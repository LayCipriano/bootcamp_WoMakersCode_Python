# definindo a classe televisão e o seu comportamento padrão
class Televisao :
    def __init__(self):
        self.ligada = False
        self.canal = 3
        self.canalMin = 1
        self.canalMax = 99
        self.volume = 30
        self.volumeMax = 100
        self.volumeMin = 0
    
    def ligar(self):
        self.ligada = True
        
    def desligar(self):
        self.ligada = False
        
    def mudarCanalCima(self):
        if not self.ligada:
            return
        
        if self.canal < self.canalMax:
            self.canal += 1
            
    def mudarCanalBaixo(self):
        if not self.ligada:
            return
        
        if self.canal > self.canalMin:
            self.canal -= 1
        
    
    def aumentarVolume(self):
        if not self.ligada:
            return
    
        if self.volume < self.volumeMax:
            self.volume += 5
            
    def diminuirVolume(self):
        if not self.ligada:
            return
    
        if self.volume > self.volumeMin:
            self.volume -= 5
            
# criando as instâncias

tvSala = Televisao()
tvQuarto = Televisao()

tvSala.ligar()
print(f"tvSala está ligada? {tvSala.ligada}")
print(f"tvQuarto está ligada? {tvQuarto.ligada}")

for _ in range(3):
    tvSala.aumentarVolume()

print(f"tvSala volume: {tvSala.volume}")
print(f"tvQuarto volume: {tvQuarto.volume}")