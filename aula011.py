print('\033[4;30;45mOlá mundo!\033[m')

nome = 'Ferreira'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{} !!!'.format(cores['pretoebranco'], nome, cores['limpa']))