#Mostrar cinco números sorteados em um tuplas. Depois mostrar o menor e o maior número sorteado

from random import randint

sorteado = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(sorteado)
print(f'O maior número sorteado foi {max(sorteado)}')
print(f'O menor número sorteado foi {min(sorteado)}')