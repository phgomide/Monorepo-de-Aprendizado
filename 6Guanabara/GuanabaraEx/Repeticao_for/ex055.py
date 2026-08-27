# Maior e Menor peso lidos

maior_peso = 0
menor_peso = 0

for i in range(1, 6):
    peso_atual = int(input(f'Peso da {i}° pessoa: '))
    if i == 1:
        maior_peso = peso_atual
        menor_peso = peso_atual
    else:
        if peso_atual > maior_peso:
            maior_peso = peso_atual
        if peso_atual < menor_peso:
            menor_peso = peso_atual

print(f'O maior peso lido foi: {maior_peso}kg')
print(f'O menor peso lido foi: {menor_peso}kg')