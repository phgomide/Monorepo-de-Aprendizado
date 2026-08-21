km = float(input('Digite a distância da viagem em km: '))

if km <= 200:
    valor_viagem = km*0.5
    print(f'O valor da viagem será de R${valor_viagem:.2f}')
elif km <= 0:
    print('Por favor digite uma distância válida!')
else:
    valor_viagem = km*0.45
    print(f'O valor da viagem será de R${valor_viagem:.2f}')