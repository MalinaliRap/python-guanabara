#Crie um programa que leia um n[umero Real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
num = float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira e {}'.format(num, trunc(num)))