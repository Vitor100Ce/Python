#Tuplas - São imutavéis  

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) #Mostra em ordem alfabética 

print(lanche[2]) #Mostrar o item especifíco de acorco com a posição escolhida

a = (3, 8, 7)
b = (8, 6, 8)
c = a + b
print(c)
print(c.count(8)) #Conta quantas vezes apareceu um determinado valor
print(c.index(8))