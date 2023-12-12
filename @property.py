import datetime

class Pessoa:
    def __init__(self, nome, nascimento, cpf, rg, endereco, estado_civil):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__endereco = endereco
        self.__estado_civil = estado_civil

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self._nascimento = nascimento

    @property
    def cpf(self):
        return "********" + self.__cpf[-4:]

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def rg(self):
        return "********" + self.__rg[-4:]

    @rg.setter
    def rg(self, rg):
        self._rg = rg

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def estado_civil(self):
        return self.__estado_civil

    @estado_civil.setter
    def estado_civil(self, estado_civil):
        self._estado_civil = estado_civil

    def calcular_idade(self):
        data_atual = datetime.datetime.now()
        data_nascimento = datetime.datetime.strptime(self._nascimento, "%d/%m/%Y")
        idade = data_atual.year - data_nascimento.year
        if data_atual.month < data_nascimento.month or (data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
            idade -= 1
        return idade

    def retornar_dados_formatados(self):
        return f"Nome: {self._nome}\nNascimento: {self._nascimento}\nCPF: {self.cpf}\nRG: {self.rg}\nEndereço: {self._endereco}\nEstado Civil: {self._estado_civil}"

pessoa = Pessoa("Pedro Henrique", "07/11/1991", "12345678901", "987654321", "Rua 206,2", "Casado")
print(pessoa.calcular_idade)
print(pessoa.retornar_dados_formatados)

print(pessoa.nome)
pessoa.nome ='josé'
print(pessoa.nome)

print(pessoa.nascimento)
pessoa.nascimento ='12/10/1890'
print(pessoa.nascimento)

print(pessoa.cpf)
pessoa.cpf ='019876545455'
print(pessoa.cpf)

print(pessoa.rg)
pessoa.rg ='123434456'
print(pessoa.rg)

print(pessoa.endereco)
pessoa.endereco ='Rua 308,3'
print(pessoa.endereco)

print(pessoa.estado_civil)
pessoa.estado_civil ='soltero'
print(pessoa.estado_civil)
