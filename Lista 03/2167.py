n = int(input())
r = list(map(int,input().split()))
q = 0
    
for i in range(1, n):
    if (r[i-1] > r[i]):
        q = i + 1
        break
        
print(q)