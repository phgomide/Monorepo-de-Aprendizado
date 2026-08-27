from time import sleep

posicao = 0
bateria = 100

for i in range(1,5):
    posicao += 2
    bateria -= 15
    
    print(f'Robô está andando! Posição atual: {posicao} Bateria: {bateria}')

    if posicao == 4 or posicao == 8:
        print('Opa, consegui um posto de recarga! Ganhei +20 de bateria!')
        print(f'Bateria atual: {bateria}')
    
    print('Descansando para mais uma rodada!\n')
    sleep(3)

print(f'Posição final é: {posicao}')
print(f'Bateria final: {bateria}')