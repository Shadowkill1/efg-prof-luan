
    
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
class FormaGeometrica:
    def __init__(self, lado):
     self.__lado = lado

    @property
    def area(self):
        pass
    
    @property
    def perimetro(self):
        pass

    @property
    def lado(self):
        return self.__lado
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__(raio)
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