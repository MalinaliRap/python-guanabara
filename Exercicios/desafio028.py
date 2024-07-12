#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuárioa tentar descobrir
#qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randrange
random_number = randrange(0,5)
user_number = int(input('Digite um número de 1 a 5 : '))
if random_number == user_number:
    print('Você ganhou!',end='')
else:
    print('Você perdeu!',end='')
print(', o número era {}'.format(random_number))    