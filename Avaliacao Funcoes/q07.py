def ordenado(lista):
    tamanho = len(lista) #Tamaho da lista

    if(tamanho == 0):
        return True

    penultElement = lista[tamanho - 2] #Pega o penúltimo elemento
    ultimoElement = lista[tamanho - 1] #Pega o último elemento

    sl = lista[:-1] #Retira o último elemento
    res = ordenado(sl) #Passa o resultado pra res e chama a função recursivamente

    if(penultElement > ultimoElement): #Verifica se não está ordenado
        return False
    return res

lista = [1, 2, 3, 4, 5, 8, 2, 4]
s = ordenado(lista)
print(s)