largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
latas = area/2

print('Com largura: {} e altura: {}, sua area total vale: {}'.format(largura, altura, area))
print('Voce precisará de {} latas para pintar toda a parede'.format(latas))