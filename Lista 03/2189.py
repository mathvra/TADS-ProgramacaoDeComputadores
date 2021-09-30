teste = 1
while True:
    n = int(input())

    if n == 0:
        break

    participantes = list(map(int,input().split()))
    vencedor = [participantes[x] for x in range(n) if participantes[x] == (x + 1)]

    print('Teste {}' .format(teste))
    teste = teste + 1
    print(vencedor[0])
    print()