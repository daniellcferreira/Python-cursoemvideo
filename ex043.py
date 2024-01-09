peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO normal')
elif imc >= 18.5 and imc < 25:
    print('PARABENS! voce esta na faixa de PESO NORMAL')
elif imc >= 25 and imc < 30:
    print('Voce esta em SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Voce esta em OBESIDADE')
else:
    print('Voce esta em OBESIDADE MORBIDA, cuidado! ')
