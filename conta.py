# class Mamifero:
#    def som(self):
#        print('emetir som')

# class Homem(Mamifero):
#    def som (self):
#        print('Oi')

# class Cachorro(Mamifero): 
#    def som(self):
#        print('Au! Au!')

# class Gato(Mamifero):
#    def som(self):
#        print('Meawwww')

# mamifero = Mamifero() 
# mamifero.som()

# animais = [Homem(), Cachorro(), Gato()]
# for animal in animais: animal.som()

class ContaCorrente:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def exibir_saldo(self):
        return self.saldo

class Poupanca(ContaCorrente):
    def __init__(self, saldo: float):
        super().__init__(saldo)

class ContaImposto(ContaCorrente):
    def __init__(self, saldo: float, percentualImposto: float):
        super().__init__(saldo)
        self.percentualImposto = percentualImposto

    def calculaImposto(self):
        self.saldo -= self.saldo * self.percentualImposto


saldo_conta_corrente = float(input("Digite o saldo da conta corrente: "))
saldo_poupanca = float(input("Digite o saldo da poupança: "))
saldo_conta_imposto = float(input("Digite o saldo da conta imposto: "))
percentual_imposto = float(input("Digite o percentual do imposto: "))

conta_corrente = ContaCorrente(saldo_conta_corrente)
poupanca = Poupanca(saldo_poupanca)
conta_imposto = ContaImposto(saldo_conta_imposto, percentual_imposto)


conta_imposto.calculaImposto()
print(conta_imposto.exibir_saldo())
