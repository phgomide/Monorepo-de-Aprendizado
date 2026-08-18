import random
pontosJogador = 0
pontosComputador = 0
acao = 0

while True:
    if pontosComputador < 3 and pontosJogador < 3:
        print('\n' + '-'*20)
        print('[1] Pedra')
        print('[2] Papel')
        print('[3] Tesoura')
        print('[4] Sair')
        print('-'*20)
        acao = int(input('Digite qual você vai jogar: '))
        
        jogadaPC = random.randint(1,3)
        
        if acao == 1:
            if jogadaPC == 1:
                print('A jogada do computador também foi pedra! Ninguém pontuou!')
            elif jogadaPC == 2:
                print('O computador escolher papel, você perdeu essa rodada!')
                pontosComputador += 1
                print(f'Agora você tem {pontosJogador} pontos e o computador {pontosComputador}')
            else:
                print('O computador escolheu tesoura! Você vencou essa rodada!')
                pontosJogador += 1
                print(f'Agora você tem {pontosJogador} pontos e o computador {pontosComputador}')
        elif acao == 2:
            if jogadaPC == 1:
                print('O computador escolheu pedra, e você foi de papel, parabéns você pontuou!')
                pontosJogador += 1
                print(f'Agora você tem {pontosJogador} pontos e o computador {pontosComputador}')
            elif jogadaPC == 2:
                print('O computador também jogou papel, ninguém pontuou!')
            else:
                print('O computador escolheu tesoura, aqui você perdeu!')
                pontosComputador += 1
                print(f'Agora você tem {pontosJogador} pontos e o computador {pontosComputador}')
        elif acao == 3:
            if jogadaPC == 1:
                print('O computador escolheu pedra e você foi de tesoura, aqui você perdeu papai!')
                pontosComputador += 1
                print(f'Agora você tem {pontosJogador} pontos e o computador {pontosComputador}')
            elif jogadaPC == 2:
                print('O computador escolheu papel, você foi de tesoura, então você pontuou!')
                pontosJogador += 1
                print(f'Agora você tem {pontosJogador} pontos e o computador {pontosComputador}')
            else:
                print('A jogada do computador também foi tesoura! Ninguém pontuou!')
        elif acao == 4:
            break
        else:
            print('Digite um valor válido!')
    elif pontosJogador == 3:
        print('Parece que já temos um ganhador! Parabéns você fez 3 pontos e venceu o computador!')
        break
    else:
        print('Parece que você perdeu, fica para a proxima, o pc te amassou fdp kkkkkk')
        break
print('Jogo acabou, obrigado por jogar!')