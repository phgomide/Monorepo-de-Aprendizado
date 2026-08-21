nome = input('Digite seu nome ao lado: ')

nomes_separados = nome.split()

print(f'Seu primeiro nome é: {nomes_separados[0]}')
print(f'Seu último nome é: {nomes_separados[len(nomes_separados) - 1]}')