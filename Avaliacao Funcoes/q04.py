def somaPares(lista):
    print(lista)
    if len(lista) == 1: #Quando a lista chega à 1 ou tem apenas 1 elemento
        if(lista[0]%2==0):
            return lista[0]
        else:
            return 0
    elif(lista[0]%2==0): #Verificação pros demais elementos, se são pares
        return lista[0]+somaPares(lista[1:])
    else: #Se não for par, continua a recursividade
        return somaPares(lista[1:])


lista = [1, 2, 3, 4, 5, 8, 2, 4]
pares = somaPares(lista)
print (pares)