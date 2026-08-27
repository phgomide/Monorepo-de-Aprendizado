from random import randint
from time import sleep

tentativas = 0
numero_sorteado = randint(1, 10)

print('*' * 30)
print('Vamos jogar um jogo da advinha? Vou pensar em um número de 1 a 10...')
sleep(2)
print('Pronto, já pensei, sua vez agora!')
print('*' * 30)

chute = int(input('Digite qual número você acha que eu pensei: '))

while chute != numero_sorteado:
    chute = int(input(f'Parece que você errou, não era {chute}, Tenta dnv: '))
    tentativas +=1

print(f'Boa, o número que eu tinha pensado era de fato {numero_sorteado}!')
print(f'Você precisou de {tentativas} palpites para acertar!')