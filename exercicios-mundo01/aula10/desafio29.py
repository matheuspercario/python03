print('------------ ATENÇÃO ------------')
print('Limite de velocidade: 80KM/h')
print('---------------------------------')
print('\n')
lim = float(80.0)
v = float(input('Informe a velocidade do carro: '))
if v > lim:
    m = float(7.0)
    print('Valor da multa: R${:.2f}'.format((v - lim) * m))
print('Boa viagem! Dirija com segurança...')