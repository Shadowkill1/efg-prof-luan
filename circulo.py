import math

class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    @property
    def obter_diametro(self):
        return 2 * self.__raio
    
    @property
    def obter_area(self):
        return math.pi * self.__raio ** 2
    
    @property
    def obter_perimetro(self):
        return (2 * math.pi) * (self.__raio)

raio = float(input("Digite o valor do raio do círculo: "))

circulo = Circulo(raio)

print("Diâmetro do círculo:", circulo.obter_diametro)
print("Área do círculo:", circulo.obter_area)
print("Perímetro do círculo:", circulo.obter_perimetro)