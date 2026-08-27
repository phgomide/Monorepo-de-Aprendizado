ano = int(input('Digite o ano que você nasceu: '))
idade = 2026 - ano

if idade < 9:
    print('ATLETA MIRIM')
elif idade < 14:
    print('ATLETA INFANTIL')
elif idade < 19:
    print('ATLETA JÚNIOR')
elif idade < 20:
    print('ATLETA SÊNIOR')
else:
    print('ATLETA MASTER')