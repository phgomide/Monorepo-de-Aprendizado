frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] #Essa aqui é uma forma simples e direta de fazer com fatiamento

'''inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra] '''

    # Caso queira usar o for ^^^

if inverso == junto:
    print('A frase é um palindromo!')
else:
    print('A palavra não é um palindromo!')
print(f'A frase digitada foi: {junto} e seu inverso é: {inverso}')