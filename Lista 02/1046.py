hInicial, hFinal = map(int, input().split())

if hInicial == hFinal:
    tempo = 24
elif hInicial > hFinal:
    tempo = (24 - hInicial) + hFinal
elif hInicial < hFinal:
    tempo = hFinal - hInicial

print("O JOGO DUROU {} HORA(S)" .format(tempo))