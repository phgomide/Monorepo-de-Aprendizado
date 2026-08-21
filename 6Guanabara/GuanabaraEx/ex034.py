salario = float(input('Digite o valor do seu salário: R$'))

if salario > 1250:
    aumento = salario*1.10
    print(f'O novo salário com aumento é: R${aumento}')
elif salario <= 0:
    print('Digite um salário válido!')
else:
    aumento = salario*1.15
    print(f'O novo salário com aumento é: R${aumento}')