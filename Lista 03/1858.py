N = int(input())
X = list(map(int,input().split()))

minimum = min(X)
result = X.index(minimum) + 1

print(result)