import math

a,b,c,d = map(int,input().split())

x = math.gcd(b,d)

mmc = (b*d)//x

w = (mmc*a)//b 
y = (mmc*c)//d
p = w+y 
q = math.gcd(mmc,p)

pq = p//q
mmcq = mmc//q

print(pq, mmcq)