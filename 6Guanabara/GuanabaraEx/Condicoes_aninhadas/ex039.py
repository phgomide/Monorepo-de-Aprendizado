from time import sleep


ano = int(input('Digite o ano que você nasceu: '))

idade = 2026 - ano

print('Processando sua idade...')
sleep(1)

if idade < 18:
    print(f'Ainda não está na hora de se alistar! Faltam {18 - idade} anos para se alistar!')
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print('Já passou da hora de se alistar!')