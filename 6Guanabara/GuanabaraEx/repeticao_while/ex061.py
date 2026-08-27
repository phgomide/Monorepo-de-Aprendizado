termo1 = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = 1

while termo <= 10:
    print(f'O {termo}° termo vale: {termo1}')
    termo1 += razao
    termo += 1

print('Pronto, finalizado!')