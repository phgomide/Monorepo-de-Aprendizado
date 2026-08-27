# Tabuada

num_tabuada = int(input('Digite o número que você quer fazer a tabuada: '))
print('{:-^20}'.format(' Tabuada '))

for i in range(0, 11):
    print('{} x {} = {}'.format(num_tabuada, i, num_tabuada*i))

print('Fim!')