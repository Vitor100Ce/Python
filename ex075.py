
n = (int(input('Digite um número')), int(input('Digite outro número')), int(input('Digite mais um número')), int(input('Digite o último número')))

print(f'Os valores digitados foram {n}')
print(f'O número 9 foi digitado {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro numero 3 apareceu na posição {n.index(3)}')
else:
    print('O valor 3 não foi digitado')

print('Os valores pares digitados foram', end=' ')
for c in n:
    if c % 2 == 0:
        print(c, end= ' ')
