#Validador de dados. Validar se o sexo é masculino ou feminino

sexo = str(input('Informe o seu sexo [M/F]')).upper()

while sexo not in 'MF':
    sexo = str(input('ERROR, informe o sexo corretamente [M/F]')).upper()
print('O sexo digitado foi {}'.format(sexo))