from random import randint
from time import sleep

print('-'*30)
print('Seja bem vindo ao jogo do pedra, papel e tesoura!')
print('-'*30 + '\n')

print('Escolha o que você vai jogar')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
jogada_usuario = int(input('Indique aqui: '))

jogada_computador = randint(1, 3)

print('\nO resultado vem em três...')
sleep(1)
print('Dois...')
sleep(1)
print('Um...\n')
sleep(1)

if jogada_computador == jogada_usuario:
    if jogada_usuario == 1:
        jogada_usuario = 'Pedra'
    elif jogada_usuario == 2:
        jogada_usuario = 'Papel'
    else:
        jogada_usuario = 'Tesoura'

    print(f'Rapaz, o jogo deu empate! Você jogou {jogada_usuario} e eu também!')

elif (jogada_usuario == 1 and jogada_computador == 3) or (jogada_usuario == 2 and jogada_computador == 1) or (jogada_usuario == 3 and jogada_computador == 2):
    if jogada_computador == 1:
        jogada_computador = 'Pedra'
    elif jogada_computador == 2:
        jogada_computador = 'Papel'
    else:
        jogada_computador = 'Tesoura'

    if jogada_usuario == 1:
        jogada_usuario = 'Pedra'
    elif jogada_usuario == 2:
        jogada_usuario = 'Papel'
    else:
        jogada_usuario = 'Tesoura'
        
    print(f'Parabéns, você me venceu! Eu joguei {jogada_computador} e você {jogada_usuario}!')
elif (jogada_usuario == 1 and jogada_computador == 3) or (jogada_usuario == 2 and jogada_computador == 1) or (jogada_usuario == 3 and jogada_computador == 2):
    if jogada_computador == 1:
        jogada_computador = 'Pedra'
    elif jogada_computador == 2:
        jogada_computador = 'Papel'
    else:
        jogada_computador = 'Tesoura'

    if jogada_usuario == 1:
        jogada_usuario = 'Pedra'
    elif jogada_usuario == 2:
        jogada_usuario = 'Papel'
    else:
        jogada_usuario = 'Tesoura'

    print(f'Haha, dessa vez quem te venceu fui eu! Eu joguei {jogada_computador} e você {jogada_usuario}!')
else:
    print('Por favor digite uma opção válida na próxima!')