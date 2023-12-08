#prfloat('alo mundo')

# numero = int(input('Escreva um numero: '))
# print(f'O numero informado foi: {numero}')

# numero1 = float(input('digite o primeiro numero: '))
# numero2 = float(input('digite o segundo numero: '))

# soma = numero1 + numero2
# print('A soma dos dois numeros é :',soma)

# nota1 = float(input('digite a primeira nota: '))
# nota2 = float(input('digite a segunda nota: '))
# nota3 = float(input('digite a terceira norta: '))
# nota4 = float(input('digite a quarta nota: '))

# media =(nota1 + nota2 + nota3 + nota4) / 4
# print('A soma de suas notas foi: ', media )

#-------------- parte 2 --------------#

# print('Escreva dois numeros para verificar qual o maior deles: ')
# num1 = int(input('primeiro: ' ))
# num2 = int(input('segundo: '))
# if num1 > num2: 
#     print(num1)
# else:
#     print(num2)

# valor = float(input('digite um valor: '))
# if valor >= 0 :
#     print('o valor é positivo: ')
# else:
#     print('O valor é negativo: ')

# letra = input('digite uma letra : ')
# if letra =='a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#     print('A letra digitada é uma vogal. ')
# if letra =='A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
#     print('A letra digitada é uma vogal. ')
# else:
#     print('A letra digitada é uma consoante: ')

# x = input('Digite uma letra: ')

# if x.lower() in ['a' , 'e' , 'i' , 'o' , 'u']:
#     print('E vogal.')
# else:
#     print('É consoante')

# fim = int(input('digite o numero:')) 
# x = 1
# while x <= fim:
#     if x % 2 == 0:
#       print(f'o numero{x} é par')
#     else:
#       print(f'o numero {x} é impar')
#     x += 1
################## parte 3 ##################
 

# def contar_digitos(numeros):
#     return len(str(numero))
# numero = int(input('digite um numero inteiro: '))
# quantidade_digitos = contar_digitos(numero)
# print(f'o numero{numero} possui {quantidade_digitos} digitos. ')

#---------------------------------------------------------

# def somar(n1, n2, n3):
#     return n1 + n2 + n3
# num1 = int(input('digite o primeiro numero: '))
# num2 = int(input('digite o segundo numero: '))
# num3 = int(input('digite o terceiro numero: '))
# resultado = somar(num1, num2, num3)
# print('A soma dos tres numeros é: ', resultado)

#--------------------------------------------------------
# def funcao():
#     a=int(input('digite um numero: '))
#     print(len(str(a)), 'digitos')
# funcao()

#------------------------------------------------------------------
# from datetime import datetime
# def quantidade_digitos(numero):

#     return len(str(abs(numero)))

# def data_por_extenso(data):
#     try:
#          datetime_object = datetime.strptime(data, '%d,/%m/Y')
#     except ValueError:
#          return None
#     dia = datetime_object.day
#     mes = datetime_object.strftime('%B').capitalize()
#     ano = datetime_object.year
#     return f'{dia} de {mes}de {ano}'
# numero = 12345
# print(quantidade_digitos(numero))
# data = '17/11/2023'
# print(data_por_extenso(data))


#----------------------------------------------------------------
# def imprima(parametro):
#     print(parametro)
# imprima('ola mundo! ')
#-----------------------------------------------
# def imprime_par_impar(numero):
#     if numero % 2 == 0:
#         print(f'o numero {numero} e impar.' )
#     else:
#         print(f'o numero {numero} e impar.' )
#         imprime_par_impar(9)
#         imprime_par_impar(12)
