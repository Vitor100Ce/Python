distancia = float(input('Digite a distância da viagem'))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preco da viagem é {:.2f}'.format(preco))