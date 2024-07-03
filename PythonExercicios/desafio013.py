#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('digite o valor do seu salario: '))
aumento = (salario * 0.15) 
novosalario = aumento + salario
print('o valor do seu novo salário com 15% de aumento e {:.2f}'.format(novosalario))