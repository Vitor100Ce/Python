""" Tabuada """

n = int(input('Digite um número'))

for cont in range(1, 11):
    result = cont * n
    print('{} x {} = {}'.format(n,cont,result))