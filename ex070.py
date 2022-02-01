#Estatísticas de produtos
total = 0
totmil = 0
menor = 0
cont = 0
while True:
    print('LOJA QUE TEM TUDO')
    produto = input('Nome do produto: ')
    valor = float(input('Preço: '))
    cont += 1
    if valor > 1000:
        totmil += 1
    total += valor

    if cont == 1 or valor < menor:  #Estrutura para mostrar o nome do produto mais barato e o seu valor
        menor = valor
        barato = produto
  
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar [S/N]: ').strip().upper()
    if option == 'N':
        break
    
print(f'''O total da compra foi {total:.2f}
Temos {totmil} produtos custando mais de R$1000.00
O produto mais barato foi {barato} que custou {menor:.2f}
''')