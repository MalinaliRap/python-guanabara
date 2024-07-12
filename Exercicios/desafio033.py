#Faça um programa que leia três números e mostra qual é o maior e qual é o menor
n1 = int(input('Digite o número 1 : '))
n2 = int(input('Digite o número 2 : '))
n3 = int(input('Digite o número 3 : '))

if n1 < n2 < n3:
    print('O menor é o n1 ({}) e o maior é o n3 ({})'.format(n1,n3))
elif n2 < n3 < n1:
    print('O menor é o n2 ({}) e o maior é o n1 ({})'.format(n2,n1))
elif n3 < n1 < n2:
    print('O menor é o n3 ({}) e o maior é o n2 ({})'.format(n3,n2))
elif n3 < n2 < n1:
    print('O menor é o n3 ({}) e o maior é o n1 ({})'.format(n3,n1)) 
elif n1 < n3 < n2:
    print('O menor é o n1 ({}) e o maior é o n2 ({})'.format(n1,n2))
elif n2 < n1 < n3:
    print('O menor é o n2 ({}) e o maior é o n3 ({})'.format(n2,n3))
    