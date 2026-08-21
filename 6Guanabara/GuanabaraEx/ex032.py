ano = int(input('Digite um ano qualquer e eu direi se é bissexto ou não: '))

if ano % 4 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')