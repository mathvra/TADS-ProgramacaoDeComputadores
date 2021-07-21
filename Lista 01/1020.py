idade = int(input())

anos = idade // 365
restoAnos = idade%365

meses = restoAnos//30

dias = restoAnos%30

print("{} ano(s)" .format(anos))
print("{} mes(es)" .format(meses))
print("{} dia(s)" .format(dias))