opcao = ''
soma = 0
total_num = 0
maior = 0
menor = 1

while opcao != 'n':
    numAtual = int(input('Digite um número: '))
    if total_num == 0:
        maior = numAtual
        menor = numAtual

    soma += numAtual
    total_num += 1

    if numAtual > maior:
        maior = numAtual
    
    opcao = str(input('Deseja continuar? [S/N]')).strip().lower()

media = soma/total_num
print(f'Você digitou {total_num} número, a média deles é {media}')
print(f'O maior valor dentre todos os digitados é: {maior} e o menor é: {menor}')