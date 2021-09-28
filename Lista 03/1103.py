
def tempoDormir(H1, M1, H2, M2):
    inicial = H1 * 60 + M1
    final = H2 * 60 + M2

    if final <= inicial:
        final += 24 * 60
    print(abs(final-inicial))


while True:
    H1, M1, H2, M2 = map(int,input().split())
    if H1 == M1 == H2 == M2 == 0:
        break
    else:
        tempoDormir(H1, M1, H2, M2)
