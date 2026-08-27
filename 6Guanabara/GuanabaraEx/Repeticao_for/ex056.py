homem_velho = ''
idade_mais_velho = 0

soma_idades = 0

mulheres_jovens = 0

for i in range(1,5):
    print(f'---- {i}° Pessoa ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma_idades += idade

    if sexo == 'M':
        if idade_mais_velho < idade:
            idade_mais_velho = idade
            homem_velho = nome
    elif sexo == 'F':
        if idade < 20:
            mulheres_jovens += 1

media_idades = soma_idades/4

print(f'Média da idade do grupo é: {media_idades}')
print(f'O homem mais velho tem {idade_mais_velho} e se chama {homem_velho}')
print(f'Ao todo são {mulheres_jovens} mulheres com menos de 20 anos!')