#Progressão aritmética com 10 termos utilizando while

primeiro = int(input('Digite o termo'))
raz = int(input('Digite a razão'))
termo = primeiro
cont = 1

while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo = termo + raz
    cont += 1


