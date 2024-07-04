# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos, Faça um programa que leia o nome dos quatro alunos e mostre a orderm sorteada

import random

# Create a list
var1 = input('Digite o primeiro Aluno : ')
var2 = input('Digite o segundo Aluno : ')
var3 = input('Digite o terceiro Aluno : ')
var4 = input('Digite o quarto Aluno : ')
my_list = random.shuffle([var1, var2, var3, var4])

print(my_list)
# Shuffle the list
print('A lista de ordem de apresentação é {} '.format(my_list))
