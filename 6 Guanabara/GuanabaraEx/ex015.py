dias = int(input('Quantos dias voce ficou com o carro alugado? '))
km = float(input('Digite quantos km foram rodados: '))

pagar = (60*dias) + (0.15*km)

print('O valor que deve ser pago será: {}'.format(pagar))