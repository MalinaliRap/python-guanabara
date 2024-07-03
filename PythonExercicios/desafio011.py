#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m2
largura = float(input('digite a largura da parede: '))
altura = float(input('digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print('sua parede tem {:.2f}m2, e precisar de {:.2f}l de tinta para pinta-la'.format(area, tinta))