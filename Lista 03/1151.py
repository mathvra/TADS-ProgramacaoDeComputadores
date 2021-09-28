n = int(input())
atual = 0

if(n > 0):
    lista = [0, 1]
    for i in range (2, n):
        atual = lista[i-2] + lista[i-1]
        lista.append(atual)
    for x in range(0, len(lista)):
        if(x+1 < len(lista)):
            print('%d'%(lista[x]),end=' ')
        else:
            print('%d'%(lista[x]),end='')
    print()
else:
    lista = [0]
    print(lista)