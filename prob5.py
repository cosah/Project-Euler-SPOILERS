num = 2520
go = True


def whileEven(val):
    for div in range(20, 3, -1):
        if val % div != 0:
            return True
    return False

while go:
    num += 20
    go = whileEven(num)

print(num)
