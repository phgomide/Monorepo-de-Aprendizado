cidade = str(input('Digite o nome da cidade: ')).strip()
primeironome = cidade.upper().split()

if primeironome[0] == 'SANTO':
    print('A cidade digitada começa com Santo!')
else:
    print('A cidade digitada não começa com Santo!')