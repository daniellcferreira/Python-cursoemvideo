lista = list()
for c in range(0, 5):
    n = int(input('Digie um valor: '))
    if c == 0:
        lista.append(n)
    elif n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final de lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitado em ordem foram {lista}')
