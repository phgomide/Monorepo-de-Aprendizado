# Progressão aritimetica

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(1, 11):
    print('O termo da posição {} é: {}'.format(i, termo))
    termo += razao