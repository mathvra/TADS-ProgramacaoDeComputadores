xm, ym, xr, yr = map(int, input().split())

distanciaX = xr - xm 
distanciaY = yr - ym

if(distanciaX < 0):
    distanciaX = distanciaX*(-1)

if(distanciaY < 0):
    distanciaY = distanciaY*(-1)

distanciaTotal = distanciaX + distanciaY

print(distanciaTotal)