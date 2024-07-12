n1 = float(input('Digite sua nota 1 : '))
n2 = float(input('Digite sua nota 2 : '))
m = (n1+n2)/2
print('Sua media: {:.2}'.format(m))
if m >= 0 and m < 6:
    print('Reprovou')
elif m>=6 and m<=10:
    print('Passou')
else:
    print('Inválida')