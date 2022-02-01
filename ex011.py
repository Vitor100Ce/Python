# cada dois metros quadrados da parede precisam de 1lt de tinta para ser pintado

altura = float(input('Digite a altura da parede'))
largura = float(input('Digite a largura da parede'))

area = altura * largura
tinta = area / 2

print('A aréa da parede é {}, e será necessário {} l para pintá-la'.format(area,tinta))
