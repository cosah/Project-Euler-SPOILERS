def reverse(halfindrome):
    drome = ""
    while halfindrome:
        drome += halfindrome[(len(halfindrome)-1)]
        halfindrome = halfindrome[:(len(halfindrome)-1)]
    return drome


def palindrome(product):
    strProduct = str(product)
    if len(strProduct) % 2 == 0:
        halfLen = int(len(strProduct) / 2) -1
        firstHalf = strProduct[:halfLen+1]
        secHalf = reverse(strProduct[halfLen+1:])
        if firstHalf == secHalf:
            return True
    else:
        halfLen = int(len(strProduct) / 2)
        firstHalf = strProduct[:halfLen + 1]
        secHalf = reverse(strProduct[halfLen + 2:])
        if firstHalf == secHalf:
            return True
    return False


biggest = 0
for foo in range(999, 1, -1):
    for bar in range(999, 1, -1):
        prod = bar * foo
        if palindrome(prod):
            print(prod)
            if bar * foo > biggest:
                biggest = bar * foo
print(biggest)
