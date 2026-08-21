velocidade = int(input('Digite a velocidade do carro em km/h: '))

if velocidade <= 80:
    print('Tudo bem, está dentro do permitido')
else:
    multa = (velocidade - 80) * 7
    print(f'A velocidade estava acima da média, a velocidade era: {velocidade}')
    print(f'A multa ficou em R${multa}')