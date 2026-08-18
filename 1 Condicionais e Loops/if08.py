salario = float(input('Digite o valor do seu salário: R$'))
valorreal = round(salario, 2) #Limita a duas casas decimais

if valorreal <= 2259.20:
    salariobruto = valorreal
    porcentagem = 0
    descontado = salariobruto*porcentagem
    salarioliquido = salariobruto - descontado
    
    print('Salário bruto: {:.2f}'.format(salariobruto))
    print('Porcentagem aplicada: {:.2f}'.format(porcentagem))
    print('Valor descontado do imposto: {:.2f}'.format(descontado))
    print('Salário Líquido final: {:.2f}'.format(salarioliquido))
elif 2259.20 < valorreal <= 2826.65:
    salariobruto = valorreal
    porcentagem = 0.075
    descontado = salariobruto*porcentagem
    salarioliquido = salariobruto - descontado
    
    print('Salário bruto: {:.2f}'.format(salariobruto))
    print('Porcentagem aplicada: {:.2f}'.format(porcentagem))
    print('Valor descontado do imposto: {:.2f}'.format(descontado))
    print('Salário Líquido final: {:.2f}'.format(salarioliquido))
elif 2826.65 < valorreal <= 3751.05:
    salariobruto = valorreal
    porcentagem = 0.15
    descontado = salariobruto*porcentagem
    salarioliquido = salariobruto - descontado
    
    print('Salário bruto: {:.2f}'.format(salariobruto))
    print('Porcentagem aplicada: {:.2f}'.format(porcentagem))
    print('Valor descontado do imposto: {:.2f}'.format(descontado))
    print('Salário Líquido final: {:.2f}'.format(salarioliquido))
elif 3751.05 < valorreal <= 4664.68:
    salariobruto = valorreal
    porcentagem = 0.225
    descontado = salariobruto*porcentagem
    salarioliquido = salariobruto - descontado
    
    print('Salário bruto: {:.2f}'.format(salariobruto))
    print('Porcentagem aplicada: {:.2f}'.format(porcentagem))
    print('Valor descontado do imposto: {:.2f}'.format(descontado))
    print('Salário Líquido final: {:.2f}'.format(salarioliquido))
else:
    salariobruto = valorreal
    porcentagem = 0.275
    descontado = salariobruto*porcentagem
    salarioliquido = salariobruto - descontado
    
    print('Salário bruto: {:.2f}'.format(salariobruto))
    print('Porcentagem aplicada: {:.2f}'.format(porcentagem))
    print('Valor descontado do imposto: {:.2f}'.format(descontado))
    print('Salário Líquido final: {:.2f}'.format(salarioliquido))