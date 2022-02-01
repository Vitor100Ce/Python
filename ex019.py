import random
nome1 = input('Digite o nome do aluno')
nome2 = input('Digite o nome do aluno')
nome3 = input('Digite o nome do aluno')
lista = [nome1,nome2,nome3]
sorteado = random.choice(lista)

print('O aluno sorteado foi {}'.format(sorteado))
