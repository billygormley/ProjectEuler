startingNum1 = 1
startingNum2 = 1
someSum = 0

while startingNum2 < 4000000:
    if startingNum2 % 2 == 0:
        someSum += startingNum2

    number3 = startingNum1 + startingNum2
    startingNum1 = startingNum2
    startingNum2 = number3

print(someSum)
