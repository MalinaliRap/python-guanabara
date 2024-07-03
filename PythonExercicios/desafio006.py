#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('digite um valor: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2) #transformar raiz quadrada em potência https://www.youtube.com/watch?v=9c2J0o3JAt8&ab_channel=MarcosAbaMatem%C3%A1tica
print('o dobro de {} vale {}, o triplo vale {} e a raiz quadrada vale {:.2f}'.format(n1, d, t, r))