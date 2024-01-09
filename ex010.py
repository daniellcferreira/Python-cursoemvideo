real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.73
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))