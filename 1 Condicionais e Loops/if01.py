nascimento = int(input('Digite o ano que voce nasceu: '))
idade = 2026 - nascimento

if idade < 18:
    print('Você é menor de idade')
else:
    print('Você é maior de idade')