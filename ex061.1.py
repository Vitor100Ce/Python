#Progressão aritmética

primeiro = int(input('Digite um número'))
raz = int(input('Digite a razão'))
cont = 1

while cont <= 10:
    print('{}'.format(primeiro))
    primeiro += raz
    cont += 1