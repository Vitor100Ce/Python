peso = float(input('Digite o seu peso'))
altura = float(input('Digite a sua altura'))
imc = peso / (altura ** 2)


print(imc)
if imc < 18.5:
    print('IMC {:.2f}. ABAIXO DO PESO'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC {:.2f}. PESO IDEAL'.format(imc))
elif 25 <= imc < 30:
    print('IMC {:.2f}. SOBREPESO'.format(imc))
elif 30 <= imc < 40:
    print('IMC {:.2f}. OBESIDADE'.format(imc))
else:
    print('IMC{:.2f}. OBESIDADE MÓRBIDA'.format(imc))
