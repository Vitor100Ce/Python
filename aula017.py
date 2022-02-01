
#Primeiro exemplo da aula de listas

num = [1,2,3,4,5]
num[2] = 8
num.append(9)
num.sort(reverse=True)
num.insert(4, 30)
if 4 in num:
    num.remove(4)
else:
    print('Não localizei o número 4')
print(num)
print(f'Essa lista tem {len(num)} itens')


#Segundo exemplo
valores = []
valores.append(2)
valores.append(7)
valores.append(9)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

#Terceiro exemplo

valores = []

for c in range(0, 5):
    valores.append(int(input('Digite um número')))
print(valores)

#Como criar uma cópia de uma lista
a = [2,5,7,8]
b = a[:] #dessa forma cria uma cópia
b[3] = 9
print(a,b)

