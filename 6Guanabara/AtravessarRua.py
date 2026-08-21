direita = input('Está vindo carro pela direita? (sim/nao): ')
esquerda = input('Está vindo carro pela esquerda? (sim/nao): ')

vemCarroDireita = (direita == 'sim')
vemCarroEsquerda = (esquerda == 'sim')

if vemCarroDireita and vemCarroEsquerda:
    print('Tem carro vindo na direita e esquerda, não da para atravessar')
    
elif vemCarroEsquerda:
    print('Nao posso atravessar, vem carro da esquerda')
    
elif vemCarroDireita:
    print('nao posso atravessar vem carro da direita')
else:
    print('Atravessando!')