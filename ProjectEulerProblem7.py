import math

prime1 = 0
primeCounter = 0

def isprime(x):
    #print("Checking if {} is prime".format(x))
    sqRoot = math.floor(math.sqrt(x))
    sqRootList = list()

    if x == 0 or x == 1:
        #print("{} is 1 or 0, therefore not prime".format(x))
        result = False

    elif x == 2 or x == 3:
        #print("{} is 2 or 3, therefore is prime".format(x))
        result = True
    
    else:
        if x % 2 == 0:
            #print("{} is even, therefore not prime".format(x))
            result = False

        else:
            for j in range(2,sqRoot+1):
                sqRootList.append(x % j)

            if min(sqRootList) == 0:
                result = False
            else:
                result = True

    return result

while primeCounter < 10001:
    if isprime(prime1):
        primeCounter += 1

    prime1 += 1

print(prime1 - 1)
