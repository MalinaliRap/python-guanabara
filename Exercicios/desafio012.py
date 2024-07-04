#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('digite o valor do produto: '))
d = p * 0.95
print('o valor do produto com 5% de desconto é R${:.2f}'.format(d))