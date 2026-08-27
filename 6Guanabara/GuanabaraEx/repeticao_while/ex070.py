total_gasto = produtos1000 = mais_barato = 0
nome_barato = ''
contador = 1

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$'))

    if contador == 1:
        mais_barato = preco
        nome_barato = produto
    else:
        mais_barato = preco
        nome_barato = produto
    
    if preco >= 1000:
        produtos1000 += 1
    
    total_gasto += preco
    contador += 1

    opcao = ' '
    while opcao not in 'sn':
        opcao = str(input('Deseja continuar? [s/n]')).strip().lower()[0]
    
    if opcao == 'n':
        break

print(f'Total gasto: R${total_gasto:.2f}')
print(f'Produto mais barato: {nome_barato} custa: R${mais_barato:.2f} ')