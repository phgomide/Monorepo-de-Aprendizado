soma = 0
qtd_nums = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    qtd_nums += 1

print(f'Você digitou {qtd_nums} números e a soma entre eles foi {soma}.')