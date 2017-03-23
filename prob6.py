smlSquare = 0
bigSquare = 0

for num in range(101):
    smlSquare += num * num
    bigSquare += num

bigSquare *= bigSquare

print(bigSquare - smlSquare)