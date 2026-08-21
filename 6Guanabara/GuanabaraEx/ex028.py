from random import randint
from time import sleep

print('-=-'*20)
print('Vou pensar em um número, sua vez de advinhar!')
print('-=-'*20)
numero_sorteado = randint(1, 5)


chute = int(input('Digite seu chute de 1 a 5: '))
print('Processando...')
sleep(1)

if chute == numero_sorteado:
    print('Parábens, você advinhou o número corretamente!')
else:
    print(f'Não foi dessa vez, mas pode tentar de novo! O número pensado foi: {numero_sorteado}')