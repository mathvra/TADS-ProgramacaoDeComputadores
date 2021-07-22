a1 = int(input())
a2 = int(input())
a3 = int(input())

temp1a = (a2*2) + (a3*4)

temp2a = (a1*2) + (a3*2)

temp3a = (a1*4) + (a2*2)

if temp1a <= temp2a and temp1a <= temp3a:
    menor = temp1a
    print("temp1a")
elif temp2a <= temp1a and temp2a <= temp3a:
    menor = temp2a
    print("temp2a")
else:
    menor = temp3a
    print("temp3a")

print(menor)