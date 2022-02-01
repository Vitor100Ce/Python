""" Progressão aritmética com 10 termos """

primeiro = int(input('Digite o termo'))
raz = int(input('Digite a razão'))
decimo = primeiro + (10-1) * raz

for c in range(primeiro, decimo + raz, raz):
    print('{}'.format(c))
print('Fim')
   