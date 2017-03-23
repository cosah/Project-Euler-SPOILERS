def findIt():
    for a in range(1, 500):
        for b in range(1, 500):
            for c in range(998, 1, -1):
                if ((c*c) == (a*a) + (b*b)) and (1000 == a + b + c):
                    print(a, " ", b, " ", c)
                    return a*b*c

print(findIt())