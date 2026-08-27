from time import sleep

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quantos anos você irá pagar? '))

prestacao = valor_casa / (anos*12)

print('PROCESSANDO...')
sleep(2)

print(f'A prestação mensal ficou no valor: R${prestacao:.2f} e 30% do seu salário é: R${(salario*0.3):.2f}')
if prestacao/salario <= 0.30:
    print('Parábens, empréstimo para sua casa está aprovada!')
else:
    print('Não temos condição de aprovar o empréstimo')