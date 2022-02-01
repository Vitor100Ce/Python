salario = float(input('Digite o seu salário'))
valor_casa = float(input('Qual o valor da casa?'))
anos = int(input('Em quantos anos deseja pagar?'))
parcela = valor_casa / (anos * 12) 

if parcela <= salario * 30/100:
    print('O seu salário é {}, o valor da casa é {}, cada parcela ficou {} e será pago em {} anos. Financiamento aprovado!'.format(salario,valor_casa,parcela, anos))
else:
    print('O seu salário é {}, o valor da casa é {}, cada parcela ficou {} e será pago em {} anos. Financiamento reprovado!'.format(salario,valor_casa,parcela, anos))
