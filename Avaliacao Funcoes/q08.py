def f(x,y):
    if (x>=y):
        print((x+y)/2)
        return (x+y)/2
    else:
        print(x+2,y-1)
        print(x+1,y-2)
        print('-------')
        return f(f(x+2,y-1),f(x+1,y-2))

print(f(13,20))