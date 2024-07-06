# Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "A"
# 2. Em que posição ela aparece a primeira vez
# 3. Em que posição ela aparece a última vez
frase = input('Digite uma frase : ')

frase_lower = frase.lower()

print(len(frase_lower))
print('A letra "a" aparece {} vezes'.format(frase_lower.count('a')))
print('A letra "a" aparece a primeira vez na posição {}'.format(frase_lower.find('a')))
print('A letra "a" aparece pela ultima vez na posição {}'.format(frase_lower.rfind('a')))
