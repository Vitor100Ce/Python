nome = str(input('Digite seu nome completo')).strip()
separa = nome.split()
print('Seu primeiro nome {}'.format(separa[0]))
print('Seu último nome {}'.format(separa[-1]))