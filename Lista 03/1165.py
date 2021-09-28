N = int(input())

for i in range(1, N+1):
    x = int(input())
    divisores = 0

    for j in range(1, x):
        if(x%j == 0):
            divisores = divisores + 1
    
    if(divisores<2):
        print(x,"eh primo")
    else:
        print(x,"nao eh primo")
    
