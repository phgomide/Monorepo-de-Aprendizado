import random

vidaHeroi = 100
vidaMonstro = 120

pocoesHeroi = 3
curaPocao = 25

def acaoMonstro():
    global vidaHeroi
    
    if vidaMonstro <= 0:
        return('O monstro morreu! O jogo acabou!')
    else:
        ataqueMonstro = random.randint(10,25)
        vidaHeroi -= ataqueMonstro
        return f'O monstro te atacou! Ele tirou {ataqueMonstro} de dano, você só tem {vidaHeroi} de hp!'

while vidaHeroi > 0 and vidaMonstro > 0:
    print('\n' + '-'*20)
    print('[1] Ataque Básico')
    print('[2] Ataque Forte')
    print('[3] Usar Poção')
    print('-'*20)
    escolha = int(input('Digite qual ação quer fazer esse turno: '))
    
    if escolha == 1:
        ataque = random.randint(10, 20)
        vidaMonstro -= ataque
        print(f'Você usou o Ataque Básico, você tirou {ataque} de dano')
        print(f'Agora o monstro está com {vidaMonstro} de vida!')
        print(acaoMonstro())
    elif escolha == 2:
        chanceAcerto = random.randint(0, 100)
        if chanceAcerto < 30:
            print('Poxa, dessa vez você errou o ataque')
            print(acaoMonstro())
        else:
            ataque = random.randint(25, 40)
            vidaMonstro -= ataque
            print(f'Você usou o Ataque Forte e acertou! Você tirou {ataque} de dano!')
            print(f'Agora o monstro está com {vidaMonstro} de vida!')
            print(acaoMonstro())
    elif escolha == 3:
        if pocoesHeroi < 1:
            print('Você não tem mais poções!')
        else:
            if vidaHeroi + curaPocao > 100:
                print('Você não pode tomar poções, se não terá mais que 100 de vida!')
            else:
                vidaHeroi += curaPocao
                pocoesHeroi -= 1
                print(f'Você acabou de se curar com 25 pontos, agora você tem {vidaHeroi} de vida')
                print(f'Agora você só tem mais {pocoesHeroi} poções')
                print(acaoMonstro())
    else:
        print('\nDigite uma opção válida por favor!')