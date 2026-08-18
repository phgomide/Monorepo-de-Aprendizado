num = float(input('Digite um valor: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print('O numero digitado foi {}, o seu dobro eh {}'.format(num, dobro), end=' ')
print('o seu triplo eh {}, e sua raiz eh {:.3f}'.format(triplo, raiz))

print('-'*30)

print('O numero digitado foi {}, o seu dobro eh {}'.format(num, num*2), end=' ')
print('o seu triplo eh {}, e sua raiz eh {:.3f}'.format(num*3, num ** (1/2)))