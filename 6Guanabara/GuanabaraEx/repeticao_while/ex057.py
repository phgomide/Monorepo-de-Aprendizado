sexo = str(input('Digite o seu sexo [M/F]: ')).strip().lower()

while sexo != 'm' and sexo != 'f':
    sexo = str(input(f'Por favor, digite um sexo válido! [M/F]: ')).strip().lower()

if sexo == 'f':
    print(f'Cadastrei o seu sexo! Seu sexo é feminino!')
if sexo == 'm':
    print(f'Cadastrei o seu sexo! Seu sexo é masculino!')