#crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva no nome" no nome
nome = input('Digite seu nome completo : ')
nome_lower = nome.lower()

if 'silva' in nome_lower:
    print('Seu nome possui Silva')
else:
    print('Seu nome não possui Silva')