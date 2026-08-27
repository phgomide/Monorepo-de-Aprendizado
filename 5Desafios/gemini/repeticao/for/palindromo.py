frase = str(input('Digite uma frase para verificar um palindromo: ')).strip().upper()
palavras = frase.split()
frase_sanitizada = ''.join(palavras)
frase_invertida = ''

for i in range(len(frase_sanitizada) -1, -1, -1): # Aqui eu preciso faer len(frase_sanitizada) -1, pq ele contaria a posição 0 como a primeira em um len
    frase_invertida += frase_sanitizada[i]


if frase_invertida == frase_sanitizada:
    print(f"""Opa! Achamos um palíndromo, sua frase foi: {frase_sanitizada} 
e a frase ao contrário é: {frase_invertida}""")
else:
    print(f"""É, a sua frase não é um palíndromo, sua frase foi: {frase_sanitizada} e a 
frase ao contrário é: {frase_invertida}""")

print('Programa finalizado!')