def fat(n):
    if (n == 0 or n == 0): 
        return 1
    else:
        return n*fat(n-1)

while True:
    try:
        a, b = map(int, input().split())
        
        soma = fat(a) + fat(b)
        print(soma)
    except EOFError:
            break