""" Leia a data de nascimento de sete pessoas e mostre se elas são maiores ou menores de idade """ 

from datetime import date

tot_menor = 0
tot_maior = 0

for c in range(0,7):
    ano = int(input('Digite seu ano de nascimento'))
    idade = date.today().year - ano
    if idade < 18:
        tot_menor += 1
    else:
        tot_maior += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(tot_maior))
print('Ao todo tivemos {} pessoas menores de idade'.format(tot_menor))