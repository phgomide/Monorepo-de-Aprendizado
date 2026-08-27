num = int(input('Você quer calcular o fatorial de que número? Digite: '))
fatorial = 1

print(f'Calculando {num}! = ', end='')

if num == 0:
    print('1')
elif num > 0:
    for i in range(num, 0, -1):
        if i != 1:
            print(f'{i} x ', end='')
            fatorial *= i
        else:
            print(f'{i} ', end='')
            fatorial *= i
    print(f'= {fatorial}')
else:
    print('Valores negativos não tem fatorial!')