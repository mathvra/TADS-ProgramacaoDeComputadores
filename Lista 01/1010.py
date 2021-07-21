a1, b1, c1 = input().split()
a2, b2, c2 = input().split()

codigo1 = int(a1)
nPecas1 = int(b1)
valor1 = float(c1)

codigo2 = int(a2)
nPecas2 = int(b2)
valor2 = float(c2)

print('VALOR A PAGAR: R$ {:.2f}' .format((nPecas1*valor1) + (nPecas2*valor2)))