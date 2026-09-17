numero = int(input('Digite um numero: '))
tabuada = 0
for multiplicador in range(1, 11):
    tabuada = numero * multiplicador
    print('{} x {} = {}'.format(numero, multiplicador, tabuada))