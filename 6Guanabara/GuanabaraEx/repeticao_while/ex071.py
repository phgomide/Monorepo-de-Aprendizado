print('='* 30)
print(f'{"BANCO GOMIDE":^30}')
print('='*30)
valor = int(input('Que valor você deseja sacar? R$'))

notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0

while True:
    if valor//50 >= 1:
        valor -= 50
        notas50 += 1
    elif valor//20 >= 1:
        valor -= 20
        notas20 += 1
    elif valor//10 >= 1:
        valor -= 10
        notas10 += 1
    elif valor//1 >= 1:
        valor -=1
        notas1 += 1
    else:
        break

print(f'Total de {notas50} cédulas de R$50!')
print(f'Total de {notas20} cédulas de R$20!')
print(f'Total de {notas10} cédulas de R$10!')
print(f'Total de {notas1} cédulas de R$1!')
