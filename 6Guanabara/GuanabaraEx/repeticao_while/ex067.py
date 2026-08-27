num = 0
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    else:
        print(f'{'Tabuada':*^20}')
        for i in range(1, 11):
            print(f'{num} x {i} = {num*i}')
        print('*'*20)

print('Finalizado papai!')