#Progressão aritmética v2.0 com while

primeiro = int(input('Digite um número'))
raz = int(input('Digite a razão'))
cont = 0
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(primeiro))
        primeiro += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?')) 
print('Progressão com {} temos mostrados'.format(total))



