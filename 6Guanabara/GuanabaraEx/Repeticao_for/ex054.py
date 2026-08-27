# Verificar maior idade de 7 pessoas

maiores_idade = 0
menores_idade = 0

for i in range(1, 8):
    nascimento = int(input(f'Em que ano a pessoa {i}° nasceu? '))
    idade = 2026 - nascimento
    
    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

print(f'Ao todo tivemos {maiores_idade} pessoas maiores de idade')
print(f'E também tivemos {menores_idade} pessoas menores de idade')