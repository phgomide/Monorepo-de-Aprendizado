a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

soma = a + b
sub = a - b
mul = a * b
div = a / b
pot = a**b
divint = a//b
resto = a%b

print("A soma de {} + {} = {},".format(a, b, soma), end=' ')
print("a subtracao de {} - {} = {}".format(a, b, sub), end=' ')
print("a multiplicacao de {} * {} = {}".format(a, b, mul))
print("A divisao de {} / {} = {:.3f}".format(a, b, div), end=' ')
print("a potencia de {} ** {} = {}".format(a, b, pot), end=' ')
print("a divisao inteira de {} // {} = {}".format(a, b, divint), end=' ')
print("e o resto da divisao de {} % {} = {}".format(a, b, resto))