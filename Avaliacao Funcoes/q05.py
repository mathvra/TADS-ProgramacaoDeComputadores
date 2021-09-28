def f(n,d):
    if (n==0):
        return 0
    res = 0
    if (n%10==d):
        res = res+1
    print(res)
    print(n//10)
    print("-----------")
    return res + f(n//10,d)

print(f(326172837830, 0))