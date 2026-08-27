from time import sleep

moedas = 0
posicao = 0

for i in range(0,3):
    print('Andei')
    posicao += 1
    print('Pulei')
    posicao += 2
    if posicao == 3 or posicao == 9:
        print('Opa, acabei de pegar uma moeda!')
        moedas += 1
    print(f'Pausa para descansar! Estou na posição {posicao}')
    sleep(1)
print('Andei')
posicao += 1
print(f'Peguei a maça, acabou! Cheguei na posição {posicao} e peguei {moedas} moedas')