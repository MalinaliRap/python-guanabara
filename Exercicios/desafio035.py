#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo

a = float(input('Digite o segmento 1 : '))
b = float(input('Digite o segmento 2 : '))
c = float(input('Digite o segmento 3 : '))

if a < b+c and b < a+c and c < a+b:
    print('Podemos ter um triângulo')
else:
    print('Não podemos ter um triângulo')


