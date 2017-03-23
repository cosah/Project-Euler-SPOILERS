def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True

primeCount = 1
primeNum = 1
while primeCount < 10001:
    primeNum += 2
    if isPrime2(primeNum):
        primeCount += 1

print(primeNum)