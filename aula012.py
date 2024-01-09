nome = str(input('Qual é seu nome? '))
if nome == 'Daniel':
    print('Que nome bonito!')
elif nome == 'Pedro' or name == 'Maria' or nome =='Paulo':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))