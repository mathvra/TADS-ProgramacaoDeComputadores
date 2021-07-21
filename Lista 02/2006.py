T = int(input())

A, B, C, D, E = map(int, input().split())

contador = 0

if A == T:
    contador = contador + 1
if B == T:
    contador = contador + 1
if C == T:
    contador = contador + 1
if D == T:
    contador = contador + 1
if E == T:
    contador = contador + 1

print(contador)