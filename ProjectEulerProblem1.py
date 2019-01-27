startingNum = 1
someSum = 0


while startingNum < 1000:

    if startingNum % 3 == 0 or startingNum % 5 == 0:
        someSum = someSum + startingNum

    startingNum +=1

print(someSum)


