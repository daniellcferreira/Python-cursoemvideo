'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''pais = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'Sâo Paulo', 'sigla': 'SP'}
pais.append(estado1)
pais.append(estado2)
print(pais[0])
print(pais[0]['uf'])'''

estado = dict()
pais = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    pais.append(estado.copy())
print(pais)
for e in pais:
    for v in e.values():
        print(v, end=' ')
    print()

