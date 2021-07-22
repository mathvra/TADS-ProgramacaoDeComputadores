x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

if(a <= x):
    diferenca1 = 0
else:
    diferenca1 = a - x

if(b <= y):
    diferenca2 = 0
else:
    diferenca2 = b - y

if(c <= z):
    diferenca3 = 0
else:
    diferenca3 = c - z

print(diferenca1 + diferenca2 + diferenca3)