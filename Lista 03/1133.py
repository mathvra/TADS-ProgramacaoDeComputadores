X = int(input())
Y = int(input())

if(X < Y):
    for n in range(X+1,Y):
        if(n%5 == 2 or n%5 == 3):
            print(n)
elif(X > Y):
    for n in range(Y+1,X):
        if(n%5 == 2 or n%5 == 3):
            print(n)