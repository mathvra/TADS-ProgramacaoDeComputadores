N = int(input())
lista = {}

for i in range(1, N+1):
	v = int(input())
	if(v in lista):
		lista[v] += 1
	else:
		lista[v] = 1


chaves = lista.keys()
chaves = sorted(chaves)

for j in chaves:
	print("{} aparece {} vez(es)" .format(j,lista[j]))
