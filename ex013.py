sal = float(input('Qual o salario do funcionario? R$ '))
novo = sal + (sal * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passara a receber R${:.2f}'.format(sal, novo))
