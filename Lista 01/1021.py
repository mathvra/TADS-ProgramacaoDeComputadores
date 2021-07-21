valor = float(input())

notas = int(valor)

n100 = notas//100
resto100 = notas%100

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

print("NOTAS:")
print("{} nota(s) de R$ 100.00" .format(n100))
print("{} nota(s) de R$ 50.00" .format(n50))
print("{} nota(s) de R$ 20.00" .format(n20))
print("{} nota(s) de R$ 10.00" .format(n10))
print("{} nota(s) de R$ 5.00" .format(n5))
print("{} nota(s) de R$ 2.00" .format(n2))

diferenca = (((valor - notas)*100)+0.001)
moedas = int(diferenca)

m100 = resto5%2

m50 = moedas//50
restom50 = moedas%50

m25 = restom50//25
restom25 = restom50%25

m10 = restom25//10
restom10 = restom25%10

m5 = restom10//5
restom5 = restom10%5

m1 = restom5//1

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00" .format(m100))
print("{} moeda(s) de R$ 0.50" .format(m50))
print("{} moeda(s) de R$ 0.25" .format(m25))
print("{} moeda(s) de R$ 0.10" .format(m10))
print("{} moeda(s) de R$ 0.05" .format(m5))
print("{} moeda(s) de R$ 0.01" .format(m1))