termo1 = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = 1

qtd_termos = 10

while qtd_termos > 0:
    print(f'O {termo}° termo vale: {termo1}')

    termo1 += razao
    termo += 1
    qtd_termos -= 1

    if qtd_termos == 0:
        qtd_termos = int(input('Digite mais quantos termos quer mostrar: '))

print('Pronto, finalizado!')