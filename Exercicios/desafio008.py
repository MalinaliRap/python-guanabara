#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimitros.
# 1 m = 100 cm = 1000 mm
m = float(input('digite um valor em metros: '))

# turbinada no exercicio após explicação
#quilômetro → km
#hectômetro → hm
#decâmetro → dam
#metro → m
#decímetro → dm
#centímetro → cm
#milímetro → mm

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('o valor {} metros em milimetros é {} mm'.format(m, mm))
print('o valor {} metros em centimetros é {} cm'.format(m, cm))
print('o valor {} metros em decimetros é {} dm'.format(m, dm))
print('o valor {} metros em decametros é {} dam'.format(m, dam))
print('o valor {} metros em hectometros é {} hm'.format(m, hm))
