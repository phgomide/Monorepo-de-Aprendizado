menu = 0

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

while menu != 5:

    print('\n' + '='*30)
    print('Digite qual opção você quer!')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Encerrar')
    menu = int(input('Digite aqui: '))
    print('='*30)

    if menu == 1:
        
        print(f'A soma entre os dois valores é: {num1 + num2}')
    elif menu == 2:
        print(f'A multiplicação dos dois número é: {num1 * num2}')
    elif menu == 3:
        if num1 > num2:
            print(f'O maior número entre os digitados é: {num1}')
        elif num2 > num1:
            print(f'O maior número entre os digitados é: {num2}')
    elif menu == 4:
        num1 = int(input('Digite o novo número 1: '))
        num2 = int(input('Digite o novo número 2: '))
    elif menu == 5:
        break
    else:
        print('Digite uma opção válida!')
    
print('Programa finalizado! Obrigado por usar!')