frase = str(input('Digite uma frase qualquer: ')).strip()

print('A quantidade de A na sua frase foi: {}'.format(frase.lower().count('a')))
print('A primeira letra A aparece na posição {} da string'.format(frase.lower().find('a') + 1))
print(f'A última vez que a letra A aparece é na posição: {frase.lower().rfind('a') + 1}')