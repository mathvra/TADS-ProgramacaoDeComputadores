numero = int(input())

def tabuada(numero):
    for x in range(1, 11):
        print("{} x {} = {}".format(x, numero,  numero*x))

tabuada(numero)