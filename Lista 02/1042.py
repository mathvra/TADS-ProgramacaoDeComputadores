n1, n2, n3 = map(int, input().split())

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

if menor == n1 and maior == n2:
    medio = n3
elif menor == n2 and maior == n1:
    medio = n3
elif menor == n1 and maior == n3:
    medio = n2
elif menor == n3 and maior == n1:
    medio = n2
elif menor == n2 and maior == n3:
    medio = n1
elif menor == n3 and maior == n2:
    medio = n1

print(menor)
print(medio)
print(maior)

print("")

print(n1)
print(n2)
print(n3)