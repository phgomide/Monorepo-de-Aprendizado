nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1+nota2)/2

if media < 5:
    print(f'REPROVADO, sua média foi: {media:.2f}')
elif media < 7:
    print(f'RECUPERAÇÃO, sua média ficou: {media:.2f}')
else:
    print(f'APROVADO, sua média foi: {media:.2f}')