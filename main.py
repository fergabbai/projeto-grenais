vitorias_inter = 0
vitorias_gremio = 0
empates = 0
grenais = 0

while True:
    print('Insira os gols do Inter:')
    gols_inter = int(input())
    print('Insira os gols do Gremio:')
    gols_gremio = int(input())
    grenais += 1

    if gols_inter > gols_gremio:
        vitorias_inter += 1
    elif gols_gremio > gols_inter:
        vitorias_gremio += 1
    else:
        empates += 1

    print('Novo grenal (1-sim 2-nao)')
    resposta = int(input())

    if resposta == 2:
        break

print('{} grenais'.format(grenais))
print('Inter:{}\nGremio:{}\nEmpates{}'.format(vitorias_inter, vitorias_gremio, empates))

if vitorias_inter > vitorias_gremio:
    print('Inter venceu mais')
elif vitorias_gremio > vitorias_inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
