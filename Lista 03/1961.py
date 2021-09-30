P, N = map(int,input().split())

alturaCanos = list(map(int,input().split()))

win = 0

for i in range(0, N-1):
    print(P, abs((alturaCanos[i+1] - alturaCanos[i])))
    if((P >= abs((alturaCanos[i+1] - alturaCanos[i])))):
        win = win + 1

if(win == N-1):
    print("YOU WIN")
else:
    print("GAME OVER")