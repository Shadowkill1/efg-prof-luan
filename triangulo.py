
import math

class Triangulo:
    def __init__(self, base, altura, lado_a, lado_b, lado_c, angulo_ab, angulo_ac, angulo_bc):
        self.__base = base
        self.__altura = altura
        self.__lado_a = lado_a
        self.__lado_b = lado_b
        self.__lado_c = lado_c
        self.angulo_ab = angulo_ab
        self.angulo_ac = angulo_ac
        self.angulo_bc = angulo_bc

    @property
    def calcular_area(self):
        return (self.__base * self.__altura) / 2

    @property
    def calcular_perimetro(self):
        return self.__lado_a + self.__lado_b + self.__lado_c

    @property
    def verificar_tipo_triangulo(self):
        if self.__lado_a == self.__lado_b == self.__lado_c:
            return "Equilátero"
        elif self.lado_a == self.__lado_b or self.__lado_a == self.__lado_c or self.__lado_b == self.__lado_c:
            return "Isósceles"
        else:
            return "Escaleno"

base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))
lado_a = float(input("Digite o valor do lado a do triângulo: "))
lado_b = float(input("Digite o valor do lado b do triângulo: "))
lado_c = float(input("Digite o valor do lado c do triângulo: "))
angulo_ab = int(input("Digite o valor do ângulo AB do triângulo (em graus): "))
angulo_ac = int(input("Digite o valor do ângulo AC do triângulo (em graus): "))
angulo_bc = int(input("Digite o valor do ângulo BC do triângulo (em graus): "))

triangulo = Triangulo(base, altura, lado_a, lado_b, lado_c, angulo_ab, angulo_ac, angulo_bc)

print("Área do triângulo:", triangulo.calcular_area)
print("Perímetro do triângulo:", triangulo.calcular_perimetro)
print("Tipo do triângulo:", triangulo.verificar_tipo_triangulo)