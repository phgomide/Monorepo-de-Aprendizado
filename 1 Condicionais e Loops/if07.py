preco = float(input('Digite o valor do produto: '))

print('(1) PIX | 10% de desconto')
print('(2) Cartão de Crédito | 5% de desconto')
print('(3) 2x no Cartão | Preço normal')
print('(4) 3x ou mais | 20% juros')
opcao = int(input('Digite qual opção você deseja: '))

if opcao == 1:
    precofinal = preco*0.90
    print(f'O preço com desconto de 10% será: {precofinal}')
elif opcao == 2:
    precofinal = preco*0.95
    print(f'O preço final com desconto de 5% será: {precofinal}')
elif opcao == 3:
    precoparcela = preco/2
    print(f'O preço final será {preco}, e o valor de cada parcela será: {precoparcela}')
elif opcao == 4:
    parcelas = int(input('Digite quantas parcelas você deseja: '))
    precojuros = preco*1.20
    precoparcela = (precojuros)/parcelas
    print(f'O valor total ficou: {precojuros} e cada parcela ficou: {precoparcela}')
else:
    print('Essa não é uma opção válida!')