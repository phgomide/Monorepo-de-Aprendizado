nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2)/2

if media >= 7:
    print('Aprovado!')
elif media < 7 and media >= 5:
    print('Recuperação')
else:
    print('Reprovado')