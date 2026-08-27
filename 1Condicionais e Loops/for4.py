somatorio = 0

final = int(input('Por favor, digite quantos termos terá seu somatório: '))

for i in range(0, final):
    s = int(input(f'Digite o termo {i + 1}: '))
    somatorio += s

print(f'O resultado do somatório é: {somatorio}')