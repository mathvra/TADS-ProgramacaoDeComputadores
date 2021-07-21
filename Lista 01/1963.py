a, b = input().split()

antes = float(a)
depois = float(b)

aumento = ((depois - antes)/antes)*100

print("{:.2f}%" .format(aumento))