#faça um programa que leia o nome completoo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente

#ex: Ana Maria de Souza
#primeiro=Ana
#último=Souza

nome = input('Digite o nome completo : ')

primeiro = nome.split()[0]
ultimo = nome.split()[-1]

print('O primeiro nome é {} e o ultimo nome é {}'.format(primeiro,ultimo))