#crie um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos digitos separados

#Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = input('Digite um numero de 0 a 9999 : ')
if numero.isnumeric() :
    if '-' in numero:
        print('Números negativos são inválidos')
    elif len(numero) == 4:
        print('unidade {}'.format(numero[3]))
        print('dezena {}'.format(numero[2]))
        print('centena {}'.format(numero[1]))
        print('milhar {}'.format(numero[0]))
    elif len(numero) == 3:  
        print('unidade {}'.format(numero[2]))
        print('dezena {}'.format(numero[1]))
        print('centena {}'.format(numero[0]))
    elif len(numero) == 2:  
        print('unidade {}'.format(numero[1]))
        print('dezena {}'.format(numero[0]))
    elif len(numero) == 1:  
        print('unidade {}'.format(numero[0]))
    else:
        print('Inválido')
else:
    print('Não é um número')