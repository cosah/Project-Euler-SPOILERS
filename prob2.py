sum = 0
valOne = 1
valTwo = 2
valSwap = 0
while valTwo <= 4000000:
    if valTwo%2 is 0:
        sum += valTwo
    valSwap = valOne
    valOne = valTwo
    valTwo += valSwap
print(sum)