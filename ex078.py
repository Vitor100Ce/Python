
n = []
max = 0
min = 0

for c in range(0, 5):
    n.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        max = min = n[c]
    else:
        if n[c] > max:
            max = n[c]
        if n[c] < min:
            min = n[c]
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {max} na posição', end=' ')
for i, v in enumerate(n):
    if v == max:
        print(f'{i}...', end=' ')
print(f'O menor valor digitado foi {min}',end=' ')
for i, v in enumerate(n):
    if v == min:
            print(f'{i}...', end=' ')

