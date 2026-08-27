r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))

if (r1 + r2 > r3) and (r2 + r3 > r1) and (r1 + r3 > r2):
    print(f'Podemos formar um triângulo de lados {r1}, {r2}, {r3}')
else:
    print('Não dá para formar um triângulo')

if r1 == r2 == r3:
    print('O triângulo é equilatéro!')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('O triângulo é isísceles!')
else:
    print('O triângulo é escaleno')