tamanho = int(input('Que número será o a base da pirâmide? Digite: '))

for i in range(1, tamanho+1):
    for j in range(0, i):
        print(f'{j+1}', end=' ')
    print()