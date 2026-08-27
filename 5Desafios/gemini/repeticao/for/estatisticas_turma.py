maior_nota = 0
menor_nota = 0
media_notas = 0
total_notas = 0

for i in range(1,6):
    print(f'---- NOTA {i} ----')
    nota = float(input('Digite a nota: '))

    if i == 1:
        maior_nota = nota
        menor_nota = nota
    else:
        if nota > maior_nota:
            maior_nota = nota
        elif nota < menor_nota:
            menor_nota = nota

    total_notas += nota

media_notas = total_notas/5
print(f'A média das notas foi: {media_notas:.2f}')
print(f'A maior nota dentre todas foi: {maior_nota:.2f}')
print(f'A menor nota dentre todas foi: {menor_nota:.2f}')