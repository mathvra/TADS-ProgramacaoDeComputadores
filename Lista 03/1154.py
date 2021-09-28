x = 0
soma = 0
qtd = 0

while True:
    x = int(input())
    if(x>=0):
        qtd = qtd + 1
        soma = soma + x
    else: 
        break

media = soma / qtd
print('{:.2f}'.format(media))