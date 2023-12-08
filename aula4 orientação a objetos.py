class Carro:
    def __init__(self, marca, cor, modelo):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.status_motor = "desligado"
        self.status_movimento = "parado"

    def ligarMotor(self):
        if self.status_motor == "desligado":
            self.status_motor = "ligado"
        else:
            print("O motor já está ligado sr pedro.")

    def desligarMotor(self):
        if self.status_motor == "ligado":
            self.status_motor = "desligado"
        else:
            print("O motor já está desligado.")

    def andar(self):
        if self.status_motor == "ligado":
            if self.status_movimento == "parado":
                self.status_movimento = "andando"
                print("O carro está em movimento.")
            else:
                print("O carro já está em movimento.")
        else:
            print("É necessário ligar o motor antes sr pedro.")

    def parar(self):
        if self.status_motor == "ligado":
            if self.status_movimento == "andando":
                self.status_movimento = "parado"
                print("O carro está parado.")
            else:
                print("O carro esta parado.")
        else:
            print("liga o carro antes seu mané.")

    def exibirStatus(self):
        print("Marca: ", self.marca)
        print("Cor: ", self.cor)
        print("Modelo: ", self.modelo)
        print("Status do motor:", self.status_motor)
        print("Status do movimento:", self.status_movimento)


carro = Carro("Ford", "Preto", "camaro")
carro.exibirStatus()

carro.ligarMotor()
carro.andar()
carro.exibirStatus()

carro.andar()
carro.parar()
carro.exibirStatus()

carro.parar()
carro.desligarMotor()
carro.exibirStatus()