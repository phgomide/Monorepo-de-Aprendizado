kg = float(input('Digite seu peso em kg: '))
m = float(input('Digite sua altura em metros: '))

imc = kg/(m**2)

if imc < 18.5:
    print('Abaixo do Peso!')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')