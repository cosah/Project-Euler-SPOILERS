def even(n):
    return n/2


def odd(n):
    return (3 * n) + 1

bigChain = 0
for i in range(999999, 1, -1):
    index = i
    chain = 1
    while i > 1:
        chain += 1
        if 0 == i % 2:
            i = int(even(i))
        else:
            i = odd(i)
    if chain > bigChain:
        bigChain = chain
        answer = index

print(bigChain, ", ", answer)