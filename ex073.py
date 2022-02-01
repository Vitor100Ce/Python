#Mostrar a colocação do brasileirão

time = ('Corinthias', 'Flamengo', 'Santos', 'Cruzeiro', 'Atlético', 'Goiás', 'Gama', 'Ibis', 'São Paulo', 'Botafogo', 'Piaiu', 'Maranhão', 'Avaí', 'Ponte Preta')

print(time)

print(f'Os cinco primeros colocados são {time[0:5]}')
print(f'Os quatro últimos são {time[10:14]}')
print(f'Times em ordem alfabética {sorted(time)}')
print(f'O Santos está na posição {time.index("Santos")}') 
