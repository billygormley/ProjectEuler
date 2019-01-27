def primeFinder(x):
    primeNumber = x
    primeRoot = x**.5
    primeCounter = 0
    iterator = 1

    while iterator <= primeRoot:
        if primeNumber % iterator == 0:
            primeCounter = primeCounter + 1

        iterator = iterator + 1

    print("The %th prime number is %", (primeNumber, primeCounter)

primeFinder(11)
    
    
