valorTotal = 0
produtoMais50 = 0
produtos = []
totalProdutos = 0

produtoMaisBarato = ''
menorValor = 0

formaPagamento = 0

while True:
    produto = input('Digite o produto que você está comprando: ')
    produtos.append(produto)
    totalProdutos += 1
    
    valor = float(input('Digite o valor desse produto que você quer comprar: '))
    valorTotal += valor
    
    if valor >= 50:
        produtoMais50 += 1
    
    if totalProdutos == 1 or valor < menorValor:
        produtoMaisBarato = produto
        menorValor = valor
    
    escolha = input('Você deseja continuar com a sua compra? [S/N]')
    
    if escolha == 'N':
        print('Vamos finalizar sua compra então!')
        break

print('Todos os produtos que foram comprados: {}'.format(produtos))
print('Foram comprados {} produtos ao todo!'.format(totalProdutos))
print('O valor total ficou em: R${}'.format(valorTotal))
print('O produto mais barato comprado foi: {}'.format(produtoMaisBarato))
print('Você comprou {} produtos que custam mais que R$50'.format(produtoMais50))

while True:
    print('\n' + '-'*30)
    print('Qual será a forma de pagamento?')
    print('[1] À vista no Pix | Ganha 10% de desconto')
    print('[2] Cartão em até 2x | Preço normal')
    print('[3] Cartão em 3x ou mais | Acréscimo de 15% de juros\n')
    formaPagamento = int(input('Digite a forma de pagamento:'))
    
    if formaPagamento > 0 and formaPagamento < 4:
        if formaPagamento == 1:
            valorTotal *= 0.90
            print('Valor total: R${:.2f}'.format(valorTotal))
            break
        elif formaPagamento == 2:
            valorParcela = valorTotal/2
            print('Cada parcela ficará: R${:.2f}'.format(valorParcela))
            break
        else:
            while True:
                qtdParcelas = int(input('Digite em quantas vezes você deseja parcelar: '))
                if qtdParcelas < 3:
                    print('Digite um valor de parcelas válidas!')
                else:
                    valorJuros = valorTotal * 1.15
                    valorParcela = round((valorJuros/qtdParcelas), 2)
                    print('O valor total ficou: R${:.2f} e cada parcela ficou: R${:.2f}'.format(valorJuros, valorParcela))
                    break
    else: 
        print('Por favor digite uma forma de pagamento válida!')