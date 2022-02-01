#Programa para ler o nome, idade e sexo de 04 pessoas. No final mostrar: média de idade; Qual é o homem mais velho; Quantas mulheres com menos de 20 anos.

lst_idade = []
lst_homem = []
lst_homem_idade = []
tot_mulheres_20 = 0

for cont in range(1,5):
    nome = input('Digite o nome da {}° pessoa'.format(cont)).strip()
    idade = int(input('Digite a idade da pessoa'))
    lst_idade = lst_idade + [idade]
    sexo = input('Digite o sexo [M/F]').upper().strip()
    if sexo == 'M':
        lst_homem = lst_homem + [nome]
        lst_homem_idade = lst_homem_idade + [idade]
    elif idade < 20 and sexo == 'F':
        tot_mulheres_20 += 1

# A média da idade
soma_idade = sum(lst_idade)
media_idade = soma_idade / cont
print('A média de idade do grupo é de {}'.format(media_idade))

#Homem mais velho
maior_idade_homem = max(lst_homem_idade)
index = lst_homem_idade.index(maior_idade_homem)
print('O homem mais velho se chama {} e tem {} anos'.format(lst_homem[index], maior_idade_homem))

#Qtd mulheres com menos de 20 anos
print('Ao todo são {} mulheres com menos de 20 anos'.format(tot_mulheres_20))




