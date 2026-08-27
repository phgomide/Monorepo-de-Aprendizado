largura = int(input('Digite a largura: '))
comprimento = int(input('Digite o comprimento: '))

for linhas in range(1, largura + 1):
    for colunas in range(1, comprimento + 1):
        if linhas == 1 or linhas == largura or colunas == 1 or colunas == comprimento:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()