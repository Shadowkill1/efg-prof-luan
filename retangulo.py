class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def area(self):
        return self.base * self.__altura
    @property
    def base(self):
        return self.__base * self.__altura
    
    @property
    def perimetro(self):
        return(self.__base * 2) + (self.__altura * 2)
    
base = float(input('qual a base'))
altura = float(input('qual a altura'))

r = Retangulo(base, altura)
print(r.base)
print(r.perimetro)