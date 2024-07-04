#um professor quer sortear um dos seus quatro alunos para apagar o quadro,
#faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido[aleatório]

from random import choice
n1 = input('digite o nome do primeiro aluno: ')
n2 = input('digite o nome do segundo aluno: ')
n3 = input('digite o nome do terceiro aluno: ')
n4 = input('digite o nome do quarto aluno: ')

print('o aluno escolhido foi {}'.format(choice([n1, n2, n3, n4])))