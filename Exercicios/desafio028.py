#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuárioa tentar descobrir
#qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu
from time import sleep
from random import randrange
random_number = randrange(0,5)
print('\033[0;30;45m-=-\033[m'*20)
print('\033[1;37;41mVou pensar um número de 0 a 5, tente adivinhar ....\033[m')
print('\033[0;30;45m-=-\033[m'*20)
user_number = int(input('\033[4;33mDigite um número de 1 a 5 : \033[m'))
print('\033[0;35mPROCESSANDO ...\033[m')
sleep(3)
if random_number == user_number:
    print('\033[1;32mVocê ganhou!',end='')
else:
    print('\033[1;31mVocê perdeu!',end='')
print(', o número era {}\033[m'.format(random_number))    