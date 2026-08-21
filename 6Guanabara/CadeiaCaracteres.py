frase = 'Curso em Vídeo Python'

print(frase[9])
print(frase[9:13])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(len(frase[5:]))
print(len(frase))

print(frase.count('o')) #Quantos 'o' tem?
print(frase.count('O')) #Como não tem 'O' ele retorna 0
print(frase.upper().count('O')) # Aqui eu estou colocando tudo de frase no upper e depois contando!
print(frase.replace('Curso', 'Viado'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.find('Android'))
print(frase.find('Vídeo'))
print(frase.split())
print('ibirichibi'.join(frase.split()))

print('Curso' in frase)
print('Curso' in frase.replace('Curso', 'Doidao'))

dividido = frase.split()
print(dividido[2])
print(dividido[3].upper())
print(dividido[0][::2])