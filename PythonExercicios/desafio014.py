#escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
# 1 °C = 1,8 °F
c = float(input('digite uma temperatura em °C: '))
f = (c * 1.8) + 32
print('a temperatura de {}°C corresponde a {}°F'.format(c, f))