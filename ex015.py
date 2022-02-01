
dias = int(input('Quantos dias com o carro alugado?'))
km = float(input('Quantos km rodados?'))

pagar = (dias * 60) + (km*0.15)


print('Dias alugados {}'.format(dias))
print('km rodados {}'.format(km))
print('O total a pagar é {}'.format(pagar))
