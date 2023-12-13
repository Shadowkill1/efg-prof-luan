class Quadrado:
    def __init__(self, lado):
        self.__lado = lado

    @property
    def area(self):
        print()
        return self.__lado ** 2
    
    @property
    def perimetro(self):
        print()
        return self.__lado * 4

q = Quadrado(8)
print(q.area)
print(q.perimetro)