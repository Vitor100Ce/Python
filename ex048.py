
soma = 0
multiplos = 0

for cont in range(1, 501, 2):
        if cont % 3 == 0:
            multiplos = multiplos + 1
            soma += cont
print('Soma dos {} valores é {}'.format(multiplos,soma))


          