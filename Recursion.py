def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

print(gcd(66,20))           #Euclidean algorithm