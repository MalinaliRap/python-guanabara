#faça um programa que pergunte a distância de uma viagem em KM. 
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km
#e R$0,45 para viagens mais longas
km = int(input('Digite a kilometragem da sua viagem : '))
if km <= 200:
    print('O valor da sua viagem é de {}'.format(km*0.50))
else: 
    print('O valor da sua viagem é de {}'.format(km*0.45))