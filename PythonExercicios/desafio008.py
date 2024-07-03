#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimitros.
# 1 m = 100 cm = 1000 mm
m = float(input('digite um valor em metros: '))
print('O valor {} em metros equivale a {} cm e {} mm'.format(m, m*100, m*1000))