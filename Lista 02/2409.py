a, b, c = map(int, input().split())

h, l = map(int, input().split())

if(l >= b and h >= a):
    print("S")
elif(l >= a and h >= b):
    print("S")
elif(l >= c and h >= a):
    print("S")
elif(l >= b and h >= c):
    print("S")
elif(l >= a and h >= c):
    print("S")
elif(l >= c and h >= b):
    print("S")
else:
    print("N")