fatorial = int(input('Digite qual valor você quer calcular o fatorial: '))
resultado = 1

print(f'Fatorial de {fatorial} = {fatorial}! = ', end='')
while fatorial > 0:
    if fatorial > 1:
        print(f'{fatorial} x', end=' ')
    else:
        print(f'{fatorial} =', end=' ')
    resultado *= fatorial
    fatorial -= 1

print(f'{resultado}')