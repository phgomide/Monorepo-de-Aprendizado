notas100 = 10
notas50 = 10
notas20 = 10
notas10 = 20
notas5 = 20

saldoAtual = 2000
opcao = 0

while opcao != 3:
    print('\n' + '='*30)
    print('[1] Sacar')
    print('[2] Ver Saldo do Caixa')
    print('[3] Encerrar')
    print('='*30)
    opcao = int(input('Digite a opção desejada: '))
    
    if opcao == 1:
        saque = int(input('Digite o valor que você deseja sacar: R$ '))
        
        if saque <= 0:
            print('Erro: Digite um valor maior que zero.')
        elif saque > saldoAtual:
            print('Erro: O caixa não possui saldo total suficiente.')
        else:
            # Variável auxiliar para ir descontando sem perder o valor original do saque
            restante = saque
            
            # --- NOTAS DE 100 ---
            preciso = restante // 100
            if preciso <= notas100:
                entregar_100 = preciso
            else:
                entregar_100 = notas100
            restante -= entregar_100 * 100

            # --- NOTAS DE 50 ---
            preciso = restante // 50
            if preciso <= notas50:
                entregar_50 = preciso
            else:
                entregar_50 = notas50
            restante -= entregar_50 * 50

            # --- NOTAS DE 20 ---
            preciso = restante // 20
            if preciso <= notas20:
                entregar_20 = preciso
            else:
                entregar_20 = notas20
            restante -= entregar_20 * 20

            # --- NOTAS DE 10 ---
            preciso = restante // 10
            if preciso <= notas10:
                entregar_10 = preciso
            else:
                entregar_10 = notas10
            restante -= entregar_10 * 10

            # --- NOTAS DE 5 ---
            preciso = restante // 5
            if preciso <= notas5:
                entregar_5 = preciso
            else:
                entregar_5 = notas5
            restante -= entregar_5 * 5

            # --- VERIFICAÇÃO FINAL ---
            if restante == 0:
                # 1. Atualiza o estoque real de notas
                notas100 -= entregar_100
                notas50 -= entregar_50
                notas20 -= entregar_20
                notas10 -= entregar_10
                notas5 -= entregar_5
                
                # 2. Atualiza o saldo geral
                saldoAtual -= saque
                
                print('\nSaque realizado com sucesso! Cédulas entregues:')
                if entregar_100 > 0:
                    print(f'-> {entregar_100} nota(s) de R$ 100')
                if entregar_50 > 0:
                    print(f'-> {entregar_50} nota(s) de R$ 50')
                if entregar_20 > 0:
                    print(f'-> {entregar_20} nota(s) de R$ 20')
                if entregar_10 > 0:
                    print(f'-> {entregar_10} nota(s) de R$ 10')
                if entregar_5 > 0:
                    print(f'-> {entregar_5} nota(s) de R$ 5')
            else:
                print('Erro: O caixa não possui cédulas suficientes para formar esse valor exato!')
                print('Operação cancelada.')

    elif opcao == 2:
        print(f'\nSaldo total disponível: R$ {saldoAtual}')
        print('Estoque de notas:')
        print(f'R$ 100: {notas100} | R$ 50: {notas50} | R$ 20: {notas20} | R$ 10: {notas10} | R$ 5: {notas5}')
        
    elif opcao == 3:
        print('Sistema finalizado. Obrigado!')
        
    else:
        print('Por gentileza, digite uma opção válida!')