import math

co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjacente: '))

hipotenusa1 = math.sqrt((co**2) + (ca**2))
hipotenusa2 = math.hypot(co, ca)
hipotenusa3 = (co*co + ca*ca)**(1/2)

print('O valor da hipotenusa desse triangulo será igual a: {:.4f}'.format(hipotenusa1))
print('O valor da hipotenusa desse triangulo será igual a: {:.4f}'.format(hipotenusa2))
print('O valor da hipotenusa desse triangulo será igual a: {:.4f}'.format(hipotenusa3))