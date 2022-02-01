
while True:
    n = int(input('Deseja verificar a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
       result = n * c
       print(f'{n} X {c} = {result}')
print('Programa encerrado')