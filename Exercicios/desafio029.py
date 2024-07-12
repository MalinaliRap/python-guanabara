#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada KM acima do limite
km = int(input('Digite a Velocidade do carro : '))
if km > 80:
    multa = (km - 80)*7
    print('Você foi multado e o valor da multa é de {}'.format(multa))