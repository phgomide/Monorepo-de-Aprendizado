homensComMais30NaoTreinam = 0
mulheresComMenos25Treinam = 0

idadeMaisVelha = 0

qtdPessoas = 1
idades = 0
mediaIdades = 0

escolha = ''

while True:
    while True:
        idade = int(input('Digite a idade da pessoa: '))
        if idade <= 0:
            print('Digite uma idade válida')
        else:
            break
    while True:
        sexo = input('Digite o sexo da pessoa: [M/F]')
        if sexo != 'M' or sexo != 'F':
            print('Digite um sexo válido!')
        else:
            break
    while True:
        atividadeFisica = input('Pratica atividade física? [s/n]')
        if atividadeFisica != 's' or atividadeFisica != 'n':
            print('Digite uma opção válida!')
        else:
            break
    
    idades += idade
    
    if idade > idadeMaisVelha:
        idadeMaisVelha = idade
    
    if sexo == 'M' and idade > 30 and atividadeFisica == 'n':
        homensComMais30NaoTreinam += 1
    
    if sexo == 'F' and idade < 25 and atividadeFisica == 's':
        mulheresComMenos25Treinam += 1
    
    mediaIdades = idades/qtdPessoas
    
    qtdPessoas += 1
    
    escolha = input('Você deseja continuar? [s/n]')
    if escolha == 'n':
        break

print(f'A idade da pessoa mais velha é: {idadeMaisVelha}')
print(f'O total de homens com mais de 30 anos que não praticam atividade física é: {homensComMais30NaoTreinam}')
print(f'O total de mulheres com menos de 25 anos que praticam atividade física é: {mulheresComMenos25Treinam}')
print(f'A média das idades de todas as pessoas é: {mediaIdades}')