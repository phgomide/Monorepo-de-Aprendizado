# Leia 6 digitos e faça o somatório apenas dos que forem pares!

somatorio = 0

for i in range(1, 7):
    num = int(input(f'Digite o número {i}: '))
    if num % 2 == 0:
        somatorio += num

print(f'Somatório dos pares: {somatorio}')