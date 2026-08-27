quantidade = int(input('Digite até qual termo da sequência de Fibonacci você quer: '))

termo1 = 1
termo2 = 1
print(f'{termo1}, {termo2},', end=' ')

contador = 3
while contador <= quantidade:
    termo3 = termo1 + termo2
    print(f'{termo3},', end=' ')
    termo1 = termo2
    termo2 = termo3
    contador += 1

print('Fim!')