import math
angulo = int(input('Digite o valor do seu angulo: '))
radianos = math.radians(angulo)

print('O seno do angulo {} vale: {:.3f}'.format(angulo, math.sin(radianos)))
print('O cosseno do angulo {} vale: {:.3f}'.format(angulo, math.cos(radianos)))
print('A tangente do angulo {} vale: {:.3f}'.format(angulo, math.tan(radianos)))