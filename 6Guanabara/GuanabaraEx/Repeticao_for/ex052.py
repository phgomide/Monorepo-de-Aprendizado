# Número é ou não primo?

num = int(input('Digite um número: '))
total_divisores = 0

for i in range(1, num+1):
    if num % i == 0:
        print(f'\033[33m{i}\033[m', end=' ')
        total_divisores += 1
    else:
        print(f'\033[31m{i}\033[m', end=' ')

print(f'\nO número {num} foi divisivel {total_divisores}x')

if total_divisores == 2:
    print('O número é primo!')
else:
    print('O número não é primo')

print('Fim!')