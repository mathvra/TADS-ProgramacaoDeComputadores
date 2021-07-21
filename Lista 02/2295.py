a, g, Ra, Rg = map(float, input().split())

mediaA = Ra/a

mediaG = Rg/g

if(mediaA > mediaG):
    print('A')
elif(mediaG >= mediaA):
    print('G')