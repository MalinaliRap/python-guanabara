#desenvolva um programa que leia as duas notas de um aluno. calcule e mostre a sua media
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A media final das notas {:.1f} e {:.1f} é {:.1f}'.format(nota1, nota2, media))