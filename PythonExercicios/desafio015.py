#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('digite a quantidade de km percorridos: '))
dias = float(input('digite a quantidade de dias que o carro foi alugado: '))

total = (km * 0.15) + (dias * 60)

print('o valor total a ser pago pelo aluguel do automovel foi de R${:.2f}'.format(total))