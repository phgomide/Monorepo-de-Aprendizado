from random import randint
from time import sleep

tentativas = 0

print('Vamos jogar um par ou ímpar contra o computador?')
while True:
    while True:
        jp = str(input('Você quer ser ímpar ou par? Digite [impar/par]:')).strip().lower()
        if jp == 'impar':
            jc = 'par'
            break
        elif jp == 'par':
            jc = 'impar'
            break
        else:
            print('Digite uma opção válida para jogar contra mim!')

    while True:
        print('Agora vamos jogar, vou pensar em um valor!')
        sleep(1)
        nc = randint(1, 10)
        print('Pensei, agora sua vez de pensar!')
        np = int(input('Digite qual número você vai jogar [1 a 10]: '))
        print('-'*30)

        if np > 10 or np < 0:
            print('Digite um valor válido')
        else:
            break

    resultado = np+nc
    for i in range(3, 0, -1):
        print(f'Beleza então vamos mostrar em: {i}')
        sleep(0.5)
        
    if jp == 'par' and resultado % 2 == 0 or jp == 'impar' and resultado % 2 == 1:
        print(f'Você me venceu, você jogou {np} e eu joguei {nc}, a soma era {jp}, Vamos dnv!')
        tentativas += 1
    elif jc == 'par' and resultado % 2 == 0 or jc == 'impar' and resultado % 2 == 1:
        print(f'Você perdeu! Eu pensei no número {nc} e você {np}, a soma era {jc}')
        print(f'Eu precisei de {tentativas} tentativas!')
        break

print('Programa finalizado!')