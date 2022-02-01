preco = float(input('Digite o valor do produto'))
opcao = int(input('''Qual será a forma de pagamento
[1] à vista no dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão'''))

if opcao == 1:
    desconto = preco - (preco * 10/100)
    print('O valor original do produto é {:.2f}, mas com o desconto de 10% ficou {:.2f}'.format(preco,desconto))
elif opcao == 2:
    desconto = preco - (preco * 5/100)
    print('O valor original do produto é {:.2f}, mas com o desconto de 5% ficou {:.2f}'.format(preco,desconto))
elif opcao == 3:
    parcela = preco / 2
    print('O valor do produto é {:.2f}, e foi divido em duas parcelas de {:.2f} SEM JUROS'.format(preco,parcela))
elif opcao == 4:
    parcela = (preco + (preco * 20/100)) / 3
    print('O valor do produto é {:.2f}, e foi divido em três parcelas de {:.2f}, com 20% de juros'.format(preco,parcela))
else:
    print('Opção inválida para pagamento, escolha as opções de 1 a 4')