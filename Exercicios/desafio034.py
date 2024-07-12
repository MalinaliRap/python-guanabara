#escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#para salários superiores a R$1250,00, calcule um aumento de 10%
#para inferiores ou iguais o aumento é de 15%
salario = float(input('Digite o seu salário : '))
if(salario <= 1250):
    print('Seu salário é {} e o aumento é {}'.format(salario,salario*0.15))
else:
    print('Seu salário é {} e o aumento é {}'.format(salario,salario*0.10))