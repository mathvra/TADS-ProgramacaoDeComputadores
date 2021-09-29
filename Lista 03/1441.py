while True:
    n = int(input())
    if n == 0:
        break
    m = 0
    while (n != 0 and ((n & (n - 1)) == 0)) != True:
        if n > m:
            m = n
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = n*3 + 1
    if n > m:
        m = n
    print(m)