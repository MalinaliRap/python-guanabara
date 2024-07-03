n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o valor 2: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d1 = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira vale {} e a potência vale {}'.format(d1, e))