a, b, c = map(int, input().split())

if((a-b == 0) or (a-c == 0) or (b-c == 0)):
    print('S')
elif((a+b-c == 0) or (a-b+c == 0) or (b-a-c == 0) or (b+c-a == 0) or (a-b-c == 0) or (c-a-b == 0)):
    print('S')
else:
    print('N')