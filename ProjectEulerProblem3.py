import math

#"Nonprivate" variables that the user can manipulate
primeToCheck = 600851475143  #The number that we are finding the largest prime factor for
currentPrimeFactor = 0
maxPrimeFactor = 0
factorList = list()

def isprime(x):
    print("Checking if {} is prime".format(x))
    sqRoot = math.floor(math.sqrt(x))
    sqRootList = list()

    if x == 0 or x == 1:
        print("{} is 1 or 0, therefore not prime".format(x))
        result = False

    elif x == 2 or x == 3:
        print("{} is 2 or 3, therefore is prime".format(x))
        result = True
    
    else:
        if x % 2 == 0:
            print("{} is even, therefore not prime".format(x))
            result = False

        else:
            for j in range(2,sqRoot+1):
                sqRootList.append(x % j)

            if min(sqRootList) == 0:
                result = False
            else:
                result = True

    return result

#Get the factors of primetoCheck        
for i in range(2,primeToCheck):

    if i != 1 or i != primeToCheck:
        if primeToCheck % i == 0:
            factorList.append(i)

print(factorList)

for k in factorList:
    if isprime(k):
        currentPrimeFactor = k

    if currentPrimeFactor > maxPrimeFactor:
        maxPrimeFactor = currentPrimeFactor

print(maxPrimeFactor)

