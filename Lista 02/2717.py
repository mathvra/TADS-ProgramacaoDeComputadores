n = int(input())

a, b = map(int, input().split())

total = a + b

if(n >= total):
    print("Farei hoje!")
else:
    print("Deixa para amanha!")