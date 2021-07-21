l, d = map(int, input().split())
k, p = map(int, input().split())

nPedagios = l//d

valorPedagio = nPedagios * p
desgaste = k*l

print(valorPedagio + desgaste)