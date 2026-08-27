from time import sleep

preco = float(input('Digite o preço do produto: '))

print('-'*30)
print('[1] Pagamento a vista (10% de desconto)')
print('[2] A vista no cartão (5% de desconto)')
print('[3] Em até 2x no cartão (Preço Normal)')
print('[4] 3x ou mais (20% de juros)')
print('-'*30)

opcao = int(input('Digite a opção de pagamento: '))

print('Processando...')
sleep(1)

if opcao == 1:
    preco_final = preco*0.9
    print(f'O valor da sua compra ficou: R${preco_final:.2f}')
elif opcao == 2:
    preco_final = preco*0.95
    print(f'O valor da sua compra ficou: R${preco_final:.2f}')
elif opcao == 3:
    preco_parcela = preco/2
    print(f'O valor da sua compra ficou: R${preco:.2f} e cada parcela: R${preco_parcela:.2f}')
elif opcao == 4:
    parcelas = int(input('Digite o valor de parcelas: '))
    if parcelas >= 3:
        preco_parcela = (preco*1.2)/parcelas
        print(f'O valor da sua compra ficou: R${(preco*1.2):.2f} e cada parcela: R${preco_parcela:.2f}')
    else:
        print('Opção de parcelas inválida!')
else:
    print('Digite uma opção válida!')