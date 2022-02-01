#Sorteador de número com while

from random import randint

computador = randint(0,10)
n = int(input('Pensei em um número entre 0 e 10. Você consegue adivinhar qual foi?'))

cont = 0
while n != computador:
    if n < computador:
       n = int(input('Mais...Tente mais uma vez'))
       cont += 1
    else:
       n = int(input('Menos..tente mais uma vez'))
       cont += 1 
print('Você acertou com {} tentativas. Parabéns, o número sorteado foi {}'.format(cont,computador))

