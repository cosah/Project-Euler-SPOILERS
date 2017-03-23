def factor(num):
    limit = num // 2
    test = 2
    faclist = [1, num]
    while test < limit:
        if num % test == 0:
            faclist.append(test)
            faclist.append(int(num/test))
            limit = num/test
        test += 1
    return faclist


divlist = []
trinum = 1
indx = 2

while len(divlist) <= 500:
    trinum += indx
    indx += 1
    divlist = factor(trinum)

print(trinum)