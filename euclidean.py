def gcd(a,b,count=0):
    c = a%b
    if c==0: return (b,count+1)
    return gcd(b,c,count+1)

max1=0
i1=0
i2=0
for i in range(100):
    for j in range(100):
        if i==0 or j==0:
            continue
        (a,b)=gcd(i,j)
        if b>max1:
            max1=b
            i1=i
            i2=j
print(max1)
print(i1)
print(i2)