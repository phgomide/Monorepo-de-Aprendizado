nome = input('Digite seu nome completo: ')

print(f'Seu nome completo com todas as letras maiúsculas: {nome.upper()}')
print(f'Seu nome completo com todas as letras minusculas: {nome.lower()}')
print(f'O total de caracteres do seu nome sem espaços: {len(''.join(nome.split()))}')
print(f'O total de caracteres do seu nome é: {len(nome)}')

primeironome = nome.split()

print(f'Seu primeiro nome é: {primeironome[0]}')