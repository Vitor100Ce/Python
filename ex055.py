""" Leia o peso de cinco de pessoas e mostre o maior e menor """

for c in range(1,6):
    peso = float(input('Digite o pessoa da {}° pessoa'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
    


""" Abaixo um jeito mais simples de fazer esse exercício """

""" lst=[]  #lista vazia
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lst += [peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lst))  #maximo valor da lista
print('O Menor peso foi:', min(lst))  #minimo valor da lista """