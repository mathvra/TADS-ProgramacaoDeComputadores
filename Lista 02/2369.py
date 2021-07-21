n = int(input())

if(n <= 10):
    preco = 7
elif(n >= 11 and n <= 30):
    preco = ((n - 10)*1) + 7
elif(n >= 31 and n <= 100):
    preco = ((n - 30)*2) + 27
elif(n >= 101):
    preco = ((n - 100)*5) + 167

print(int(preco))