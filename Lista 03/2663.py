n = int(input())
k = int(input())
competidor = []

for i in range(n):
    competidor.append(int(input()))

competidor.sort(reverse=True)
total = k
while total < n and competidor[total] == competidor[k-1]:
    total += 1

print(total)