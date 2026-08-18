ladoA = int(input('Digite o valor do lado A: '))
ladoB = int(input('Digite o valor do lado B: '))
ladoC = int(input('Digite o valor do lado C: '))

def verificaTriangulo(ladoA, ladoB, ladoC):
    if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
        print('Tudo certo! É possível formar um triângulo!')
        if ladoA == ladoB == ladoC:
            print('Tipo: Triângulo Equilátero (3 lados iguais)')
        elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
            print('Tipo: Triângulo Isósceles (2 lados iguais)')
        else:
            print('Tipo: Triângulo Escaleno (todos os lados diferentes)')
            
    else:
        return print("Não é possível formar um triângulo com esses lados!")

verificaTriangulo(ladoA, ladoB, ladoC)