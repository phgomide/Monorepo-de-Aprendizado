# Soma de todos os números ímpares e múltiplos de 3 entre 1 até 500!

somatorio = 0

for i in range(1, 501):
    if i % 3 == 0:
        if i % 2 == 1:
            somatorio += i

print(f'O somatório é: {somatorio}')