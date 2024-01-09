n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(n1, n2, m))
if m >= 5 and m < 7:
    print('O aluno esta em RECUPERAÇÃO!')
elif m < 5:
    print('O aluno esta REPROVADO!')
elif m >= 7:
    print('O aluno esta APROVADO!')

