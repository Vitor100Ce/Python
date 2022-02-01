n1 = int(input('Digite o primero número'))
n2 = int(input('Digite o segundo número'))



if n2 < n1:
    maior = n1
    print('O primeiro valor é maior. Valor {}'.format(maior))
elif n2 > n1:
    maior = n2
    print('O segundo valor é maior. Valor {}'.format(maior))
else:
    print('Ambos números são iguais')
