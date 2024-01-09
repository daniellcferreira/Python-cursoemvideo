jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na {c+1}° partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*25)
print(jogador)
print('-='*25)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print('-='*25)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')


