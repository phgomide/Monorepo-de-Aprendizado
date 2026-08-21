num = int(input('Digite um número: '))

print("{:-^20}".format('Tabuada'))
for i in range(11): 
    print('{} x {} = {}'.format(num, i, num*i))