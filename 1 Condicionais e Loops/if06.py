casa = int(input('Digite o valor da sua casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Em quantos anos você pretende pagar: '))

meses = 12*anos
prestacao = casa/meses
limite = salario*0.30

if limite >= prestacao:
    print('Empréstimo APROVADO! Valor da parcela: R$ {:.2f}, seu limite era: {}'.format(prestacao, limite))
else:
    print('Empréstimo NEGADO! A parcela de R$ {:.2f} excede 30% do seu salário (R$ {:.2f})'.format(prestacao, limite))