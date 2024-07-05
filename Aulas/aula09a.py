#malipulando cadeias de texto
frase = 'Curso em Vídeo Python'

#Fatiamento
#print(frase[9])
#print(frase[9:21])
#print(frase[9:21:2])
#print(frase[:5])
#print(frase[15:])
#print(frase[9::3])
#print(len(frase))
#print(frase.count('o'))
#print(frase.count('o',0,13))
#print(frase.find('deo'))
#print(frase.find('Android'))
#print('Curso' in frase)
#print('Android' in frase)

#Transformação
#print(frase.replace('Python','Android'))
#print(frase.upper())
#print(frase.lower())
#print(frase.capitalize())
#print(frase.title())
#frase = '   Aprenda Python  '
#print(frase.strip()) #remove espaço
#print(frase.rstrip()) #remove espaço a direita
#print(frase.lstrip()) #remove espaço a esquerda

#Divisão

#print(frase.split())

#Junção

#print('-'.join(frase.split()))

#algumas dicas 

#para um texto grande com quebra de paragrafo use """ no c0meço e no fim da frase

# print(
#     """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
#     standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make
#     a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining
#     essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
#     passages, and more recently with desktop publishing software like Aldus PageMaker including
#     versions of Lorem Ipsum."""
# )

#MANIPULANDO STRING COMO LISTAS
# dividido = frase.split()
# print(dividido)
# print(dividido[2][3])