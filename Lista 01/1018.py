valor = int(input())

n100 = valor//100
resto100 = valor%100
n50 = resto100//50
resto50 = resto100%50
n20 = resto50//20
resto20 = resto50%20
n10 = resto20//10
resto10 = resto20%10
n5 = resto10//5
resto5 = resto10%5
n2 = resto5//2
resto2 = resto5%2
n1 = resto2//1

print(valor)
print(n100, "nota(s) de R$ 100,00")
print(n50, "nota(s) de R$ 50,00")
print(n20, "nota(s) de R$ 20,00")
print(n10, "nota(s) de R$ 10,00")
print(n5, "nota(s) de R$ 5,00")
print(n2, "nota(s) de R$ 2,00")
print(n1, "nota(s) de R$ 1,00")