x = 1
lista = []

while x!= 0:
    x = int(input())
    for i in range(1, x+1):
        lista.append(i)
        lista[i-1] = str(lista[i-1])
        i = i + i
    lista=' '.join(lista)
    if x!= 0:      
        print(lista)
        lista =[]