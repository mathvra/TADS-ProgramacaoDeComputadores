while True:
    try:
        L = int(input())
        x = list(map(int,input().split()))
        Nivel = 0
        x.sort()
        if (int(x[L-1]) < 10):
            Nivel = 1
        elif (int(x[L-1]) >= 10) and (int(x[L-1]) < 20):
            Nivel = 2
        else:
            Nivel = 3
        print(Nivel)

    except EOFError:
        break