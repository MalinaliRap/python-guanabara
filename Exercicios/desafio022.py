#crie um programa que leia o nome completo de uma pessoa e mostra
#1. O nome com todas as letras maiúsculas
#2. O nome com todas a letras minúsculas
#3. Quantas letras ao todo(sem considerar empaços).
#4. Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo : ')

print('Seu nome em letras maiusculas {}'.format(nome.upper()))
print('Seu nome em letras minusculas {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome.strip().replace(' ',''))))
print('Seu primeiro nome tem {}'.format(len(nome.split()[0])))
