r1 = float(input('Digite o primeiro segmento'))
r2 = float(input('Digite o segundo segmento'))
r3 = float(input('Digite o terceiro segmento'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isóceles')
    else:
        print('Escaleno')
else:
    print('Os segmentos não podem formar um triângulo')