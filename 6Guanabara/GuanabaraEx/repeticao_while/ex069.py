maiores_18 = 0
total_h = 0
mulheres_menores20 = 0

while True:
    while True:
        idade = int(input('Digite uma idade: '))
        sexo = str(input('Digite o sexo [m/f]: ')).strip().lower()
        if idade > 0 and sexo in ['m', 'f']:
            break
        else:
            print('Digite dados válidos!')
    if idade >= 18:
        maiores_18 += 1
    if sexo == 'm':
        total_h += 1
    if sexo == 'f' and idade < 20:
        mulheres_menores20 += 1

    while True:
        opcao = str(input('Voce deseja continuar? [s/n]: ')).strip().lower()
        if opcao == 's':
            break
        elif opcao == 'n':
            break
        else:
            print('Digite uma opção válida!')

    if opcao == 'n':
        break

print(f'{maiores_18} são maior(es) de idade!')
print(f'{total_h} homem(ns) foram cadastrados!')
print(f'{mulheres_menores20} mulher(es) tem menos de 20 anos!')