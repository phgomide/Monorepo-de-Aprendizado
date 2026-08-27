final = int(input('Até que número você quer detectar múltiplos: '))
multiplos_de3 = 0
soma = 0

for i in range(1, final+1):
    if i % 3 == 0:
        if i % 2 == 1:
            print(f'\033[32m{i}\033[m', end=' ')
            multiplos_de3 += 1
            soma += i
    else:
        print(f'\033[m{i}\033[m', end=' ')

print(f'\nSoma total dos valores: {soma}')