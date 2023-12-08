class Carro:
    def __init__(self):
        self.status_motor = "desligado"
        self.status_movimento = "parado"
    
    def ligar_motor(self):
        print("Motor ligado.")
        self.status_motor = "ligado"
    
    def desligar_motor(self):
        print("Motor desligado.")
        self.status_motor = "desligado"
        self.status_movimento = "parado"
    
    def andar(self):
        print("O carro está andando.")
        self.status_movimento = "andando"
    
    def parar(self):
        print("O carro parou.")
        self.status_movimento = "parado"
    
    def exibir_status_motor(self):
        print("Status do motor:", self.status_motor)
    
    def exibir_status_movimento(self):
        print("Status do movimento do carro:", self.status_movimento)

# Exemplo de uso dos métodos, atributos e métodos adicionais
carro = Carro()
carro.exibir_status_motor(desligado)  # desligado
carro.exibir_status_movimento(parado)  # parado

carro.ligar_motor()
carro.exibir_status_motor()  # ligado

carro.andar()
carro.exibir_status_movimento()  # andando

carro.parar()
carro.exibir_status_movimento()  # parado

carro.desligar_motor()
carro.exibir_status_motor()  # desligado