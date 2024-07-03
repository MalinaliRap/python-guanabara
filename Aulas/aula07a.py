#operadores aritméticos
n1=int(input('digite um valor:'))
n2=int(input('digite outro valor:'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
mo=n1%n2
print('a soma entre {} e {} vale {}'.format(n1,n2,s))
print('a multiplicação entre {} e {} vale {}'.format(n1,n2,m))
print('a divisão entre {} e {} vale {:.3f}'.format(n1,n2,d))
print('a divisão inteira entre {} e {} vale {}'.format(n1,n2,di))
print('a potencia entre {} e {} vale {}'.format(n1,n2,e))
print('o resto da divisão entre {} e {} vale {}'.format(n1,n2,mo))

#ordem de precedência
#1 ()
#2 **
#3 *, /, //, %
#4 +, -
# a precedência dos operadores aritmeticos leva em consideração quem chegar primeiro caso aparece primeiro