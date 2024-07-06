#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = input('Digite o nome da cidade : ')

cidade_lower = cidade.lower()

if cidade_lower.startswith('santo'):
    print('Sim, a cidade começa com Santo')
else:
    print('Não, a cidade não começa com santo')