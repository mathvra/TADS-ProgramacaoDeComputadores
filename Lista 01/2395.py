a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

comprimento = x//a
largura = y//b
altura = z//c

print(comprimento*largura*altura)