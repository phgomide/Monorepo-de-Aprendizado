num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

menor_valor = 0
maior_valor = 0

if num1 > num2 and num1 > num3:
    maior_valor = num1
elif num2 > num1 and num2 > num3:
    maior_valor = num2
else:
    maior_valor = num3

if num1 < num2 and num1 < num3:
    menor_valor = num1
elif num2 < num1 and num2 < num3:
    menor_valor = num2
else:
    menor_valor = num3

print(f'O maior valor era {maior_valor} e o menor valor era {menor_valor}')