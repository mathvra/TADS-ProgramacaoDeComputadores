T = int(input())

for i in range(1, T+1):
    pa,pb,g1,g2 = map(float, input().split())

    pa = int(pa)
    pb = int(pb)
    
    anos = 0
    while(pa <= pb):
        cpa = int((pa * (g1 / 100)))
        cpb = int((pb * (g2 / 100)))
        anos = anos + 1
        pa = pa + cpa
        pb = pb + cpb
        
        if(anos > 100):
            break

    if(anos>100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos." %anos)