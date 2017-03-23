def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True

facOne = 3
bigPrime = 0
while facOne < int(600851475143/3):
    if 600851475143%facOne is 0:
        if isPrime2(facOne):
            bigPrime = facOne
            print(bigPrime , " " , bigPrime)
        facOne += facOne
        print(facOne)
    facOne += 1
print(bigPrime)
