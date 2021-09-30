j, r = map(int,input().split())
entrada = list(map(int, input().split()))

pontos = [0] * j

for i in range(j):
    pontos[i] = sum(entrada[i::j])

pontos = pontos[::-1]
vencedor = j - pontos.index(max(pontos))
print(vencedor)