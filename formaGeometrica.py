
    
# class Quadrado(FormaGeometrica):
   
#     def __init__(self, lado):
#         super().__init__(lado)

#     @property
#     def area(self):
#         return self.lado ** 2
    
# q = Quadrado(4)
# print(q.area)

# class Retangulo(FormaGeometrica):
#     def __init__(self, base, altura):
#         super().__init__(base)
#         self.__altura = altura

#     @property
#     def area(self):
#         return self.base * self.__altura
#     @property
#     def altura(self):
#         return self.__altura
    
#     @property
#     def base(self):
#         return super().lado  # Fica melhor usar return self.lado
    
    
#     @property
#     def perimetro(self):
#         return(self.base * 2) + (self.altura * 2)
    
# base = float(input('qual a base: '))
# altura = float(input('qual a altura: '))

# r = Retangulo(base, altura)
# print(r.area)
# print(r.perimetro)


    
# class Circulo(FormaGeometrica):
#     def __init__(self, raio):
#         super().__init__(raio)
#         self.__raio = raio

#     @property
#     def obter_diametro(self):
#         return 2 * self.__raio
    
#     @property
#     def obter_area(self):
#         return math.pi * self.__raio ** 2
    
#     @property
#     def obter_perimetro(self):
#         return (2 * math.pi) * (self.__raio)

# raio = float(input("Digite o valor do raio do círculo: "))

# circulo = Circulo(raio)

# print("Diâmetro do círculo:", circulo.obter_diametro)
# print("Área do círculo:", circulo.obter_area)
# print("Perímetro do círculo:", circulo.obter_perimetro)


# class FormaGeometrica:
#     def __init__(self, lado):
#         self.__lado = lado

#     @property
#     def lado(self):
#         return self.__lado

# class Triangulo(FormaGeometrica):
#     def __init__(self, base, altura, lado_a, lado_b, lado_c, angulo_ab, angulo_ac, angulo_bc):
#         super().__init__(lado_a)
#         self.base = base
#         self.altura = altura
#         self.lado_b = lado_b
#         self.lado_c = lado_c
#         self.angulo_ab = angulo_ab
#         self.angulo_ac = angulo_ac
#         self.angulo_bc = angulo_bc

#     @property
#     def area(self):
#         return (self.base * self.altura) / 2

#     @property
#     def perimetro(self):
#         return self.lado + self.lado_b + self.lado_c

#     def verificar_tipo_triangulo(self):
#         if self.lado_a == self.lado_b == self.lado_c:
#             return "Equilátero"
#         elif self.lado_a == self.lado_b or self.lado_a == self.lado_c or self.lado_b == self.lado_c:
#             return "Isósceles"
#         else:
#             return "Escaleno"

# base = float(input("Digite o valor da base do triângulo: "))
# altura = float(input("Digite o valor da altura do triângulo: "))
# lado_a = float(input("Digite o valor do lado a do triângulo: "))
# lado_b = float(input("Digite o valor do lado b do triângulo: "))
# lado_c = float(input("Digite o valor do lado c do triângulo: "))
# angulo_ab = int(input("Digite o valor do ângulo AB do triângulo (em graus): "))
# angulo_ac = int(input("Digite o valor do ângulo AC do triângulo (em graus): "))
# angulo_bc = int(input("Digite o valor do ângulo BC do triângulo (em graus): "))

# triangulo = Triangulo(base, altura, lado_a, lado_b, lado_c, angulo_ab, angulo_ac, angulo_bc)

# print("Área do triângulo:", triangulo.area)
# print("Perímetro do triângulo:", triangulo.perimetro)
# print("Tipo do triângulo:", triangulo.verificar_tipo_triangulo)
    
