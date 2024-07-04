#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import sin, cos, tan, radians
angulo = float(input('digite o valor do angulo: '))
radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)
print('o angulo de {} graus tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))