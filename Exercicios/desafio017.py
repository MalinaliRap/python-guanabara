#Fa;a um programa que leia o comprimento do cateto oposto e adjacente de um triangulo retangulo
# e calcule e mostre o comprimento da hipotenusa

# soma do quadrado dos catetos é igual o quadrado da hipotenusa

from math import hypot
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
hi = hypot(co, ca) #formula da hipotenusa
print('o valor da hipotenusa é {:.2f}'.format(hi))