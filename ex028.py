import random
import time

n_sorteado = random.randint(0,5)
n = int(input('Em que número eu pensei?'))

print('PROCESSANDO...')
time.sleep(3)

if n == n_sorteado:
    print('Parabéns, você venceu!')
else:
    print('Eu venci!')









#COPIAR DEPOIS PARA O EX 059
n1 = int(input('Digite o primeiro valor'))
n2 = int(input('Digite o segundo valor'))
menu = int(input("""
Escolha uma das opções abaixo
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

"""))