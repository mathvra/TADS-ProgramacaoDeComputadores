def nBits(n):
    res = 0
    if (n==0):
       return res + 1
    if (n > 1):
        res = res + 1
    return res + nBits(n//2)

print(nBits(78996))


