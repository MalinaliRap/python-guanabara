#faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano  = int(input('Digite o ano : '))
d = ano % 100
if(d % 4 == 0):
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')