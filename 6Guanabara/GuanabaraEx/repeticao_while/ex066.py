qtd_nums = 0
s = 0

while True:
    num = int(input(f'Digite um número [999 para sair]: '))
    if num == 999:
        break
    qtd_nums += 1
    s += num

print(f'A soma dos números digitados é: {s}')
print(f'Você digitou {qtd_nums} números!')