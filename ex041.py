n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))

media = (n1 + n2) / 2

if media < 5:
    print('Sua média foi {}.REPROVADO'.format(media))
elif 7 > media >= 5:
    print('Sua média foi {} RECUPERAÇÃO'.format(media))
else:
    print('Sua media foi {}.APROVADO'.format(media))