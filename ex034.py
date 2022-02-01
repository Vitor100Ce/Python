salario = float(input('Digite o seu salário'))

if salario <= 1250:
    aumento = salario + (salario * 15/100)
else:
    aumento = salario + (salario * 10/100)

print('O seu salário anterior era {} e aumentou para {}'.format(salario,aumento))