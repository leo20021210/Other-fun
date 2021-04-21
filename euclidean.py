def gcd(a,b,count=0):
    c = a%b
    #count is the number of operations the algorith takes
    if c==0: return (b,count+1)
    return gcd(b,c,count+1)

#calculate two integers i1 and i2 from 1-100 such that gcd(i1, i2) takes the longest time to operate

max1=0 # store the maximum operation count
i1=0 # store the first parameter of the longest gcd
i2=0 # store the second parameter of the longest gcd
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
